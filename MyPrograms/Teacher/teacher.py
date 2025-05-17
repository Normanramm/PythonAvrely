#__________________________________print.input,int(input),if,elif,else_________________________________________________

# Один из вариантов написания Тернарный оператор
name = input('Введите ваше имя')
age = input('Введите ваш возраст')
message = 'Проходите, ' + name if int(age) >= 18 else 'Вам пока рано, ' + name
print(message)

name_game = (f'Здраствуй сталкер {name}, я консольная игра "Cказочный Мир".')
print(name_game)
age = float(input("Введите свой возраст!: "))
age >= 18
if age < 18:
    result = ("Пока не дорос, конец игры! ")
    print("Пока не дорос, конец игры! ")
    exit() # Используется для закрытия
elif age > 18 and age < 50:          # and сумарное значение проверки будет True, если с обеих сторон True
    result = "Доступ разрешен!. "    # or достаточно чтобы с одной стороны было True
elif age > 51 and age < 59:
    result = "Вы скоро станете пенсионером. "
elif age > 60 and age < 110:
    result = "Вы пенсионер. "
else:
    result = "Бессмертный!"
print(result)
name = input('Как тебя зовут?: ')
print('Добро пожаловать в "Русский мир",' + name + '!')

# Программа голосования
Za = 99
Za_Putina = 0
Protiv_Putina = 0
i = 0
while i < 10:
    plebiscit = input('Введите ЗА или ПРОТИВ')
    plebiscit = plebiscit.lower()
    if plebiscit == 'против' or plebiscit == 'за':
        Za_Putina += 1.5
        Za += 1.5
        print('Ваш голос принят Гражданин. ')
    elif Za > 99:
        Za = 0
        Protiv_Putina += 1
    else:
        print('Вы агент госдепа!')
    Za_Putina = int(Za_Putina)
    i += 1


# Проверка числа
num =int(input('Выведить целое число: '))
if num % 2 == 0:
    print('Четное')
else:
    print("Нечётное")



import random
num = random.randint(1,10)
guess = int(input('Введите число от 1 до 10: '))
if guess == num :
    print('Угадали!')

#________________________________Продвинутые строки____________________________________________________________________

# замена строки с помощью метода
string = 'Хобот'
string = string.replace("Х", "Р")
print(string)

# замена строки с помощью среза
string = 'Хобот'
string = "Р" + string[1:]
print(string)


# пропуск строки
a = input()
b = a.find('#')
print(a[0:b])

a = input()
b = a.find('#')
if '#' in a:
    print(a[0:b])

a = input()
b = a.find('#')
c = ('#')
if c in a:
    print(a[0:b])

a = input()
b = a.find('#')
c = ('#')
if c in a:
    print(a[0:b])
else:
    print(a)

a = input()
b = a.find('#')
if '#' in a:
    print(a[0:b])
else:
    print(a)

# Скрыть номер телефона
string = input()
if len(string) >= 8 and string.isdigit():
    a = len(string[:-4]) * '*'
    b = string[-4:]
    print(a + b)
else:
    print('Ошибка')


#_________________________________ЦИКЛ WHILE___________________________________________________________________________
i = 0
a = 1
while i < 100 and a < 100:
    i += 2
    print(f'четные {i} / нечетные {a}')
    a += 2

maxBid = int(input())
while(True):
    bid = int(input())
    if bid > maxBid:
        break
print("Sold: ", bid)
# Ставка выводит самое большое значение

#_______Затяжка_____________________________
a = input('затяжка: ')
b = 0
while a != b:
    b += 1
    print(f'Колличество тяг: {b}')
    a = input('затяжка: ')

a = int(input('затяжка: '))
b = 0
while a != b:
    b += 1
    print(f'Колличество тяг: {int(a) + int(1)}')
    a = input('затяжка: ')

# Пропустить символ
string = input()
i = 0
while True:
    if i == string.find('#'):
        break
    print(string[i])
    i += 1

string = input()
a = string.find('#')
print(string[:a])

string = input()
i = 0
while i < string.find('#'):
    print(string[i])
    i += 1

string = input()
i = 0
while i < len(string):
    if i == string.find('#'):
        break
    print(string[i])
    i += 1

string = input()
i = 0
while i < len(string):
    if string[i:i + 2] in '##':
        break
    print(string[i])
    i += 1

string = input()
i = 0
while i < len(string):
    if string[i] == '!':
        break
    print(string[i])
    i = i + 1
else:
    print('Восклицательного знака не найдено')

string = 'АБ#ВГ'
i = 0
while i < len(string):
    symbol = string[i]
    i = i + 1
    if symbol == '#':
        continue
    print(symbol)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

i = 0
while i < 10:
    i += 1
    if i == 5:
        print('1000')
        continue
    print(i)



#___________________________________Модули_____________________________________________________________________________
import time
print(time.asctime())

# Гиперболический тангенс
import math
print(math.atanh(0.5))

import random #подключаем модуль псевдослучайных функций Python
members = ["Василий", "Евгений", "Олег", "София", "Инна", "Василиса", "Петр"] #описание списка участников
print(random.choice(members)) #выбор и вывод имени победителя на экран

import random
while True:
    num = random.randint(1,10)
    guess = int(input('Введите число от 1 до 10: '))
    if guess == num :
        print('Угадали!')
    else:
        print('Не угадали')

# Модуль tkinder
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
window.mainloop()

# Рисовалка
import tkinter as tk
# Функция для отслеживания движения мыши и рисования
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    # Измените цвет карандаша, установив параметр fill
    canvas.create_oval(x1, y1, x2, y2, fill="blue", width=2)  # В данном случае цвет - синий
# Создаем окно приложения
root = tk.Tk()
root.title("Рисовалка")
# Создаем холст для рисования
canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()
# Привязываем функцию paint к событию "Button-1" (нажатие левой кнопки мыши)
canvas.bind("<B1-Motion>", paint)  # Используем <B1-Motion> для отслеживания движения мыши
# Запускаем графический интерфейс
root.mainloop()

# Шахматная игра
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(0, 0, 300, 200, fill='black')
cellsize = 20
allrows = 10
allcolumns = 15
row = 0
while row < allrows:
    column = 0
    while column < allcolumns:
        x1 = column * cellsize
        x2 = x1 + cellsize
        y1 = row * cellsize
        y2 = y1 + cellsize
        if (row + column) / 2 == int((row + column) / 2):
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        column += 1
    row += 1
window.mainloop()

# Использованеие random и tkinder
import random
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
i = 0
while i < 10:
    x = random.randint(0, 280)
    y = random.randint(0, 180)
    i += 1
    canvas.create_rectangle(x, y, random.randint(x+10, 300), random.randint(y+10, 200))
window.mainloop()


# Анимация прямоугольника

import tkinter as tk
import time
# Создание окна
root = tk.Tk()
root.title("Прямоугольник")
# Создание холста
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
# Создание прямоугольника
rectangle = canvas.create_rectangle(0, 0, 50, 50, fill="blue")
# Переменная x
x = 0
# Цикл анимации
while x < 200:
    x += 2  # Увеличиваем x на 2
    canvas.coords(rectangle, x, 0, x + 50, 50)  # Изменяем координаты прямоугольника
    canvas.update()  # Обновляем содержимое окна
    time.sleep(0.01)  # Делаем паузу в 0.01 секунду
# Запуск главного цикла окна
root.mainloop()

# Анимация прямоугольника который ходит туда сюда

import tkinter as tk
import time
# Создание окна
root = tk.Tk()
root.title("Летающий прямоугольник")
# Создание холста
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
# Создание прямоугольника
rectangle = canvas.create_rectangle(0, 0, 100, 50, fill="blue")
# Начальные значения
x = 0
delta = 2  # Изменение координаты x на каждой итерации
# Бесконечный цикл для движения прямоугольника
while True:
    x = x + delta  # Изменяем координату x
    # Изменяем направление, если прямоугольник достигает границы холста
    if x < 0 or x > 300:
        delta = -delta  # Меняем направление движения
    canvas.coords(rectangle, x, 0, x + 100, 50)  # Изменяем координаты прямоугольника
    canvas.update()  # Обновляем содержимое окна
    time.sleep(0.01)  # Делаем паузу в 0.01 секунду
# Запуск главного цикла окна (не будет достигнуто из-за бесконечного цикла выше)
root.mainloop()


# Подключаем только ту часть, которая отвечает за цвет текста
from colorama import Fore
# Строки Fore.BLACK, Fore.WHITE, Fore.RED и так далее
# содержат специальные символы для установки цвета.
# Чтобы изменить цвет текста, достаточно вывести на экран
# строку со специальными символами и цвет текста изменится
print(Fore.BLACK + 'Черный')
print(Fore.WHITE + 'Белый')
print(Fore.RED + 'Красный')
print(Fore.GREEN + 'Зеленый')
print(Fore.YELLOW + 'Желтый')
print(Fore.BLUE + 'Синий')
print(Fore.MAGENTA + 'Пурпурный')
# Fore.RESET устанавливает цвет таким, каким он был
# до первой покраски
print(Fore.RESET + 'Цвет по-умолчанию')





#________________________________СПИСКИ________________________________________________________________________________
#В Python списки - это упорядоченные коллекции объектов произвольных типов.
# Списки могут содержать элементы различных типов данных, включая числа, строки, другие списки и даже функции.
# Элементы списка могут быть изменяемыми (mutable), что означает, что их можно изменить после создания списка.
# Списки в Python определяются с использованием квадратных скобок [].
#Вот некоторые примеры использования списков в Python:

# Создание списка
my_list = [1, 2, 3, 4, 5]  # список чисел
str_list = ["apple", "banana", "cherry"]  # список строк
mixed_list = [1, "hello", 3.14, True]  # список с разными типами данных
empty_list = []  # пустой список

# Доступ к элементам списка
print(my_list[0])  # Выведет: 1 (первый элемент списка)
print(str_list[1])  # Выведет: banana (второй элемент списка)

# Изменение элементов списка
my_list[0] = 100  # Изменяет первый элемент на 100
print(my_list)  # Выведет: [100, 2, 3, 4, 5]

# Добавление элементов в список
my_list.append(6)  # Добавляет 6 в конец списка
print(my_list)  # Выведет: [100, 2, 3, 4, 5, 6]

# Удаление элемента из списка
my_list.remove(3)  # Удаляет первое вхождение числа 3
print(my_list)  # Выведет: [100, 2, 4, 5, 6]

# Длина списка (количество элементов в списке):
print(len(my_list))  # Выведет: 5

#Срезы (slices) в списках:
print(my_list[1:4])  # Выведет: [2, 4, 5] (срез с индекса 1 по индекс 3)
print(my_list[:3])  # Выведет: [100, 2, 4] (срез с начала до индекса 2)
print(my_list[2:])  # Выведет: [4, 5, 6] (срез с индекса 2 до конца)

# SELFEDU уроки________по спискам__________

# Функция которая сортирует, делает по порядку и обратная сортировка
marks = [2, 3, 4, 3, 5, 2]
print(sorted(marks))

marks = [2, 3, 4, 3, 5, 2]
print(sorted(marks, reverse = True))

# Для вычисления суммы
marks = [2, 3, 4, 3, 5, 2]
print(sum(marks))

# Минимальное число и максимально
marks = [2, 3, 4, 3, 5, 2]
print(min(marks))

marks = [2, 3, 4, 3, 5, 2]
print(max(marks))

# Обьединение списков
a = [1, 2, 3]
b = ['один','два','три']
print(a + b)

# Добавление элемента в список
a = [1, 2, 3]
b = ['один','два','три'] + ['четыре']
print(a + b)

# Продублировать список, увеличить на три раза
a = [1, 2, 3] * 3
print(a)

a = ['I'] + ['Love'] * 3 + ['Python']
print(a)

# Проверить если такое в списке с помощью оператора in
marks = [2, 3, 4, 3, 5, 2]
if 11 in marks:
    print(marks)
else:
    print('такого нет')

# Этот метод удаляет элемент по указанному индексу и возвращает его значение. Если индекс не указан, то удаляет последний элемент.
a = [1, 2, 3, 4, 5, 6]
a = a.pop(2)
print(a)

# Удаляет из списка и возвращает полный список без удаленного
a = [1, 2, 3, 4, 5, 6]
del a[1]
del a[1][1]
print(a)

# Удаление нескольких элементов
a = [1, 2, 3, 5 ,6 ,7 ,8 ,9]
del a[0:3]
print(a)

#remove() — удаляет по названию;
#pop() — удаляет по индексу, положительному или отрицательному;
#clear() — удаляет всё содержимое списка;
#del — позволяет удалить как отдельный элемент, так и целый срез по индексу.

# Срез списка и изменение списка, копия списка
a = ['Москва','Yfa', 'Tver', 'Kazan']
print(a[0:3])
a[0] = 'Voronej'
print(a)
b = a[:] # копия списка
print(b)
с = list(a) # тоже копия списка
print(a)

# [start:stop:шаг]
a = ['Москва','Yfa', 'Tver', 'Kazan', 1, 2, 3, 4, 5, 6]
print(a[0:-1:2])
print(a[:-1:2]) # можно указать без границы
print(a[0::2]) # это сразу до конца
print(a[::2]) # все элементы через один с начала
print(a[::-1]) # перебираем все элементы с конца инверсия

# Изменение в сприске
a = ['Москва','Yfa', 'Tver', 'Kazan', 1, 2, 3, 4, 5, 6]
a[4:5] = ['one','two'] # тут меняем в индексе на что либо
print(a)

# Групповое присваивание + разные варианты
a = ['Москва','Yfa', 'Tver', 'Kazan', 1, 2, 3, 4, 5]
a[:8:2] = [0,0,0,0] # нужно чтобы было начало и клнец и совпадало с индексом конечным
print(a)

a = ['Москва','Yfa', 'Tver', 'Kazan', 1, 2, 3, 4, 5]
a[:9] = 1,1,1,1,1,1,1,1,1
print(a)

# Основные методы списков
a = [1, - 54, 3, 23, 43, -45, 0]
a.append(100) # добавляет элемент в конец списка и даже вложенный список
a.insert(3, -1000) # позволяет вставлять в список в определенную позицию определенные значения
a.remove() # удаляет по значению элимента, в скобках написать, что удаллить
a.pop() # удаляет последний элемент если не написать ничего, также он возвращает удаляемы элимент,
a.pop(1) # также он может удалять по индексу элемент

b = [1, - 54, 3, 23, 43, -45, 0]
end = b.pop()
print(end) # этим способом можно обратится к удаленному элементу и засунуть его в переменную

a.clear() # удаляет, очищает полностью список

c = a.copy() # просто копия списка, если переменной присвоить это она станет копией списка, но это уже будет другой список
print(c)
c = a[:] # тоже самое, что и копия но спомощью среза
c = list(a) # тоже самое,что и копия

a.count(1) # показывает сколько таких элементов в списке
a.index(3) # позволяет определять индекс определенного значения
a.index(0, 3) # первое, что ищем, а второе это сиартовый элемент с которого ищем
'1' in a # это способ чтобы проверить есть ли такой элемент, чтобы не забывать

a.reverse() # меняет порядок следования элементов на обратный
a.sort() # позволяет выполнять сортировку значений по возрастанию текущего списка, применяется к текущему списку
a.sort(reverse=True) # этот метод позволяет вывести сначала максимальные потом минимальные
print(a)

c = sorted(a) # возвращает новый отсортированный список причем прежний список остается неизменным
print(c)

# Вложенные списки
line = [1, 7, 6, 11, 3]  # одномерный список
img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
img = [line[:], line[:], line[:], line[:], line[:]] # копия одномерного списка и многомерный список
print(img[0][1]) # обращение к элементу вложенного списка
img[1] = [0, 0, 0, 0, 0] # замена в списке
img[1] = [0] * 5 # замена в списке второй вариант
img[1][:] = [1] * 5 # третий вариант с помощью среза, но в существующие значения новые значения
print(img)

t = [['Люблю','тебя', 'петра', 'творенье'],          #0 индексы строк
     ['Люблю','твой', 'строгий', 'стройный', 'вид'], #1
     ['Невы', 'державное', 'теченье'],               #2
     ['Береговой', 'ее', 'гранит']                   #3
     ]
t[0][2] = 'Питон' # замена в списке
print(t[1][1]) # отображение нужного слова в списке, первое индекс списка, второе индекс в строке
t.append(['Твоих', 'оград', 'узор', 'чугунный']) # добавляет в конец вложенный список
del t[1] # удаляет выбранный элемент
print(t)

a = [[[True, False],[1, 2, 3]], ['матрица', 'вектор']] # двумерный и одномерный список
print(a[0][1][0]) # обращение к двумерному списку

#________________________________________________
#список list
m = [1,2,3,4,5]
print (m[0])

m = [1,2,3,4,5]
print (m[-1])

