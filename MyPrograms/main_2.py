import random


class NumberChoiceGame:
    def __init__(self):
        self.numbers = list(range(1, 10))
        random.shuffle(self.numbers)
        self.wins = 0

    def start(self):
        print("🤖 Игра началась!")

        while self.numbers:
            numbers_choice = self.numbers.pop()
            print(f"\nОсталось чисел: {len(self.numbers)}")

            try:
                user_choice = int(input("Введите число от 1 до 9: "))
            except ValueError:
                print("☠ 🤡 Вы ввели не число 🤡 ☠")
                continue

            if user_choice == numbers_choice:
                self.wins += 1
                print(f"🤑 Вы угадали, число {numbers_choice}!")
            else:
                print(f"🤬 Вы не угадали, число {numbers_choice}!")

            total_result = 9 - len(self.numbers)
            print(f"\nПобед: {self.wins} из {total_result}")

        print(f"\n💤 Игра окончена! Результат: {self.wins} 💤")


if __name__ == "__main__":
    game = NumberChoiceGame()
    game.start()
