import random
num = random.randint(1,10)
guess = int(input('Введите число от 1 до 10: '))
if guess == num :
    print('Угадали!')
elif guess != num :
    print ('Не угадали')


# Миниальное число вывести
a = int(input())
b = int(input())
c = int(input())
min (a,b,c)
z = min(a,b,c)
print(min(a,b,c))

# Функция делает число положительным
m = abs(-10)
print(m)

# Попытка сделать игру
a = str(input('Сколько сторон у четырехугольника?\nВыберите один из четырех вариантов!\n 1, 2, 3, 4: \n'))
q = 1
w = 2
e = 3
r = 4

while a:
    if a == q:
        print('Дебил!')

    if a == w:
        print('Точно дебил!')

    if a == e:
        print('Трижды дебил!')

    if a == r:
        print('Правильно!')
    else:
        print('Не туда жмешь!')

# КАЛЬКУЛЯТОР
def cal():
    calculator = ("************ Калькулятор VAI ************")
    print(calculator)
    a = int(input("Ввелите первое число 1: "))
    b = int(input("Введите второе число 2: "))
    c = int(input("Какую операцию выполнить?\n 1 Сложение \n 2 Вычитание \n 3 Умножение \n 4 Возведение в степень \n 5 Остаток от деления \n 6 Деление \n 7 Деление без остатка \n Выберите операцию: " ))
    if c == 1:
        r = a + b
        z = 'сложения'
        w = z
    if c == 2:
        r = a - b
        x = 'вычитания'
        w = x
    if c == 3:
        r = a * b
        v = 'умножения'
        w = v
    if c == 4:
        r = float(a ** b)
        n = 'возведения в степень'
        w = n
    if c == 5:
        r = float(a % b)
        m = 'остаток от деления'
        w = m
    if c == 6:
        r = float(a / b)
        l = 'деления'
        w = l
    if c == 7:
        r = float(a//b)
        k = 'деления без остатка'
        w = k
    print("Результат ",w," =", r)
cal()
while True:
    flag = input('Еще раз? [да/нет]: ')
    if flag == 'да':
        cal()
    else:
        break


# __________
def cal():
    convertor = ("************ Конвертор VAI из мегабайт в гигабайты и обратно ************")
    print(convertor)
    print ('Выберите задачу!' '\n'
           '1 - конвертация из мегабайт в гигабайты' '\n'
           '2 - конвертация из гигабайт в мегабайты')
    a = int(input("Введите задачу: "))
    if a == 1:
        m = float(input('Введите количество мегабайт: '))
        g = m / 1024
        print(g)
    if a == 2:
        g = float(input('Введите количество гигабайт: '))
        m = g * 1024
        print(m)
cal()
while True:
    flag = input('Еще раз? [да/нет]: ')
    if flag == 'да':
        cal()
    else:
        break
#______________________
while True:
    a = input("Введите арифметическое выражение: ")
    a = a.replace(" ", "")
    if "+" in a:
        b = a.find("+")
        result = int(a[:b]) + int(a[b+1:])
    elif "-" in a:
        b = a.find("-")
        result = int(a[:b]) - int(a[b+1:])
    elif "*" in a:
        b = a.find("*")
        result = int(a[:b]) * int(a[b+1:])
    elif "/" in a:
        b = a.find("/")
        result = int(a[:b]) / int(a[b+1:])
    else:
        result = "Ошибка"
    print(f"{a} = {result}")


# Код создания простейшего калькулятора___
def cal():
    while True:
        print(eval(input()))


cal()



# Еще один калькулятор с  помощью классов___
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




#_______________________________

#Пароль с функцией len
a = input('Придумайте пароль: ')
b = input('Введите пароль: ')
c = input('Повторите пароль: ')
if not a:
    print('Вам нужно придумать пароль!')
if len(a) < 5:
    print('Пароль должен быть пять символов или больше!')
    a = len(a)
    print(f'Ваш пароль состоит из {a} букв или цифр!')
    exit()
if a == b and c == a:
    print('Пароль верный')
    p = input(a)
    i = 0
    print(p[i], p[i + 1], p[i + 2], p[i + 3], p[i + 4])
    a = len(a)
    print('Ваш пароль состоит из ' + str(a) + ' букв или цифр, все правильно!')
else:
    print('Доступ запрещен, пароль не верный!')

# Тоже len скрываем цифры
a = input()
if len(a) >= 8 and a.isdigit():
    print('*' * (len(a) -4) + a[-4:])
else:
    print('Ошибка')

a = input()
if len(a) >= 8 and a.isdigit():
    b = a.replace(a,'****',4)
    print(b + (a[-4:]))
else:
    print('Ошибка')


string = input()
if len(string) >= 8 and string.isdigit():
    a = len(string[:-4]) * '*'
    b = string[-4:]
    print(a + b)
else:
    print('Ошибка')







#____________Пароль while__________________________
a = input('Придумай пароль:')
b = ""
while b != a:
    b = input('Повтори пароль:')
    print('Не верно')
print('Правильно')

#______________Палиндром___________________________
a = input().upper()
b = a[::-1]
if a.replace(" ","") == b:
    print('да')
else:
    print('нет')

#______________Скрывает номер первые цифры____________
a = input()
if len(a) >= 8 and a.isdigit():
    print("*" * (len(a)-4) + a[-4:])
else:
    print('Ошибка')

#______Таблица умножения__________________
while True:
    print('***Таблица умножения***')
    a = input('Введи число: ')
    if a.isdigit() and int(a) < 9999999999999999:
        a = int(a)
        i = 0
        while i < 9:
            i = i + 1
            print(f'{a} * {i} = {a * i}')
    else:
        print('Введите число от 1 до ...')
#_______тоже таблица умножения___________________
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, " " * (5 - len(str(i * j))), end=" ")
    print("\n", end="")

