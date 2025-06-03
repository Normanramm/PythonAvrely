from random import uniform

# Генерируем случайное число с одним знаком после точки
drobnoe = round(uniform(0, 10), 1)

# Получаем ввод пользователя, преобразуем в float с одним знаком
try:
    user_guess = round(
        float(input("Угадайте число от 0 до 10 (с точностью до 0.1): ")), 1)
except ValueError:
    print("Ошибка! Введите число.")
    exit()

# Проверяем угадал ли пользователь
if user_guess == drobnoe:
    print(f"Поздравляю! Вы угадали число {drobnoe:.1f}")
else:
    print(f"К сожалению, вы не угадали. Загаданное число было {drobnoe:.1f}")


# ____________________________________________________________________________________________


class NumberGuessingGame:
    def __init__(self, min_num=0, max_num=10):
        self.min_num = min_num
        self.max_num = max_num
        self.target_number = self._generate_number()
        self.attempts = 0

    def _generate_number(self):
        """Генерирует случайное число с одним знаком после точки"""
        return round(uniform(self.min_num, self.max_num), 1)

    def _get_user_guess(self):
        """Получает и проверяет ввод пользователя"""
        while True:
            try:
                guess = input(
                    f"Угадайте число от {self.min_num} до {self.max_num} (с точностью до 0.1): ")
                return round(float(guess), 1)
            except ValueError:
                print("Ошибка! Введите корректное число.")

    def check_guess(self, guess):
        """Проверяет, угадал ли пользователь"""
        self.attempts += 1
        if guess == self.target_number:
            print(
                f"Поздравляю! Вы угадали число {self.target_number:.1f} за {self.attempts} попыток.")
            return True
        elif guess < self.target_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
        return False

    def play(self):
        """Основной игровой цикл"""
        print(
            f"Угадайте число от {self.min_num} до {self.max_num} (с точностью до 0.1)")

        while True:
            user_guess = self._get_user_guess()
            if self.check_guess(user_guess):
                break


# Запуск игры
if __name__ == "__main__":
    game = NumberGuessingGame(min_num=0, max_num=10)
    game.play()
