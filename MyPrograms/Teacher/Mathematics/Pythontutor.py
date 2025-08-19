# Сколько прошло времени между часами_____

# первое решение
import datetime

a = datetime.timedelta(hours=13, minutes=30, seconds=43)
b = datetime.timedelta(hours=14, minutes=00, seconds=00)
print(str(b - a))

# второе решение
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
print((x - a) * 3600 + (y - b) * 60 + z - c)

# Задача улитка(за сколько дней проползет)_____

# первое решение
h = int(input())  # высота
a = int(input())  # поднимаясь в день
b = int(input())  # спускаясь за ночь
i = 0
dn = 0
while i < h:
    i += a
    dn += 1
    if i >= h:
        break
    i -= b
print(dn)

# второе решение
h = int(input())
a = int(input())
b = int(input())
print(int((h - a - 1) // (a - b) + 2))

# Дано натуральное число. Найдите число десятков в его десятичной записи_____
n = int(input())
print(n // 10 % 10)

# Дано трехзначное число. Найдите сумму его цифр_____

# первый вариант
n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)

# второй вариант
a = (input())
b = int(a[0:1])
c = int(a[1:2])
e = int(a[2:3])
print(b + c + e)

# Процентная ставка через год

p = int(input())  # процент
x = int(input())  # рубли
y = int(input())  # копейки
money_before = 100 * x + y
money_after = int(money_before * (100 + p) / 100)
print(money_after // 100, money_after % 100)

# Цикл for______________________________________________________________________________

# Ряд - 1___

a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(i, end=' ')

# Ряд - 2___
# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')

# Ряд - 3___
# Даны два целых числа A и В, A>B
# Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

a = int(input())
b = int(input())

for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')

# Факториал числа___

n = int(input())
sum = 1
for i in range(1, n + 1):
    sum *= i
print(sum)

# Cумма факториалов числа___

n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)

# Подсчет количества нулей___

num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

# Лесенка___

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()

# Потерянная карточка___

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
# можно доказать формулу:
# sum == n * (n + 1) // 2
# но мы посчитаем это значение циклом
for i in range(n - 1):
    sum -= int(input())
print(sum)

# По данному натуральному n вычислите сумму 13+23+33+...+n3.___

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)

# Сумма N чисел___

n = int(input())
sum = 0
for i in range(n):
    number = int(input())
    sum += number
print(sum)

# Сумма десяти чисел___
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)

# Строки________________________________________________________________________________________

# Количество слов___
q = (input().count(' ') + 1)
print(q)

# Две половинки(переставить метсами слова)___
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# Переставте два слова___

s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)

# второй вариант

s = input()
x = s.find(" ")
print(s[x + 1:], s[:x])

# Первое и последнее вхождения(встречается ли такой символ)___

q = input()
if q.count('f') == 1:
    print(q.find('f'))
elif q.count('f') >= 2:
    print(q.find('f'), q.rfind('f'))

# Второе вхождение(покажет индекс)___

s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))

# Удаление фрагмента___

s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)

# второй вариант
s = input()
t1 = s.find('h')
t2 = s.rfind('h') + 1
print(s.replace(s[t1:t2], ''))

# Обращение фрагмента___

s = input()
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

# Замена строки___

s = input()
b = s.replace('1', 'one')
print(b)

# Удаление символа___

s = input()
b = s.replace('@', '')
print(b)

# Замена внутри фрагмента(кроме первого и последнего)___

s = input()
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

# Удалить каждый третий символ___

s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)

# второй вариант

str = input()

for i in range(len(str)):
    if not (i % 3 == 0):
        print(str[i], end="")

# Цикл while________________________________________________________________

# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.___

q = int(input())
i = 1
while i ** 2 <= q:
    print(i ** 2)
    i += 1

# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.___

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.___
# Выведите показатель степени и саму степень.

n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)

# Второй вариант

n = int(input())
i = 1
while n >= 2 ** i:
    i += 1
print((i - 1), 2 ** (i - 1))

# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.___
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)

# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.___
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности
# (не считая завершающего числа 0).
# Числа, следующие за числом 0, считывать не нужно.

len = 0
while int(input()) != 0:
    len += 1
print(len)

# Определите сумму всех элементов последовательности, завершающейся числом 0. ___
# В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
summa = 0
element = int(input())

while element != 0:
    summa += element
    element = int(input())
print(summa)

# Определите среднее значение всех элементов последовательности, завершающейся числом 0.___

sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)

# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)

# Последовательность состоит из натуральных чисел и завершается числом 0.___
# Определите значение наибольшего элемента последовательности.

max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)

# Последовательность состоит из натуральных чисел и завершается числом 0.___
# Определите индекс наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.

