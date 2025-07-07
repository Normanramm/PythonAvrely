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
