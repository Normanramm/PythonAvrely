


choice = input("Введите числа через пробел: ")
numbers = [int(num) for num in choice.split() if num.lstrip('-').isdigit()]
print(f"Сумма чисел: {sum(numbers)}")
