
                            
                            # Итератор
my_list = [1, 2, 3]
my_iter = iter(my_list)
next(my_iter)  # 1
next(my_iter)  # 2
# Генератор
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)
# Generator expression
squares = (x**2 for x in range(10))
# itertools
from itertools import count, cycle, chain
for i in count(0, 2):
    print(i)  # 0, 2, 4...


