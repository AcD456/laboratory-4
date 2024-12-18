import aiohttp
from config import API_URL, DATASET

async def fetch_city_info(city: str) -> dict:
    params = {
        'dataset': DATASET,
        'q': city,  # Искать только по названию города
        'rows': 50,  # Получаем до 50 городов на случай совпадений
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    # Отладочный вывод для диагностики
                    print("RAW API Response:", data)

                    if data['nhits'] > 0:
                        cities_info = []
                        # Собираем информацию о всех городах
                        for record in data['records']:
                            fields = record['fields']
                            population = fields.get("population", 0) or 0  # Убедимся, что есть население
                            cities_info.append({
                                "name": fields.get("name", "Неизвестно"),
                                "country": fields.get("cou_name_en", "Неизвестно"),
                                "population": int(population),
                                "latitude": fields.get("coordinates", [None, None])[0],
                                "longitude": fields.get("coordinates", [None, None])[1]
                            })

                        # Находим город с наибольшим населением
                        largest_city = max(cities_info, key=lambda x: x["population"])
                        return largest_city
                    else:
                        return {"error": "Город не найден."}
                else:
                    return {"error": f"Ошибка API: {response.status}"}
    except Exception as e:
        return {"error": str(e)}