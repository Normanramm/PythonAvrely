import os
import openai
from dotenv import load_dotenv # для загрузки переменных из .env


# pip install python-dotenv. Чтобы Python умел читать .env-файлы, используй библиотеку
# Загружаем переменные из .env это для хранения ключа  в отдельном файле
load_dotenv()

# Получаем ключ API
api_key = os.environ.get("API_KEY") # берем ключ из переменной окружения .env
openai.api_key = api_key

# Приветствие
print("🤖 Привет! Я твой мини-ChatGPT. Напиши что-нибудь, или 'выход' для завершения.\n")

# История сообщений
messages = []

while True:
    # Ввод пользователя
    user_input = input("Ты: ")

    # Проверка на выход
    if user_input.lower() in ["выход", "exit", "quit"]:
        print("🫡 Пока-пока!")
        break

    # Добавляем сообщение пользователя
    messages.append({"role": "user", "content": user_input})

    # Отправляем запрос
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Получаем и выводим ответ
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print("ChatGPT:", reply, "\n")