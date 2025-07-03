import turtle

colors = [
    (1, 0, 0), (1, 0.5, 0), (1, 1, 0),
    (0.5, 1, 0), (0, 1, 0), (0, 1, 0.5),
    (0, 0.5, 1), (0, 0, 1), (0.5, 0, 1),
    (1, 0, 1)
]

steps = range(200, 400, 20)  

turtle.speed(5)
turtle.pensize(3)

for color, step in zip(colors, steps):
    turtle.color(color)
    turtle.forward(step)  
    turtle.right(30)

turtle.done()

# И в классе _____________________________________________________________

import turtle
from math import sin, cos, pi

class ColorFlower:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        turtle.bgcolor('black')
        self.t.width(2)
        
        # Генерация цветов с корректными RGB значениями (0-1)
        self.colors = [
            (abs(sin(i/15)), abs(cos(i/20)), abs(sin(i/25 + pi/3)))
            for i in range(200)
        ]
        
        # Диапазон для шагов
        self.steps = range(1, 201)
        
        # Углы поворота
        self.angles = [45 + 10 * cos(i/15) for i in range(200)]
    
    def draw_flower(self):
        # Используем zip для объединения всех параметров
        for color, step, angle in zip(self.colors, self.steps, self.angles):
            self.t.color(color)
            self.t.forward(step * 0.7)
            self.t.right(angle)
            
            # Изменяем толщину каждые 15 шагов
            if step % 15 == 0:
                self.t.width(step/80 + 1)
    
    def run(self):
        self.draw_flower()
        turtle.done()

# Создание и запуск
flower = ColorFlower()
flower.run()


# тоже самое, но чуть по другому_________________________________________

import turtle
from math import sin, cos, pi

class LetpyFlower:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        turtle.bgcolor('black')
        self.t.width(2)
        
        # Генерация 200 цветов с корректными RGB значениями (0-1)
        self.colors = [
            (abs(sin(i/15)), abs(cos(i/20)), abs(sin(i/25 + pi/3)))
            for i in range(200)
        ]
        
        # Фиксированные параметры для 200 шагов
        self.steps = [i * 0.7 for i in range(1, 201)]
        self.angles = [45 + 10 * cos(i/15) for i in range(200)]
    
    def draw_flower(self):
        # Четко ограниченный цикл на 200 итераций
        for color, step, angle in zip(self.colors, self.steps, self.angles):
            self.t.color(color)
            self.t.forward(step)
            self.t.right(angle)
            
            # Изменение толщины каждые 15 шагов
            if step % 15 == 0:
                self.t.width(step/80 + 1)
        
        # Явное завершение работы
        self.t.hideturtle()
    
    def run(self):
        self.draw_flower()
        turtle.done()

# Создание и запуск
flower = LetpyFlower()
flower.run()