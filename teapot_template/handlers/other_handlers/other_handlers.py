from aiogram import Bot, F, Router
from aiogram.types import Message

from teapot_template.lexicon.lexicon_ru import DICTIONARY_RU

router = Router()


@router.message(F.text)
async def usual_message_answer(message: Message):
    await message.answer(DICTIONARY_RU['USUAL_COMMANDS_ANS']['/usual'])


@router.message(F.photo)
async def photo_ans(message: Message):
    await message.answer(DICTIONARY_RU['USUAL_COMMANDS_ANS']['/photo'])

# ...
