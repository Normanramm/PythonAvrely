import requests
from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()
WEATHER_API_KEY = "your_key"
cache = {}

@app.get("/weather/{city}")
async def get_weather(city: str):
    # Проверяем кэш (актуальность 10 минут)
    if city in cache:
        cached_time, data = cache[city]
        if datetime.now() - cached_time < timedelta(minutes=10):
            return {"source": "cache", **data}
    
    # Запрос к внешнему API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        
        # Сохраняем в кэш
        cache[city] = (datetime.now(), weather_data)
        return {"source": "api", **weather_data}
    else:
        return {"error": "City not found"}