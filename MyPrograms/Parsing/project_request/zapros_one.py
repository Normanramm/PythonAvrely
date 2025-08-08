import requests
import json
import os

# Данные нового пользователя (в формате JSON)
new_user = {
    "id ": 11,
    "name": "Иван Иванов",
    "username": "ivan_ivanov",
    "email": "ivan@example.com",
    "address": {
        "street": "Ленина",
        "suite": "42",
        "city": "Москва",
        "zipcode": "123456"
    },
    "phone": "+7 999 123-45-67",
    "website": "ivanov.ru",
    "company": {
        "name": "ООО Рога и Копыта",
        "catchPhrase": "Решения без компромиссов",
        "bs": "делать всё лучше"
    }
}

# URL для добавления пользователя
url = 'https://jsonplaceholder.typicode.com/users'

# Отправляем POST-запрос
response = requests.post(url, json=new_user)

# Проверяем статус ответа
if response.status_code == 201:
    print("Пользователь успешно добавлен:")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)


# URL для получения списка пользователей
url = 'https://jsonplaceholder.typicode.com/users'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    users = response.json()

    # Выводим каждого пользователя в виде строки
    for user in users:
        print(f"{user['id']}. {user['name']} - {user['email']}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)


# URL для получения списка фото
url = 'https://jsonplaceholder.typicode.com/photos'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    photos = response.json()

    # Сохраняем в файл (опционально)
    with open('photos.json', 'w', encoding='utf-8') as f:
        json.dump(photos, f, indent=4, ensure_ascii=False)

    print("Данные о фото успешно загружены и сохранены в файл 'photos.json'")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)


# Создаем папку для сохранения фото, если её нет
os.makedirs('downloaded_photos', exist_ok=True)

# URL для получения списка фото
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

if response.status_code == 200:
    photos = response.json()

    # Скачиваем первые 5 фото
    for photo in photos[:5]:
        image_url = photo['url']
        image_id = photo['id']

        # Загружаем изображение
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            with open(f'downloaded_photos/photo_{image_id}.jpg', 'wb') as f:
                f.write(img_response.content)
            print(f"Фото {image_id} успешно скачано")
        else:
            print(f"Не удалось загрузить фото {image_id}")

else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)