def calculator():
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    try:
        operation = input("Введите операцию (+, -, *, /): ")
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))

        result = operations[operation](a, b)
        print("Результат:", result)

    except ValueError:
        print("Ошибка: неверный формат числа.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except KeyError:
        print("Ошибка: неизвестная операция.")


calculator()