max = 0
index_of_max = -1
element = -1
len = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)

# Колличество четных элементов___

num = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num += 1
print(num)

# Последовательность состоит из натуральных чисел и завершается числом 0.___
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)

# Последовательность состоит из различных натуральных чисел и завершается числом 0.___
# Определите значение второго по величине элемента в этой последовательности.
# Гарантируется, что в последовательности есть хотя бы два элемента.

first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)

# Последовательность состоит из натуральных чисел и завершается числом 0.___
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1
print(num_maximal)

# Задача «Числа Фибоначчи»___

n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)

# Второе решение

n = int(input())
fibb = int((((1 + 5 ** 0.5) / 2) ** n - (((1 - 5 ** 0.5) / 2) ** n)) / (5 ** 0.5))
print(fibb)

# Номер числа Фибоначчи___
# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)

# Второй вариант
n = int(input())
j = 0
x = 0
a = 0
b = 1

while j <= n:
    j = a + b
    c = b
    b = a + b
    a = c
    x = x + 1

if c == n:
    print(x)
else:
    print(-1)

# Дана последовательность натуральных чисел, завершающаяся числом 0.___
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)

# Стандартное отклонение___
from math import sqrt

partial_sum = 0
partial_sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partial_sum += x_i
    partial_sum_squares += x_i ** 2
    x_i = int(input())
print(sqrt((partial_sum_squares - partial_sum ** 2 / n) / (n - 1)))

# Списки______________________________________________________________________________________________________________

# Просто создаем список___

a = []  # заводим пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)

# Вторая версия и она короче

a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)

# Третий вариант

a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())
print(a)

# Извлечь цифры из списка___

# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

# Как сделать чтобы цифры были не строкой, а целыми числами___

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

# второй вариант с помощью генераторов

a = [int(s) for s in input().split()]

# Вывести четные индексы___

a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

# Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!___

s = input()
a = [int(s) for s in s.split()]
for i in a:
    if int(i) % 2 == 0:
        print(i, end=' ')

# второй вариант

a = input().split()

for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        print(a[i])

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.___

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# второй вариант

a = input().split()
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.___
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, ___
# и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.___
# Если наибольших элементов несколько, выведите индекс первого из них.

index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)

# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.___
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети.
# Все числа во входных данных натуральные и не превышают 200.
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.

a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)

# второй вариант

a = [int(s) for s in input().split()]
pi = int(input())
k = 0
for i in range(len(a)):
    if a[i] >= pi:
        k += 1
print(k + 1)

# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.___

a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)

# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). ___
# Если элементов нечетное число, то последний элемент остается на своем месте.

a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.___

a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))

# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.___
# Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
# Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
# Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.

a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))

# Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом___
# kэлемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
# Поскольку при этом количество элементов в списке увеличивается,
# после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.

a = [int(s) for s in input().split()]

# обратите внимание на множественное присваивание:
# справа от "=" стоит список из двух элементов,
# а слева -- две переменные,
# поэтому так делать можно
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. ___
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. ___
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

# N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. ___
# Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
# Определите, какие кегли остались стоять на месте.
# Программа получает на вход количество кеглей N и количество бросков K.
# Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N
# Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.

n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))

# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.___
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')


# Функции и рекурсия__________________________________________________________________________________________________

# Факториал числа___

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(3))
print(factorial(5))


# второй вариант

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


for i in range(1, 6):
    print(i, '! = ', factorial(i), sep='')


# Выводим максимальное число___

def max(a, b):
    if a > b:
        return a
    else:
        return b


print(max(3, 5))
print(max(5, 3))
print(max(int(input()), int(input())))


# Выводим максимальное число из трех___

def max(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max(max(a, b), c)


print(max3(3, 5, 4))


# второй вариант

def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res


print(max(3, 5, 4))


# Рекурсия___
# Подобный прием (вызов функцией самой себя) называется рекурсией, а сама функция называется рекурсивной.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Длина отрезка(Теорема пифагора)___

from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))


# Отрицательная степень___
# (Дано действительное положительное число a и целоe число n.Вычислите an.)

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input()), int(input())))


# второе решение

def st(a, n):
    res = a ** n
    print(res)


st(float(input()), int(input()))


# Большие буквы___

def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]


source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))


# Возведение в степень___

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))


# Разворот последовательности___

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()


# Числа Фибоначчи___

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))

# Двумерные массивы_______________________________________________________________________________________________

# Используем два вложенных цикла для подсчета суммы всех чисел в списке___

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

# второй вариант

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)

# Пример обработки двумерного массива___

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))

# второй вариант

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

# Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,___
# в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот,
# \у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)

# Снежинка___

n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

# Шахматная доска___

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))

# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. ___
# На главной диагонали должны быть записаны числа 0.
# На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))

# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу___
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()


# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.___
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j)

def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]


n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))

# Множества____________________________________________________________________________________________________________

# Дан список чисел. Определите, сколько в нем встречается различных чисел___

print(len(set(input().split())))

# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.___

print(len(set(input().split()) & set(input().split())))

# Даны два списка чисел. Найдите все числа, которые входят как в первый, ___
# так и во второй список и выведите их в порядке возрастания.

print(*sorted(set(input().split()) & set(input().split()), key=int))

# Во входной строке записана последовательность чисел через пробел. ___
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)


# Кубики___

def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])


N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))

print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)

# Дан текст: в первой строке записано число строк, далее идут сами строки. ___
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))

# Угадай число___

n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))

# Угадай число - 2___

n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible_nums & guess) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= guess
    else:
        print('NO')
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))

# Полиглоты___

students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')

# Забастовки___

N, K = [int(s) for s in input().split()]
work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_strikes = set(work_days)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_strikes -= {a + b * i for i in range(max_strikes)}
print(len(work_days) - len(no_strikes))

# Словари_____________________________________________________________________________________________________________

# Создание словаря___
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia='Moscow', Ukraine='Kiev', USA='Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)

# Безопасный способ удалить элемент из словаря___

A = {'ab': 'ba', 'aa': 'aa', 'bb': 'bb', 'ba': 'ab'}

key = 'ac'
if key in A:
    del A[key]

try:
    del A[key]
except KeyError:
    print('There is no element with key "' + key + '" in dict')
print(A)

# Перебор ключей словаря___

A = dict(zip('abcdef', list(range(6))))
for key in A:
    print(key, A[key])

# второй вариант

A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)

# Создадим пустой словать Capitals___
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Russia', 'France', 'USA', 'Russia']

for country in Countries:
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)

# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,___
# сколько раз оно встречалось в этом тексте ранее.

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. ___
# Все слова в словаре различны. Для слова из словаря, записанного в последней строке, определите его синоним

n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

# Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. ___
# Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
# Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата.
# На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата,
# то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов.
# В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и число голосов,
# отданных за него в одном из штатов. Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.
# Участников нужно выводить в алфавитном порядке.

num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)

# Дан текст: в первой строке задано число строк, далее идут сами строки.___
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))

# В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. ___
# Для каждого файла известно, с какими действиями можно к нему обращаться:
# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
# В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
# Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл.
# К одному и тому же файлу может быть применено любое колличество запросов.
# Вам требуется восстановить контроль над правами доступа к файлам
# (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция,
# или же Access denied, если операция недопустима.

ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

# Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. ___
# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны — то по второму. Это почти то, что требуется в задаче.

from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# Дан список стран и городов каждой страны. Затем даны названия городов. ___
# Для каждого города укажите, в какой стране он находится.

motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country

for i in range(int(input())):
    print(motherland[input()])

# Англо-латинский словарь___

from collections import defaultdict

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)

print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))

# Контрольная по ударениям___

n = int(input())
accents = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)

errors = 0
sent = input().split()
for word in sent:
    base_form = word.lower()
    if (base_form in accents and word not in accents[base_form]
            or len([l for l in word if l.isupper()]) != 1):
        errors += 1
print(errors)

# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида ___
# Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.

from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)

for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])


# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.___
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе N.
# Далее следует N−1строка, задающие родителя для каждого элемента древа, кроме родоначальника.
# Каждая строка имеет вид имя_потомка имя_родителя.
# Программа должна вывести список всех элементов древа в лексикографическом порядке.
# После вывода имени каждого элемента необходимо вывести его высоту.

def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])


p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)


# Даны два элемента в дереве. Определите, является ли один из них потомком другого.___
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K.
# В каждой из следующих K строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2,
# если второй является предком первого или 0, если ни один из них не является предком другого.

def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in p_tree:
        man = p_tree[man]
        if man == older_man:
            return True
    return False


p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

for i in range(int(input())):
    first, second = input().split()
    if is_ancestor(second, first):
        print(1, end=' ')
    elif is_ancestor(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')


# В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor). ___
# Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A,
# C является предком B, при этом глубина C является наибольшей из возможных.
# При этом элемент считается своим собственным предком.
# Формат входных данных аналогичен предыдущей задаче
# Для каждого запроса выведите наименьшего общего предка данных элементов.

def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result


p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

m = int(input())
for i in range(m):
    child_1, child_2 = input().split()
    ancestors_for_1 = set(ancestors(child_1, p_tree))
    for ancestor in ancestors(child_2, p_tree):
        if ancestor in ancestors_for_1:
            print(ancestor)
            break
