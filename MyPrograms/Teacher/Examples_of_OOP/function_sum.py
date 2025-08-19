user_s = input()
numbers = []

for i in user_s.split():
    if i.lstrip('-').isdigit():
        numbers.append(int(i))
    else:
        print("Введите числа, дробные тоже нельзя!")

print(sum(numbers))

# _________________________________________________
choice = input("Введите числа: ")
numbers = []
for item in choice.split():
    try:
        numbers.append(int(item))
    except ValueError:
        pass
print(f"Сумма: {sum(numbers)}")


#___________________________________________________

choice = input("Введите числа через пробел: ")
numbers = [int(num) for num in choice.split() if num.lstrip('-').isdigit()]
print(f"Сумма чисел: {sum(numbers)}")