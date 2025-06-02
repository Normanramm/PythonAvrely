import turtle
from random import random

t = turtle.Turtle()
t.speed(100)

for _ in range(6):  # квадрат
    t.forward(50)
    t.right(90)

for _ in range(8):  # круг мнгоугольник
    t.color('red')
    t.forward(50)
    t.left(50)

t.penup()  # поднять перо
t.forward(150)
t.right(55)
t.pendown()  # опустить перо

for _ in range(12):  # пятиугольник
    t.color('green')
    t.width(20)
    t.backward(50)
    t.right(45)
    t.left(10)

for _ in range(5):
    t.penup()
    t.forward(50)
    t.home()  # вернуться в центр координат
    t.pendown()
    t.color('black')


def pen():
    t.penup()
    t.width(0)
    t.left(90)
    t.forward(100)
    t.pendown()


pen()


for steps in range(50):
    for c in ('blue', 'red', 'green', 'yellow', "#EE07C4"):
        t.color(c)
        t.forward(steps)
        t.right(30)

pen()

t.fillcolor("red")  # Установка цвета
t.begin_fill()      # Начало зоны заливки
for _ in range(4):  # Рисуем квадрат
    t.forward(100)
    t.left(90)
t.end_fill()   # конец зоны заливки


for i in range(100):  # рисует галематью
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.home()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break


turtle.done()