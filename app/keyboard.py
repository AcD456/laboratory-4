from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура на русском
main_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/Информация по городу"), KeyboardButton(text="/Настройки")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню:"
)

# Клавиатура на английском
main_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/City Information"), KeyboardButton(text="/Settings")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose an option:"
)

# Клавиатура настроек на русском
settings_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/Изменить язык"), KeyboardButton(text="/Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие:"
)

# Клавиатура настроек на английском
settings_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/Change Language"), KeyboardButton(text="/Back")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose an action:"
)

# Клавиатура для выбора языка на русском
language_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/Русский"), KeyboardButton(text="/English")],
        [KeyboardButton(text="/Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите язык:"
)

# Клавиатура для выбора языка на английском
language_menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/Russian"), KeyboardButton(text="/English")],
        [KeyboardButton(text="/Back")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose a language:"
)