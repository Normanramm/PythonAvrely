class QuestionChecker:
    def __init__(self):
        self.stroka = input("Введите строку: ")
        self.index_stroka = len(self.stroka) // 2

        self.positive_response = "Четная строка!"
        self.negative_response = "Нечетная строка!"

    def ask_questions(self):
        if len(self.stroka) % 2 != 0:
            print(self.stroka[self.index_stroka])
            print(self.negative_response)
        else:
            print(self.positive_response)


checker = QuestionChecker()
checker.ask_questions()


# По условиям задачи Leypy_____________________________________________

class QuestionChecker:
    def __init__(self):
        self.stroka = input("Введите строку: ")
        self.index_stroka = len(self.stroka) // 2

    def ask_questions(self):
        if len(self.stroka) % 2 != 0:
            print(self.stroka[self.index_stroka])

        else:
            print("Длина строки должна быть нечетной")


checker = QuestionChecker()
checker.ask_questions()
