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
