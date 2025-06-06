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
