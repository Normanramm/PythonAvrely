import turtle
import random

t = turtle.Turtle()
t.speed(0)


def zvezda():

    i = 0
    while i < 50:
        t.forward(200)
        t.left(170)
        t.backward(10)
        i += 1


def zvezda_2():

    for steps in range(50):
        for c in ('blue', 'red', 'green', 'yellow', "#EE07C4"):
            t.width(3)
            t.color(c)
            t.forward(steps)
            t.right(30)


colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'purple', 'pink', 'violet']


def zvezda_3():
    i = 0
    while i < 50:
        # Выбираем случайный цвет для каждого луча
        t.color(random.choice(colors))
        t.forward(130)
        t.backward(70)
        t.right(6)
        t.left(65)
        t.backward(35)
        i += 1


def one_line():
    t.penup()
    t.forward(400)
    t.pendown()


def two_line():
    t.penup()
    t.left(27)
    t.backward(350)
    t.pendown()


zvezda()
one_line()
zvezda_2()
two_line()
zvezda_3()


turtle.done()


# _____________________________________________________________


t = turtle.Turtle()
t.speed(0)

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break


turtle.done()

# ________________________________________________________________


t = turtle.Turtle()
t.speed(0)

while True:
    t.forward(200)
    t.left(170)
    t.backward(10)
    if t.distance(0, 0) < 3:
        break


turtle.done()


# _____________________________________________________________


t = turtle.Turtle()
t.speed(0)

i = 0
while i < 50:
    t.forward(200)
    t.left(170)
    t.backward(10)
    i += 1

turtle.done()


# _____________________________________________________________

import turtle

t = turtle.Turtle()
t.speed(10)  # Средняя скорость рисования

# Рисуем спираль
for i in range(1000):  # 36 итераций (3 полных оборота)
    t.forward(i * 5)  # Длина шага увеличивается с каждой итерацией
    t.right(100)       # Поворот на 30 градусов

turtle.done()



# _____________________________________________________________

import turtle
import colorsys

t = turtle.Turtle()
t.speed(100)
turtle.colormode(255)  # Используем RGB режим (0-255)

for i in range(1000):
    # Генерируем цвет в HSV и конвертируем в RGB
    hue = i / 1000  # Плавное изменение оттенка
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Максимальная насыщенность и яркость
    
    # Конвертируем в диапазон 0-255
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    t.color(r, g, b)  # Устанавливаем цвет
    t.width(3)
    t.forward(i * 0.5)  # Уменьшил шаг для более плотной спирали
    t.right(100)

turtle.done()