word = 'python'
name_word = input().lower()

if word in name_word:
    print('Такое писать нельзя, извините.')
else:
    print('Сообщение принято')


# ____________________________________________________

class QuestionChecker:
    def __init__(self):
        self.question1 = "Введите текст:"
        self.positive_response = "Такое писать нельзя, извините."
        self.negative_response = "Сообщение принято"

    def ask_questions(self):
        answer1 = input(self.question1 + " ").lower()
        word = "python"

        if word in answer1:
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()

# __________________________________________________


class QuestionChecker:
    def __init__(self):
        self.question1 = "Введите текст:"
        self.positive_response = "Такое писать нельзя, извините."
        self.negative_response = "Сообщение принято"
        self.word = "python"

    def ask_questions(self):
        answer1 = input(self.question1 + " ").lower()

        if self.word in answer1:
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()

# ______________________________________________


class QuestionChecker:
    def __init__(self):
        self.question1 = "Введите текст: "
        self.positive_response = "Такое писать нельзя, извините."
        self.negative_response = "Сообщение принято"
        self.forbidden_words = ["python", "PYTHON", "Python"]

    def ask_questions(self):
        answer = input(self.question1).strip()

        if any(word.lower() in answer.lower() for word in self.forbidden_words):
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()
