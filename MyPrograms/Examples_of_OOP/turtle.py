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


# и в классах


class MyTurtle(turtle.Turtle):
    def __init__(self, speed=100):
        super().__init__()
        self.speed(speed)

    def draw_square(self, size=50):
        for _ in range(4):
            self.forward(size)
            self.right(90)

    def draw_polygon(self, sides=8, length=50, color='red'):
        self.color(color)
        angle = 360 // sides
        for _ in range(sides):
            self.forward(length)
            self.left(angle)

    def move(self, x=150, angle=55):
        self.penup()
        self.forward(x)
        self.right(angle)
        self.pendown()

    def draw_pentagon(self, sides=12, length=50, width=20, color='green'):
        self.color(color)
        self.width(width)
        angle = 360 // sides
        for _ in range(sides):
            self.backward(length)
            self.right(angle)
            self.left(10)

    def return_home_lines(self, steps=50):
        for _ in range(5):
            self.penup()
            self.forward(steps)
            self.home()
            self.pendown()
            self.color('black')

    def reset_position(self, distance=100):
        self.penup()
        self.width(0)
        self.left(90)
        self.forward(distance)
        self.pendown()

    def colorful_pattern(self, iterations=50):
        for steps in range(iterations):
            for c in ('blue', 'red', 'green', 'yellow', "#EE07C4"):
                self.color(c)
                self.forward(steps)
                self.right(30)

    def filled_square(self, size=100, fill_color="red"):
        self.fillcolor(fill_color)
        self.begin_fill()
        for _ in range(4):
            self.forward(size)
            self.left(90)
        self.end_fill()

    def random_walk(self, steps=100):
        for _ in range(steps):
            step = int(random() * 100)
            angle = int(random() * 360)
            self.right(angle)
            self.forward(step)

    def spiral_return(self):
        self.home()
        while True:
            self.forward(200)
            self.left(170)
            if abs(self.pos()) < 1:
                break


# === Запуск программы ===
if __name__ == "__main__":
    t = MyTurtle()

    t.draw_square()
    t.draw_polygon(sides=8, length=50, color='red')
    t.move(x=150, angle=55)
    t.draw_pentagon(sides=12, length=50, width=20, color='green')
    t.return_home_lines(steps=50)
    t.reset_position(distance=100)
    t.colorful_pattern(iterations=50)
    t.reset_position(distance=100)
    t.filled_square(fill_color="red")
    t.reset_position(distance=100)
    t.random_walk(steps=100)
    t.spiral_return()

    turtle.done()
