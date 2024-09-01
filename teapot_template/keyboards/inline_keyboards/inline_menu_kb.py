from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

tea_parties_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                          ['TEA_PARTIES_BUTTON']['NAME'],
                                          callback_data=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                          ['TEA_PARTIES_BUTTON']['CALLBACK'])
reminder_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                       ['REMINDER_BUTTON']['NAME'],
                                       callback_data=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                       ['REMINDER_BUTTON']['CALLBACK'])
my_skill_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                       ['MY_TEAPOT_BUTTON']['NAME'],
                                       callback_data=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                       ['MY_TEAPOT_BUTTON']['CALLBACK'])
my_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                     ['MY_TEA_BUTTON']['NAME'],
                                     callback_data=DICTIONARY_RU['INLINE_BUTTONS']['MENU']
                                     ['MY_TEA_BUTTON']['CALLBACK'])
menu_kb_builder = InlineKeyboardBuilder()

menu_kb_builder.row(tea_parties_button, my_tea_button, reminder_button, my_skill_button, width=2)


menu_kb: InlineKeyboardMarkup = menu_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

