# По простому_________________________________________
qwerty = input()
qwerty_2 = input()

qwerty, qwerty_2 = qwerty_2, qwerty

print(qwerty, qwerty_2)


# C ООП______________________________________________
class ValueSwapper:
    def __init__(self):
        self.first_value = ""
        self.second_value = ""

    def get_input(self):
        """Запрашивает у пользователя два значения"""
        self.first_value = input("Введите первое значение: ")
        self.second_value = input("Введите второе значение: ")

    def swap_values(self):
        """Меняет значения местами"""
        self.first_value, self.second_value = self.second_value, self.first_value

    def show_result(self):
        """Выводит результат после обмена"""
        print("После обмена:")
        print(f"Первое значение: {self.first_value}")
        print(f"Второе значение: {self.second_value}")

# === Основная часть программы ===
if __name__ == "__main__":
    swapper = ValueSwapper()
    swapper.get_input()
    swapper.swap_values()
    swapper.show_result()