# таблица умнлжения с помощью цикла while
# Задаем размер таблицы умножения
размер = 10
# Выводим заголовок таблицы
print("Таблица умножения")
# Выводим верхнюю горизонтальную линию
print("-" * 20)
# Инициализируем первый множитель
умножитель_1 = 1
# Внешний цикл для умножителя 1
while умножитель_1 <= размер:
    # Инициализируем второй множитель
    умножитель_2 = 1
    # Внутренний цикл для умножителя 2
    while умножитель_2 <= размер:
        # Выводим результат умножения и добавляем пробел для форматирования
        print(умножитель_1 * умножитель_2, end="\t")
        # Увеличиваем умножитель 2
        умножитель_2 += 1
    # Переходим на новую строку после завершения внутреннего цикла
    print()
    # Увеличиваем умножитель 1
    умножитель_1 += 1
# Выводим нижнюю горизонтальную линию
print("-" * 20)

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


#Подсчет слов
string = input()
a = string.split()
b = len(a)
print(b)

string = input()
print(len(string.split()))

# показывает количество одинаковых слов
a = input().lower()
a = a.replace(".", " ").replace(",", " ").split()
b = input().lower()
print(a.count(b))


sent = input("Введите предложение:").lower()
word = input("Введите слово:").lower()
sent = sent.replace(".", ' ').replace(",", ' ')
sent_list = sent.split()
if word in sent_list:
    print(sent_list.count(word))


a = input().lower()
b = input().lower()
a = a.replace(".", ' ').replace(",", ' ')
d = a.split()
if b in d:
    print(d.count(b))


sentence = input().lower()
word_to_count = input()
sentence = sentence.replace(".", ' ').replace(",", ' ')
word_list = sentence.split()
count = word_list.count(word_to_count)
print(f'Слово {word_to_count}" встречается {count} раз.')


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

# отфильтровывает слова и списковые включения
a = input().split()
words = []
for i in a:
    if i.isalnum():
        words.append(i)
print(words)

a = input()
words = [i for i in a.split() if i.isalnum()]
print(words)


# Перетасовка дел
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

# Аппарат для голосования
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
r = Tk()
def t():
    showinfo(title="Спасибо", message="Спасибо что проголосовали. Ваше мнение для нас важно")
def o():
    showerror(title="Ошибка", message="Мы вас раскусили! Вы агент госдепа! Уходите.")
r.resizable(width=False, height=False)
r.title("Аппарат для голосования")
r.geometry("300x700")
e = Frame(r, bg='white')
e.place(relwidth=1, relheight=1)
u = Button(e, text='За', padx="300", pady="330", bg="green", command=t)
u.pack()
y = Button(e, text='Против', padx="300", pady="1", bg="red", command=o)
y.pack()
r.mainloop()


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


