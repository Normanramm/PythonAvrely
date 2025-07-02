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