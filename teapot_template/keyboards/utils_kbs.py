from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

dont_want_button = KeyboardButton(text=DICTIONARY_RU['REPLY_BUTTONS']['SKIP_KB']['NAME'])

dont_want_kb = ReplyKeyboardMarkup(keyboard=[[dont_want_button]],
                                   one_time_keyboard=True,
                                   resize_keyboard=True)
