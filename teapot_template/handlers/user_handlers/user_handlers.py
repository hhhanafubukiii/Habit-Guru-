from aiogram import (Router, Bot, F)
from aiogram.types import (Message, FSInputFile, ChatMemberUpdated, CallbackQuery, ReplyKeyboardRemove)
from aiogram.filters import (Command, ChatMemberUpdatedFilter, KICKED, MEMBER, StateFilter)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from logging import *
from logging.config import dictConfig

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

from teapot_template.config_data.config import load_config
from teapot_template.config_data.logging.logging_settings import logging_config

from teapot_template.keyboards.reply_keyboards.reply_menu import start_kb
from teapot_template.keyboards.inline_keyboards.inline_menu_kb import menu_kb
from teapot_template.keyboards.inline_keyboards.tea_parties_menu import tea_parties_kb
from teapot_template.keyboards.inline_keyboards.tea_keyboard import tea_kb
from teapot_template.keyboards.inline_keyboards.choice_tea_keyboard import choice_tea_kb
from teapot_template.keyboards.utils_kbs import dont_want_kb
from teapot_template.keyboards.inline_keyboards.confirm_kb import confirm_kb

from teapot_template.database.database_insert import insert_user_state_db
from teapot_template.database.database_update import update_state_in_user_state_db

from teapot_template.states.database_states import is_in_db
from teapot_template.states.FSM_states import FSMFillForm

config = load_config('.env')
dictConfig(logging_config)

logger = getLogger(__name__)
logger.propagate = False

bot = Bot(token=config.tg_bot.token)
router = Router()

# подобие оперативной памяти

tea_dict: dict[str: int | str | None] = {
    'user_id': 0,
    'type': "❌",
    'tea_type': "❌",
    'tea_name': "❌",
    'prod_year': "❌",
    'rate': "❌",
    'descr': "❌"
}

party_dict: dict[str: int | str | None] = {
    'user_id': 0,
    'party_id': 0,
    'tea_id': 0,
    'grams': "❌",
    'water_temp': "❌",
    'date': ""
}


@router.callback_query(F.data == 'new_button_pressed')
async def process_select_party_press(callback: CallbackQuery):
    print(callback)
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.message.from_user.id}')
    await callback.message.answer(text='!!!')
    await callback.answer()


# Обработчики блокировки и разблокировки бота
@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    update_state_in_user_state_db(user_id=event.from_user.id, state='inactive')
    logger.info(f'Пользователь {event.from_user.id} заблокировал бота')


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblock_bot(event: ChatMemberUpdated):
    update_state_in_user_state_db(user_id=event.from_user.id, state='active')
    logger.info(f'Пользователь {event.from_user.id} разблокировал бота')


# Обработчики основных команд
@router.message(Command("start"), StateFilter(default_state))
async def start_handler(message: Message):
    print(type(message.from_user.id))
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.reply(text=f"👋Привет, <b>{message.from_user.first_name}!</b> Я <b>TeaPot</b> - твой персональный "
                             f"помощник в сфере чайных дел.☕"
                             f"\n\nЕсли тебе понадобится <b>помощь</b>, пришли мне команду <b>/help</b>",
                        reply_markup=start_kb)
    if is_in_db(message.from_user.id):
        insert_user_state_db(user_id=message.from_user.id, state='active', total_parties=0)


@router.message(Command("help"), StateFilter(default_state))
async def help_handler(message: Message):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.reply(DICTIONARY_RU['USUAL_COMMANDS']['/help'])


@router.message(Command("cancel"), ~StateFilter(default_state))
async def cancel_handler(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text=DICTIONARY_RU['USUAL_COMMANDS']['/cancel'],
                         reply_markup=start_kb)
    await state.set_state(default_state)


@router.message(Command("menu"))
async def menu_handler(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    photo = FSInputFile(r'C:\Users\1\Desktop\For TeaPot_tg\TeaPot_tg\teapot_bot\menu_ru.jpg')
    await message.answer_photo(photo=photo,
                               caption=DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['MENU']['ANSWER'],
                               reply_markup=menu_kb)
    await state.set_state(default_state)


# ОБРАБОТЧИКИ КНОПОК REPLY-МЕНЮ

# обработчик кнопки меню

@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['MENU']['NAME'], StateFilter(default_state))
async def menu_button_handler(message: Message):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    photo = FSInputFile(r'C:\Users\1\Desktop\For TeaPot_tg\TeaPot_tg\teapot_bot\menu_ru.jpg')
    await message.answer_photo(photo=photo,
                               caption=DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['MENU']['ANSWER'],
                               reply_markup=menu_kb)


# ОБРАБОТЧИКИ КНОПОК INLINE-МЕНЮ

# обработчик кнопки чаепития

@router.callback_query(F.data == DICTIONARY_RU['INLINE_BUTTONS']['MENU']['TEA_PARTIES_BUTTON']['CALLBACK'],
                       StateFilter(default_state))
