from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

router = Router()


@router.message(CommandStart()) # type: ignore
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для получения справочной информации о городах.\n Введите название города, чтобы получить данные.')