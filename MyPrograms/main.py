book = {
    "letpy": "1984",
    "admin": "password"
}

for i in range(3):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if login in book and book[login] == password:
        print("Вы успешно вошли в систему")
        break
    else:
        print("Неверный логин или пароль")

    print(f"Осталось попыток: {2 - i}\n")
    
else:
    print("Вы не смогли войти в систему")