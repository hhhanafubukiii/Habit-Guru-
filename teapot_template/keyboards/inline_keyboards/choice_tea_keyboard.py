from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

new_tea_button = InlineKeyboardButton(text='создать новый чай',
                                      callback_data='new_tea_button_pressed')
choice_tea_button = InlineKeyboardButton(text='выбрать из "мои чаи"',
                                         callback_data='choice_tea_button_pressed')

builder = InlineKeyboardBuilder()

builder.row(new_tea_button, choice_tea_button, width=1)

choice_tea_kb: InlineKeyboardMarkup = builder.as_markup()
