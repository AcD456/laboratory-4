from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Информация по городу"), KeyboardButton(text="Настройки")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню:"
)