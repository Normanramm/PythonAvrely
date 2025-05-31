class QuestionChecker:
    def __init__(self):
        # Сохраняем оригинальные вводы для вычислений
        self.number1 = input("Первое число: ")
        self.number2 = input("Второе число: ")

        # Очищенные версии для проверки
        self.clean1 = self.number1.lstrip('-').replace('.', '', 1)
        self.clean2 = self.number2.lstrip('-').replace('.', '', 1)

        self.positive_response = "Правильно!"
        self.negative_response = "Нужно вывести два числа."

    def ask_questions(self):
        if self.clean1.isdigit() and self.clean2.isdigit():
            # Преобразуем оригинальные вводы в числа
            num1 = float(self.number1)
            num2 = float(self.number2)
            print(f'Сумма двух чисел: {num1 + num2}')
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()


# Без метода isdigit() с проверкой try/except
# ___________________________________________________________
class QuestionChecker:
    def __init__(self):
        self.number1 = input("Первое число: ")
        self.number2 = input("Второе число: ")
        self.positive_response = "Правильно!"
        self.negative_response = "Нужно вывести два числа."

    def ask_questions(self):
        # Проверяем, что введены числа (целые или с плавающей точкой)
        try:
            num1 = float(self.number1)
            num2 = float(self.number2)
            print(f'Сумма двух чисел: {num1 + num2}')
            print(self.positive_response)
        except ValueError:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()


# ___________________________________________________________
class QuestionChecker:
    def __init__(self):
        try:
            self.number1 = float(input("Первое число: "))
            self.number2 = float(input("Второе число: "))
        except ValueError:
            print("Ошибка: нужно ввести числа")
            exit()

        self.positive_response = "Правильно!"
        self.negative_response = "Нужно вывести два числа."

    def ask_questions(self):
        if self.number1 is not None and self.number2 is not None:
            print(f"Сумма чисел: {self.number1 + self.number2}")
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()
