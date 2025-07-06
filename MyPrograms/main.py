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
            print(f"🤑 Вы угадали число {numbers_choice}!")
        else:
            print(f"🤬 Вы не угадали число {numbers_choice}!")

        print(f"\nПобед: {i} из {len(range(1, 10)) - len(number)}")

    print(f"\n💤 Игра окончена! Результат: {i}")


if __name__ == '__main__':
    number_choice()
