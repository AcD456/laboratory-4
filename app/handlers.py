from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

import app.keyboard as kb

router = Router()


@router.message(CommandStart()) # type: ignore
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для получения справочной информации о городах.', reply_markup = kb.main)