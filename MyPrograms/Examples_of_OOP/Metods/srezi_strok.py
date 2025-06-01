class QuestionChecker:
    def __init__(self):
        self.stroka = input("Введите строку: ")

    def ask_questions(self):
        if len(self.stroka) > 15:
            print(f'{self.stroka[:15]}...')

        else:
            print(self.stroka)


checker = QuestionChecker()
checker.ask_questions()