# Код для VPN образец________________________________________________________
# Создание VPN с использованием Python может быть сложной задачей,
# и в большинстве случаев лучше использовать специализированные инструменты.
# Однако, если у вас есть конкретные требования или вы хотите попробовать создать простой VPN для
# обучения или экспериментов, вы можете использовать библиотеку asyncio для создания асинхронного сервера и клиента.
# Ниже приведен пример кода для создания очень простого VPN с использованием библиотеки asyncio.
# Этот код предназначен только для образовательных целей и не гарантирует безопасность в реальном мире.
import asyncio
import socket

async def handle_client(reader, writer):
    while True:
        data = await reader.read(4096)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()

async def start_server(host, port):
    server = await asyncio.start_server(
        handle_client, host, port
    )
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

async def start_client(server_host, server_port, local_port):
    reader, writer = await asyncio.open_connection(server_host, server_port)

    local_server = await asyncio.start_server(
        handle_client, '127.0.0.1', local_port
    )
    addr = local_server.sockets[0].getsockname()
    print(f'Local server listening on {addr}')

    async with local_server:
        await local_server.serve_forever()

if __name__ == '__main__':
    server_host = '0.0.0.0'
    server_port = 8888

    local_port = 9999

    server_task = asyncio.ensure_future(start_server(server_host, server_port))
    client_task = asyncio.ensure_future(start_client(server_host, server_port, local_port))

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server_task.cancel()
        client_task.cancel()
        loop.run_until_complete(asyncio.gather(server_task, client_task))
        loop.close()

# Обратите внимание, что этот код создает очень простой VPN сервер и клиент.
# Он просто пересылает данные между клиентом и сервером.
# В реальном мире VPN требуют дополнительных слоев безопасности,
# шифрования и управления сеансами. Настоятельно рекомендуется использовать проверенные библиотеки и
# инструменты для создания VPN, такие как OpenVPN, WireGuard или другие.

#_______________________________________________________________________________________________

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


# Таймер/ секундомер = как вариант написать программу на весь экран для гирь
import time
timer = 0
while True:
    time.sleep(1)
    print(timer)
    timer += 1


# Работа с файлами
print('''Выберете операцию: 
1 - записать текст в файл 
2 - прочитать файла 
3 - создать файл''')
a = input()

if a == '1':
    z = input('В какой файл добавить информацию: ')
    q = input('Введите текст для в файл: ')
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


# Пароль рандом
import random

x = input("Введите пароль: ")
pas = " "
for y in range(16):
    pas += random.choice("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789")
print(x, ", ваш пароль - ", pas)





# Черепашка
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



# Факториал числа, самое лучшее если выводить циклом for так как это быстрее
def fact_loop(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

print(fact_loop(3))


# Рисуем в канвас__________________________________________________________
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
#_______________________________
# Еще канвас
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



# Самое длинное слово
# Получаем текст от пользователя
введенный_текст = input("Введите предложение: ")
# Разбиваем текст на слова
список_слов = введенный_текст.split()
# Инициализируем переменную для хранения самого длинного слова
самое_длинное_слово = ""
# Пробегаемся по списку слов
for слово in список_слов:
    # Сравниваем длину текущего слова с длиной самого длинного слова
    if len(слово) > len(самое_длинное_слово):
        # Если текущее слово длиннее, обновляем значение самого длинного слова
        самое_длинное_слово = слово
# Выводим самое длинное слово на экран
print(самое_длинное_слово)

# короткий вариант самое длинное слово
print(max(input().split(), key=len))


# Поиск одинаковых слов
a = input().lower()
a = a.replace(".", " ").replace(",", " ").split()
b = input().lower()
print(a.count(b))



# Отфильтровываем слова
# Получаем строку с текстом от пользователя
user_input = input("Введите текст: ")
# Разбиваем строку на список слов
words_list = user_input.split()
# Создаем переменную с пустым списком для отфильтрованных слов
filtered_words = []
# Перебираем слова из списка и добавляем в filtered_words только те, которые состоят из букв и/или цифр
for word in words_list:
    if word.isalnum():
        filtered_words.append(word)
# Выводим отфильтрованные слова на экран
print("Отфильтрованные слова:", ' '.join(filtered_words))


# Отфильтровывает слова и возвращает только цифры либо пустой список
a = input().split()
numbers = []
for i in a:
    if i.isdigit():
        numbers.append(int(i))
numbers.sort()
print(numbers)


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




# Модуль requests Для работы с HTTP запросами в Питоне есть отдельный модуль requests.
# можно посмотреть как сделан сайт
import requests
result = requests.get('https://letpy.com/simple-html-example/')
print(result.text)




# Обработка событий
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


# Обработка событий вторая версия
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


# Рикошетящие круги
import tkinter
import time
import random
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width = 600, height = 600)
canvas.pack()
circles = []
colors = ('Red', 'White', 'Green', 'Blue', 'Cyan', 'Gold', 'Orange')

