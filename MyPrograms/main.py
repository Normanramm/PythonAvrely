import tkinter as tk
import random

# Настройки игры
WIDTH = 400      # Ширина игрового поля
HEIGHT = 400     # Высота игрового поля
DIRECTIONS = ["Up", "Down", "Left", "Right"]  # Возможные направления движения
CELL_SIZE = 10  # Размер одной клетки змейки и еды
DELAY = 100     # Скорость игры (задержка между движениями змейки в мс)


# Создание главного окна
root = tk.Tk()
root.title("Змейка | Счет: 0")
root.resizable(False, False)  # Запрет на изменение размера окна


canvas = tk.Canvas(
    root,            # Родительское окно
    width=WIDTH,     # Ширина поля
    height=HEIGHT,   # Высота поля
    bg="black",      # Цвет фона (чёрный)
    highlightthickness=0  # Убираем границу
)
canvas.pack()  # Размещаем canvas в окне


# создание змеи
snake = [(100, 100), (90, 100), (80, 100)]
direction = "Right"  # Начальное направление движения
# food = None # Начальное положение еды
score = 0  # Начальный счет
game_over = False  # cтатус игры


# Функция для создания новой еды
def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:  # Проверяем, не находится ли еда внутри змейки
            return (x, y)


food = create_food()

# Отрисовка еды


def draw_food():
    canvas.create_rectangle(
        food[0], food[1],             # Верхний левый угол (x1, y1)
        food[0] + CELL_SIZE,          # x-координата правого края
        food[1] + CELL_SIZE,          # y-координата нижнего края
        fill="red",                   # Цвет заливки
    )

# Отрисовка змейки


def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],  # Верхний левый угол
            segment[0] + CELL_SIZE,  # Нижний правый угол (x)
            segment[1] + CELL_SIZE,  # Нижний правый угол (y)
            fill="green",         # Цвет заливки
            outline="darkgreen"      # Цвет обводки
        )


# Проверка на съеденную еду, Добавим проверку совпадает ли голова змейки с координатами еды
def check_food_collision():
    global food, score
    if snake[0] == food:
        score += 1                # Увеличиваем счёт
        food = create_food()      # Генерируем новую еду
        return True               # Сообщаем, что еда съедена
    return False                  # Еда не съедена


# Обработчик нажатия клавиш
def on_key_press(event):
    global direction
    key = event.keysym
    if key in DIRECTIONS:
        # Запрещаем поворот в противоположную сторону
        if (key == "Up" and direction != "Down" or
            key == "Down" and direction != "Up" or
            key == "Left" and direction != "Right" or
                key == "Right" and direction != "Left"):
            direction = key


root.bind("<KeyPress>", on_key_press)  # Привязываем обработчик к окну

# Теперь, если еда съедена — не удаляем хвост (чтобы змейка стала длиннее).


def move_snake():
    head_x, head_y = snake[0]

    if direction == "Up":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "Left":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "Right":
        new_head = (head_x + CELL_SIZE, head_y)

    snake.insert(0, new_head)  # Добавляем новую голову

    if not check_food_collision():  # Если еда не съедена
        snake.pop()  # Удаляем хвост


def update_title():
    root.title(f"Змейка | Счёт: {score}")


# Игровой цикл
def game_loop():
    global snake, food, score
    move_snake()           # Двигаем змейку, обновляет координаты змейки
    canvas.delete("all")  # Очищаем холст, очищает предыдущий кадр
    draw_food()             # Рисуем еду, рисуют текущее состояние
    draw_snake()  # Рисуем змейку, рисуют текущее состояние
    update_title()
    # Повторяем через DELAY мс, запускает этот цикл снова через DELAY миллисекунд
    root.after(DELAY, game_loop)


# Первоначальная отрисовка
draw_food()
draw_snake()
root.after(DELAY, game_loop)

# Запуск главного цикла программы
root.mainloop()
