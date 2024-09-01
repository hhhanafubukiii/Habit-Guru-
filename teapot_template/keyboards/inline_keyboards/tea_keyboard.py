from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

shu_puer_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                       ['SHU_PUER']['NAME'],
                                       callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                       ['SHU_PUER']['CALLBACK'])

shen_puer_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['SHEN_PUER']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['SHEN_PUER']['CALLBACK'])

oolong_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                     ['OOLONG']['NAME'],
                                     callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                     ['OOLONG']['CALLBACK'])

red_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                      ['RED_TEA']['NAME'],
                                      callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                      ['RED_TEA']['CALLBACK'])

white_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['WHITE_TEA']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['WHITE_TEA']['CALLBACK'])

green_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['GREEN_TEA']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['GREEN_TEA']['CALLBACK'])

berry_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['BERRY_TEA']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['BERRY_TEA']['CALLBACK'])

fruit_tea_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['FRUIT_TEA']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
                                        ['FRUIT_TEA']['CALLBACK'])

tea_kb_builder = InlineKeyboardBuilder()

tea_kb_builder.row(shu_puer_button, shen_puer_button, oolong_button, red_tea_button, white_tea_button,
                   green_tea_button, berry_tea_button, fruit_tea_button,
                   width=2)

tea_kb: InlineKeyboardMarkup = tea_kb_builder.as_markup()

# print(DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']['TEAS']
#       ['SHU_PUER']['CALLBACK'])
