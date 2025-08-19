class WeatherMoodChecker:

    def __init__(self):
        self.question = "Введите текст: "
        self.good_message = "Да, это палиндром"
        self.bad_message = "Нет, это не палиндром"

    def check_conditions(self):
        answer = input(self.question).lower().strip()
        clear_answer = answer.replace('.', '').replace(
            ',', '').replace('!', '').replace('?', '').replace(' ', '')

        if clear_answer[::-1] == clear_answer:
            print(self.good_message)
        else:
            print(self.bad_message)


checker = WeatherMoodChecker()
checker.check_conditions()