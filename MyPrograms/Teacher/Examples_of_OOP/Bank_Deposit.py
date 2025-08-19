my_money = float(input('Начальная сумма денег: '))
year_procent = float(input('Годовая ставка в процентах: '))
years = int(input('На какое количество лет: '))

for _ in range(years):
    my_money += my_money * (year_procent / 100)

print(f"Через {years} лет на вашем счету будет: {my_money:.2f}")


# _______________________________________________________

# Создаем класс для работы с депозитами
class BankDeposit:
    def __init__(self):
        self.initial_amount = 0.0
        self.interest_rate = 0.0
        self.years = 0
        self.final_amount = 0.0

    def get_user_input(self):
        """Получаем данные от пользователя"""
        self.initial_amount = float(input('Начальная сумма денег: '))
        self.interest_rate = float(input('Годовая ставка в процентах: '))
        self.years = int(input('На какое количество лет: '))

    def calculate_final_amount(self):
        """Рассчитываем итоговую сумму с процентами"""
        self.final_amount = self.initial_amount
        for _ in range(self.years):
            self.final_amount += self.final_amount * (self.interest_rate / 100)

    def display_result(self):
        """Выводим результат"""
        print(
            f"\nЧерез {self.years} лет на вашем счету будет: {self.final_amount:.2f}")

    def run(self):
        """Основной метод для запуска программы"""
        self.get_user_input()
        self.calculate_final_amount()
        self.display_result()


# Создаем экземпляр класса и запускаем программу
if __name__ == "__main__":
    deposit = BankDeposit()
    deposit.run()


#______________________________________________________

class BankDeposit:
    def __init__(self):
        """Инициолизируем конструктор"""
        self.my_money = 0.0
        self.years_procent = 0.0
        self.years = 0

    def get_user_money(self):
        """Запрос от пользователя"""
        self.my_money = float(input("Введите сумму вклада: "))
        self.years_procent = float(input("Введите процент годовых: "))
        self.years = int(input("Введите срок вклада в годах: "))

    def calculate_deposit(self):
        """Тут делаем расчет"""
        for _ in range(self.years):
            self.my_money += self.my_money * (self.years_procent / 100)

    def print_result(self):
        """Вывод результата"""
        print(
            f"\n Через {self.years} года вы получите {self.my_money:.2f} денег.")

    def run(self):
        """Запуск функций"""
        self.get_user_money()
        self.calculate_deposit()
        self.print_result()

# Запуск программы
if __name__ == "__main__":
    bd = BankDeposit()
    bd.run()


#______________________________________________________
# Создаем класс для работы с депозитами while

class BankDeposit:
    def __init__(self):
        """Инициализация и получение данных от пользователя"""
        self.my_money = self._get_positive_float("Введите сумму вклада: ")
        self.years_procent = self._get_positive_float("Введите процент годовых: ")
        self.years = self._get_positive_int("Введите срок вклада в годах: ")
    
    def _get_positive_float(self, prompt):
        """Получение положительного числа с плавающей точкой"""
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Значение должно быть положительным!")
                    continue
                return value
            except ValueError:
                print("Ошибка! Введите число.")
    
    def _get_positive_int(self, prompt):
        """Получение положительного целого числа"""
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Значение должно быть положительным!")
                    continue
                return value
            except ValueError:
                print("Ошибка! Введите целое число.")
    
    def calculate_deposit(self):
        """Расчет вклада с использованием цикла while"""
        current_year = 1
        while current_year <= self.years:
            self.my_money += self.my_money * (self.years_procent / 100)
            current_year += 1
    
    def show_result(self):
        """Отображение результата"""
        print(f"\nЧерез {self.years} лет на вашем счету будет: {self.my_money:.2f}")
    
    def run(self):
        """Запуск программы"""
        self.calculate_deposit()
        self.show_result()


# Использование класса
if __name__ == "__main__":
    deposit = BankDeposit()
    deposit.run()


#______________________________________________________
# Вместе с while for

class BankDeposit:
    def __init__(self):
        """Инициализация параметров"""
        self.my_money = 0.0
        self.years_procent = 0.0
        self.years = 0
        self.my_money_for = 0.0
        self.my_money_while = 0.0

    def get_user_input(self):
        """Получение данных от пользователя"""
        self.my_money = float(input("Введите сумму вклада: "))
        self.years_procent = float(input("Введите процент годовых: "))
        self.years = int(input("Введите срок вклада в годах: "))

        # Сохраняем исходную сумму для второго расчета
        self.my_money_for = self.my_money
        self.my_money_while = self.my_money

    def calculate_deposit_for(self):
        """Расчет с использованием цикла for"""
        for _ in range(self.years):
            self.my_money_for += self.my_money_for * (self.years_procent / 100)

    def calculate_deposit_while(self):
        """Расчет с использованием цикла while"""
        current_year = 1
        while current_year <= self.years:
            self.my_money_while += self.my_money_while * \
                (self.years_procent / 100)
            current_year += 1

    def print_for_result(self):
        """Вывод результата для цикла for"""
        print("\nРезультат с циклом for:")
        print(
            f"Через {self.years} лет на вашем счету будет: {self.my_money_for:.2f}")

    def print_while_result(self):
        """Вывод результата для цикла while"""
        print("\nРезультат с циклом while:")
        print(
            f"Через {self.years} лет на вашем счету будет: {self.my_money_while:.2f}")

    def run(self):
        """Основной метод выполнения программы"""
        self.get_user_input()

        # Расчет и вывод для for
        self.calculate_deposit_for()
        self.print_for_result()

        # Расчет и вывод для while
        self.calculate_deposit_while()
        self.print_while_result()


# Запуск программы
if __name__ == "__main__":
    deposit = BankDeposit()
    deposit.run()