#как узнать длину списка
m = [1,2,3,4,5]
print (len(m))

#как посмотеть длинну вложенного списка
m = [[5,6], [1,2], ['s', 'f']]
print (len(m[0]))

# Чтобы обратиться к элементу вложенного списка
m = [1,2,3,4,5,'a', [1,2], ['s', 'f']]
print (m[-1][0])

#изменяем список
m = [[5,6], [1,2], ['s', 'f']]
m[0] = 9
print(m) #тут заменили индекс 0 на 9
m[0] = m[0] + 2
print(m) #тут к идексу 0 прибавили 2

#поменять вложенные списки местами
m = [[5,6], [1,2], ['s', 'f']]
m[1], m[2] = m[2], m[1]
print(m)

# к списку можно добавит значение из другого списка
m = [[5,6], [1,2], ['s', 'f']]
m = m + [7]
print(m)

#так же список можно продублировать с помощью умножения
m = [[5,6], [1,2], ['s', 'f']]
m = m*2
print(m)

#конвертация списка с помощью функции list
n = list('stroka')
print(n)

#функция range генереирует последовательность чисел
n = list(range(10))
print(n)

#проитетрируем список через цикл for
n = list(range(10))
for i in n:
    print(i)

#проитетрируем список через цикл for пропускаем цифру 8 с помощью continue
n = list(range(10))
m = []
for i in n:
    if i == 8:
        continue
    m += [i]
else:
    print(m)

# Методы списка
x = [9,8,7,6,5]
x.append(4)
x.insert(1, 7)
print (x.count(7))
x.sort()
x.reverse()
y = x.pop(0)
print(y)
x.remove(7)
x.clear()
x.extend(['a','s'])
h = x.copy()
print(h)

# Примеры работы списков

n = list(range(1, 21))
m = []
for i in n:
    if i % 2 == 0:    #если i кратно 2,то остаток 0
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)


n = list(range(1, 21))
b = n.copy() #чтобы скопировать список до его изменения
m = []
for i in n:
    if i % 2 ==0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[::] #метод среза, тоже копирует полный список
m = []
for i in n:
    if i % 2 ==0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[0::2] #можно выбарать любой диапазон [start:stop:step]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)



n = list(range(1, 21))
b = n[:5] # Если указать так, то будет от 1 до 5
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)

n = list(range(1, 21))
b = n[5:] # если указать так, то будет от 5 до 20
m = []
for i in n:
    if i % 2 ==0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)

x = [9, 8, 7 ,6 ,5, 4 ,3] #Увеличиваем список на 3
for i in range(len(x)):
    x[i] += 3
print(x)

# Программа удаляет имя из списка имен и формирует новый список
# Ввод списка имен и имя, которое необходимо удалить вводиться с клавиатуры
list_str = input().split(" ") # Ввод списка имен через пробел
print(list_str)               # Печать списка
del_list_str = input().lower()# Ввод имени которое необходимо удалить из списка
new_list = []                 # Новый пустой список, в который будет запись
i = 0
for i in range(len(list_str)):
    if list_str[i].lower() == del_list_str:
         i +=1
    else:
        new_list.append(list_str[i])
        i += 1
print(new_list) # Печать нового списка

# Программа которая убирает лишние пробелы_ _ _ _ _

# Получаем предложение от пользователя
string = input("Введите что-нибудь: ")
# Список для хранения слов
words = []
# Переменная для накопления текущего слова
word = ''
# Перебираем символы в строке
for char in string:
    # Если текущий символ не пробел, добавляем его к текущему слову
    if char != ' ':
        word += char
    else:
        # Если текущий символ - пробел, добавляем текущее слово в список и сбрасываем word
        if word:
            words.append(word)
            word = ''
# Добавляем последнее слово после выхода из цикла (если оно не пустое)
if word:
    words.append(word)
# Выводим список слов на экран
print(words)


string = ("Введите   что   нибудь  ")
words = []
i = 0
word = ''
while i < len(string):
    if string[i] == ' ':
        words.append(word)
        word = ''
    else:
        word += string[i]
    i += 1
words.append(word)
while '' in words:
    words.remove('')
    i += 1
print(words)


string =input("Введите что-нибудь: ")
words = []
i = 0
word = ''
while i < len(string):
    if string[i] == ' ':
        if word:                # если переменная содержит символ(ы)
            words.append(word)  # добавляем в список
            word = ''           # очищаем
    else:
        word += string[i]
    i += 1
if word:                        # проверяем снова есть ли символы
    words.append(word)
print(words)

# тот же код только меньше
words = input("Введите что-нибудь: ").split()
print(words)

# выводит текст с обратной стороны списком
q = input().split()
w = q[::-1]
print(w)

# выводит текст с обратной стороны строкой
q = input().split()
q = q[::-1]
q = ' '.join(q)
print(q)

# перевернутый текст трэщ
q = ('задача интересная Это').split()
for i in q:
    q = q[::-1]
    q = ' '.join(q)
    print(q)




#___________________________________ЦИКЛ FOR___________________________________________________________________________
#Цикл for в языке программирования Python используется для итерации (повторения)
#через последовательность элементов, таких как строки, списки, кортежи и другие.

#Цикл for в Python предоставляет удобный способ обработки
#элементов в последовательности без явного использования индексов.

#Синтаксис цикла for выглядит следующим образом:
for переменная in последовательность:
    # блок кода, выполняемый на каждой итерации
# Где:
#переменная - это переменная, которая принимает значение каждого элемента из последовательность.
#последовательность - это объект, который поддерживает итерацию, например, список, строка, кортеж и т. д.
#блок кода - это набор инструкций, который будет выполняться на каждой итерации цикла

# Пример с использованием списка
fruits = ["яблоко", "груша", "банан"]
for fruit in fruits:
    print(fruit)


#Также можно использовать функцию range() для генерации последовательности чисел и итерации по ней:
for i in range(5):
    print(i)


#уроки selfedu_________________________
d = [1, 2, 3, 4, 5] # выведет список
for x in d:
    print(x)

for x in 'python': # выведет слово
    print(x)

d = [1, 2, 3, 4, 5]
p = 1
for x in d:
    p *= x # умножит все числа поочередно
    print(p)

d = [1, 2, 3, 4, 5]
for i in [0, 1, 2, 3, 4]: # обращаемся не к элементам списка, а к их индексу
    d[i] = 0 # индекс от нуля
print(d) # таким образом изменили список

# для удобства есть функция range
#(start, stop, step)
#(start, stop, step)
#(stop)

d = [1, 2, 3, 4, 5]
for i in range(5):
    d[i] = 0 # если тут вместо i указать индекс, изменится этот индекс
print(d)

#второй способ лучше так как тут не нужно указывать длинну
d = [1, 2, 3, 4, 5]
for i in range(len(d)):
    d[i] = 0
print(d)

#арифметический пример
# Задача: s = 1/2 + 1/3 + 1/4 + ... 1/1000
s = 0
for i in range(2, 1001):
    s += 1/i
print(s)

# Вывод четных и нечетных чисел в диапазоне от 1 до 10
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} - четное число")
    else:
        print(f"{i} - нечетное число")

# Вычисление факториала от натурального числа n:
# Факториал это n! = 1*2*3*...*n
n = int(input('Введите натуральное число до 100: '))
if n < 1 or n > 100:
    print('Неверно введено натуральное число')
else:
    p = 1
    for i in range(1, n + 1):
        p *= i
        print(f'Факториал числа{n}! = {p}')

# Создание елки
for i in range(1, 7):
    print('*' * i)

# Как список слов сделать предложением
words = ["Python", "дай", "силы"]
s = ''            # переменная для хранения результата
for w in words:   # перебираем коллекцию из строк
    s += ' ' + w  # соединение строк между собой
print(s)
print(s.lstrip()) # уберет пробел слева, это метод строк

# ну и просто быстрый способ
words = ["Python", "дай", "силы"]
print(" ".join(words))


# Нужно заменить все двухзначные цифры
digs = [4, 3, 100, -53, -30, 1, 34, -8]
for i in  range(len(digs)):     # будет пробегать длину списка
    if 10 <= abs(digs[i]) <= 99: # это проверка если текущие значения находятся от и до
        digs[i] = 0 # если это так приравнять нулю
print(digs)

# Нужно заменить все двухзначные цифры с помощью функции enumerate
digs = [4, 3, 100, -53, -30, 1, 34, -8]
for i, d in  enumerate(digs):     # будет пробегать длину списка
    if 10 <= abs(d) <= 99: # это проверка если текущие значения находятся от и до
        digs[i] = 0 # если это так приравнять нулю
print(digs)


# Преобразование кириллицы в латиницу
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
     'shch', '', 'y', '', 'e', 'yu', 'ya'
]
start_index = ord('а') #вспомогательная переменная начала с а
title = "Программирование на Python - лучший курс"
slug = '' # тут хранится преобразование в латиницу
for s in title.lower(): # пробегает все символы и делает их маленькими
    if 'а' <= s <= 'я': # проход по алфавиту
        slug += t[ord(s) - start_index] # и тогда в slug добавляем из t символы, и проход по индексу
    elif s == 'ё': # ниже делаем проверки и заменяем одно на другое
        slug += 'yo'
    elif s in ' !?;:,.':
        slug += '-'
    else:
        slug += s
while slug.count('--'): # это нужно для того чтобы убрать пунктиры
    slug = slug.replace('--', '-')
print(slug)


# код подсчета букв, цикл в цикле for
x = 'аювгдеёжзийклмнопрстуфхцчшщьыъэюя'
y = input('Введите строку')
for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0: #это позволяет не выводить все буквы, а только те которые ввел
        print('Букв', i, ',было', count)

# тоже цикл for start, финишь, шаг
for x in range(5, -3 , -2):
    print(x)
#_____________________________
#Цикл for делает то же, что и while — повторяет действия,
#заданные программистом. Но for при переборе списков выглядит более изящно:
list_ = [1, 2, 3, 66, 13]
for el in list_:
    print(el)

#четное и нечетное
for i in range(1, 20):
    if i % 2 == 0:
        print(f"{i} - четное число")
    else:
        print(f"{i} - нечетное число")

# самое длинное слово выводит
q = input().split()
w = ''
for i in q:
    if len(i) > len(w):
        w = i
print(w)

# выводит списком
q = input().split()
w = ''
e = []
for i in q:
    if len(i) > len(w):
        w = i
        e = [i]
print(e)


q = input().split()
w = ''
e = []
for i in q:
    if len(i) > len(w):
        w = i
        e = [i]
    elif len(i) == len(w):
        e.append(i)
print(e)


print(max(input().split(), key=len))

text = input('input something: ').split()
print(max(text,key = len))

string = input ('input sam... ')
line_string = string.split()
print(max(line_string, key=len))


text = input()
clean_text = ''
for x in text:
    if x.isalpha() or x.isspace():
        clean_text += x
    else:
        clean_text += ' '
list_ = clean_text.split()
longest = ''
longestl = []
for el in list_:

    if len(el) > len(longest):
        longest = el
        longestl = [el]

    elif len(el) == len(longest):
        longestl.append(el)
if len(longestl) == 1:
    print('Самое длинное слово:')
    print(longestl[0])
else:
    print('Самые длинные слова:')
    i = 0
    for word in longestl:
        i += 1
        print(f'{i}. {word}')

# Меняет цвет если слово начинается с заглавной буквы
from colorama import Fore
q = input().split()
w = ''
for i in q:
    if i.istitle():
        w += (Fore.RED + i)
        w += ''
    else:
        w += (Fore.RESET + i)
        w += ''
print(w)


from colorama import Fore
def col():
    q = input('Cлово с заглавной буквы: ').split()
    w = ''
    c = int(input("Каким цветом раскрасить?\n 1 Красным \n 2 Зеленым \n 3 Желтым \n Выберите операцию: " ))
    if c == 1:
        for i in q:
            if i.istitle():
                w += (Fore.RED + i)
                w += ''
            print(w)
    if c == 2:
        for i in q:
            if i.istitle():
                w += (Fore.GREEN + i)
                w += ''
            print(w)
    if c == 3:
        for i in q:
            if i.istitle():
                w += (Fore.YELLOW + i)
                w += ''
            print(w)
    else:
        w += (Fore.RESET + i)
        w += ''
    print(w)
col()
while True:
    flag = input('Еще раз? [да/нет]: ')
    if flag == 'да':
        col()
    else:
        break

# перевернутый текст трэщ, другие способы в списках смотреть
q = ('задача интересная Это').split()
for i in q:
    q = q[::-1]
    q = ' '.join(q)
    print(q)

from colorama import Fore
q = ('задача интересная Это').split()
for i in q:
    q = q[::-1]
    q = ' '.join(q)
    print(Fore.RED,q)


# Показывает количество слов в тексте
a = input("Введите предложение: ").lower()
a = a.replace(".", ' ').replace(",", ' ')
b = a.split()
c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
for i, q in c.items():
    print(f'Слово "{i}" встречается {q} раз.')

# Фильтрация слов и ниже тоже самое
a = input().split()
words = []
for i in a:
    if i.isalnum():
        words.append(i)
print(words)
# Cписковые включения
a = input()
words = [i for i in a.split() if i.isalnum()]
print(words)
# еще одна сортировка
a = input()
numbers = [int(i) for i in a.split() if i.isdigit()]
numbers.sort()
print(numbers)

# Примеры списковых включений
# Списковые выражения — удобная синтаксическая конструкция для решения определенных задач.
# Однако, не стоит применять их везде и всюду. Помните, что читаемость программы очень важна.
# И если применение спискового включения ухудшает ее — лучше его не использовать.

# Список квадратов чисел от 1 до 5
squares = [x * x for x in (1, 2, 3, 4, 5)]
print(squares)

# Все фрукты, в которых есть буква «а»
fruits = ["яблоко", "банан", "вишня", "киви", "манго"]
filtered_fruits = [x for x in fruits if "а" in x]
print(filtered_fruits)

# Список цен со скидкой
original_prices = [100, 200, 500, 1100]
discount = 0.15  # 15%
new_prices = [i * (1 - discount) for i in original_prices]
print(new_prices)

# Улучшенный список цен со скидкой
original_prices = [100, 200, 500, 1100, 116.15]
discount = 0.15  # 15%
new_prices = [i * (1 - discount) for i in original_prices]
formatted_prices = [f'{int(price)} руб.' if price == int(price) else f'{price:.2f} руб.' for price in new_prices]
print(', '.join(formatted_prices))



# Тернарный оператор как выражение для обработки элемента
text = 'Сколько лет, сколько зим'
parts = ['*' if i == 'о' else i for i in text]
new_text = ''.join(parts)
print(new_text)

# Списковые выражения можно передавать в качестве аргументов методам и функциям,
text = 'Сколько лет, сколько зим'
new_text = ''.join(['*' if i == 'о' else i for i in text])
print(new_text)

# Шифруем текст (алфавит наоборот)
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
inverted = alphabet[::-1]
input_ = input().lower()
cipher = [inverted[(alphabet.index(el))] if el in alphabet else el for el in input_]
print(''.join(cipher))

# Перетасовка дел и список дел по порядку

import random
# Создаем пустой список для дел
tasks = []
# Бесконечный цикл для ввода дел
while True:
    task = input("Введите дело (или нажмите Enter для завершения): ")
    # Если пользователь нажал Enter, завершаем цикл
    if not task:
        break
    # Добавляем дело в список
    tasks.append(task)
# Перетасовываем список с помощью random.shuffle
random.shuffle(tasks)
# Выводим перемешанные дела на экран
print("Список дел в случайном порядке:")
for task in tasks:
    print(task)

# Cписок дел по порядку
tasks = []
while True:
    a = input("Введите дело (или нажмите Enter для завершения): ")
    if not a:
        break
    tasks.append(a)
print("Список дел:")
for a in tasks:
    print(a)


# Функция range(start, stop, step)
# Встроенная функция языка range нужна для того, чтобы генерировать последовательности чисел.
# Результат работы range очень похож на список и с ним можно работать также, как со списком.
# Например, использовать для создания цикла for.

#примеры:

# таблица умножения с помощью цикла for
# Задаем размер таблицы умножения
размер = 10
# Выводим заголовок таблицы
print("Таблица умножения")
# Выводим верхнюю горизонтальную линию
print("-" * 20)
# Внешний цикл для умножителя
for умножитель_1 in range(1, размер + 1):
    # Внутренний цикл для множителя
    for умножитель_2 in range(1, размер + 1):
        # Выводим результат умножения и добавляем пробел для форматирования
        print(умножитель_1 * умножитель_2, end="\t")
    # Переходим на новую строку после завершения внутреннего цикла
    print()
# Выводим нижнюю горизонтальную линию
print("-" * 20)

