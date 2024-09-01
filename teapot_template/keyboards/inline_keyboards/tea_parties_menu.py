from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

new_party_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']
                                        ['NEW_PARTY_BUTTON']['NAME'],
                                        callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']
                                        ['NEW_PARTY_BUTTON']['CALLBACK'])
select_party_button = InlineKeyboardButton(text=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']
                                           ['SELECT_PARTY_BUTTON']['NAME'],
                                           callback_data=DICTIONARY_RU['INLINE_BUTTONS']['TEA_PARTIES']
                                           ['SELECT_PARTY_BUTTON']['CALLBACK'])
tea_parties_kb_builder = InlineKeyboardBuilder()

tea_parties_kb_builder.row(new_party_button, select_party_button, width=1)

tea_parties_kb: InlineKeyboardMarkup = tea_parties_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

