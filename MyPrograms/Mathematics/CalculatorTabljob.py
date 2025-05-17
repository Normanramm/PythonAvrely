# Создаем пустой список для хранения чисел
numbers = []

# Запрашиваем у пользователя ввод чисел
while True:
    user_input = input("Введите число (и 'ok' для сложения): ")
    if user_input == 'ok' and 'ок':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")

# Складываем все числа в списке
total_sum = sum(numbers)

# Считаем количество чисел в списке
total_coll = len(numbers)

# Выводим результат
print(f"Сумма введенных чисел: {total_sum}")
print(f'Количество чисел: {total_coll}')