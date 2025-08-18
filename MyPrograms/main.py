import requests

url = "https://letpy.com/handbook/"

response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    # Сохраняем HTML-контент в файл
    with open("output.html", "w+", encoding="utf-8") as file:
        file.write(response.text)
    
    print("HTML успешно сохранён в output.html")
else:
    print(f"Ошибка запроса: {response.status_code}")
    print("Ответ сервера:", response.text)
