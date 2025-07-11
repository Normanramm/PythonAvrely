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
        self.number = []
        for i in self.choice.split():
            if i.isdigit():
                self.number.append(int(i))

    def sort(self):
        self.choice_sort = sorted(self.number, reverse=True)

    def result(self):
        print("Отсортированные целые числа в порядке убывания:", self.choice_sort)


if __name__ == '__main__':
    sortirivshik = Sortirivshik()
    sortirivshik.get_input()
    sortirivshik.sortirovka()
    sortirivshik.sort()
    sortirivshik.result()


# Используем key для сортировки_______________________________________________

import data_sandbox # тут готовый список студентов типо

number = (data_sandbox.get_students()) # тут готовый список студентов типо
choice_sort = sorted(number, key=lambda student: student[1], reverse=True)
print("Отсортированные целые числа в порядке убывания:", choice_sort)

# Используем key с OOP_______________________________________________________

import data_sandbox # тут готовый список студентов типо

class StudentSorter:
    def __init__(self):
        self.students = []

    def load_students(self):
        """Загружает данные о студентах из внешнего модуля"""
        self.students = data_sandbox.get_students() # тут готовый список студентов типо

    def sort_students(self):
        """Сортирует студентов по оценке (второй элемент кортежа) по убыванию"""
        self.students = sorted(self.students, key=lambda student: student[1], reverse=True)

    def display_sorted_list(self):
        """Выводит отсортированный список студентов"""
        print("Отсортированные студенты по оценке (по убыванию):")
        for name, score in self.students:
            print(f"{name}: {score}")

# === Основная часть программы ===
if __name__ == "__main__":
    sorter = StudentSorter()
    sorter.load_students()
    sorter.sort_students()
    sorter.display_sorted_list()


# С использованием key, enumerate с OOP________________________________________

import data_sandbox # тут готовый список студентов типо

class StudentSorter:
    def __init__(self):
        self.students = []

    def load_students(self):
        """Загружает данные о студентах из внешнего модуля"""
        self.students = data_sandbox.get_students()

    def sort_students(self):
        """Сортирует студентов по оценке (второй элемент кортежа) по убыванию"""
        self.students = sorted(self.students, key=lambda student: student[1], reverse=True)

    def display_sorted_list(self):
        """Выводит отсортированный список студентов с нумерацией"""
        print("Рейтинг студентов по убыванию оценок:")
        for index, (name, score) in enumerate(self.students, start=1):
            print(f"{index}. {name}: {score}")

# === Основная часть программы ===
if __name__ == "__main__":
    sorter = StudentSorter()
    sorter.load_students()
    sorter.sort_students()
    sorter.display_sorted_list()



#_________________________________________________________

from data_sandbox import get_random_search_queries

queries = get_random_search_queries()
my_dict = {}

for query in queries:
    my_dict.setdefault(query, 0)
    my_dict[query] += 1


query_count_list = [(query, count) for query, count in my_dict.items()]
sorted_query = sorted(query_count_list, key=lambda x: x[1])
print(sorted_query)