class PasswordChecker:
    def __init__(self, correct_password='123456'):
        self.correct_password = correct_password

    def check_password(self):
        user_password = input("Введите пароль: ")
        if user_password == self.correct_password:
            return True
        else:
            print("Доступ запрещен")
            return False

    def process_access(self):
        if self.check_password():
            print("Доступ разрешен")



if __name__ == "__main__":
    checker = PasswordChecker()
    checker.process_access()


# ___________________________________________________________________
# Запрашивает пароль у пользователя три раза

class PasswordChecker:
    def __init__(self, correct_password='123456'):
        self.correct_password = correct_password

    def check_password(self):
        for i in range(3):
            user_password = input("Введите пароль: ")
            if user_password == self.correct_password:
                return True
        else:
            print("Доступ запрещен")
            return False

    def process_access(self):
        if self.check_password():
            print("Доступ разрешен")



if __name__ == "__main__":
    checker = PasswordChecker()
    checker.process_access()