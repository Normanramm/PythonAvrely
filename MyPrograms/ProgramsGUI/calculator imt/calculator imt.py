# Калькулятор IMT

try:
    while True:
        kg = float(input('Введите вес в килограммах: ').replace(',', '.'))
        rost = float(input('Введите рост в сантиметрах: ').replace(',', '.'))
        imt = kg / ((rost / 100) ** 2)

        if imt < 18.5:
            print("Недостаточный вес")
        elif imt >= 18.5 and imt < 25:
            print("Нормальный вес")
        elif imt >= 25 and imt < 30:
            print("Избыточный вес")
        elif imt >= 30:
            print("Ожирение")
        else:
            print("Вызывай врача")

except ValueError:
    print('Ошибка! Введите число.')