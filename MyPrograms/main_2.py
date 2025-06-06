class BankDeposit:
    def __init__(self):
        """Инициоизируем конструктор"""
        self.my_money = 0.0
        self.years_procent = 0.0
        self.years = 0
        
    def get_user_money(self):
        """Запрос от пользователя"""
        self.my_money = float(input("Введите сумму вклада: "))
        self.years_procent = float(input("Введите процент годовых: "))
        self.years = int(input("Введите срок вклада в годах: "))

    def calculate_deposit_for(self):
        """Тут делаем расчет for"""
        for _ in range(self.years):
            self.my_money += self.my_money * (self.years_procent / 100)
            

    def calculate_deposit_while(self):
        """Тут делаем расчет while"""
        current_year = 1
        while current_year <= self.years:
            self.my_money += self.my_money * (self.years_procent / 100)
            current_year += 1
            

    def print_result(self):
        """Вывод результата"""
        print(
            f"\n Через {self.years} года вы получите {self.my_money:.2f} денег.")

    def run(self):
        """Запуск функций"""
        self.get_user_money()
        self.calculate_deposit_for()
        self.calculate_deposit_while()
        self.print_result()


# Запуск программы
if __name__ == "__main__":
    bd = BankDeposit()
    bd.run()
