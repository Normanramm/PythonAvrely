class QuestionChecker:
    def __init__(self):
        self.text = input("Введите строку: ")

    def ask_questions(self):

        position = (self.text).find("#")
        if position != -1:
            print("Найдено. Позиция:", self.text[:position])

        else:
            print(self.text)


checker = QuestionChecker()
checker.ask_questions()