import aiohttp
from config import API_URL, DATASET

async def fetch_city_info(city: str) -> dict:
    params = {
        'dataset': DATASET,
        'q': city,  # Искать только по названию города
        'rows': 5,  # Возвращаем несколько результатов на случай совпадений
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    # Отладочный вывод
                    print("API Response:", data)  # Это нужно для диагностики
                    if data['nhits'] > 0:
                        cities_info = []
                        # Перебираем все найденные города
                        for record in data['records']:
                            fields = record['fields']
                            cities_info.append({
                                "name": fields.get("name", "Неизвестно"),
                                "country": fields.get("cou_name_en", "Неизвестно"),
                                "population": fields.get("population", "Нет данных"),
                                "latitude": fields.get("coordinates", [None, None])[0],
                                "longitude": fields.get("coordinates", [None, None])[1]
                            })
                        return cities_info
                    else:
                        return {"error": "Город не найден."}
                else:
                    return {"error": f"Ошибка API: {response.status}"}
    except Exception as e:
        return {"error": str(e)}