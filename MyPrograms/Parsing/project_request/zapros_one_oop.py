import requests
import json
import os


class UserPhotoManager:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'
        self.photos_dir = 'downloaded_photos'  # Папка для сохранения фото
        os.makedirs(self.photos_dir, exist_ok=True)  # Создаем папку, если она не существует

    def add_user(self, user_data):
        url = f'{self.base_url}/users'
        response = requests.post(url, json=user_data)
        if response.status_code == 201:
            print("Пользователь успешно добавлен:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(
                f"Ошибка при добавлении пользователя: {response.status_code}")
            print(response.text)

    def get_users(self):
        url = f'{self.base_url}/users'
        response = requests.get(url)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                print(f"{user['id']}. {user['name']} - {user['email']}")
        else:
            print(
                f"Ошибка при получении пользователей: {response.status_code}")
            print(response.text)

    def save_photos_to_json(self, filename='photos.json'):
        url = f'{self.base_url}/photos'
        response = requests.get(url)
        if response.status_code == 200:
            photos = response.json()
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(photos, f, indent=4, ensure_ascii=False)
            print(f"Данные о фото сохранены в файл '{filename}'")
        else:
            print(f"Ошибка при загрузке фото: {response.status_code}")
            print(response.text)

    def download_first_n_photos(self, n=5):
        url = f'{self.base_url}/photos'
        response = requests.get(url)
        if response.status_code == 200:
            photos = response.json()
            for photo in photos[:n]:
                image_url = photo['url']
                image_id = photo['id']
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    with open(f'{self.photos_dir}/photo_{image_id}.jpg', 'wb') as f:
                        f.write(img_response.content)
                    print(f"Фото {image_id} успешно скачано")
                else:
                    print(f"Не удалось загрузить фото {image_id}")
        else:
            print(f"Ошибка при загрузке фото: {response.status_code}")
            print(response.text)


# Пример использования
if __name__ == '__main__':
    manager = UserPhotoManager()

    # Добавление нового пользователя
    new_user = {
        "id": 11,
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

    # Добавляет пользователя
    manager.add_user(new_user)

    # Получение всех пользователей
    manager.get_users()

    # Сохранение данных о фото в JSON
    manager.save_photos_to_json()

    # Скачивание первых 5 фото
    manager.download_first_n_photos(n=5)
