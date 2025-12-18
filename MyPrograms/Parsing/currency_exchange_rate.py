import requests

responce = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
# print(responce.status_code)

data = responce.json()
code = input("Введите код валюты (например, USD): ").upper()
usd = data["Valute"][code]["Value"]
print(f"Цена {code} = {usd} руб.")