# Еще одна таблица умножения
a = input('Введите число: ')
try: # теперь можно вводить float числа
# если ввод разделен запятой, а не точкой
    a = a.replace(',','.')
    a = float(a)
    for i in range(1, 10):
    # округляем до 2х знаков после точки
    # если число не целое
        x = a * i
        x_f = (int(x) if x == int(x) else round(x, 2))
        a_f = (int(a) if a == int(a) else round(a, 2))
        print(f'{(a_f)} * {i} = {x_f}')
except ValueError:
    print('Введено не число')

# Генерация пароля
import random
symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = int(input("Введите длину пароля: "))
b = ''.join(random.choice(symbols)
for i in range(a))
print("Ваш сгенерированный пароль:", b)

# Еще одна генерация
import random
symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = int(input('Какой длины должен быть пароль: '))
for i in range(a):
    b = random.choice(symbols)
    print(b, end = '')


# Рисуем круги куча версий

import tkinter as tk
# Создаем окно
window = tk.Tk()
window.title("Разноцветные круги 123")
# Создаем холст и размещаем его в окне
canvas = tk.Canvas(window, width=200, height=200, bg="white")
canvas.pack()
# Координаты центра круга
x = 100
y = 100
# Рисуем концентрические круги
for i in range(5, 100, 5):
    # Вычисляем координаты прямоугольника, в который вписан круг
    x0 = x - i
    y0 = y - i
    x1 = x + i
    y1 = y + i
    # Определяем цвет круга
    color = "red" if i % 10 == 0 else "grey"
    # Создаем круг на холсте
    canvas.create_oval(x0, y0, x1, y1, outline=color)
# Запускаем цикл обработки событий
window.mainloop()


# Гипнотические круги
import tkinter
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
x = 150
y = 100
offset = 70
# количество кругов, после которых начнется удаление
circles = []
while True:
    for R in range(95, 4, -1):
        x0 = x - R
        y0 = y - R
        x1 = x + R
        y1 = y + R
        if R % 5:
            circle = canvas.create_oval(x0, y0, x1, y1, outline='black')
        else:
            circle = canvas.create_oval(x0, y0, x1, y1, outline='magenta')
        circles.append(circle)
        window.update()
        time.sleep(0.03)
        # Если у нас достаточно кругов, начинаем удалять первые
        if len(circles) >= offset:
            canvas.delete(circles[0])
            circles.remove(circles[0])
            window.update()
window.mainloop()


import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
x0 = 50
y0 = 50
x1 = 150
y1 = 150
x = 145
y = 100
for R in range(5, 100, 5):
    x0 = x - R
    y0 = y - R
    x1 = x + R
    y1 = y + R
    color = "red" if R % 10 == 0 else "grey"
    canvas.create_oval(x - R, y - R, x + R, y + R, outline = color)
window.mainloop()


import tkinter as tk
import random
# Создаем окно
window = tk.Tk()
window.title("ТРЭШ")
# Создаем холст и размещаем его в окне
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()
# Координаты центра круга
x = 145
y = 100
# Рисуем концентрические круги
for radius in range(5, 100, 5):
    # Генерируем случайные значения цветов
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    # Создаем круг на холсте
    circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=color)
# Функция для перемещения кругов
def move_circles():
    for circle in canvas.find_all():
        # Генерируем случайное смещение для каждого круга
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        canvas.move(circle, dx, dy)
    # Запускаем функцию снова через 100 миллисекунд
    window.after(100, move_circles)
# Запускаем функцию для перемещения кругов
move_circles()
# Запускаем цикл обработки событий
window.mainloop()





#_____________________________________Кортеж tuple_____________________________________________________________________
# Кортеж обозначается с помощью запятых. Если в кортеже всего один элемент, после него нужно ставить запятую.
# Здесь переменные a, b и c будут кортежами, а d — строкой.
a = (1, 2, 3)
b = 1, 2, 3   # Это все кортеж
c = ("s", )
# Круглые скобки не обязательны, но лучше их все же ставить.
# Тем более, что бывают случаи, когда скобки все‑таки нужны. В первом print — это три параметра:
# 1, 2 и 3. А во втором — это один параметр — кортеж из трех элементов.
print(1, 2, 3)
print((1, 2, 3))



x = (9, 8, 7, 6)
print(type(x))


x = tuple('stroka') #Функция, при помощи которой создается кортеж
print(x)

x = (9, 8, 7)
z , c, b = x  #пример распаковки кортежа
print(x)

x = (9, 8, 7, 6, 5, 4, 3)
print(x[1:5])    #Срез кортежа


x = (9, 8, 7, 6, 5, 4, 3)
y = []
for i in range(len(x)):
    y.append (x[i] + 3) #Взять значение из кортежа, добавить к нему значение 3
print(x)                #и добавить это значение в y
                        #итог кортеж не меняется,а новые значения добавились в список


x = (9, 8, 7, 6, 5, 4, 3)
y = []
for i in range(len(x)):
    y.append (x[i] + 3)
print(x)
t = list(x)  #При помощи конвертирующей функции list, список пределывается в кортеж
t[0] = 10
x = tuple(t)
print(x)

#Методы кортежа их всего два count и index
x = (9, 8, 7, 6, 5, 4, 3)
print(x.count(9)) #Позволяет узнать сколько элиментов в кортеже

x = (9, 8, 7, 6, 5, 4, 3)
print(x.index(9)) #Возвращает индекс элимента

h = (1, 2, 3) #К кортежу можно добавить еще один кортеж
h += (4, 5)
print(h)


h = (1, 2, 3)
g = h    #Тут не просто передается ссылка на объект, а он копируется
h += (4, 5)
print(h)
print(g) #создается новый для этой переменной

# Функция enumerate________________________________________________________________________________________________
# Эта функция преобразует каждый элемент последовательности в кортеж.
# Первым в кортеже будет идти индекс элемента последовательности.
# Вторым — сам элемент последовательности.
i = 0
list_ = ["Первое слово", "Второе", "Третье слово"] # Корявая версия ниже лучше
for e in list_:
    print(i, e)
    i += 1

list_ = ["Первое слово", "Второе", "Третье слово"]
for el in enumerate(list_):
    # в каждой итерации enumerate будет
    # создавать кортеж из двух элементов
    print(el[0], el[1])

list_ = ["Первое слово", "Второе", "Третье слово"]
for el in enumerate(list_):
    i, e = el
    print(i, e)

list_ = ["Первое слово", "Второе", "Третье слово"]
for i, e in enumerate(list_):
    # в каждой итерации enumerate будет
    # создавать кортеж из двух элементов.
    # Этот кортеж, в свою очередь,
    # будет распакован в переменные
    print(i, e)

# Выводит списком текст несколько разных версий
a = ("Китайские товары со всего мира")
q = a.split()
for i, w in enumerate(q, start=1):
    print(f"{i} {w}")

a = input()
q = a.split()
for i, w in enumerate(q, start=1):
    print(f"{i} {w}")

a = input().split()
for i, w in enumerate(a, start=1):
    print(f"{i} {w}")

a = input().split()
for i, w in enumerate(a):
    print(i + 1, w)

a = input("Введите предложение: ")
for i, w in enumerate(a.split(), 1):
    print(f"{i} {w}")

for i, w in enumerate(input().split(), 1):
    print(f"{i} {w}")

print(*[f"{i} {word}" for i, word in enumerate(input("Введите предложение: ").split(), 1)], sep='\n')

# Рисуем круги которые шевелятся
import random
import tkinter
import time
colors = ('chocolate2', 'cornflower blue', 'DarkViolet', 'GreenYellow', 'DodgerBlue4', 'DeepPink', 'MediumPurple')
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()
while True:
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    for i, q in enumerate(range(150, 180, 5)):
       canvas.create_oval(x + q, y + q, x - q, y - q, outline=colors[i])
       time.sleep(0.05)
       window.update()
window.mainloop()


# версия чуть проще
import random
import tkinter as tk
import time
colors = ('chocolate2', 'cornflower blue', 'DarkViolet', 'GreenYellow', 'DodgerBlue4', 'DeepPink', 'MediumPurple')
window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
while True:
    x, y = random.randint(0, 400), random.randint(0, 400)
    for i, q in enumerate(range(150, 180, 5)):
        canvas.create_oval(x + q, y + q, x - q, y - q, outline=colors[i])
        time.sleep(0.05)
        window.update()
window.mainloop()



import tkinter as tk
import random
import time
def create_circle(canvas, x, y, radius, color):
    return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=color)
def main():
    window = tk.Tk()
    window.title("Animated Circles")
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()
    colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
    while True:
        for radius in range(150, 181, 5):
            color_index = (radius - 150) // 5
            color = colors[color_index]
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            circle = create_circle(canvas, x, y, radius, color)
            canvas.update()
            time.sleep(0.05)
            canvas.delete(circle)
    window.mainloop()
if __name__ == "__main__":
    main()

# Игра
import tkinter
import random
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(0, 0, 300, 110, fill = 'LightSkyBlue1')
canvas.create_rectangle(0, 110, 300, 200,outline = 'green4', fill = 'green4')
canvas.create_rectangle(269, 70, 278, 140,outline = 'Black', fill = 'burlywood4')
canvas.create_oval(250, 30, 297, 100, outline = "Black", fill = 'chartreuse4')
canvas.create_rectangle(11, 60, 49, 175,outline = 'Black', fill = 'burlywood4')
canvas.create_oval(-50, -85, 110, 85, outline = "Black", fill = 'chartreuse4')
canvas.create_rectangle(100, 0, 200, 200,outline = 'Black', fill = 'burlywood4')
x = 150
y = 100
target = int((x / y) * 10)
colors = ["red", "white"]
fill_color = "red"
for i in range(5, 0, -1):
    canvas.create_oval(x - 20 * i, y - 20 * i, x + 20 * i, y + 20 * i, outline = "black", fill = fill_color)
    fill_color = colors[i % 2]
canvas.create_rectangle(142, 99, 158, 101, outline = 'Grey')
canvas.create_rectangle(149, 92, 150, 108, outline = 'Grey')
window.update()
for i in range(1, 21):
    window.update()
    a = input(f'Выстрел {i}: ')
    if a.isdigit():
        a = int(a)
        if a > target:
            print('Перетянул тетиву!')
        elif a < target:
            print('Недотянул тетиву!')
        else:
            print('В яблочко!!')
            canvas.create_rectangle(147, 97, 153, 103, fill = 'Black')
            window.update()
            break
        x_ = random.randint(100, 200)
        y_ = random.randint(20, 180)
        canvas.create_rectangle(x_, y_, x_ + 3, y_ + 3, fill = 'Black')
        window.update()
    else:
        print('Потерял стрелу! (ввел не число)')
else:
    print('Закончились стрелы!')
window.mainloop()



# Треугольник паскаля
n = 7
p = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = p[i - 1][j - 1] + p[i - 1][j]
    p.append(row)
for r in p:
    print(r)




#____________Преобразование коллекций_______________________________________________________________________
# Иногда бывает нужно преобразовать кортеж или, например, строку в список.
# Встроенная функция list() создана как раз для этого.
# Вообще, list() преобразует в список любую коллекцию. Эта программа
my_string = "Моя строка"
my_tuple = ("Мой", "кортеж")
print(list(my_string))
print(list(my_tuple))
# То есть, каждая буква строки my_string и каждый элемент кортежа my_tuple стали элементами списка.

# Функция tuple() работает точно также, но на выходе будет не список, а кортеж. Результатом выполнения этого кода
my_string = "Моя строка"
my_list = ["Мой", "список"]
print(tuple(my_string))
print(tuple(my_list))

# Если попробовать преобразовать в список или кортеж число, программа закончится с ошибкой
# То есть, преобразование в список или кортеж возможно только из коллекций.!!!!!!!!!!!!!!





#______________________________Словарь__________________________________________________________________
# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# Их иногда ещё называют ассоциативными массивами или хеш-таблицами.

# Методы словарей

# dict.clear() - очищает словарь.
# dict.copy() - возвращает копию словаря.
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# dict.values() - возвращает значения в словаре.

# Чтобы работать со словарём, его нужно создать.
# Сделать это можно несколькими способами. Во-первых, с помощью литерала:

q = {}
print(q)

w = {'dict': 1, 'dictionary': 2}
print(w)

# Во-вторых, с помощью функции dict:
e = dict(short='dict', long='dictionary')
print(e)

r = dict([(1, 1), (2, 4)])
print(r)

# В-третьих, с помощью метода fromkeys:
t = dict.fromkeys(['a', 'b'])
print(t)
y = dict.fromkeys(['a', 'b'], 100)
print(y)

# В-четвертых, с помощью генераторов словарей, которые очень похожи на генераторы списков.
u = {a: a ** 2 for a in range(7)}
print(u)

# Добавление в словарь и изменение
i = {1: 2, 2: 4, 3: 9}
i[1] = 'изменили цифру на 5'
print(i)
i[4] = 'добавление значения'
print(i)

#Чтобы получить значение ключа в каждой итерации,
# нужно указать ключ k для my_dict в квадратных скобках. Например, эта программа
# и плюс два способа
my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}
for k in my_dict:
    print(k, '=', my_dict[k])


my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}
for k,e in enumerate(my_dict):
    print(k,'=',e)


my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}
for k,e in my_dict.items():
    print(k,'=',e)


# Некоторая работа со словарем___

y = dict.fromkeys(['a', 'b'], 100)
d = y.copy()
d['c'] = 222
q = d.get('f', ['ложь'])
d.setdefault('d','555')
print(q)
print(y)
print(d)
for i in d: # обходит по ключам keys
    print(i)
for x in d.values(): # обходит по значению ключа, использовал метод возвращения ключа
    print(x)
for v in d.items(): # обходит по словарю, возвращает все значения в виде кортежа
    print(v)
for key, value in d.items(): # вернул ключ и значение
    print(key, value)
d2 = {'a':'one', 2:'two', 3: 'free', 4:'four'} # тут изменили ключ вначале, нужно смотеть внимательно, так можно полностью изменить словарь
d2 = d.update(d2)                              # главное, чтобы ключи совпадали одного словаря и из пременной где новые значения
print(d)
d3 = {**d, **y} # Объединение двух словарей, выше способ тоже помогает
print(d3)       # тут главное не путаться если менять местами переменные


# работа одного из методов
first_dict = {
    "Давление":750,
    ('утро', 'день', 'вечер'):["низ","сред", "выс"],
    15.7:"широта"}
for k, v in first_dict.items():
    print(k, v)

# Для того чтобы код было удобнее читать, при создании словаря можно расположить его элементы на разных строках:
my_dict = {
    "first": "Первый",
    "second": "Второй",
    3: "Третий"
}

# Код создания словаря
# Инициализация пустого словаря
my_dict = {}
# Запрос у пользователя ввода данных для словаря
while True:
    key = input("Введите ключ (или введите 'exit' для завершения): ")
    # Проверка на выход из цикла
    if key.lower() == 'exit':
        break
    value = input(f"Введите значение для ключа '{key}': ")
    # Добавление пары ключ-значение в словарь
    my_dict[key] = value
# Вывод окончательного словаря
print("Ваш словарь:", my_dict)

# Еще работа со словарем, все одно и тоже
catalog = {}
for i in range(3):
    t = input('товар ')
    c = int(input('цифра '))
    catalog[t] = c
for k, e in catalog.items():
    print(k,'=',e)

catalog = {}
for i in range(3):
    name = input("Введите название: ")
    catalog[name] = int(input("Введите кол-во: "))
print(catalog)

catalog = {}
for i in range(3):
    name = input("Наименование товара ")
    catalog[name] = input("Количество ")
for name in catalog:
    print("{}: {}".format(name, catalog[name]))

catalog={}
for i in range(3):
      catalog.update({input():input()})
for c in catalog:
    print(c,catalog[c])

catalog = {}
for i, w in enumerate(range(3), start=1):
    t = input(f"Введите наименование товара {i}: ")
    c = input("Введите количество товара: ")
    catalog[t] = c
print("\nТовары в каталоге:")
for k, e in catalog.items():
    print(f"{k}: {e}")

# этот считает правильней кодличество товара
catalog = {}
for i in range(3):
    t = input('товар ')
    if t in catalog:
        catalog[t] += int(input())
        continue
    c = int(input('цифра '))
    catalog[t] = c
for k, e in catalog.items():
    print(k,'=',e)

# C методом get
catalog = {}
for _ in range(3):
    name = input('Введите наименование: ')
    quant = int(input('Введите количество: '))
    catalog[name] = catalog.get(name, 0) + quant
print(catalog)


# Программа подсчета слов одинаковых все одно и тоже
a = input().replace('.', ' ').replace(',', ' ').lower().split()
q = {}
for i in a:
    q[i] = a.count(i)
for w, s in q.items():
    print(w, '/', s)


string = input().lower().replace(',', ' ').replace('.', ' ').split()
result = {}
for word in string:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1
for key in result:
    print(f'{key}: {result[key]}')


