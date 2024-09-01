from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

menu_button = KeyboardButton(text=DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['MENU']['NAME'])
settings_button = KeyboardButton(text=DICTIONARY_RU['REPLY_BUTTONS']['MAIN_KB']['SETTINGS']['NAME'])

start_kb_builder = ReplyKeyboardBuilder()
start_kb_builder.row(menu_button, settings_button, width=2)

start_kb: ReplyKeyboardMarkup = start_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

