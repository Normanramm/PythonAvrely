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

