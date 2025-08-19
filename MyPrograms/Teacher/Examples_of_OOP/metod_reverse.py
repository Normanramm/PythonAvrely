# Обычный способ________________________________________
numbers = input().split()
numbers.reverse()
print(numbers) 

# Добавил вывод строкой________________________________
numbers = input().split()
numbers.reverse()
number = ' '.join(numbers)
print(number)  

# Превратил в класс____________________________________
class NumbersReverser:
    def __init__(self):
        self.numbers = []

    def number_input(self):
        self.numbers = input("Введи текст: ").split()

    def number_replace(self):
        self.numbers.reverse()

    def number_join(self):
        return ' '.join(self.numbers)


if __name__ == '__main__':
    numbers = NumbersReverser()
    numbers.number_input()
    numbers.number_replace()
    print(f"Перевернутый текст: {numbers.number_join()}")