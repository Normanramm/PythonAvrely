class QuestionChecker:
    def __init__(self):
        self.stroka = input("Введите строку: ")
        self.positive_response = "Принято!"
        self.negative_response = "Ошибка!"

    def ask_questions(self):
        if len(self.stroka) == 8 and not self.stroka[0].isdigit():
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()