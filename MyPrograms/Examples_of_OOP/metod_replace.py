text = input()
word = 'кот'

if word in text:
    new_text = text.replace('кот', 'собака')
    print(new_text)
else:
    print(text)

# ______________________________________________________________


class QuestionChecker:
    def __init__(self):
        self.question1 = "кот съел котлету"

    def ask_questions(self):
        answer1 = (self.question1).lower().replace('кот', 'собака')
        word = "кот"

        if word not in answer1:
            print(answer1)


checker = QuestionChecker()
checker.ask_questions()

# _____________________________________________________________


class QuestionChecker:
    def __init__(self, origin_text="кот съел котлету"):
        self.origin_text = origin_text
        self.question1 = "кот"
        self.question2 = "собака"

    def ask_questions(self):
        """Заменяет указанное слово в тексте и возвращает результат"""
        modified_text = self.origin_text.lower().replace(
            self.question1,
            self.question2
        )
        return modified_text

    def print_questions(self):
        """Показывает результат замены, если слово было найдено"""
        new_text = self.ask_questions()
        if self.question1 in self.origin_text.lower():
            print(self.origin_text)
            print(new_text)
        else:
            print("Слово для замены не найдено!")


if __name__ == "__main__":
    checker = QuestionChecker()
    checker.print_questions()

    user_text = input("Замена слова вручную: ")
    user_text2 = QuestionChecker(user_text)
    user_text2.print_questions()
