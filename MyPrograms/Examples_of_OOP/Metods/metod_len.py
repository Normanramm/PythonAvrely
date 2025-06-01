class QuestionChecker:
    def __init__(self):
        self.question1 = "Введите строку: "
        self.positive_response = "Отлично!"
        self.negative_response = "Строка слишком коротка."

    def ask_questions(self):
        answer1 = input(self.question1 + " ").lower().strip()

        if len(answer1) > 6:
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()
