# Первая версия________________________________________________________________________________________

import random


def number_choice():
    number = list(range(1, 10))
    random.shuffle(number)
    i = 0

    print("🤖 Игра началась!")

    while number:
        numbers_choice = number.pop()
        print(f"\nОсталость чисел, {len(number)}")

        try:
            choice = int(input("Введите число от 1 до 9: "))
        except ValueError:
            print("☠ 🤡 Вы ввели не число 🤡 ☠")
            continue

        if choice == numbers_choice:
            i += 1
            print(f"🤑 Вы угадали, число {numbers_choice}!")
        else:
            print(f"🤬 Вы не угадали, число {numbers_choice}!")

        print(f"\nПобед: {i} из {len(range(1, 10)) - len(number)}")

    print(f"\n💤 Игра окончена!  Результат: {i} 💤")
    
    
if __name__ == '__main__':
    number_choice()


# В Функции____________________________________________________________________________________________
import random

def number_guessing_game():
    # Создаем список уникальных чисел (можно изменить диапазон и количество)
    numbers = list(range(1, 10))  # Числа от 1 до 9
    random.shuffle(numbers)
    score = 0
    
    print("✨ Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал числа от 1 до 9, попробуй угадать их по порядку!")
    
    while numbers:
        current_num = numbers.pop()  # Берем последнее число из списка
        print(f"\nОсталось чисел: {len(numbers)}")
        
        try:
            guess = int(input("Твой вариант: "))
        except ValueError:
            print("⚠️ Пожалуйста, вводи только числа!")
            continue
            
        if guess == current_num:
            score += 1
            print(f"✅ Верно! Это было число {current_num}")
        else:
            print(f"❌ Не угадал! Это было число {current_num}")
        
        print(f"Текущий счет: {score}/{len(range(1, 10)) - len(numbers)}")
    
    print(f"\n🎮 Игра окончена! Твой финальный счет: {score}/9")

# Запуск игры
if __name__ == "__main__":
    number_guessing_game()

# В классе______________________________________________________________________________________________


import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=9):
        """
        Инициализация игры
        :param min_num: минимальное число в диапазоне
        :param max_num: максимальное число в диапазоне
        """
        self.min_num = min_num
        self.max_num = max_num
        self.numbers = list(range(min_num, max_num + 1))
        self.score = 0
        self.attempts_count = 0

    def _prepare_game(self):
        """Подготовка игры: перемешивание чисел"""
        random.shuffle(self.numbers)
        print(f"✨ Добро пожаловать в игру 'Угадай число'!")
        print(f"Я загадал числа от {self.min_num} до {self.max_num}, попробуй угадать их по порядку!")

    def _get_user_guess(self):
        """Получение и валидация ввода пользователя"""
        while True:
            try:
                return int(input("Твой вариант: "))
            except ValueError:
                print("⚠️ Пожалуйста, вводи только числа!")

    def _process_round(self, current_num):
        """Обработка одного раунда угадывания"""
        self.attempts_count += 1
        guess = self._get_user_guess()
        
        if guess == current_num:
            self.score += 1
            print(f"✅ Верно! Это было число {current_num}")
        else:
            print(f"❌ Не угадал! Это было число {current_num}")
        
        print(f"Текущий счет: {self.score}/{self.attempts_count}")

    def start(self):
        """Основной метод для запуска игры"""
        self._prepare_game()
        
        while self.numbers:
            current_num = self.numbers.pop()
            print(f"\nОсталось чисел: {len(self.numbers)}")
            self._process_round(current_num)
        
        print(f"\n🎮 Игра окончена! Твой финальный счет: {self.score}/{self.attempts_count}")
        return self.score


if __name__ == "__main__":
    # Создаем экземпляр игры с настройками
    game = NumberGuessingGame(min_num=1, max_num=9)
    
    # Запускаем игру и получаем финальный счет
    final_score = game.start()
    
    # Дополнительная логика обработки результата
    if final_score == game.attempts_count:
        print("🔥 Потрясающе! Ты угадал все числа!")
    elif final_score / game.attempts_count > 0.7:
        print("👍 Хороший результат!")
