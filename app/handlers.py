from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.api_client import fetch_city_info
import app.keyboard as kb

router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для получения информации о городах. Выберите действие:",
        reply_markup=kb.main
    )

# Обработчик кнопки "Информация по городу"
@router.message(F.text == "Информация по городу")
async def ask_city_name(message: Message):
    await message.answer("Введите название города:")

# Получение информации о городе
@router.message(F.text.regexp(r"^[А-Яа-яA-Za-z\s\-]+$"))
async def get_city_info(message: Message):
    city_name = message.text.strip()
    await message.answer(f"🔍 Ищу информацию по городу: {city_name}...")

    cities_info = await fetch_city_info(city_name)

    if isinstance(cities_info, list) and len(cities_info) > 0:
        # Если несколько городов найдены, выводим информацию о каждом
        for city in cities_info:
            answer = (
                f"🌆 Город: {city['name']}\n"
                f"🌍 Страна: {city['country']}\n"
                f"👥 Население: {city['population']}\n"
                f"📍 Координаты: {city['latitude']}, {city['longitude']}\n\n"
            )
            await message.answer(answer, reply_markup=kb.main)
    elif isinstance(cities_info, dict) and "error" in cities_info:
        # Если произошла ошибка или город не найден
        await message.answer(f"❌ Ошибка: {cities_info['error']}")
    else:
        await message.answer("❌ Не удалось найти информацию о городе.")