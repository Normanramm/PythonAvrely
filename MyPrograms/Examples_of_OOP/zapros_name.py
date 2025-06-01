class QuestionChecker:
    def __init__(self):
        self.question1 = "Как тебя зовут? "
        self.positive_response = "Привет,"
        self.negative_response = "Придумай имя!"

    def ask_questions(self):
        answer1 = input(self.question1 + " ").title().strip()

        if answer1:
            print(f'{self.positive_response} {answer1}!')
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()