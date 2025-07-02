class NumberSorter:
    def __init__(self):
        self.input_str = ""
        self.numbers = []

    def get_input(self):
        """Получает строку от пользователя"""
        self.input_str = input("Введите числа через пробел: ")

    def filter_numbers(self):
        """Оставляет только целые положительные числа"""
        self.numbers = []
        for part in self.input_str.split():
            if part.isdigit():  # Проверяем, что это целое число
                self.numbers.append(int(part))

    def sort_numbers(self):
        """Сортирует числа в порядке убывания"""
        self.numbers.sort(reverse=True)

    def show_result(self):
        """Выводит результат"""
        print("Отсортированные целые числа в порядке убывания:", *self.numbers)

# === Основная часть программы ===
if __name__ == "__main__":
    sorter = NumberSorter()
    sorter.get_input()
    sorter.filter_numbers()
    sorter.sort_numbers()
    sorter.show_result()
