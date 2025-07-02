# Метод sort________________________________________________________

choice = input("Введите числа через пробел: ")
numbers = []

for i in choice.split():
    if i.isdigit():
        numbers.append(int(i))

# Сортировка на месте с помощью .sort()
numbers.sort(reverse=True)

print(numbers)


# Метод sorted________________________________________________________

choice = input("Введите числа через пробел: ")
numbers = []

for i in choice.split():
    if i.isdigit():
        numbers.append(int(i))

choice_sort = sorted(numbers, reverse=True)
print(choice_sort)


# Метод sort с OOP________________________________________________________

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


# Метод sorted с OOP________________________________________________________

class Sortirivshik:
    def __init__(self):
        self.choice = ''
        self.number = []

    def get_input(self):
        self.choice = input("Введите числа через пробел: ")

    def sortirovka(self):
        self.numbers = []
        for i in self.choice.split():
            if i.isdigit():
                self.numbers.append(int(i))

    def sort(self):
        self.choice_sort = sorted(self.numbers, reverse=True)

    def result(self):
        print("Отсортированные целые числа в порядке убывания:", self.choice_sort)


if __name__ == '__main__':
    sortirivshik = Sortirivshik()
    sortirivshik.get_input()
    sortirivshik.sortirovka()
    sortirivshik.sort()
    sortirivshik.result()
