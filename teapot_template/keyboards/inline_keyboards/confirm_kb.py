from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

confirm_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['CONFIRM']['CONFIRM_BUTTON']['NAME'],
                                      callback_data=DICTIONARY_RU['INLINE_BUTTONS']['CONFIRM']
                                      ['CONFIRM_BUTTON']['CALLBACK'])
unconfirm_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['CONFIRM']['UNCONFIRM_BUTTON']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['CONFIRM']
                                        ['UNCONFIRM_BUTTON']['CALLBACK'])

confirm_kb_builder = InlineKeyboardBuilder()

confirm_kb_builder.row(confirm_button, unconfirm_button, width=1)

confirm_kb: InlineKeyboardMarkup = confirm_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)