def practic():
    """Обычный стиль"""
    temperature = int(input())
    if temperature < -4:
        print("Морозно")
    elif -4 <= temperature < 0:
        print("Холодно")
    elif 0 <= temperature < 12:
        print("Прохладно")
    elif 12 <= temperature < 27:
        print("Тепло")
    else:
        print("Жарко")


practic()
# ___________________________________________________________________________


class QuestionChecker:
    def __init__(self):
        self.question1 = "Сейчас день?"
        self.question2 = "На улице солнечно?"
        self.positive_response = "Отличное время для прогулки!"
        self.negative_response = "Посидите лучше дома"

    def ask_questions(self):
        answer1 = input(self.question1 + " ").lower().strip()
        answer2 = input(self.question2 + " ").lower().strip()

        if answer1 == "да" and answer2 == "да":
            print(self.positive_response)
        else:
            print(self.negative_response)


checker = QuestionChecker()
checker.ask_questions()


# ___________________________________________________________________________


class TemperatureAnalyzer:
    """Добавил ООП"""

    def __init__(self, temperature):
        self.temperature = temperature

    def analyze(self):
        if self.temperature < -4:
            return "Морозно"
        elif -4 <= self.temperature < 0:
            return "Холодно"
        elif 0 <= self.temperature < 12:
            return "Прохладно"
        elif 12 <= self.temperature < 27:
            return "Тепло"
        else:
            return "Жарко"

    def print_result(self):
        print(self.analyze())


if __name__ == "__main__":
    temp = int(input("Введите температуру: "))
    analyzer = TemperatureAnalyzer(temp)
    analyzer.print_result()


# ___________________________________________________________________________


class TemperatureAnalyz:
    """Добавил ООП и оператор and"""

    def __init__(self, temperatur):
        self.temperatur = temperatur

    def analyze(self):
        if self.temperatur < -4:
            return "Морозно"
        elif self.temperatur >= -4 and self.temperatur < 0:
            return "Холодно"
        elif self.temperatur >= 0 and self.temperatur < 12:
            return "Прохладно"
        elif self.temperatur >= 12 and self.temperatur < 27:
            return "Тепло"
        elif self.temperatur >= 27:
            return "Жарко"

    def print_result(self):
        print(self.analyze())


if __name__ == "__main__":
    temp = int(input("Введите температуру: "))
    analyzer = TemperatureAnalyz(temp)
    analyzer.print_result()


# _______________________________________________________________________

class MoodChecker:
    """Добавил or"""

    def __init__(self):
        self.question = "Ваши дела хороши? "
        self.positive_answer = "Отлично!"
        self.negative_answer = "Жаль.."

    def check_mood(self):
        answer = input(self.question).lower().strip()
        if answer == "да" or answer == "ага":
            print(self.positive_answer)
        else:
            print(self.negative_answer)


mood_checker = MoodChecker()
mood_checker.check_mood()


# ___________________________________________________________________________

class WeatherMoodChecker:
    """Добавил сравнение на равенство or, and"""

    def __init__(self):
        self.question1 = "Сейчас день? "
        self.question2 = "На улице солнечно? "
        self.good_message = "Отличное время для прогулки!"
        self.bad_message = "Посидите лучше дома"

    def check_conditions(self):
        answer1 = input(self.question1).lower().strip()
        answer2 = input(self.question2).lower().strip()

        if (answer1 == "да" or answer1 == "ага") and (answer2 == "да" or answer2 == "ага"):
            print(self.good_message)
        else:
            print(self.bad_message)


checker = WeatherMoodChecker()
checker.check_conditions()
