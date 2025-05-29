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

