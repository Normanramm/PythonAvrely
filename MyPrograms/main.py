class PasswordChecker:
    def __init__(self, correct_password='123456'):
        self.correct_password = correct_password

    def check_password(self):
        for i in range(3):
            user_password = input("Введите пароль: ")
            if user_password == self.correct_password:
                break
        else:
            print("Доступ запрещен")
            return False
        return True

    def process_access(self):
        if self.check_password():
            print("Доступ разрешен")


if __name__ == "__main__":
    checker = PasswordChecker()
    checker.process_access()
