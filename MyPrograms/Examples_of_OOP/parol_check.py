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


# _________________________________________________________________
# изменил и добавил break

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


# ________________________________________________________________
# Генерирует случайный пароль

import random

def get_parol(length=8, symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    parol = "".join([random.choice(symbols) for i in range(length)])
    return parol

print(get_parol(10))

# _________________________________________________________________
import random

def get_parol(length=8, symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    for i in range(length):
        result = "".join(random.choice(symbols) for i in range(length))
    return result 

print(get_parol(10))

# _________________________________________________________________
import random


def get_parol(length=8, symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    i = 0
    parol = ''
    while i < length:
        parol += random.choice(symbols)
        i += 1
    return parol


print(get_parol(10))
