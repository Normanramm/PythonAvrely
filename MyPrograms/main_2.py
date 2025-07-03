import turtle

colors = ['red', 'green', 'blue', 'yellow']
lengths = [100, 100, 100, 100]

t = turtle.Turtle()
for color, length in zip(colors, lengths):
    t.color(color)
    t.forward(length)
    t.right(90)

turtle.done()
