choice = input("Введите числа через пробел: ")
numbers = []

for i in choice.split():
    if i.isdigit():
        numbers.append(int(i))

choice_sort = sorted(numbers, reverse=True)
print(choice_sort)
 

