from random import uniform
import turtle


def random_color():
    """Генерирует случайный цвет в RGB формате"""
    return uniform(0, 1), uniform(0, 1), (uniform(0, 1))


def draw_random_polygon(sides=6):
    """Рисует многоугольник со случайными параметрами"""
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(uniform(1, 5))

    for _ in range(sides):
        # Случайные параметры для каждой стороны
        t.color(random_color(), random_color())  # Контур и заливка
        t.begin_fill()
        t.forward(uniform(50, 150))
        t.left(360/sides)
        t.end_fill()


# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Случайные многоугольники")

# Рисуем 3 случайных шестиугольника
for _ in range(3):
    draw_random_polygon(6)

turtle.done()


# с добвалением as

from random import uniform as random_uniform
import turtle


def random_color():
    return random_uniform(0, 1), random_uniform(0, 1), (random_uniform(0, 1))


def draw_random_polygon(sides=6):
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(random_uniform(1, 5))

    for _ in range(sides):
        t.color(random_color(), random_color())
        t.begin_fill()
        t.forward(random_uniform(50, 150))
        t.left(360/sides)
        t.end_fill()


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Случайные многоугольники")

for _ in range(3):
    draw_random_polygon(6)

turtle.done()