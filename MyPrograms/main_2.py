import data_sandbox

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