async def process_tea_parties_button_press(callback: CallbackQuery):
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.message.from_user.id}')
    photo = FSInputFile(r"C:\Users\1\Desktop\For TeaPot_tg\TeaPot_tg\teapot_bot\tea_parties_ru.jpg")
    await callback.message.answer_photo(photo=photo,
                                        caption='Это <b>твои чаепития</b>.\nВыбери, что хочешь сделать',
                                        reply_markup=tea_parties_kb)
    await callback.answer()


# ОБРАБОТЧИКИ СОЗДАНИЯ ЧАЕПИТИЯ И ЧАЯ

# обработчик кнопки новое чаепитие

@router.callback_query(F.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['NEW_PARTY_BUTTON']['CALLBACK'],
                       StateFilter(default_state))
async def process_new_party_button_press(callback: CallbackQuery, state: FSMContext):
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.from_user.id}')
    await callback.message.answer(text='Отлично! <b>Выбери чай</b>', reply_markup=choice_tea_kb)
    await state.set_state(FSMFillForm.new_tea_party)
    await callback.answer()


# обработчики кнопки новый чай:

@router.callback_query(F.data == 'new_tea_button_pressed', StateFilter(FSMFillForm.new_tea_party))
async def process_new_tea_button_press(callback: CallbackQuery, state: FSMContext):
    global tea_dict
    tea_dict['type'] = "новый чай"
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.from_user.id}')
    await callback.message.answer(text='Отлично! <b>Выбери вид чая</b>',
                                  reply_markup=tea_kb)
    await state.set_state(FSMFillForm.fill_tea_type)
    await callback.answer()


# обработчик кнопки выбора вида чая; ссылка на отправление названия чая
@router.callback_query(F.data.startswith('TEA'), StateFilter(FSMFillForm.fill_tea_type))
async def process_fill_tea_type(callback: CallbackQuery, state: FSMContext):
    global tea_dict
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.from_user.id}')
    tea_dict['user_id'] = callback.from_user.id
    if callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['SHU_PUER']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['SHU_PUER']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['SHEN_PUER']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['SHEN_PUER']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['OOLONG']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['OOLONG']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['RED_TEA']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['RED_TEA']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['WHITE_TEA']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['WHITE_TEA']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['GREEN_TEA']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['GREEN_TEA']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['BERRY_TEA']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['BERRY_TEA']['NAME']
    elif callback.data == DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['FRUIT_TEA']['CALLBACK']:
        tea_dict['tea_type'] = DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']['FRUIT_TEA']['NAME']
    await callback.message.answer(text='Хорошо! Теперь отправь <b>название чая:</b>')
    await state.set_state(FSMFillForm.fill_tea_name)
    await callback.answer()


