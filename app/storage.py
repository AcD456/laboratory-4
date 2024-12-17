import sqlite3
from config import DATABASE

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_settings (
            user_id INTEGER PRIMARY KEY,
            city TEXT
        )
    """)
    conn.commit()
    conn.close()

# Сохранение города пользователя
def save_user_city(user_id: int, city: str):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_settings (user_id, city)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET city = excluded.city
    """, (user_id, city))
    conn.commit()
    conn.close()

# Получение города пользователя
def get_user_city(user_id: int) -> str:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT city FROM user_settings WHERE user_id = ?
    """, (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None