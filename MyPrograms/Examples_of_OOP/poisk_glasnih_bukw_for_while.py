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