# обработчик названия чая; ссылка на год выпуска
@router.message(StateFilter(FSMFillForm.fill_tea_name))
async def process_fill_name(message: Message, state: FSMContext):
    global tea_dict
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    tea_dict['tea_name'] = message.text
    await message.answer(text='Хорошо! Теперь, <b>если хочешь</b> отправь <b>год выпуска:</b>\n\n❗<i>Данные'
                              ' можно будет дозаписать в любой момент во вкладке "мои чаи"</i>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_prod_year)
    print(tea_dict)


# обработчики года выпуска чая
# обработчик кнопки не хочу; ссылка на ввод оценки чаю
@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'], StateFilter(FSMFillForm.fill_prod_year))
async def process_dont_want_button_press(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='Теперь, <b>если хочешь</b> отправь <b>оценку чаю по шкале от 1 до 10:</b>'
                              '\n\n❗<i>Данные можно будет дозаписать в любой момент '
                              'во вкладке "мои чаи"</i>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_tea_grade)


# обработчик года выпуска чая; ссылка на ввод оценки чаю
@router.message(F.text.isdigit(), StateFilter(FSMFillForm.fill_prod_year))
async def process_prod_year(message: Message, state: FSMContext):
    global tea_dict
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    tea_dict['prod_year'] = int(message.text)
    await message.answer(text='Теперь, <b>если хочешь</b> отправь <b>оценку чаю по шкале от 1 до 10:</b>\n\n❗<i>Данные'
                              ' можно будет дозаписать в любой момент во вкладке "мои чаи"</i>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_tea_grade)


# обработчики ввода оценки чая
# обработчик кнопки не хочу; ссылка на ввод описания чая
@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'], StateFilter(FSMFillForm.fill_tea_grade))
async def process_dont_want_tea_grade(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='Теперь, <b>если хочешь,</b> отправь <b>описание чая:</b>'
                              '\n\n❗<i>Описание можно будет дозаписать в '
                              'любой момент во вкладке "мои чаи"</i>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_tea_description)


# обработчик оценки чая; ссылка на ввод описания чая
@router.message(F.text.isdigit(), StateFilter(FSMFillForm.fill_tea_grade))
async def process_fill_tea_rate(message: Message, state: FSMContext):
    global tea_dict
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    tea_dict['rate'] = message.text
    await message.answer(text='Теперь, <b>если хочешь,</b> отправь <b>описание чая:</b>'
                              '\n\n❗<i>Описание можно будет дозаписать в '
                              'любой момент во вкладке "мои чаи"</i>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_tea_description)


# обработчики для описания чая
# обработчик кнопки не хочу; ссылка на ввод количества грамм чая
@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'],
                StateFilter(FSMFillForm.fill_tea_description))
async def process_dont_want_tea_descr(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='Теперь, <b>если хочешь, </b>отправь <b>количество грамм чая:</b>',
                         reply_markup=dont_want_kb)
    await state.set_state(FSMFillForm.fill_grams_amount)


# обработчик описания чая
@router.message(StateFilter(FSMFillForm.fill_tea_description))
async def process_fill_tea_descr(message: Message, state: FSMContext):
    global tea_dict
    tea_dict['descr'] = message.text
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='Теперь, <b>если хочешь, </b>отправь <b>количество грамм чая:</b>',
                         reply_markup=dont_want_kb)
    print(tea_dict)
    await state.set_state(FSMFillForm.fill_grams_amount)


# обработчики для грамм чая
# обработчик кнопки не хочу; ссылка на ввод температуры воды
@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'], StateFilter(FSMFillForm.fill_grams_amount))
async def process_dont_want_grams_amount(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='Теперь, <b>если хочешь, </b> отправь <b>температуру воды:</b>')
    await state.set_state(FSMFillForm.fill_water_temp)


# обработчик граммов чая; ссылка на ввод температуры воды
@router.message(F.text.isdigit(), StateFilter(FSMFillForm.fill_grams_amount))
async def process_fill_grams_amount(message: Message, state: FSMContext):
    global party_dict
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    party_dict['user_id'] = message.from_user.id
    party_dict['grams'] = message.text
    await message.answer(text='Теперь, <b>если хочешь, </b> отправь <b>температуру воды:</b>')
    await state.set_state(FSMFillForm.fill_water_temp)


# обработчики температуры воды
# обработчик кнопки не хочу; конец создания чаепития
@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'], StateFilter(FSMFillForm.fill_water_temp))
async def process_dont_want_water_temp(message: Message, state: FSMContext):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    await message.answer(text='ок',
                         reply_markup=start_kb)
    await state.set_state(default_state)


@router.message(F.text.isdigit(), StateFilter(FSMFillForm.fill_water_temp))
async def process_fill_water_temp(message: Message, state: FSMContext):
    global tea_dict
    global party_dict
    party_dict['water_temp'] = message.text
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    if tea_dict['type'] == 'новый чай':
        await message.answer(text=f'<b>Отлично! Теперь проверь введенные тобою данные:</b>'
                                  f'\n\n<b>Тип чая:</b> <u>{tea_dict['type']}</u>'
                                  f'\n\n\t\t\t<i>Вид чая:</i> {tea_dict['tea_type']}'
                                  f'\n\t\t\t<i>Название чая:</i> {tea_dict['tea_name']}'
                                  f'\n\t\t\t<i>Год выпуска чая:</i> {tea_dict['prod_year']}'
                                  f'\n\t\t\t<i>Оценка чаю:</i> {tea_dict['rate']}'
                                  f'\n\t\t\t<i>Описание чая:</i> {tea_dict['descr']}'
                                  f'\n\n<b>Количество грамм:</b> {party_dict['grams']}'
                                  f'\n<b>Температуры воды:</b> {party_dict['water_temp']}',
                             reply_markup=confirm_kb)
    await state.set_state(FSMFillForm.confirm_state)
    print(party_dict)


@router.callback_query(F. StateFilter(FSMFillForm.confirm_state))
async def process_confirm_data(callback: CallbackQuery, state: FSMContext):
    logger.info(f'chat_id = {callback.chat.id} - user_id = {callback.from_user.id}')
    # здесь будет реализована передача данных в базы данных
    await callback.message.answer(text='!!!', reply_markup=start_kb)
    await callback.answer()
    await state.set_state(default_state)


@router.callback_query(F.data == DICTIONARY_RU['INLINE_BUTTONS']['MENU']['MY_TEA_BUTTON']['CALLBACK'],
                       StateFilter(default_state))
async def process_new_button_press(callback: CallbackQuery):
    logger.info(f'chat_id = {callback.chat.id} - user_id = {callback.from_user.id}')
    photo = FSInputFile(r'C:\Users\1\Desktop\For TeaPot_tg\TeaPot_tg\teapot_bot\my_tea_ru.jpg')
    await callback.message.answer_photo(photo=photo, caption="Это твои чаи")
    await callback.answer()


@router.callback_query(F.data == "REMINDERS_BUTTON_PRESSED")
async def process_reminder_button_press(callback: CallbackQuery):
    logger.info(f'chat_id = {callback.message.chat.id} - user_id = {callback.message.from_user.id}')
    await callback.message.edit_caption(caption='heh')
    await callback.answer()


@router.message(F.text == DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['SETTINGS']['NAME'])
async def settings_button_handler(message: Message):
    logger.info(f'chat_id = {message.chat.id} - user_id = {message.from_user.id}')
    photo = FSInputFile(r'C:\Users\1\Desktop\For TeaPot_tg\TeaPot_tg\teapot_bot\settings_ru.jpg')
    await message.answer_photo(photo=photo, caption=DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['SETTINGS']['ANSWER'])

