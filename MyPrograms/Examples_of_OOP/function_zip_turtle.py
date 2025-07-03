# прсотая версия ________________________________________________________
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

# Версия с модулем из Letpy в котором хранятся цвета и длины ____________

import turtle
from data_sandbox import get_rainbow_colors

colors = get_rainbow_colors(100)
steps = range(1, 100)  

turtle.bgcolor('black')

for color, step in zip(colors, steps):
    turtle.color(color)           
    turtle.forward(step)  

    turtle.right(40) # поставить 80 будет цветочек, 40 заветвление, step странный круг           

turtle.done()


# Цвета выбором цифр_____________________________________________________
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


# Создание АТОМА_____________________________________________________________

import turtle


colors = (
    'alice blue', 'antique white', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4',
    'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2',
    'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanched almond',
    'blue', 'blue violet', 'blue1', 'blue2', 'blue3', 'blue4', 'brown', 'brown1', 'brown2', 'brown3', 'brown4',
    'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'CadetBlue1', 'CadetBlue2',
    'CadetBlue3', 'CadetBlue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate',
    'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4',
    'cornflower blue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan1', 'cyan2',
    'cyan3', 'cyan4', 'dark blue', 'dark cyan', 'dark goldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
    'DarkGoldenrod4', 'dark gray', 'dark green', 'dark grey', 'dark khaki', 'dark magenta', 'dark olive green',
    'dark orange', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'dark orchid', 'DarkOrchid1', 'DarkOrchid2',
    'DarkOrchid3', 'DarkOrchid4', 'dark red', 'dark salmon', 'dark sea green', 'DarkSeaGreen1', 'DarkSeaGreen2',
    'DarkSeaGreen3', 'DarkSeaGreen4', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise',
    'dark violet', 'deep pink', 'DeepPink1', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'deep sky blue', 'DeepSkyBlue1',
    'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'dim gray', 'dim grey', 'dodger blue', 'DodgerBlue1', 'DodgerBlue2',
    'DodgerBlue3', 'DodgerBlue4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white',
    'forest green', 'gainsboro', 'ghost white', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'Goldenrod1',
    'Goldenrod2', 'Goldenrod3', 'Goldenrod4', 'gray', 'green', 'green yellow', 'green1', 'green2', 'green3', 'green4',
    'grey', 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'HotPink1', 'HotPink2', 'HotPink3',
    'HotPink4', 'indian red', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'ivory', 'ivory1', 'ivory2', 'ivory3',
    'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'LawnGreen', 'lemon chiffon',
    'light blue', 'light coral', 'light cyan', 'LightCyan1', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'light goldenrod',
    'light goldenrod yellow', 'light gray', 'light green', 'light grey', 'light pink', 'LightPink1', 'LightPink2', 'LightPink3',
    'LightPink4', 'light salmon', 'LightSalmon1', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'light sea green',
    'light sky blue', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'light slate blue', 'light slate gray',
    'light slate grey', 'light steel blue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4',
    'light yellow', 'LightYellow1', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'lime green', 'linen', 'magenta',
    'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine',
    'medium blue', 'medium orchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'medium purple',
    'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'medium sea green', 'medium slate blue',
    'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'MistyRose1',
    'MistyRose2', 'MistyRose3', 'MistyRose4', 'moccasin', 'navajo white', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3',
    'NavajoWhite4', 'navy', 'old lace', 'olive drab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'OliveDrab4', 'orange',
    'orange red', 'orange1', 'orange2', 'orange3', 'orange4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4',
    'pale goldenrod', 'pale green', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'pale turquoise', 'PaleTurquoise1',
    'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'pale violet red', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3',
    'PaleVioletRed4', 'papaya whip', 'peach puff', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'peru', 'pink',
    'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1',
    'purple2', 'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosy brown', 'RosyBrown1', 'RosyBrown2',
    'RosyBrown3', 'RosyBrown4', 'royal blue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'saddle brown',
    'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3',
    'SeaGreen4', 'seashell', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3',
    'sienna4', 'sky blue', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'slate blue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'slate gray', 'slate grey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'spring green', 'SpringGreen1',
    'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'steel blue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4',
    'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1',
    'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet',
    'violet red', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4',
    'white', 'white smoke', 'yellow', 'yellow green', 'yellow1', 'yellow2', 'yellow3', 'yellow4'
)
steps = range(1, 10000)

turtle.bgcolor('black')

for color, step in zip(colors, steps):
    turtle.color(color)
    turtle.forward(step)

    # Создание Атома
    turtle.right(step)
    
    turtle.speed(300)

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