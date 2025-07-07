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

#______________________________________________________

book = {
    "admin": "letpy",
    "password": "1984",
}

for i in range(3):

    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login == book["admin"] and password == book["password"]:
        print("Вы успешно вошли в систему")
        break

    print(f"Неверный логин или пароль, осталось попыток {2 - i}")

else:
    print("Вы не смогли войти в систему")

# __________________________________________________________________

book = {
    "admin": "letpy",
    "password": "1984",
}

i = 3
while i > 0:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login == book["admin"] and password == book["password"]:
        print("Вы успешно вошли в систему")
        break

    print(f"Неверный логин или пароль, осталось попыток {i - 1}")
    i -= 1
else:
    print("Вы не смогли войти в систему")


# В классе_____________________________________________________________

class CyberSystem:
    def __init__(self):
        self.book = {
            "login": "letpy",
            "parol": "1984"
        }
        self.max_num = 3

    def check_security(self):
        for i in range(self.max_num):
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            if login == self.book["login"] and password == self.book["parol"]:
                print("Вы успешно вошли в систему")
                return True

            print("Неверный логин или пароль")
            print(f"Осталось попыток: {self.max_num - 1 - i}")

        print("Вы не смогли войти в систему")
        return False


if __name__ == "__main__":
    auth = CyberSystem()
    auth.check_security()