class IMTclass:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_imt(self):
        return self.weight / ((self.height / 100) ** 2)

    def interpret(self, imt):
        if imt < 18.5:
            return "Недостаточный вес"
        elif imt >= 18.5 and imt < 25:
            return "Нормальный вес"
        elif imt >= 25 and imt < 30:
            return "Избыточный вес"
        elif imt >= 30:
            return "Ожирение"
        else:
            return "Вызывай врача"


try:
    while True:
        weight = float(input('Введите вес в килограммах: ').replace(',', '.'))
        height = float(input('Введите рост в сантиметрах: ').replace(',', '.'))
        imt = IMTclass(weight, height)
        print(imt.interpret(imt.calculate_imt()))
except ValueError:
    print('Ошибка! Введите число.')