s = input().lower().replace('.', ' ').replace(',', ' ').split()
sl = {}
for i in s:
# i-ключ
# z-значение
    z = s.count(i)
    sl[i] = z
for d in sl:
    print(d, ':', sl[d])


import collections
from collections import Counter
string = (input()).lower().replace('.', ' ').replace (',', ' ').split()
count = Counter(string)
for k in count:
    print(k, ':', count[k])


string = input()
string = string.replace('.', ' ').replace(',', ' ').lower().split()
dict_ = {}
for s in string:
    dict_[s] = string.count(s)
    print(s, ':', dict_[s])


# тоже самое, что выше, сортирует по алфавиту
a = input().replace('.', ' ').replace(',', ' ').lower().split()
q = {}
for i in a:
    q[i] = a.count(i)
k = list(q.keys())
k.sort()
for i in k:
    print(i, '/', q[i])

# список из словарей с одним ключем
dicts = []
for i in range(3):
    data = {}    # тут словарь нужно сделать в теле цикла иначе ключи будут ссылаться на один id!
    data['key'] = i
    dicts.append(data)
print(dicts)



# Разница между == и is _________
# То есть, оператор == проверяет равенство значений объектов, а оператор is — идентичность.

a = {"key": 1}
b = a
c = {"key": 1}

# a это b, то есть буквально
# это тот же самый объект в памяти
print(a is b)

# ну и конечно же a равно b
print(a == b)

# a и c -- разные объекты в памяти.
# поэтому is вернет False
print(a is c)

# но в это же время они равны
# то есть у них одинаковые значения
print(a == c)
____

# Летающие круги
import tkinter
import random
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()
colors = ("chartreuse", "cornflower blue", "dark salmon", "dark slate gray", "green yellow")
circles = []
for i in range(5):
    # случайный цвет и размер для каждого из кругов
    size = random.randint(10, 50)
    color = random.choice(colors)
    # случайные координаты для каждого из кругов
    # - size нужен для того, чтобы круги изначально не попали за границы холста
    x = random.randint(0, 400 - size)
    y = random.randint(0, 400 - size)
    circle = {
        "dx": random.randint(-10, 10),
        "dy": random.randint(-10, 10),
        "id": canvas.create_oval(x, y, x + size, y + size, fill=color),
    }
    circles.append(circle)
while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        # если левая или правая координата круга вышла за границы
        # меняем знак изменения движения
        if x0 < 0 or x1 > 400:
            circle['dx'] = -circle['dx']
        # тоже самое для верхней и нижней координаты
        if y0 < 0 or y1 > 400:
            circle['dy'] = -circle['dy']
        canvas.move(circle['id'], circle['dx'], circle['dy'])
        time.sleep(0.01)
    canvas.update()









#____________________________________________Функция def, определение и вызов_________________________________________
# ctrl + space кнопки дают возможность увидеть полный список встроенной видимости
# Функция должна быть выравнена в пайчарм это команда ctrl - alt - l
# по PIP8 должно быть два пробела до вызова функции
print('До функции')
def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
show()     # Команда запуска
print('после функции')
show()


# При чем фукцию можно расположить в рахных местах
# определение функции это всего лишь инструкция
def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
print('До функции')
show()     # Команда запуска
print('после функции')
show()






# лучший пример для чего нужна фунция, модуль черепашка
import turtle


def move(a):  # сделал функцию для того чтобы код был меньше и ниже функция вызывается
    turtle.forward(a)  # это для линии
    turtle.left(90)  # поворот


# это без цвета
def drawsquare(a):  # эта функция вызывает четыре раза команды выше, чтобы не писать много строчек кода
    for i in range(4):
        move(a)


# Это цветная
def drawsquarecolor(a, color):  # для цвета, color переменная отвечает за цвет
    turtle.color(color)  # команда для заполнения цветом и в нее передается переменная с цветом который предавался
    turtle.begin_fill()  # команда начала заполнения цвета
    drawsquare(a)  # предал сюда функцию, чтобы не писать такой же цикл for
    turtle.end_fill()  # команда конец заполнения цвета


turtle.speed(1)
drawsquarecolor(60,'red')        # можно передать аргумет чтобы изменить размер квадрата, аргумет буква а, тут в этом выводе функции пишем размер
turtle.goto(150, 150)               # координаты х, у чтобы переместится в другое место, также можно указать минус (-)
drawsquarecolor(120, 'blue')     # тут в этом выводе функции пишем размер
#




# Оператор return
def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    x = 49
    return res
# два пробела по pip8 # Функция должна быть выравнена в пайчарм это команда ctrl - alt - l
# два пробела по pip8 # Функция должна быть выравнена в пайчарм это команда ctrl - alt - l
a = get_sqrt(49)
print(a)


def even(x):
    return x % 2 == 0
# два пробела pep8
# два пробела pep8
for i in range(1, 20):
    if even(i):
        print(i)

# Четное и нечетное
def cifr(a):
    if a % 2 == 0:
        print(a, 'chetnoe')
    else:
        print(a, 'nechetnoe')


for i in range(0, 20):
    cifr(i)



def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
def show2():
    x = 7
    return x
y = show2()
print(y)
show()
# Оператор return  нужен для того, чтобы вернуть результат работы функции в точку запуска

# Также переменные нужно записывать выше точки запука
def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
def show2():
    x = 7 + z
    return x
z = 7
y = show2()
print(y)
show()

# 1 версия кода
def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
def show2():
    x = 7 + z
    return x
z = 7
y = show2()
print(y)
z = 9
t = show2()
print(t)

# 2 версия кода
def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
def show2():
    x = 7 + z
    return x
z = 7
y = show2()
print(y)
z = 9
print(show2())


def show():   # Имя функции и определение
    print('функция')  # Код принадлежащий функции
def show2():
    x = 7
    return x
y = show2()
z = show2() + 9
print(z)
show()
# return есть запуск функции через переменную с возвратом значения, мы в переменную
# помещаем, то значение, которое вернет return из функции в точку запуска,
# сохраняется в переменную y  и через эту переменную мы дальше работаем в программе


# Будем воспроизводить действие функции len
# с помощью цикла for

j = [9, 8, 7, 6]
count = 0
for i  in j:
    count += 1
print(count)
h = ['a', 'a', 'h']
k = [9, 8, 7, 5, 7, 5]
# Чтобы не повторять этот код это повод создать функцию!

def count_list():
    count = 0
    for i in j:
        count += 1
    return count
j = [9, 8, 7, 6]  # Получили длинну только этого
print(count_list())
h = ['a', 'a', 'h']
k = [9, 8, 7, 5, 7, 5]
# Встает вопрос как получить длину других списков
# для этого есть такая функция как параметр ей можно дать любое имя

def count_list(par): #parametr
    count = 0
    for i in par:    # Переменную par перебираем циклом
        count += 1
    return count
j = [9, 8, 7, 6]
print(count_list(j)) #argument
h = ['a', 'a', 'h']
k = [9, 8, 7, 5, 7, 5]
# Таким образом наша функция стала универсальной, теперь мы можем передавать в ней
# любые значения и переменные, любой последовательности в виде аргумента и нам она будет
# выдавать длину

def count_list(par):
    count = 0
    for i in par:
        count += 1
    return count
j = [9, 8, 7, 6]
print(count_list(j))
h = ['a', 'a', 'h']
print(count_list(h))
k = [9, 8, 7, 5, 7, 5]
print(count_list(k))

# Также легко выдаст длину строк
def count_list(par):
    count = 0
    for i in par:
        count += 1
    return count
print(count_list('fsfsggtehetytey'))
print(count_list('hghghdhdghghh'))
print(count_list('ghteetef'))

# Пропишем еще один параметр и переместим в него переменную count
# известный как параметр по умолчанию, изначально прописано определение какой то функции
def count_list(par, count = 0):
    for i in par:
        count += 1
    return count
j = [9, 8, 7, 6]
print(count_list(j))

# Также в параметре можно не указывать значение,
# тогда его нужно указать в аргументе
def count_list(par, count): #parametr
    for i in par:
        count += 1
    return count
j = [9, 8, 7, 6]
print(count_list(j, 0)) #argument


def count_list(par, count): #parametr
    for i in par:
        count += 1
    return count
j = [9, 8, 7, 6]
print(count_list(j, -1)) #argument

# Также в параметре можно не указывать значение,
# тогда его нужно указать в аргументе
# если прописать -1 вернет индекс последнего элимента
# Таким образом функция универсальна показывает длину списка или индекс


