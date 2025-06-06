class VowelCounter:
    """Ищем гласные буквы"""

    def __init__(self):
        self.zapros = input("Введите строку: ").lower()
        self.bukva = "аоуэыиеёюя"
        self.positive_one = "for/В строке есть гласные буквы"
        self.positive_two = "while/В строке есть гласные буквы"

    def looking_vowels(self):
        """Ищем гласные буквы for"""
        count = 0
        for i in self.zapros:
            if i in self.bukva:
                count += 1
        print(f'{self.positive_one} - {count} шт.')

    def looking_vowels_two(self):
        """Ищем гласные буквы while"""
        count = 0
        index = 0  # Начинаем с первого символа (индекс 0)

        while index < len(self.zapros):
            if self.zapros[index] in self.bukva:
                count += 1
            index += 1  # Переходим к следующему символу

        print(f'{self.positive_two} - {count} шт.')


qwerty = VowelCounter()
qwerty.looking_vowels()
qwerty.looking_vowels_two()

# ____________________________________________________________
# усовершенствоавал добавил вывод согласных букв и их подсчет

class VowelCounter:
    """Ищем гласные буквы и выводим согласные"""

    def __init__(self):
        self.zapros = input("Введите строку: ").lower()
        self.bukva = "аоуэыиеёюя"
        self.russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.positive_one = "for/В строке есть гласные буквы"
        self.positive_two = "while/В строке есть гласные буквы"
        self.positive_three = "Согласные буквы в строке"

    def looking_vowels(self):
        """Ищем гласные буквы for"""
        count = 0
        for i in self.zapros:
            if i not in self.bukva:
                continue
            count += 1
        print(f'{self.positive_one} - {count} шт.')

    def looking_vowels_two(self):
        """Ищем гласные буквы while"""
        count = 0
        index = 0  # Начинаем с первого символа (индекс 0)

        while index < len(self.zapros):
            if self.zapros[index] not in self.bukva:
                index += 1
                continue

            count += 1
            index += 1  # Переходим к следующему символу

        print(f'{self.positive_two} - {count} шт.')

    def print_soglsnie(self):
        """Выводим согласные буквы"""
        soglasnie = ""
        self.russian_alphabet = self.russian_alphabet

        for char in self.zapros:
            if char not in self.russian_alphabet:
                continue  # Пропускаем не-буквы
            if char in self.bukva:
                continue  # Пропускаем гласные
            soglasnie += char

        print(f"{self.positive_three} - {soglasnie} - {len(soglasnie)} шт.")


# Создаём экземпляр и вызываем методы
qwerty = VowelCounter()
qwerty.looking_vowels()
qwerty.looking_vowels_two()
qwerty.print_soglsnie()



# ____________________________________________________________
# еще доусовршенствованный вариант и добавил подсчет согласных букв

class VowelCounter:
    """Ищем гласные буквы и выводим согласные"""

    def __init__(self):
        self.zapros = input("Введите строку: ").lower()
        self.bukva = "аоуэыиеёюя"
        self.positive_one = "for/В строке есть гласные буквы"
        self.positive_two = "while/В строке есть гласные буквы"
        self.positive_three = "Согласные буквы в строке"

    def looking_vowels(self):
        """Ищем гласные буквы for"""
        count = 0
        for i in self.zapros:
            if i not in self.bukva:
                continue
            count += 1
        print(f'{self.positive_one} - {count} шт.')

    def looking_vowels_two(self):
        """Ищем гласные буквы while"""
        count = 0
        index = 0  # Начинаем с первого символа (индекс 0)

        while index < len(self.zapros):
            if self.zapros[index] not in self.bukva:
                index += 1
                continue

            count += 1
            index += 1  # Переходим к следующему символу

        print(f'{self.positive_two} - {count} шт.')

    def print_soglasnie(self):

        soglasnie_count = {}  # Словарь для подсчёта согласных

        for i in self.zapros:
            if i in self.bukva or not i.isalpha():
                continue  # Пропускаем гласные и не-буквы

            # Увеличиваем счётчик для текущей согласной
            soglasnie_count[i] = soglasnie_count.get(i, 0) + 1

        # Выводим результаты
        print("Согласные буквы и их количество:")
        for letter, count in soglasnie_count.items():
            print(f"{letter} - {count} шт.", end=" | ")
        print(f"\nВсего согласных: {sum(soglasnie_count.values())}")


if __name__ == '__main__':
    # Создаём экземпляр и вызываем методы
    qwerty = VowelCounter()
    qwerty.looking_vowels()
    qwerty.looking_vowels_two()
    qwerty.print_soglasnie()
