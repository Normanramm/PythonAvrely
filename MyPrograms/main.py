import turtle

colors = ('red', 'green', 'blue', 'yellow')
lengths = (100, 100, 100, 100)  # Исправлено: кортеж вместо некорректного range

t = turtle.Turtle()
t.speed(1)  # Добавлена скорость для лучшего наблюдения
t.width(3)  # Толщина линии

for color, length in zip(colors, lengths):
    t.color(color)
    t.forward(length)
    t.right(90)

t.hideturtle()  # Скрыть черепаху после завершения
turtle.done()