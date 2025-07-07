book = {
    "login": "letpy",
    "parol": "1984",
}

for i in range(3):

    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login == book["login"] and password == book["parol"]:
        print("Вы успешно вошли в систему")
        break
    else:
        print("Неверный логин или пароль")

    print(f"Осталось попыток: {2 - i}")

else:
    print("Вы не смогли войти в систему")


