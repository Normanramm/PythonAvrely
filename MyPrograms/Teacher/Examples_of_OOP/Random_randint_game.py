# Это простая версия ________________________________________________
import random

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
attempts = 0

while True:
    choice = random.choice(numbers)
    choice_2 = int(input("Выбери число от 1 до 10: "))
    attempts += 1
    
    if choice == choice_2:
        print(f"Угадал! Понадобилось попыток: {attempts}")
        break
    else:
        print(f"Не угадал! Правильный ответ был: {choice} (попытка №{attempts})\n")


# Улучшенная простая версия до ООП ________________________________________________
import random

class NumberGuessingGame:
    def __init__(self):
        """Инициализация игры"""
        self.numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.attempts = 0
    
    def play(self):
        """Основной метод игры"""
        print("Добро пожаловать в игру 'Угадай число от 1 до 10'!")
        
        while True:
            self.attempts += 1
            secret_number = random.choice(self.numbers)
            user_guess = self._get_user_input()
            
            if user_guess == secret_number:
                print(f"\nПоздравляю! Ты угадал число {secret_number} за {self.attempts} попыток!")
                break
            else:
                print(f"Не угадал! Загаданное число было: {secret_number}")
                print("Попробуй еще раз!\n")
    
    def _get_user_input(self):
        """Получение ввода от пользователя с проверкой"""
        while True:
            try:
                guess = int(input("Твой выбор (1-10): "))
                if 1 <= guess <= 10:
                    return guess
                print("Число должно быть от 1 до 10!")
            except ValueError:
                print("Пожалуйста, введи целое число!")


# Запуск игры
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()


# Это корявая версия ________________________________________________

import random


class GameNumber:
    def __init__(self):
        self.num = random.randint(1, 10)
        self.i = 0
        self.positive_choice = "Угадал"
        self.negative_choice = "Не угадал"

    def game_one(self):
        while self.i < 3:

            user_input = input("Введите число от 1 до 10: ")
            choice = int(user_input)

            if choice < 1 or choice > 10:
                print("Число должно быть от 1 до 10!")
                continue

            if choice == self.num:
                print(self.positive_choice)
                break
            else:
                print(self.negative_choice)

                self.i += 1

        else:
            print(f"Вы исчерпали все попытки. Загаданное число: {self.num}")

    def game_two(self):
        for j in range(3):
            user_input = input("Введите число от 1 до 10: ")
            choice = int(user_input)

            if choice == self.num:
                print(self.positive_choice)
                break
            else:
                print(self.negative_choice)
                print(
                    f"Вы исчерпали все попытки. Загаданное число: {self.num}")


def choose():
    game1 = GameNumber()
    choice = input("""Выберите функционал: 
    1 - Игра с циклом for
    2 - Игра с циклом while
     """
                   )
    if choice == "1":
        game1.game_one()
    elif choice == "2":
        game1.game_one()
    else:
        print("Неправильный выбор операции!")

    while True:
        flag = input("Еще раз: да / нет: ")
        if flag == "да" and choice == '1':
            game1.game_one()
        elif flag == 'да' and choice == '2':
            game1.game_two()
        elif flag == "нет":
            choose()
        else:
            break


if __name__ == "__main__":
    choose()


# __________________________________________________________________________________________
# Улучшенная версия игры

import random


class GameNumber:
    def __init__(self):
        self.num = random.randint(1, 10)
        self.positive_choice = "Угадал!"
        self.negative_choice = "Не угадал."

    def game_one(self):  # Цикл while
        i = 0
        while i < 3:
            try:
                user_input = input("Введите число от 1 до 10: ")
                choice = int(user_input)

                if not (1 <= choice <= 10):
                    print("Число должно быть от 1 до 10!")
                    continue

                if choice == self.num:
                    print(self.positive_choice)
                    return  # Завершаем игру
                else:
                    print(self.negative_choice)

                i += 1
            except ValueError:
                print("Пожалуйста, введите целое число!")

        print(f"Вы исчерпали все попытки. Загаданное число: {self.num}")

    def game_two(self):  # Цикл for
        for j in range(3):
            try:
                user_input = input("Введите число от 1 до 10: ")
                choice = int(user_input)

                if not (1 <= choice <= 10):
                    print("Число должно быть от 1 до 10!")
                    continue

                if choice == self.num:
                    print(self.positive_choice)
                    return  # Завершаем игру
                else:
                    print(self.negative_choice)

            except ValueError:
                print("Пожалуйста, введите целое число!")

        print(f"Вы исчерпали все попытки. Загаданное число: {self.num}")


def choose():
    while True:
        print("\n--- Новая игра ---")
        choice_game = input("""Выберите функционал:
1 - Игра с циклом while
2 - Игра с циклом for
>>> """)

        if choice_game in ("1", "2"):
            game = GameNumber()
            if choice_game == "1":
                game.game_one()
            else:
                game.game_two()
        else:
            print("Неверный выбор.")
            continue

        flag = input("Хотите сыграть ещё раз? (да / нет): ").lower()
        if flag != "да":
            print("До новых встреч!")
            break


if __name__ == "__main__":
    choose()