def my_click(event):
    x = event.x
    y = event.y
    r = random.randint(10, 50)
    circle = {
        'dx' : random.randint(-10, 10),
        'dy' : random.randint(-10, 10),
        'id' : canvas.create_oval(x, y, x+r, y+r, fill = random.choice(colors))}
    circles.append(circle)
    #canvas.create_oval(x-r, y-r, x+r, y+r, fill = random.choice(colors))
canvas.bind('<Button-1>', my_click)

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        if x0 < 0 or x1 > 600:
            circle['dx'] = - circle['dx']
        if y0 < 0 or y1 > 600:
            circle['dy'] = - circle['dy']
        canvas.move(circle['id'],circle['dx'] , circle['dy'])
    canvas.update()
    time.sleep(0.02)
canvas.mainloop()



# делает разноцветные пластинки
import tkinter
import random
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=500, height=400)
canvas.pack()

colors = ['azure', 'aquamarine', 'blue',  'cyan', 'DarkGrey', 'firebrick1', 'gold', 'GreenYellow', 'grey35', 'HotPink', 'light slate blue', 'LightSeaGreen', 'navy', 'purple', 'RoyalBlue', 'SpringGreen', 'white', 'yellow', 'black']
color = random.choice(colors)

def my_click(event):
    for i in range(5):
        color = random.choice(colors)
        r = random.randint(0, 50)
        canvas.create_oval(event.x-r, event.y-r, event.x + r, event.y + r, fill = color)
        print(f'Клик на холсте в точке x={event.x}, y={event.y}')

canvas.bind('<Button-1>', my_click)
window.mainloop()



# Узнать дату и время
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






# Игра крестики нолики
import tkinter


class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.window = window
        self.create_board()
        self.bind("<Button-1>", self.click)
        self.reset_game()

    def create_board(self):
        self.create_line(100, 0, 100, 300, fill="black", width=2)
        self.create_line(200, 0, 200, 300, fill="black", width=2)
        self.create_line(0, 100, 300, 100, fill="black", width=2)
        self.create_line(0, 200, 300, 200, fill="black", width=2)

    def reset_game(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = "X"
        self.delete("all")
        self.create_board()

    def click(self, event):
        x = event.x // 100
        y = event.y // 100
        if self.board[y][x] is None:
            self.board[y][x] = self.current_player
            self.draw_symbol(x, y, self.current_player)
            if self.check_winner(self.current_player):
                self.display_winner(self.current_player)
            elif all(all(cell is not None for cell in row) for row in self.board):
                self.display_winner("Никто не")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_symbol(self, x, y, player):
        if player == "X":
            self.create_line(x * 100 + 20, y * 100 + 20, x * 100 + 80, y * 100 + 80, fill="blue", width=2)
            self.create_line(x * 100 + 80, y * 100 + 20, x * 100 + 20, y * 100 + 80, fill="blue", width=2)
        else:
            self.create_oval(x * 100 + 20, y * 100 + 20, x * 100 + 80, y * 100 + 80, outline="red", width=2)

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def display_winner(self, winner):
        self.create_text(150, 150, text=f"{winner} победил!", font=("Arial", 24), fill="green")
        self.unbind("<Button-1>")
        self.window.after(2000, self.reset_game)



okno = tkinter.Tk()
game = TicTacToe(okno)
game.pack()
okno.mainloop()



