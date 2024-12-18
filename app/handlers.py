from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.api_client import fetch_city_info
import app.keyboard as kb

router = Router()

# Словарь для хранения языка пользователя
user_languages = {}

# Обработчик команды /start для русского языка
@router.message(CommandStart())
async def cmd_start_ru(message: Message):
    user_languages[message.from_user.id] = "ru"  # Устанавливаем русский язык по умолчанию
    await message.answer(
        "Привет! Я бот для получения информации о городах. Выберите действие:",
        reply_markup=kb.main_ru
    )

# Обработчик команды /start для английского языка
@router.message(CommandStart())
async def cmd_start_en(message: Message):
    user_languages[message.from_user.id] = "en"  # Устанавливаем английский язык по умолчанию
    await message.answer(
        "Hello! I am a bot for getting information about cities. Choose an option:",
        reply_markup=kb.main_en
    )

# Обработчик кнопки "/Информация по городу" для русского языка
@router.message(F.text == "/Информация по городу")
async def ask_city_name_ru(message: Message):
    await message.answer("Введите название города:")

# Обработчик кнопки "/City Information" для английского языка
@router.message(F.text == "/City Information")
async def ask_city_name_en(message: Message):
    await message.answer("Enter the city name:")

# Получение информации о городе для русского языка
@router.message(F.text.regexp(r"^[А-Яа-я\s\-]+$"))
async def get_city_info_ru(message: Message):
    city_name = message.text.strip()
    await message.answer(f"🔍 Ищу информацию по городу: {city_name}...")

    city_info = await fetch_city_info(city_name)

    if isinstance(city_info, dict) and "name" in city_info:
        answer = (
            f"🌆 Город: {city_info['name']}\n"
            f"🌍 Страна: {city_info['country']}\n"
            f"👥 Население: {city_info['population']}\n"
            f"📍 Координаты: {city_info['latitude']}, {city_info['longitude']}\n"
        )
        await message.answer(answer, reply_markup=kb.main_ru)
    else:
        await message.answer("❌ Не удалось найти информацию о городе.")

# Получение информации о городе для английского языка
@router.message(F.text.regexp(r"^[A-Za-z\s\-]+$"))
async def get_city_info_en(message: Message):
    city_name = message.text.strip()
    await message.answer(f"🔍 I'm looking for information about the city: {city_name}...")

    city_info = await fetch_city_info(city_name)

    if isinstance(city_info, dict) and "name" in city_info:
        answer = (
            f"🌆 City: {city_info['name']}\n"
            f"🌍 Country: {city_info['country']}\n"
            f"👥 Population: {city_info['population']}\n"
            f"📍 Coordinates: {city_info['latitude']}, {city_info['longitude']}\n"
        )
        await message.answer(answer, reply_markup=kb.main_en)
    else:
        await message.answer("❌ City information not found.")

# Обработчик кнопки "/Настройки" для русского языка
@router.message(F.text == "/Настройки")
async def settings_ru(message: Message):
    await message.answer("Меню настроек. Выберите действие:", reply_markup=kb.settings_ru)

# Обработчик кнопки "/Settings" для английского языка
@router.message(F.text == "/Settings")
async def settings_en(message: Message):
    await message.answer("Settings menu. Choose an option:", reply_markup=kb.settings_en)

# Обработчик кнопки "/Изменить язык" для русского языка
@router.message(F.text == "/Изменить язык")
async def change_language_ru(message: Message):
    await message.answer("Выберите язык:", reply_markup=kb.language_menu_ru)

# Обработчик кнопки "/Change Language" для английского языка
@router.message(F.text == "/Change Language")
async def change_language_en(message: Message):
    await message.answer("Choose language:", reply_markup=kb.language_menu_en)

# Обработчик кнопки "/Русский" для русского языка
@router.message(F.text == "/Русский")
async def set_language_russian(message: Message):
    user_languages[message.from_user.id] = "ru"  # Сохраняем язык пользователя
    await message.answer("Язык изменен на русский.", reply_markup=kb.main_ru)

# Обработчик кнопки "/Russian" для английского языка
@router.message(F.text == "/Russian")
async def set_language_russian_en(message: Message):
    user_languages[message.from_user.id] = "ru"  # Сохраняем язык пользователя
    await message.answer("Language changed to Russian.", reply_markup=kb.main_ru)

# Обработчик кнопки "/English" для английского языка
@router.message(F.text == "/English")
async def set_language_english(message: Message):
    user_languages[message.from_user.id] = "en"  # Сохраняем язык пользователя
    await message.answer("Language changed to English.", reply_markup=kb.main_en)

# Обработчик кнопки "/Назад" для русского языка
@router.message(F.text == "/Назад")
async def go_back_ru(message: Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=kb.main_ru)

# Обработчик кнопки "/Back" для английского языка
@router.message(F.text == "/Back")
async def go_back_en(message: Message):
    await message.answer("You are back in the main menu.", reply_markup=kb.main_en)