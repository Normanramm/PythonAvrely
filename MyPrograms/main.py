import requests
import json
import os


class UserZapros:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'
        self.photos_dir = 'downloaded_photos'  # Папка для сохранения фото
        os.makedirs(self.photos_dir, exist_ok=True)

    def add_user(self, user_data):  # user_data словарь с данными пользователя добавить
        url = f'{self.base_url}/users'
        response = requests.post(url, json=user_data)
        if response.status_code == 201:
            print("Пользователь успешно добавлен:")
            # indent=4 Позволяет форматировать JSON с отступами (в данном случае — 4 пробела на уровень вложенности). Это делает JSON читаемым для человека.
            # ensure_ascii=False Позволяет выводить не только ASCII-символы, но и другие символы, такие как кириллица и символы юникода.
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(
                f"Ошибка при добавлении пользователя: {response.status_code}")
            print(response.text)

    def get_users(self):  # Получить всех пользователей
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

    def get_posts(self):  # Получить все посты
        url = f'{self.base_url}/posts'
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            for post in posts[:10]:  # Ограничиваем вывод первыми 10 постами
                print(f"{post['id']}. {post['title']} - {post['body']}\n")
        else:
            print(f"Ошибка при получении постов: {response.status_code}")
            print(response.text)

    def get_comments(self):  # Получить все комментарии
        url = f'{self.base_url}/comments'
        response = requests.get(url)
        if response.status_code == 200:
            comments = response.json()
            for comment in comments[:10]:  # Выводим первые 10 комментариев
                print(f"Комментарий #{comment['id']}:")
                print(f"От: {comment['email']}")
                print(f"Заголовок: {comment['name']}")
                print(f"Текст: {comment['body']}\n")
        else:
            print(f"Ошибка при получении комментариев: {response.status_code}")
            print(response.text)

    def get_albums(self):  # Получить все альбомы
        url = f'{self.base_url}/albums'
        response = requests.get(url)
        if response.status_code == 200:
            albums = response.json()
            for album in albums[:10]:  # Выводим первые 10 альбомов
                print(f"Альбом #{album['id']}:")
                print(f"Пользователь ID: {album['userId']}")
                print(f"Название: {album['title']}\n")
        else:
            print(f"Ошибка при получении альбомов: {response.status_code}")
            print(response.text)

    # Сохранить данные о фото в JSON
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

    def download_first_n_photos(self, n=5):  # Скачать первые n фото
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


if __name__ == '__main__':
    manager = UserZapros()
    print("Пользователи:")
    manager.get_users()
    print("\nПосты:")
    manager.get_posts()
    print("\nКомментарии:")
    manager.get_comments()
    print("\nАльбомы:")
    manager.get_albums()

    # Сохранение данных о фото в JSON
    manager.save_photos_to_json()

    # Скачивание первых 5 фото
    manager.download_first_n_photos(n=5)

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