# Добавим еще один функционал,добавим параметр и булевое значение
def count_list(par, par2 = False,count = 0): #parametr
    if par2 == True:
        typ = type (par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count
j = [9, 8, 7, 6]
print(count_list(j, True)) #argument #Тут можно укзать три параметра (j, True, -1))


# Можно распаковать на две переменных в одной длина списка
# в другой тип данных
def count_list(par, par2 = False,count = 0): #parametr
    if par2 == True:
        typ = type (par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count
j = [9, 8, 7, 6]
h,p = count_list(j, True) #argument







# Функции переменное количесиво аргументов, параметр *args
# *args - звездочка упаковывает в кортеж
# * упаковывает все в список, если пременных меньше или больще a, *b, c = 1, 2, 3, 4, 5, 6 , помогает распаковывать
# **kwargs распаковывает в словарь
def name (*a):
    print(a)
name (7, )

# Первый праметр упаковывается в первый аргумент, остальное в кортеж
def name (h, *args):
    print (h)
    print(args)
name (1, 2 , 3)

# Также могут быть дополнительные параметры
def name (h,g, *args):
    print (h)
    print(g)
    print(args)
name (1, 2 , 3)

# Могут понадобиться дополнительные параметры они записываются после *args
# и называются ключевые параметры
# Особенность ключевого параметра ему нужно присвоить значение иначе ошибка
def name (h,g, *args, key):
    print (h)
    print(g)
    print(args)
    print(key)
name (1, 2 , 3,5,6, key=10)





def f(**kwargs):
    print(kwargs)

f(a=1, b=2,c=3)

# Задача создать функцию, алгоритм который могут использовать другие разработчики
# они будут предавать туда списки с данными, а функция будет им выдвать результат
# тоже список, только все значения будут уникальными т.е все повторяемые значения
# будут отсеиваться из всех списков которые были преданы, будет один список с уникальными
# значениями.
def  exclusive_item(*args):
    new_list = []      #тут определяем наш список
    for i in args:     #списки формируются в кортеж тут обрабатываем циклом
        for y in i:    #тут итерируем циклом
            if y not in new_list:  #тут прописываем условия
                new_list.append(y) #тогда его добавляем в новый список
    return new_list #возвращает новый список
z = [9,8,7]
x = [8,8,9,7,6,5]
c = [1,2,3,4,5,6,7,7]
t = exclusive_item(z,x,c) #все списки предаем в пременную,она все возвращает
print(t)

# Расширяем возможности функции, вернула отсортированный список
def  exclusive_item(*args, key = False):
    new_list = []      #тут определяем наш список
    for i in args:     #списки формируются в кортеж тут обрабатываем циклом
        for y in i:    #тут итерируем циклом
            if y not in new_list:  #тут прописываем условия
                new_list.append(y) #тогда его добавляем в новый список
    if key == True:  #будем тут проверять
        new_list.sort()  #сортируем список
    return new_list #возвращает новый список
z = [9,8,7]
x = [8,8,9,7,6,5]
c = [1,2,3,4,5,6,7,7]
t = exclusive_item(z,x,c, key=True) #все списки предаем в пременную,она все возвращает
print(t)


# Функции, область видимости переменных global, nonlocal____________________________

# передаем значение между функциями, захламленный код и структурированный
x = 5
def name():
    x = 100
    return x
h = name()
def name2():
    print(h)
name2()



x = 5
def name():
    x = 100
    return name2(x)
def name2(par):
    print(par)
name()


# Функция и операторы сравнения
while True:
    def cal():
        if a < b:
            return (f'{a} a меньше')
        elif a > b:
            return (f'{b} b меньше')
        elif a == b:
            return (f'{a} и {b} равны')


    a = float(input())
    b = float(input())
    print("Сумма= ", a + b)
    print(cal())







# ________________Передача значений между функциями_____________
import math
PI = math.pi
def radius():
    n = float(input('Диаметр цилиндра в см: '))
    n /= 2
    return n
def height():
    m = float(input('Высота цилиндра в см: '))
    return m
def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s * h
    return v
print('Объем цилиндра:', volume(), 'см3')
# можно закоментировать принт выше и дописать код
def massa(g):
    n = float(input('Удельный веc г/см3: '))
    return g * n / 1000
print('Вес цилиндра в кг: ', massa(volume()))
# Для чего это надо, чтобы создавать меньше переменных в глобальной зоне видимости
# это не перегружает память и код выглядит лучше





# Факториал числа с модулем и без_________
import math
b = int(input())
a = math.factorial(b)
print(a)


#_________while
def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    print('Факториал числа = ',f)
factorial(int(input('Введите число: ')))


# тоже, что и выше только с return
def factorial(n):
    f = 1
    while n > 1:
        f = f * n
        n -= 1
    return f


factorial(int(input('Введите число: ')))

#_____for
def factorial(n):
    h = 1
    for i in range(h, n + 1):
        h = h * i
    return h


number = int(input('Введите число: '))
f = factorial(number)
print(f)



# тоже, что и выше только с return
def factorial(n):
    h = 1
    for i in range(h, n + 1):
        h = h * i
    return h


factorial(int(input()))


# Обьяснение к четырем выше программам____ и как вывести на экран
# for

def factorial(n):
    # В этой переменной мы будем
    # "накапливать" факториал числа
    result = 1
    for i in range(1, n + 1):
        # каждую итерацию цикла нужно умножать
        # число из последовательности на переменную result
        result = result * i
    # возвращаем значение переменной result из функции
    return result

number = int(input('Введите число'))
f = factorial(number)
# Теперь в переменной f у нас результат работы функции factorial
print(f)

# while
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

number = int(input('Введите число: '))
f = factorial(number)
print(f)


# В этом примере введенное пользователем число проверяется на корректность,
# а затем передается в функцию factorial, которая вычисляет факториал с использованием цикла.
# Результат выводится на экран.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Получение числа от пользователя
user_input = input("Введите натуральное число для вычисления факториала: ")

# Проверка на корректный ввод числа
try:
    n = int(user_input)
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    # Вызов функции factorial и вывод результата
    result = factorial(n)
    print(f"Факториал числа {n} равен: {result}")





def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

num = int(input("Введите число: "))
print("Факториал числа", num, "равен", factorial(num))



# Необязательные аргументы____
# Аргумент функции может быть необязательным.
# Для этого ему надо назначить значение по‑умолчанию. Например, эта программа
def sum(a, b=2):
    c = a + b
    return c

z = sum(5)
print(z)


# Особенности значений по умолчанию___
#Значения по‑умолчанию вычисляются только один раз — в момент объявления функции.
#Это важная особенность, незнание которой может привести к сюрпризам. Попробуйте запустить следующий пример:
default_value = 1

def f(value=default_value):
    print(value)

f(4)    # выведет 4
f()     # выведет 1 – значение по-умолчанию
default_value = 10
f()     # все равно 1, так как default_value
        # было равно 1 на момент объявления


def add_value(value, values=None):
    if values is None:
        values = []
    values.append(value)
    print(values)

add_value(1)
add_value(2)


def add_value(value, values=None):
#    if values is None:
    values = []
    values.append(value)
    print(values)

add_value(1)            # [1]
add_value(2)            # [2]
add_value(3, [0, 0])    # [3]


# Область видимости____________
a = "Глобальная переменная"

def f():
    a = "Локальная переменная"
    print(a)

f()
print(a)

# Если внутри функции нет переменной а, но она есть глобально в файле,
# то при попытке обратиться к переменной a внутри функции, будет использована глобальная переменная:
a = "Глобальная переменная"

def f():
    print(a)

f()
print(a)


# В общем, чтобы изменить глобальную переменную из функции, нужно использовать ключевое слово global.
# Так мы можем заставить Python изменить не локальную, а глобальную переменную.
# Однако, даже с учетом того, что такая возможность есть, не нужно изменять глобальные переменные внутри функции.
# Сообщество Python объявило такую практику нежелательной, так как из‑за этого изменение кода становится намного сложнее.
a = "Глобальная переменная"

def f():
    global a
    a = a + " с дополнением из функции"
    print(a)  # или return a

print(a, '(до вызова функции)')
f()
print(a, '(после вызова функции)')




# Задача Выбор формы существительного, разные варианты:____
# Объяснение:
# Теперь разберем условия выбора варианта:
# Если последняя цифра числа равна 1, и при этом число не оканчивается на 11 (например, 11, 111, 211 и так далее), то выбирается вариант с индексом 0.
# Если последняя цифра числа находится в диапазоне от 2 до 4 (включительно),
# и при этом число не оканчивается на 12, 13, 14 (например, 12, 113, 214 и так далее), то выбирается вариант с индексом 1.
# в остальных случаях выбирается вариант с индексом 2.
def choose_plural(a, b):
    # Проверяем условия для выбора правильной формы множественного числа
    if a % 10 == 1 and a % 100 != 11:
        v = 0
    elif a % 10 >= 2 and a % 10 <= 4 and \
            (a % 100 < 10 or a% 100 >= 20):
        v = 1
    else:
        v = 2

    # Возвращаем строку, объединяя количество и выбранный вариант из списка
    return '{} {}'.format(a, b[v])


result_1 = choose_plural(23, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(7, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(51, ('цент', 'цента', 'центов'))
print(result_3)



# еще
def choose_plural(q, w):
    if q % 100 in [11, 12, 13, 14]:
        return f"{q} {w[2]}"
    elif q % 10 == 1:
        return f"{q} {w[0]}"
    elif 2 <= q % 10 <= 4:
        return f"{q} {w[1]}"
    else:
        return f"{q} {w[2]}"


result_1 = choose_plural(23, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(7, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(51, ('цент', 'цента', 'центов'))
print(result_3)


# еще с циклом for переделанная выше
def choose_plural(q, w):
    for i in range(3):
        if q % 100 in [11, 12, 13, 14]:
            return q, w[2]
        elif q % 10 == 1:
            return q, w[0]
        elif 2 <= q % 10 <= 4:
            return q, w[1]
        else:
            return q, w[2]


result_1 = choose_plural(23, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(7, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(51, ('цент', 'цента', 'центов'))
print(result_3)





# еще с циклом for
def choose_plural(a, words):
    a = str(a)
    for a5_15 in range(5, 15):
        if a[-1] == str(a5_15) or a[-2:] == str(a5_15) or a[-1] == '0':
            b = 2
            break
        elif a[-1] == '1':
            b = 0
        else:
            b = 1
    return f'{a} {words[b]}'
a = int(input())

print(choose_plural(a, ("банан", "банана", "бананов")))



result_1 = choose_plural(23, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(7, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(51, ('цент', 'цента', 'центов'))
print(result_3)



# еще
def choose_plural(quantity, cases):
    if 5 <= quantity % 10 <= 9 or quantity % 10 == 0 or 10 <= quantity % 100 <= 20:
        return quantity, cases[2]
    elif quantity % 10 == 1:
        return quantity, cases[0]
    else:
        return quantity, cases[1]



result_1 = choose_plural(746, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(304, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(20, ('цент', 'цента', 'центов'))
print(result_3)


# еще
def choose_plural(a, b):
    for i in range(3):
        # Проверяем условия для выбора правильной формы слова
        if i == 0 and a % 10 == 1 and a % 100 != 11:
            return a, b[i]                                  # способ переноса нижу
        elif i == 1 and a % 10 >= 2 and a % 10 <= 4 and \
                (a % 100 < 10 or a % 100 >= 20):
            return a, b[i]
        elif i == 2:
            return a, b[i]

# Вызываем функцию с примером: choose_plural(1, ('цент', 'цента', 'центов'))
result = choose_plural(1, ('цент', 'цента', 'центов'))

# Выводим результат
print(result)


# Шифр Цезаря________
def encrypt(s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = ""

    # Преобразование строки к верхнему регистру
    s = s.upper()

    for char in s:
        if char in letters:
            # Определение индекса символа в алфавите
            index = letters.find(char)

            # Шифрование символа с учетом направления сдвига (вправо или влево)
            encrypted_index = (index + k) % len(letters)
            result += letters[encrypted_index]
        else:
            # Символы, не принадлежащие алфавиту, добавляются «как есть»
            result += char

    return result


# Пример использования
message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)

print(encrypted_message)
print(decrypted_message)


# второй вариант_
def encrypt(message, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    message = message.upper()
    # в этой строке мы создаем сдвинутый на значение k алфавит
    # то есть, например, при ключе 3 алфавиту
    # АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
    # будет соответствовать
    # ГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ
    letters_tmp = letters[k % 33:] + letters[0:k % 33]
    # создание таблицы переводов для строки. Каждой
    # букве letters будет соответствовать буква из letters_tmp
    transtab = str.maketrans(letters, letters_tmp)
    # метод translate заменит все символы в строке согласно
    # таблице переводов transtab
    return message.translate(transtab)


message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)

print(encrypted_message)
print(decrypted_message)


# Третий вариант_
def encrypt(message, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    message = message.upper()
    result = ''
    for i in message:
        index = letters.find(i)
        if index != -1:
            # остаток от деления тут используется для того,
            # чтобы не было выхода за пределы строки letters
            # и не возникала ошибка IndexError
            result += letters[(index + k) % len(letters)]
        else:
            result += i
    return result


message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)

print(encrypted_message)
print(decrypted_message)




# Четвертый вариант_
letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
index = 0

def encrypt(s, k):
    s = s.upper()
    result = ""

    for tmp in s:
        if tmp in letters:
            index = letters.find(tmp) + k
            if index > 0 and index < 33:
                result += letters[index]
            elif index >= 33:
                while index >= 33:
                    index = index - 33
                result += letters[index]
            elif index < 0 and index > -33:
                result += letters[index]
            else:
                while index <= -33:
                    index = index + 33
                result += letters[index]
        else:
            result += tmp
    return result

message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)
print(encrypted_message)
print(decrypted_message)


# Пятый вариант
def encrypt(s, k):
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    s = s.upper()
    itog = ''
    k = k % len(letters)
    letters_2 = letters[k:] + letters[:k]
    itog = s.maketrans(letters, letters_2)
    return s.translate(itog)

print(encrypt("ПРИВЕТ WORLD!", 5))
print(encrypt("ФХНЖЙЧ WORLD!", -5))


# Шестой вариант
def encrypt(s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s = s.upper()
    k = k % len(letters)
    transtab = str.maketrans(letters, letters[k:] + letters[:k])
    return s.translate(transtab)

message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)
print(encrypted_message)
print(decrypted_message)

#______________________________________Обработка исключений______________________________________________________
# Конструкция try...except
# Чтобы обработать исключение, код, который потенциально может «выбросить» исключение нужно выполнять в блоке try,
# а исключения перехватывать в блоке except. Например, программу из прошлого урока можно переписать вот так
# Примеры
a = input("Введите число")
try:
    a = int(a)
except ValueError:
    print('Вы ввели не число')


try:
    a = int(input())
    b = int(input())
    print(a + b)
except ValueError:
    print('Вы ввели не число')



def ent_num(s=''):   # Функция ввода
    err = 0          # по умолчанию нет ошибки - 0
    a = 0
    try:
        a = int(input(f"Введите число {s}:"))
    except ValueError:
        err = 1
    return (a, err)   # Функция возвращает кортеж, из 2-х элем.
                      # где 1 - число, 2 - ошибка.

a = ent_num('A')
b = ent_num('B')

if a[1] or b[1]:      # проверка на ошибку 1 -ошибка, 0 -нет
    print('Вы ввели не число')
else:
    print("Результат суммы числа А и Б: ", a[0] + b[0])


# Также ошибки бывают разными и для каждого исключения можно прописать
# но лучше исключения разделать, чтобы понимать какое из них
try:
    a = int(input())
    z = int(input())
    div = a / z
    print(div)
except (ValueError, ZeroDivisionError):
    print("Вы ввели не число")

# вариант с разделенными исключениями
try:
    a = int(input())
    z = int(input())
    div = a / z
    print(div)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print('Второе число не может быть нулем')

# Блок finally и else___
# В конструкцию try ... except опционально можно добавить еще два блока. Это finally и else
# Для примера возьмем программу из прошлого урока, уберем обработку ZeroDivisionError и добавим еще два блока: finally и else
try:
    a = int(input())
    b = int(input())
    div = a / b
except ValueError:
    print("Вы ввели не число")
else:
    print(div)
finally:
    print('Конец программы')
print('Второй конец программы')
# Все, что находится в блоке else выполняется только тогда, когда исключений не было.
# Код в блоке finally выполняется в любом случае, было ли исключение, или нет.

# Обратите внимание, что программа выводит «Конец программы» в любом случае.
# А «Второй конец программы» только тогда, когда исключений нет или исключение обработано.
# То есть, если ввести вторым числом ноль, надпись «Второй конец программы» не будет выведена на экран.



#  Даже если в функции division был бы вызов еще одной функции, любое необработанное исключение «всплыло» бы вверх. Постарайтесь запомнить,
#  что в ваш обработчик try ... except может попасть исключение из любых вызываемых функций, если исключения не было обработано внутри этих функций.
def division(dividend, divider):
    return dividend / divider

try:
    a = int(input())
    z = int(input())
    result = division(a, z)
    print(result)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print('Второе число не может быть нулем')

# На самом деле невозможно сделать правильно проверяемыми вообще все исключения, так как некоторые исключительные ситуации по своей природе таковы,
# что их возникновение возможно в любом или почти любом месте программы, а предотвратить их программист не в состоянии.
# В общем, стоит запомнить, что обрабатывать исключения предпочтительно явно. То есть нужно указывать тип исключения после ключевого слова except.
# Также запомните, что не стоит обрабатывать все исключения. Например, возникло исключение NameError. Это означает,
# что где‑то в программе используется несуществующая переменная и нужно определенно исправлять эту ошибку, а не писать обработчик.

# лайфхак этот выведит все в виде простой функции принт если поставить звездочку
a =[1,2,3,4,5,6]
print(*a)







#_____________________________________Работа с файлами_________________________________________________________________
# Для начала нужно открыть файл. Для этого нужно использовать встроенную функцию open, первый аргумент которой — путь к файлу.
# Если и файл и программа находятся в одном каталоге, достаточно передать имя файла:
f = open('example.txt')

# Функция open возвращает объект файла, с помощью методов которого можно прочитать содержимое файла:
f = open('example.txt')
content = f.read()
print(content)
#
f = open('example.txt')
print(f.read())

# Если имя файла или путь будет неверный, функция open вызовет исключение FileNotFoundError!!!
# Можно поймать методом исключения эту ошибку:
try:
    f = open('example_1.txt')
    content = f.read()
    print(content)
except:
    print('название файла не верно')

# Можно создать так сразу с проверкой исключения:
file = input('Введите название/путь файла:')
try:
    m = open(file).read()
except FileNotFoundError:
    print('Такого файла нет!')
    quit()
print(m)

# У open есть аргумент encoding. Попробуйте вот так открыть, это если закодированный текс с каракулями
open(name, encoding="cp1251")
# этот аргумент ниже поможет разобраться с этими каракулями С‹РІР°Р°С‰РіРіРІР°
f = open('C:/Users/USER/Desktop/example.txt',encoding='utf-8')
content = f.read()
print(content)

# Еще момент который заметил символ '\' нужно ставить так '/': как пример чтения на компьютере
f = open('C:/Users/USER/Desktop/example.txt')
content = f.read()
print(content)

# Можно пробежаться циклом по кодеровкам, но лучше в списке выбрать одну кодеровку
codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8"]
for codec in codecs:
    with open("C:/Users/USER/Desktop/example.txt", "r", encoding=codec) as file:
        text = file.read()
    print(codec.rjust(12), "|", text) # тут метод строки на 12 шагов вперед

# Можно использовать знания предыдущего урока на обработку исключения
try:
    codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8"]
    for codec in codecs:
        with open("C:/Users/USER/Desktop/example.txt", "r", encoding=codec) as file:
            text = file.read()
        print(codec.rjust(12), "|", text)
except UnicodeDecodeError:
    print('такого иероглифа нет с списке')

# Ошибки, связанные с кодировками
# При возникновении ошибки, связанной с кодировками, интерпретатор выдаст одно из следующих исключений:
# UnicodeError. Это общее исключение для ошибок кодировки.
# UnicodeDecodeError. Данное исключение возбуждается, если встречается кодовая позиция, которая отсутствует в кодировке.
# UnicodeEncodeError. А это исключение возбуждается, когда символ, который необходимо закодировать, незнаком для кодировки.


# Указатель позиции в файле___
# У метода объекта файла read есть необязательный параметр size. Это максимальное количество данных, которое требуется считать.
# Если этот параметр не указан или же он отрицательный, содержимое файла будет считано целиком.
f = open('example.txt')
content = f.read(3)
print(content)
# Такая программа прочитает и выведет на экран первые три символа из файла example.txt
# Если попробовать прочитать содержимое файла несколько раз, как в этой программе:
f = open('example.txt')
chunk_1 = f.read(3)
print(chunk_1)
chunk_2 = f.read(5)
print(chunk_2)
# на экран будет выведено первые три и следующие за ними пять символов из файла example.txt.
# Так происходит из‑за внутреннего указателя на текущую позицию в файле. При открытии этот указатель становится в самое начало файла.
# После того, как на второй строке программы мы прочитали три символа из файла, указатель будет уже на четвертой позиции.
# То есть, следующий вызов read будет считывать символы начиная именно с четвертой позиции.

# Для того, чтобы узнать текущую позицию указателя, можно использовать метод объекта файла tell:
f = open('example.txt')
chunk_1 = f.read(3)
print(chunk_1, f.tell())
chunk_2 = f.read(5)
print(chunk_2, f.tell())




# Режимы открытия файлов___
# У функции open много параметров и второй из них — это режим открытия файла.
# Режим открытия файла — это строка, содержащая один или несколько символов из этого списка:
# r	открытие файла на чтение
# w	открытие файла на запись, содержимое файла удаляется, если файла не существует, создается новый
# x	открытие файла на запись, если файла не существует. Если файл существует, возникает исключение
# a	открытие файла на запись, информация добавляется в конец файла
# b	открытие файла в двоичном режиме
# t	открытие файла в текстовом режиме
# +	открытие файла на чтение и запись

# Чтобы записать информацию в файл, нужно использовать метод write у объекта файла, а после записи в файл обязательно закрывать файл методом close.
# Во‑первых, это освобождает занятую память, а во‑вторых поможет избежать странных ошибок с пропавшей или испорченной информацией.
f = open('example_x.txt', 'w')
f.write('Важная информация\n')
f.write('Вторая по важности информация')
f.close()

# Вот так, например, можно открыть файл для записи. Если файла example_x.txt не существует, он будет создан:
f = open('example_x.txt', 'w')

# У оператора with имеется контекст (блок), в котором он будет действовать. Когда приложение выходит из соответствующего контекста,
# with будет автоматически закрывать ранее используемый файл. Все это приводит к тому, что рассматриваемый элемент в the Python носит название «диспетчер контекста».
file = input()
with open(file,'w')as f:
    f.write(input())

# С функцией
#  в «a» указатель всегда в конце при открытии. + дает возможность делать чтение. Потому что «a» — это открытие на запись.
x='exampl.txt'
def read_file(x):
    f = open(x)
    content = f.read() #считываем исходный файл
    print(content)

def write_file(x):
    f = open(x,'a+')
    f.write('\n Важная информация\n')
    f.write('Вторая по важности информация\n')

    content = f.read()
    print(content)
    f.close()
# выполняем функцию
read_file(x)
write_file(x)


# Чтение и запись одновременно___
# Это происходит из‑за того, что указатель после записи передвигается на позицию за последним записанным символом.
# Попробуйте вывести текущую позицию указателя после записи с помощью метода tell, о котором было рассказано в одном из предыдущих уроков и посмотрите на результат.
# Для того, чтобы передвинуть указатель внутри файла на произвольную позицию, можно использовать метод seek.
# Этой функции можно передать два аргумента. Первый, обязательный, — это offset, то есть количество позиций, на которое нужно переместить указатель.
# Если этот аргумент положительный, указатель будет перемещен вправо, если отрицательный — влево.
# Второй, необязательный аргумент — это from_what. С помощью него можно указать, откуда следует переместить указатель:
# 0 — от начала файла, 1 — от текущей позиции и 2 — от конца файла. По‑умолчанию этот аргумент принимает значение 0
f = open('example_x.txt', 'w+')
f.write('Какая-то информация')
z = f.tell() # Позиция указателя
f.seek(0) # или ((-10, 1) и так далее
content = f.read()
print(content)
print(z)
f.close()


# Контекстный менеджер___ по нему написал программу
# Менеджер контекста используется для оборачивания части программы на Python для гарантии,
# что критические функции выполнятся в любом случае, даже при возникновении непредвиденной ошибки.
with open('example.txt', 'w') as f:
    f.write('Первая часть\n')
    user_data = int(input())
    f.write('Пользователь ввел {}'.format(user_data))
# С использованием контекстного менеджера файл будет закрыт в любом случае, даже если произойдет ошибка.
# Вызывать метод close вместе с with ... as не нужно, так как он будет вызван контекстным менеджером автоматически.
with open("example.txt", "w+") as file_example:
    file_example.write(format(input()))

#
name = input() + '.txt'
info = input()
with open(name, 'w') as f:
    f.write(info + '\n')
    f.write(f'Сработал код без ошибок')


# Каталог товаров с сохранением___
catalog = {}
for i in range(3):
    name = input('Введите наименование товара')
    count = int(input('Введите количество товара'))
    # если ключ (наименование товара) уже есть
    # в словаре
    if name in catalog:
        # увеличиваем его значение на count
        catalog[name] += count
    else:
        # иначе создаем ключ со значением count
        catalog[name] = count

# Каждый ключ и значение в каталоге нужно
# # записать в файл через двоеточие
with open('catalog.txt', 'w') as f:   # Вне цикла функция должна идти
    for i in catalog:
        f.write(i + ':' + str(catalog[i]) + '\n')

# Решение 1
catalog = {}
for i in range(3):
    goods = input('Введите название товара: ')
    count = int(input('Введите количество: '))
    if goods in catalog:
        catalog[goods] += count
    else:
        catalog[goods] = count

with open('catalog.txt', 'w') as f:
    for product in catalog:
        f.write(f"{product}:{catalog[product]}\n")



# Решение 2
catalog = {}
for i in range(3):
    n = input('Наменование товара: ')
    c = int(input('Колличество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

e = input('Придумайте название файла: ')
with open(e, 'w') as f:
    for i in catalog:
        f.write(i + ':' + str(catalog[i]) + '\n')
        print(f' файл {e} успешно создан.')

# Решение 3
catalog = {}
for i in range(3):
    n = input('Наменование товара: ')
    c = int(input('Колличество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

e = input('Придумайте название файла: ')
with open(e, 'w') as f:
    for i in catalog:
        f.write(i + ':' + str(catalog[i]) + '\n')
        print(f' файл {e} успешно создан.')

# Решение 4
catalog = {}
for i in range(3):
    n = input('Наменование товара: ')
    c = int(input('Колличество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

f = input('Придумайте название файла: ')
with open(f, 'w') as file:
        for n, c in catalog.items():
            file.write(f"{n}:{c}\n")

# Решение 5
catalog = {}
for i in range(3):
    n, c = input("Введите наименование и количество товара через пробел: ").split()
    catalog[n] = catalog.get(n, 0) + int(c)

filename = input("Введите название файла для сохранения каталога: ")
with open(filename, 'w') as file:
    file.write('\n'.join([f"{n}:{c}" for n, c in catalog.items()]))

print("Каталог сохранен в файл.")

# Решение 6
def save_catalog_to_file(catalog, filename):
    with open(filename, 'w') as file:
        for item, quantity in catalog.items():
            file.write(f"{item}:{quantity}\n")


def main():
    catalog = {}
    for _ in range(3):
        name = input("Введите наименование товара: ")
        quantity = int(input("Введите количество товара: "))

        # Если товар уже есть в каталоге, увеличиваем его количество
        if name in catalog:
            catalog[name] += quantity
        else:
            catalog[name] = quantity

    # Сохраняем каталог в текстовый файл
    filename = input("Введите название файла для сохранения каталога: ")
    save_catalog_to_file(catalog, filename)

    print("Каталог сохранен в файл.")


if __name__ == "__main__":
    main()




# Чтение данных для каталога:____
with open('catalog.txt', 'r+') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
# А еще проще сразу «пройтись» циклом по файлу
with open('catalog.txt', 'r+') as f:
    for line in f:
        print(line)
# В этом уроке нужно дополнить программу из предыдущего. Переменная catalog должна быть не пустой, а заполнена значениями из файла.
# То есть, нужно прочитать файл, разбить содержимое на строки и записать полученные данные в словарь.
# Текст до двоеточия должен быть ключом, а после двоеточия — количеством. Не забудьте преобразовать количество в целое число.
catalog = {}
with open('catalog.txt', 'r') as f:  # вот эти четыре строки дополнил
    for line in f:
        n, c = line.split(':')
        catalog[n] = int(c)
        print(line)

for i in range(3):
    n = input('Наменование товара: ')
    c = int(input('Колличество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

with open('catalog.txt', 'w') as f:
    for i in catalog:
        f.write(i + ':' + str(catalog[i]) + '\n')
        print(f' файл {f} успешно создан.')


# 2 версия чтения с каталога
catalog = {}

for i in range(3):
    n = input('Наменование товара: ')
    c = int(input('Колличество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

nazvan = input('Название файла: ')
with open(nazvan, 'a+') as f:
    for n, s in catalog.items():
        f.write(f'{n}:{s}\n')
        f.seek(0)
        v = f.read()
        print(v)
        print(f' файл {f} успешно создан.')


# 3 версия чтения с каталога
catalog = {}

with open('catalog.txt', 'r') as f:
    for line in f:
        n, c = line.split(':')
        catalog[n] = int(c)
        print(line)

for i in range(3):
    n = input('Название товара: ')
    c = int(input('Количество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

with open('catalog.txt', 'w') as file:
    for n, c in catalog.items():
        file.write(f"{n}:{c}\n")




# Учебная работа с файлом___(надо дописать)
print('Выберете операцию: \n 1 - записать текст \n 2 - открытие файла \n 3 - создать файл')
a = input()
if a == '1':
    f = open('C:/Users/USER/Desktop/Новый текстовый документ.txt', 'a')
    f.write(input())
    f.close()
elif a == '2':
    f = open('C:/Users/USER/Desktop/Новый текстовый документ.txt', 'r')
    content = f.read()
    print(content)
elif a == '3':
    f = open('C:/Users/USER/Desktop/Новый текстовый документ.txt', 'w')

#___ниже наработка:

print('''Выберете операцию: 
1 - записать текст в файл 
2 - прочитать файла 
3 - создать файл''')
a = input()

if a == '1':
    z = input('В какой файл добавить информацию: ')
    q = input('Введите текст для в файл: ') + '\n' # это для переноса текста на другую строчку
    with open(z, 'a') as f:
        f.write(q)
    print('Текст успешно записан')

elif a == '2':
    r = input('Какой файл прочитать: ')
    try:
        with open(r, 'r') as f:
            open = f.read()
            print('Содержимое файла:\n', open)
            print(f' файл {r} успешно открыт.')
    except:
        (f'Такого файла нет {r}')

elif a == '3':
    e = input('Придумайте название файла: ')
    try:
        with open(e, 'w') as f:
            print(f' файл {e} успешно создан.')
    except:
        (f'Произошла ошибка при создании файла: {e}')

else:
    print('Некорректный выбор операции!')
#

# метод size и tell (можно это добавить в верхнюю программу)
q = input('Добавить информацию: ') + '\n'
with open('qwerty.txt', 'a+') as f:
    f.write(q)
    f.seek(0) #У метода объекта файла read есть необязательный параметр size. Это максимальное количество данных, которое требуется считать. Если этот параметр не указан или же он отрицательный, содержимое файла будет считано целиком.
    v = f.read()
    print(v)
    print(f.tell()) #Для того, чтобы узнать текущую позицию указателя, можно использовать метод объекта файла tell



# Формат csv____
# Чтобы начать использовать формат csv в своих программах, нужно импортировать модуль для работы с ним
import csv
# Для того, чтобы попробовать чтение в формате csv, нам понадобится тестовый файл.
# В файл все записывается так чтобы не было пробела после запятой

# Это для чтения
import csv

with open('test.csv') as f:
    rows = csv.reader(f) # Самая важная строчка в программе — это строчка с получением итератора
    for row in rows:
        print(row)
# После выполнения этой строки в переменную rows будет записан итератор, с помощью которого можно «пробежаться» циклом по файлу.
# Ну и например распаковка
import csv

with open('test.csv') as f:
    rows = csv.reader(f)
    for name, city, address in rows:
        print(name, city, address)


# Запись файлов в формате csv
import csv

with open('test.csv', 'w') as f:
    writer = csv.writer(f) # Сначала нужно получить объект для записи в файл
    row = ['Борис', 'Минск, Беларусь', 'ул. Ракеты "Булава" 2/10']
    writer.writerow(row) # и с его помощью записать информацию в файл

# Кроме метода writerow можно использовать и метод writerows, чтобы записать сразу несколько строк
import csv

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    rows = [
        ['Борис', 'Минск, Беларусь', 'ул. Ракеты "Булава" 2/10'],
        ['Виталий', 'Минск', 'сквер "Мотовело"'],
    ]
    writer.writerows(rows)


# Чтение с каталога с csv
import csv

catalog = {}

with open('catalog.csv', 'r') as f:
    for n, c in csv.reader(f):
        catalog[n] = int(c)

for i in range(3):
    n = input('Название товара: ')
    c = int(input('Количество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

with open('catalog.csv', 'w') as file:
    writer = csv.writer(file)
    for row in catalog.items():
        writer.writerow(row)



# Формат json___
# В отличие от csv, данные в этом формате не просто разделены запятыми,
# а имеют структуру ключ-значение. Это напоминает словарь Python,
# но в отличие от словаря, ключи в json могут быть только строками, заключенными в двойные кавычки.
{
  "key_1": "value",
  "key_2": "value 2"
}
# Значения в json могут быть не только строками. Это могут быть числа, списки значений, а также вложенные объекты
{
  "key_1": [1, 2, 3, "value"],
  "key_2": {
    "inner_key": "inner value",
    "inner_key_2": ["a", "b", "c"],
    "inner_key_n": [
      {
        "key_1": "value"
      }
    ]
  }
}

# каталог товаро в json
import json

catalog = {}

with open('catalog.json', 'r') as f:
    catalog = json.load(f)

for i in range(3):
    n = input('Название товара: ')
    c = int(input('Количество товара: '))
    if n in catalog:
        catalog[n] += c
    else:
        catalog[n] = c

with open('catalog.json', 'w') as file:
    file.write(json.dumps(catalog))





# Дата и время в Python________________________________________________________________________________________
import datetime
print(datetime.datetime.now())
# Программа с методом strftime, для более красивого вывода
import datetime
datetime_x = datetime.datetime.now()
datetime_str = datetime_x.strftime("%d.%m.%Y") # можно заменить размер букв и будет другой вывод д.м.г
print(datetime_str)
# в одну строку
print(datetime.datetime.now().strftime("%d/%m/%Y")) # можно заменить точки на слэш или еще на что-то

# у модуля есть многомсвоих модулей можно смотреть в справочнике
#Формат	Значение
#%a	Сокращенное название дня недели
#%A	Полное название дня недели
#%b	Сокращенное название месяца
#%B	Полное название месяца
#%c	Дата и время
#%d	День месяца 01,31
#%H	Час (24-часовой формат) 00,23
#%I	Час (12-часовой формат) 01,12
#%j	День года 001,366
#%m	Номер месяца 01,12
#%M	Число минут 00,59
#%p	До полудня или после (при 12-часовом формате)
#%S	Число секунд 00,61
#%U	Номер недели в году (нулевая неделя начинается с воскресенья) 00,53
#%w	Номер дня недели 0(Sunday), 6
#%W	Номер недели в году (нулевая неделя начинается с понедельника) 00,53
#%x	Дата
#%X	Время
#%y	Год без века 00,99
#%Y	Год с веком
#%Z	Временная зона
#%%	Знак '%'

import datetime
my_datetime = datetime.datetime.now()
my_datetime_2 = my_datetime.strftime("%d %b\n%H:%M")
print(my_datetime_2)
# или тоже самое
import datetime
my_datetime = datetime.datetime.now().strftime("%d %b\n%H:%M")
print(my_datetime)
# еще тоже самое
import datetime
print(datetime.datetime.now().strftime("%d %b\n%H:%M"))




# Часы с помощью tkinder
import datetime
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

text_object = canvas.create_text(100, 100, fill='blue', font=('Arial', 30))

while True:
    datetime_x = datetime.datetime.now()
    datetime_str = datetime_x.strftime('%X')
    canvas.itemconfig(text_object, text=datetime_str, fill='orange') # Первый аргумент этого метода — числовой идентификатор. Далее нужно указать изменяемое свойство. Разумеется, можно изменять несколько свойств за один вызов itemconfig
    canvas.update()



# Еще часы с random и time
import datetime
import tkinter
import random
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

text_object = canvas.create_text(100, 100, font=('Arial', 30))
colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple')

while True:
    datetime_x = datetime.datetime.now()
    datetime_str = datetime_x.strftime('%X')
    canvas.itemconfig(text_object, text=datetime_str, fill=random.choice(colors))
    time.sleep(1)
    canvas.update()

window.mainloop()



# Часы с помощью tkinder и random
import datetime
import tkinter
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

text_object = canvas.create_text(100, 100, text='Привет, мир!', fill='blue', font=('Arial', 30))

def update_clock():
    datetime_x = datetime.datetime.now()
    datetime_str = datetime_x.strftime('%X')
    color = '#{:02X}{:02X}{:02X}'.format(*random.sample(range(256), 3)) # Генерация случайного цвета
    canvas.itemconfig(text_object, text=datetime_str, fill=color)
    canvas.after(1000, update_clock) # Планирование следующего обновления через 1 секунду

update_clock() # Запуск функции обновления времени

window.mainloop()


# Чтобы пользователь ввел какую‑либо дату и время
import datetime

try:
    datetime_str = input('Введите дату/время в формате ДД/ММ/ГГГГ ЧЧ:ММ:CC')
    my_datetime = datetime.datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
    print(my_datetime)
except ValueError:
    print('Ошибка')

# Дата и время вместе
import datetime

now_ = datetime.datetime.now()
date_ = now_.date() # метод выводит дату
time_ = now_.time() # метод выводит время
print(date_)
print(time_)
now_2 = datetime.datetime.combine(date_, time_) # метод который обьединяет дату и время
print(now_2)

# Пример урока примитивная сиситема блокировки
import datetime
import time
try:
    m_t = input('time H:M\n')
    my_d = datetime.datetime.strptime(m_t,'%H:%M')
    my_d = my_d.time()
    print('Пользователь был заблокирован до: {}'.format(my_d))
    while True:
        now = datetime.datetime.now()
        now = now.time()
        if now > my_d:
            print('Пользователь разбанен')
            break

except:
    print("Ошибка формата, обратитесь к администратору!")
print(now)
print(my_d)



# Вычислить время между датами
import datetime

date1 = datetime.date(2024, 4, 22)
date2 = datetime.date(2024, 5, 25)

date_diff = date2 - date1
print(date_diff)



# Вычислить время между датами с часами
import datetime

# day_x - 1 января 2019 года, 23:00
day_x = datetime.datetime(2019, 1, 1, 23, 00, 00)
# day_y - 28 февраля 2019 года, 23:15
day_y = datetime.datetime(2019, 2, 28, 23, 15, 00)

delta = day_y - day_x
print(delta)
print(delta.days, delta.seconds, delta.total_seconds()) # получить дополнительную информацию



# Программа с помощью которой можно узнать какая дата и время будет в будущем
# Объект timedelta
import datetime

delta = datetime.timedelta(days=1, hours=1, minutes=15)
now = datetime.datetime.now()
future_now = now + delta
print(future_now)


# Задача с timedelta  сколько осталось до часа Х
import datetime

def choose_plural(quantity, forms):
    str_quantity = str(quantity)
    twobezmate = str_quantity[-2:]
    bezmate = str_quantity[-1]

    if bezmate == '1' and twobezmate != '11':
        return f"{quantity} {forms[0]}"
    elif bezmate in ('2', '3', '4') and twobezmate not in ('12', '13', '14'):
        return f"{quantity} {forms[1]}"
    else:
        return f"{quantity} {forms[2]}"

try:
    datetime_str = input('Введите дату и время часа X в формате ДД.ММ.ГГГГ ЧЧ:ММ ')
    date_x = datetime.datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
    date_now = datetime.datetime.now().replace(second=0, microsecond=0)

    if date_x > date_now:
        delta = date_x - date_now
        days, remainder = divmod(delta.total_seconds(), 86400)
        hours, minutes = divmod(remainder, 3600)
        minutes //= 60

        days = int(days)
        hours = int(hours)
        minutes = int(minutes)

        result = []
        if days > 0:
            result.append(choose_plural(days, ('день', 'дня', 'дней')))
        if hours > 0:
            result.append(choose_plural(hours, ('час', 'часа', 'часов')))
        if minutes > 0 or not result:
            result.append(choose_plural(minutes, ('минута', 'минуты', 'минут')))

        print('До часа "Икс" ' + ' и '.join(result))
    else:
        print('Ошибка')
except ValueError:
    print('Ошибка')







# Веб и работа с API_________________________________________________________________________________________________
# Модуль requests Для работы с HTTP запросами в Питоне есть отдельный модуль requests.
# можно посмотреть ка сделан сайт или сделать парсинг
import requests
result = requests.get('https://letpy.com/simple-html-example/')
print(result.text)

# Поиск случайного числа:
import requests
result = requests.get('https://letpy.com/simple-html-example/')
result_2 = result.text.split(' ')
s = "".join(result_2)
print(s[282:-30])


import requests
result = requests.get('https://letpy.com/simple-html-example/')
num_str = result.text[result.text.find('Случайное число'):].split('strong')[1]
print(num_str[1:-2])


import requests
result = requests.get('https://letpy.com/simple-html-example/')
result_2 = result.text.replace('</strong>', '<strong>')
result_stroka = result_2.split('<strong>')
print(result_stroka[-2])


import requests
result = requests.get('https://letpy.com/simple-html-example/')
a = ''
for i in result.text:
    if i.isdigit():
        a += str(i)
print(a[3:])


# Получение данных с помощью API

# Текст, который вы увидите, когда перейдете по ссылке, должен вам кое‑что напомнить.
# Это данные в формате json, о котором было рассказано в разделе про файлы.
# То есть, используя модуль json мы можем преобразовать данные, полученные по API в переменную Python!
import requests
import json

result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
print(data)


# В получившемся словаре слишком много ключей. Из‑за этого трудно понять, что за данные мы получили.
# Чтобы было проще прочитать то, что нам пришло от API, можно использовать модуль pprint из стандартной библиотеки Python.
import requests
import json
# импортируем
import pprint
# и настраиваем PrettyPrinter
pp = pprint.PrettyPrinter(indent=4)  # indent=4 -- значит отступ в 4 пробела
result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
pp.pprint(data)  # "красиво" выводим на экран данные

# Помимо свойства text у ответа есть и метод json который автоматически попытается преобразовать текст ответа.
# То есть, вполне можно сделать вот так
import requests
result = requests.get('https://open.er-api.com/v6/latest/USD')
# нет необходимости импортировать модуль json отдельно,
# все нужное есть в модуле requests
data = result.json()
print(data["rates"]['RUB'])


# пример предсказание возраста по имени
import requests

name = input('Enter your name: ')
result = requests.get('https://api.agify.io?name='+name)
data = result.json()
age = data['age']
print(f'Your age: {age}')






# Начинаем писать Telegram-бота______________________________________________________________________________________
# Документация https://tlgrm.ru/docs/bots/api#authorizing-your-bot
# Для этого надо написать сообщение самому главному боту Telegram — @BotFather.
# В поиске по чатам и людям так и надо написать @BotFather.
# В открывшемся диалоге с этим супер-ботом, нужно следовать его инструкциям, чтобы создать нового бота.
import requests
result = requests.get('https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates')
data = result.json()
print(data)


# тоже самое но с JSON
import requests
import json
result = requests.get('https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates')
data = json.loads(result.text)
print(json.dumps(data, indent=2))


# Получаем сообщения
# Напишите боту что‑нибудь еще и запустите программу еще раз.
# В список, находящийся по ключу 'result' добавился еще один словарь.
# Как вы уже поняли, этот список и есть сообщения, присланные боту.
# Можно вывести только сообщения от бота
import requests
result = requests.get('https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates')
data = result.json()
for update in data['result']:
    print(update['message']['text'])
# Значение ключа 'result' — список. Каждый элемент этого списка — словарь.
# То есть в цикле каждую итерацию мы получаем очередной словарь.
# Каждый такой словарь имеет свои ключи. И по ключу 'message' находится еще один словарь,
# в котором мы наконец‑то можем найти текст сообщения.
# Получается, у нас есть этакий супер-словарь.
# примерная аналогия, что было выше сделано:
# update — это словарь. И ключ "message" в этом словаре — тоже словарь.
# То есть мы получаем словарь по ключу и потом получаем значение ключа этого словаря;
# если брать аналогию из списков
# a = [1, 2, [3, 4]]
# print(a[2][0])



# Получаем сообщения в цикле(сообщения будут появляться в реальном режиме при его запущенном состоянии)
# Напишите несколько сообщений своему боту. Все сообщения, который вы напишите, программа будет получать каждую итерацию цикла.
# Это не очень‑то хорошо, мы ведь не хотим получать одни и те же сообщения по несколько раз.
# Для того чтобы решить эту проблему, в Telegram Bot API предусмотрен дополнительный параметр
# для указания последнего обработанного сообщения и называется он offset.
# Параметры можно передать с помощью необязательного аргумента функции get. Этот параметр называется params,
# а ниже приведен код, который уже не будет выводить сообщения повторно
import requests

last_update_id = 0
while True:
    result = requests.get(
        'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        print(update['message']['text'])
        last_update_id = update['update_id']
# Параметр offset и ключ обновления 'update_id' мы взяли из документации.
# Еще раз повторюсь — документация в работе с различными API — крайне важная штука и читать ее необходимо.



# Отвечаем в чат
# Для того, чтобы послать сообщение в чат, нужно узнать идентификатор чата.
# По ключу 'message' в каждом обновлении находится словарь. В нем есть ключ 'chat'.
# Его значение — тоже словарь, в котором есть ключ 'id'. Это и есть нужный нам идентификатор чата.
# В сообщении можно использовать и имя человека, который написал боту. Для этого изучите документацию.
# Там описано, что и в каком ключе хранится.
import requests

last_update_id = 0
while True:
    result = requests.get(
        'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        send_result = requests.get(
            'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage',
            params={'chat_id': chat_id, 'text': 'Привет от LETPY'})





# Укороченная версия верхнего кода
import requests

get_ = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates'
send_ = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage'

last_update_id = 0
while True:
    result = requests.get(get_, params={'offset': last_update_id + 1})
    data = result.json()

    for update in data['result']:
        print(update)
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        send_result = requests.get(send_, params={'chat_id': chat_id, 'text': 'Привет от LETPY'})




# Бот который здоровается в зависимости от времени суток
import requests
import datetime

last_update_id = 0
while True:
    result = requests.get(
        'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()

    for update in data['result']:
        res = update['message']['text']

        name = update['message']['chat']['first_name']
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        b = datetime.datetime.now()
        h = b.strftime("%H")
        m = b.strftime("%M")
        time = h + '.' + m
        x = float(time)
        time_day = ''
        if x > 0 and x < 6:
            time_day = 'Доброй ночи'
        elif x > 6 and x < 12:
            time_day = 'Доброе утро'
        elif x > 12 and x < 18:
            time_day = 'Доброго дня'
        else:
            time_day = 'Добрый вечер'
        send_result = requests.get(
            'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage',
            params={'chat_id': chat_id, 'text': '{} {}'.format(name, time_day)}


# Тоже бот
import requests

last_update_id = 0

greetings = {
    'как тебя зовут?': 'Меня зовут [Имя Вашего бота]',
    'сколько тебе лет?': 'Я только родился)',
    'что ты умеешь?': 'Пока только здороваться)))',
    'привет': 'Приветик))',
    'кто твой друг?': 'У меня есть классная подружка, её зовут [Любое ИМЯ])',
    'ты крутой': 'Спасибо'
}

while True:
    result = requests.get(
        'https://api.telegram.org/bot[ваш_токен]/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        print(update['message']['text'])
        x = update['message']['text']
        x = x.lower()
        # print(x)
        if x in greetings:
            send_result = requests.get(
                'https://api.telegram.org/bot[ваш_токен]/sendMessage',
                params={'chat_id': chat_id, 'text': greetings.get(x)}
            )
        else:
            send_result = requests.get(
                'https://api.telegram.org/bot[ваш_токен]/sendMessage',
                params={'chat_id': chat_id, 'text': 'Я ещё не такой умный, что бы тебе ответить =)'})


# Попытка создать бота рандом
import requests
import random

get_1 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates'
send_2 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage'

last_update_id = 0
while True:
    result = requests.get(get_1, params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:

        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']


        num = random.randint(1, 10)
        guess = int(input('Введите число от 1 до 10: '))
        if guess == num:
            text = 'Угадали!'
        elif guess != num:
            text = 'Не угадали'

        send_result = requests.get(send_2, params={'chat_id': chat_id, 'text': num})


# Готовый код рандом, но нужно его исправить, добавить проверки и команды по другому возможно обрабатывать
import requests
import random

get_1 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates'
send_2 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage'

last_update_id = 0
numbers = {}

while True:
    result = requests.get(get_1, params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:

        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        text = update['message']['text']
        if text == 'start':
            numbers[chat_id] = random.randint(1, 10)
            send_result = requests.get(send_2, params={'chat_id': chat_id, 'text': "Введите число от 1 до 10: "})
        else:
            # если это не команда, то это число
            guess = int(text)
            num = numbers.get(chat_id, 0)
            if guess == num:
                requests.get(send_2, params={'chat_id': chat_id, 'text': 'Угадали'})
            elif guess != num:
                requests.get(send_2, params={'chat_id': chat_id, 'text': 'Не угадали'})


# Бот который добавляет ссылку на сайт
import requests
import random

get_1 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/getUpdates'
send_2 = 'https://api.telegram.org/bot6517489273:AAFEO4sKNRKGdoVSSOiZn9bSspoCLF_o7io/sendMessage'

last_update_id = 0
numbers = {}

while True:
    result = requests.get(get_1, params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:

        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        text = update['message']['text']
        if text == 'start':
            numbers[chat_id] = random.randint(1, 10)
            send_result = requests.get(send_2, params={'chat_id': chat_id, 'text': "Введите число от 1 до 10: "})
        else:
            # если это не команда, то это число
            guess = int(text)
            num = numbers.get(chat_id, 0)
            if guess == num:
                requests.get(send_2, params={'chat_id': chat_id, 'text': 'Угадали',
                                             'reply_markup': '{"inline_keyboard": [[{"text": "Play again", "url": "https://letpy.com/"}]]}'})
            elif guess != num:
                requests.get(send_2, params={'chat_id': chat_id, 'text': 'Не угадали',
                                             'reply_markup': '{"inline_keyboard": [[{"text": "Play again", "url": "https://letpy.com/"}]]}'})







# Функция как переменная_______________________________________________________________________________________________
# Функции в Python — это такие же объекты, как и все остальные данные.
# От остальных типов данных функции отличает только то, что их можно выполнить, а строку, например, выполнить нельзя.
my_float = float
print(my_float("10"))
# Обратите внимание, что на первой строке программы мы не вызываем функцию float, то есть пишем именно float, а не float().
# Поэтому переменная будет ссылаться на саму функцию, а не на возвращаемый функцией результат.

# а еще такие штуки часто используются в GUI когда ты присваиваешь кнопке функцию,
# если написать ИмяФункции() то при прорисовке GUI функция будет запущена сразу, а мы то хотим по событию

# Функцию, как и любой объект в Python, можно не только присвоить переменной,
# но и передать в качестве аргумента в другую функцию. Рассмотрим пример ниже:
def convert(function, value):
    return function(value)

print(convert(int, "10"))
print(convert(float, "10"))


# В этой программе мы передаем функции convert две разные функции для конвертами
# строкового значения и получаем два разных результата: целое число и число с плавающей запятой.
def my(v):
    return int(v) * 2

def convert(function, value):
    return function(value)

print(convert(int, "10"))
print(convert(float, "10"))
print(convert(my, "10"))
# Функция, которая принимает в качестве аргументов другие функции или возвращает другую функцию в качестве результата,
# называют функцией высшего порядка.
# В нашем случае такой функцией будет функция convert

# еще пример
def plus(x, y):
    return x + y
def minus(x, y):
    return x - y

def chooce_operation(operation):
    if operation == "+":
        return plus
    if operation == "-":
        return minus

def culc(operation, x, y):
    return chooce_operation(operation)(x, y)

print(culc('+', 2, 2))
print(culc('-', 2, 2))


# Метод sort и аргумент key, разбивает строку по длине с маленького по большое
# Так вот, этот метод может принимать функцию в качестве необязательного аргумента key.
# С помощью это функции мы можем управлять самим процессом сортировки.
# Во время работы встроенного алгоритма сортировки при сравнении элемента с другими элемента,
# к каждому из них будет применена функция, переданная в key. В нашем случае — это функция int.
# То есть вместо исходного строкового значения, для сортировки будет браться значение, полученное с помощью int.
# Также обратите внимание, что сам список остался списком строк.
# То есть мы не преобразовывали элементы в числа, а просто использовали функцию int в алгоритме сортировки.
a = input().split()
a.sort(key=len)
print(str(a))

a = input().split()
a.sort(key=len)
print(' '.join(a))

a = ['1', '25', '2', '101']
a.sort(key=int)
print(a)


# Собственная функция сортировки
# Разумеется, в качестве аргумента key можно передать не только встроенную функцию, но и свою собственную.
# ниже этот код с лямбдой lambda
a = input().split()


def last_letter(word):
    return word.lower()

a.sort(key=last_letter)
print(' '.join(a))



# А эта программа сортирует по последней букве
a = ['abc', 'xyz', 'zxa']

def last_letter(word):
    return word[-1]

a.sort(key=last_letter)
print(a)


# Лямбда-функции
# Если функция проста и состоит из одного выражения, то вместо обычной функции можно использовать лямбда-функцию.
# Лямбда-функция в Python — это однострочная функция без имени, которая может быть использована точно также как обычная функция.
# Чтобы создать такую функцию,
# нужно использовать ключевое слово lambda.
a = ['abc', 'xyz', 'zxa']

a.sort(key=lambda word: word[-1])
print(a)


# Если такую функцию присвоить переменной, то использовать ее можно точно также, как и обычную:
square = lambda x: x * x
print(square(5))

# передачи аргументов
square = lambda x, y: x * y
print(square(5, 6))

# необязательные аргументы
square = lambda x, y=10: x * y
print(square(5))

# измененнная программа с сортировкой из нескольких примеров выше
a = input().split()
a.sort(key=lambda a: a.lower())
print(' '.join(a))



# Обработка событий
# Событие – это сигнал о том, что что‑то произошло. Это может быть сигнал о том,
# что пользователь нажал какую‑то кнопку на клавиатуре или, например, кликнул мышкой.
# Событий таких может быть множество и все зависит от среды, где вы их будете использовать.
# Проще всего работу с событиями будет показать на примере уже знакомого нам Canvas из модуля tkinter
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

def onclick(event):
    print(f'Клик на холсте в точке x={event.x}, y={event.y}')

canvas.bind('<Button-1>', onclick)
window.mainloop()


# Простое рисование точки в центре, чтобы знать как рисовать с цента круга
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

def my_click(event):
    r = 1
    x, y = event.x, event.y
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
    print(f'Круг на холсте в точке x={event.x}, y={event.y}')
canvas.bind('<Button-1>', my_click)
window.mainloop()



# Хороший пример
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

def onclick_left(event):
    x, y = event.x, event.y

    print(f'ЛКМ x={event.x}, y={event.y}')
    canvas.create_rectangle(x, y, x+30, y+30, fill="red")

def onclick_right(event):
    x, y = event.x, event.y

    print(f'ПКМ x={event.x}, y={event.y}')
    canvas.create_rectangle(x, y, x+30, y+30, fill="blue")

canvas.bind("<Button-1>", onclick_left)
canvas.bind("<Button-3>", onclick_right)
window.mainloop()


# второй пример
import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()


def onclick(event):

    x, y = event.x, event.y

    if event.num == 1:
        print(f'ЛКМ x={event.x}, y={event.y}')
        canvas.create_rectangle(x, y, x+30, y+30, fill="red")

    elif event.num == 3:
        print(f'ПКМ x={event.x}, y={event.y}')
        canvas.create_rectangle(x, y, x+30, y+30, fill="blue")


canvas.bind("<Button-1>", onclick)
canvas.bind("<Button-3>", onclick)
window.mainloop()




# Объектно-ориентированное программирование __________________________________________________________________________
# Создать класс можно с помощью ключевого слова class
class ExampleClass:
    pass

# Создание объекта класса
# Теперь в переменной example у нас хранится объект(или экземпляр) класса ExampleClass
class ExampleClass:
    pass

example = ExampleClass()

# еще способ создания объекта класса
class MyFirstClass:
    def prints_greet(self):
        print(f"Привет, мир!")

first_object = MyFirstClass()
first_object.prints_greet()

# Если скобок не поставить, то присвоется именно класс. А если скобки поставить — объект класса.
class ExampleClass:
    pass

example = ExampleClass()
test = ExampleClass

print(example, test)


# Собственный пример в виде калькулятора_
class ExampleClass:
    def plus(self):
        a = int(input())
        b = int(input())
        return a + b

    def minus(self):
        a = int(input())
        b = int(input())
        return a - b


example = ExampleClass()


def cal():
    flag = input('Выберите операцию: + или -: ')
    if flag == '+':
        print(example.plus())
    elif flag == '-':
        print(example.minus())
    else:
        print('Не то ввел!')

cal()
while True:
    flag_2 = input('Еще раз: да / нет: ')
    if flag_2 == 'да':
        cal()
    else:
        break


# Поля объекта__
class Cat:
    pass

fil = Cat()
fil.name = 'Филимон'
print(fil.name)

# Упоротый пример полей обьекта
class Cal:
    pass


fil = Cal()
a = int(input())
b = int(input())
fil.plus = a + b
fil.minus = a - b


def cal():
    flag = input('Выберите операцию: + или -: ')
    if flag == '+':
        print(fil.plus)
    elif flag == '-':
        print(fil.minus)
    else:
        print('Не то ввел!')


cal()
while True:
    flag_2 = input('Еще раз: да / нет: ')
    if flag_2 == 'да':
        cal()
    else:
        break


# Методы объекта и self_
# Метод объекта — это функция, которая принадлежит объекту. По аналогии с полями получить доступ, то есть вызвать,
# такую функцию можно только через объект.
# Пишутся методы внутри тела класса. У каждого метода должен быть как минимум один аргумент и
# называть этот аргумент принято словом self
# Хороший пример был калькулятор, чтобы вызывать функцию нужен метод объекта, чаще всего испрользуют
# self, но будет работать и любое другое

class Cat:
    def ask_for_food(self):
        print('Хозяин, кот {} требует пищу'.format(self.name))

fil = Cat()
fil.name = 'Филимон'
fil.ask_for_food()

var = Cat()
var.name = 'Варежка'
var.ask_for_food()



# Еще пример
import datetime

day_x = datetime.datetime.now()
data_x = day_x.strftime('%d/%m/%Y')
time_x = day_x.strftime('%H:%M:%S')

class Data:
    def data_day(self):
        print(f'Текущая дата {self.d_day}')

    def time_day(self):
        print(f'Текущее время {self.d_time}')

fil = Data()
fil.d_day = data_x
fil.data_day()

var = Data()
var.d_time = time_x
var.time_day()



# Метод __init__
# В общем, если вы хотите присвоить какие‑либо значения полям объекта во время создания,
# нужно использовать специальный метод инициализации __init__. Как и для обычных методов объекта,
# первым параметром __init__ будет self. После него можно указать все аргументы, которые необходимы для создания объекта
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print(f'Хозяин, коту {self.name} лет {self.age} он {self.color}')

fil = Cat('Филимон', 8, 'разноцветный')

vil = Cat('Timofei', 22, 'черный')

fil = Cat(input('Имя кота: '), input('Возраст кота: '), input('Цвет кота: '))



# Еще пример
class Cat:
    def __init__(self,name,sposobnost,age,korm):
        self.name = name
        self.sposobnost = sposobnost
        self.age = age
        self.korm = korm

    def zapros(self):
        print(f'хозяин, кот {self.name},в свои {self.age} лет , требует {self.sposobnost}')

    def eda(self):
        print(f'хозяин, кот {self.name} требует {self.korm}' )

moty = Cat('Пуки',"урчать",5,"корм с телятинкой")

moty.zapros()
moty.eda()




# Инкапсуляция___
# Можно ли обойтись без классов и объектов? Разумеется.
# Можно использовать словарь для хранения данных, метод ask_for_food заменить на функцию и передавать в нее весь словарь целиком
den = {
    "name": 'Дэн',
    "is_fluffy": False,
    "fails": []
}

fil = {
    "name": 'Филимон',
    "is_fluffy": False,
    "fails": []
}


def cat_asks_for_food(cat):
    print('Хозяин, кот {} требует пищу'.format(cat['name']))


def dog_asks_for_food(dog):
    print('Хозяин, пёс {} требует косточку'.format(dog['name']))


cat_asks_for_food(den)
dog_asks_for_food(fil)


# В общем, чем больше питомцев, тем больше бардак. Можно, конечно, добавить дополнительный ключ 'type' и оставить одну функцию
def ask_for_food(pet):
    if pet['type'] == 'cat':
        print('Хозяин, кот {} требует пищу'.format(pet['name']))
    elif pet['type'] == 'dog':
        print('Хозяин, пёс {} требует косточку'.format(pet['name']))
    # и так далее для все питомцев



# и вот в чем прелесть инкапсуляции, все это делал выше
class Cat:
    def __init__(self, name):
        self.name = name

    def ask_for_food(self):
        print(f'Ваш кот {self.name} ')


class Dog:
    def __init__(self, name):
        self.name = name

    def ask_for_food(self):
        print(f'Ваш пес {self.name} ')


class Raccoon:
    def __init__(self, name):
        self.name = name

    def ask_for_food(self):
        print(f'Ваш енот {self.name} ')


kot = Cat('Тима')
psina = Dog('Ричард')
enot = Raccoon('Енот-Енотыч')

kot.ask_for_food()
psina.ask_for_food()
enot.ask_for_food()


# Наследование___
# Наследование — это создание нового класса на основе уже существующего.
# При этом вновь созданный класс будет использовать код, написанный в существующем классе.
# В терминах объектно-ориентированного программирования класс Pet будет супер-классом для классов Cat, Dog и Raccoon.
# Также его вполне можно назвать базовым или родительским. Классы Cat, Dog и Raccoon будут подклассами или потомками.
class Pet:
    def __init__(self, name):
        self.name = name

class Cat(Pet):
    def ask_for_food(self):
        print(f'Кот {self.name} требует пищу')


class Dog(Pet):
    def ask_for_food(self):
        print(f'Пёс {self.name} хочет есть')


class Raccoon(Pet):
    def ask_for_food(self):
        print(f'Енот {self.name} уже начинает воровать')

kot = Cat('Тима')
psina = Dog('Ричард')
enot = Raccoon('Енот-Енотыч')

kot.ask_for_food()
psina.ask_for_food()
enot.ask_for_food()



# Еще пример наследования
class Card:
    def __init__(self, number, holder, valid_date, ccv):
        self.number = number
        self.holder = holder
        self.valid_date = valid_date
        self.ccv = ccv

    def get_hidden_number(self):
        zvezda = '** **** ****'
        return f'{self.number[0:2]} {zvezda} {self.number[12:]}'

class MasterCard(Card):
    def __str__(self):
        return f'[mastercard {self.get_hidden_number()}]'

class Visa(Card):
    def __str__(self):
        return f'[visa {self.get_hidden_number()}]'


mastercard = MasterCard('4200000000000001', 'Letpy', '2024', '777')
visa = Visa('4200000000000001', 'Letpy', '2024', '777')
print(mastercard)
print(visa)





# Метод __str__
# Класс Pet является базовым для всех животных
class Pet:
    # Метод __init__ инициализирует имя объекта
    def __init__(self, name):
        self.name = name
    # Метод __str__ возвращает строковое представление объекта
    def __str__(self):
        return f'{self.name} - это {self.typ} и он {self.lang}'

# Класс Cat наследуется от Pet
class Cat(Pet):
    typ = 'кот' # Тип животного
    lang = 'мяукает' # Язык животного

# Класс Dog наследуется от Pet
class Dog(Pet):
    typ = 'пёс' # Тип животного
    lang = 'гавкает' # Язык животного

# Класс Raccoon наследуется от Pet
class Raccoon(Pet):
    typ = 'енот' # Тип животного
    lang = 'полощет' # Язык животного

# Функция ask_for_food выводит на экран сообщение о просьбе животного поесть
def ask_for_food(pet):
    print(f'Хозяин, {pet.typ} {pet.name} {pet.lang} за едой')

# Создаем экземпляры животных
sol = Cat('Соломон')
san = Dog('Сандаль')
coon = Raccoon('Полоскун')

# Вызываем функцию ask_for_food для каждого животного
ask_for_food(sol)
ask_for_food(san)
ask_for_food(coon)

# Выводим на экран строковое представление о животном
print(sol)
print(san)
print(coon)




# Cвой пример из разных уроков по классам
class Pet:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def __str__(self):
        return f'{self.name} - это {self.typ} и он {self.lang}'


class Cat(Pet):
    typ = 'котик'
    lang = 'обжора'

    def bodobilding(self):
        print(f'Кот {self.name}, ему {self.age} и он {self.sport}')


class Vlad(Pet):
    typ = 'хозяин'
    lang = 'гладит кота'
    tim = 'Тимошка'

    def gladit(self):
        print(f'Вы {self.name} и ваш кот {self.tim} ')


tima = Cat('Тима', 22, 'бодибилдер')
vlad = Vlad('Влад', 32, False)

tima.bodobilding()
vlad.gladit()

print(tima)
print(vlad)



# Передача по ссылке___
# При присваивании переменным, объекты передаются по ссылке.
# Точно так же, как, например, списки и словари.
# Если взять класс одного из прошлых уроков и попробовать написать вот такую программу
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Кот {}'.format(self.name)


fil = Cat('Филимон')
cat = fil
cat.name = 'Мурлыч'

print(fil)



# Две важные функции___
# Две важные функции в объектно-ориентированном программировании — это isinstance и issubclass.
# Первая из них, isinstance проверяет, является ли объект экземпляром указанного класса (одного из классов) или его подкласса
# Вторая, issubclass, проверяет, является ли класс потомком класса или одного из классов
# Вторым аргументом этой функции также может быть кортеж из классов.
class Pet:
    def __init__(self, name):
        self.name = name


class Cat(Pet):
    pass


class Dog(Pet):
    pass


fil = Cat('Филимон')
dan = Dog('Дэн')

print(isinstance(fil, Cat))
print(isinstance(dan, Cat))

# Dog это подкласс Pet
# поэтому isinstance вернет True
print(isinstance(dan, Pet))

# Вторым параметром функции может быть
# и кортеж классов
print(isinstance(fil, (Dog, Cat)))

print(issubclass(Cat, Dog))
print(issubclass(Cat, Pet))



# Функция super___
# Представьте, цена подписки на месяц уменьшится в два раза, а цифру в подписке со скидкой никто не поменяет.
# В итоге получится две одинаковые цены и никаких реальных скидок. Вряд ли кого‑то это обрадует.
# В общем, хотелось бы получить цену от родительского класса и вычислять скидку от нее, чтобы описанного выше казуса не произошло.
# Для этого можно использовать функцию super
# Даже не то что поменять, а вызвать метод родительсткого (супер) класса.
# Ну и с помощью этого действительно можно изменить либо дополнить функционал.
class TariffOneMonth:
    # На самом деле, тут у нас еще много всякого кода
    # для отображения в списках, работы
    # с платежными системами, валютой и так далее

    def get_price(self):
        return 10


class TariffOneMonthDiscounted(TariffOneMonth):

    # Цена с 50% скидкой
    def get_price(self):
        price = super().get_price()
        return int(price / 2)  # Менять число тут


q = TariffOneMonth()
w = TariffOneMonthDiscounted()
print(q)
print(w)
print(q.get_price())
print(w.get_price())




# Крестики-нолики_______________________________________________________________________________________________
import tkinter
import random


class TicTacToe(tkinter.Canvas):  # Крестики-нолики
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [
                         None, ] * 9  # Ходим первыми(хранить состояние игры, значение None будет обозначать то, что ячейка свободна)
        self.bind('<Button-1>', self.click)

    def get_winner(self):  # Кто победил?
        lines = [
            self.state[0:3], self.state[3:6], self.state[6:9],  # по горизонтали
            self.state[0:9:3], self.state[1:9:3], self.state[2:9:3],  # по вертикали
            self.state[0:9:4], self.state[2:7:2]  # по диагонали
        ]

        if ['x'] * 3 in lines:
            return 'x_win'
        elif ['o'] * 3 in lines:
            return 'o_win'
        elif None not in self.state:
            return 'draw'

    def bot_move(self):  # Глупый бот(создание бота, который будет играть против нас)
        index = random.choice([index for index, e in enumerate(self.state) if e is None])
        self.state[index] = 'o'
        self.add_o(column=index % 3, row=int(index / 3))

    def click(self, event):  # Ходим первыми(метод-обработчик клика по холсту)
        column = event.x // 100
        row = event.y // 100
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(column, row)
            pobeda = self.get_winner()
            if pobeda:
                self.pobedaPobeda(pobeda)
                self.deleteDelete()
            else:
                self.bot_move()  # обработчик клика
                pobeda = self.get_winner()
                if pobeda:
                    self.pobedaPobeda(pobeda)
                    self.deleteDelete()

    def pobedaPobeda(self, pobeda):  # Собираем все вместе(тут должна быть информация о победителе)
        self.create_text(150, 150, text=f"{pobeda} победил!", font=("Arial", 24), fill="green")
        self.deleteDelete()

    def deleteDelete(self):  # Собираем все вместе(очистить холст)
        self.delete("all")
        self.state = [None] * 9
        self.draw_lines()

    def add_x(self, column, row):  # Рисуем(кресты)
        self.create_line(column * 100 + 20, row * 100 + 20, column * 100 + 80, row * 100 + 80, fill="red", width=3)
        self.create_line(column * 100 + 80, row * 100 + 20, column * 100 + 20, row * 100 + 80, fill="red", width=3)

    def add_o(self, column, row):  # Рисуем(круг)
        self.create_oval(column * 100 + 20, row * 100 + 20, column * 100 + 80, row * 100 + 80, width=5, outline='blue')

    def draw_lines(self):  # Рисуем линии
        self.create_line(100, 0, 100, 300, fill="black", width=2)
        self.create_line(200, 0, 200, 300, fill="black", width=2)
        self.create_line(0, 100, 300, 100, fill="black", width=2)
        self.create_line(0, 200, 300, 200, fill="black", width=2)


okno = tkinter.Tk()
game = TicTacToe(okno)
game.pack()

# game.add_o(0, 2)  # рисует круг
# game.add_x(column=0, row=0)  # рисует крест

game.draw_lines()  # создает линии

okno.mainloop()



























#______________________________Практика python, модуль os, функция walk____________________________________
import os
('D:\\OneDrive\\Рабочий стол\\для примера', ['папка 1', 'папка 2'], ['файл 1.txt', 'файл 2.txt', 'файл 3.bmp'])
# Выше кортеж из трех элиментов, ниже распакуем его на три переменных
# также создадим список
# Также если первоначально указать весь путь к диску,то добавятся все пути к каждой папке
spisok = []
for adress, dirs, files in os.walk('D:\\OneDrive\Рабочий стол\для примера'):
    spisok.append(adress)
print(spisok)


import os
('D:\\OneDrive\\Рабочий стол\\для примера', ['папка 1', 'папка 2'], ['файл 1.txt', 'файл 2.txt', 'файл 3.bmp'])
# Выше кортеж из трех элиментов, ниже распакуем его на три переменных
# также создадим список
# Также если первоначально указать весь путь к диску, то добавятся все пути к каждой папке
# Adress один, files много c помощью цикла for будем перебирать файлы
# Функция os.path.join определяеет пути с особенностями операционной системы, автоматически
# проставляет все слэши.
spisok = []
for adress, dirs, files in os.walk('D:\\OneDrive\Рабочий стол\для примера'):
    for file in files: # Тут юудем перебирать значения в files
        spisok.append(os.path.join(adress, file)) # Тут будем соединяем значения с переменной adress
print(spisok) # Получился список с адресами к файлам, к всем файлам которые есть в папке для примера!


import os
('D:\\OneDrive\\Рабочий стол\\для примера', ['папка 1', 'папка 2'], ['файл 1.txt', 'файл 2.txt', 'файл 3.bmp'])
# Выше кортеж из трех элиментов, ниже распакуем его на три переменных
# также создадим список
# Также если первоначально указать весь путь к диску, то добавятся все пути к каждой папке
# Adress один, files много c помощью цикла for будем перебирать файлы
# Функция os.path.join определяеет пути с особенностями операционной системы, автоматически
# проставляет все слэши.
spisok = []
for adress, dirs, files in os.walk('D:\\OneDrive\Рабочий стол\для примера'):
    for file in files: # Тут юудем перебирать значения в files
        full = os.path.join(adress, file)  # Тут будем объединять адреса в переменную
        if '.txt' in full: # Тут добавим условия, запишем только файлы txt, bmp будет отсутствовать!
            spisok.append (full)
print(spisok) # Отфильровали все файлы txt, можно указать папка или любое название чтобы выдало в поиске


# Теперь будем добавлять в наш список файлы созданные в течении суток!!!
import os
import time # Cоздаем модуль time
('D:\\OneDrive\\Рабочий стол\\для примера', ['папка 1', 'папка 2'], ['файл 1.txt', 'файл 2.txt', 'файл 3.bmp'])
# os.path.getctime() path это вложенный модуль в модуль os  и в модуле path  функция getctime(),
# которая возвращает дату(время) создания файла с момента начала эпохи.
spisok = []
for adress, dirs, files in os.walk('D:\\OneDrive\Рабочий стол\для примера'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:  # Из модуля time функция time выдаст текущее время с момента начало эпохи, а потом
            spisok.append (full)   # отнимем время создания файла с начала эпохи. Если разница будем меньше чем 86400 секунд,  только в таком случаи
print(spisok)                      # мы будем добавлять в на список путь к этому файлу(full), также тут при помощи оператора and можно сделать дополнительную проверку
# Вывод таким образом можно просканировть весь диск!           # например найти скрытые файлы.



