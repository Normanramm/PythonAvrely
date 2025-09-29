import tkinter as tk

# ===== Создаём окно =====
root = tk.Tk()
# root.geometry("400x400")  # Можно включить, если нужно задать размер
root.iconbitmap("icon1.ico")
root.title("Крестики-нолики")

# ===== Глобальные переменные =====
current_player = "X"  # Первым ходит "X"
buttons = []  # Список для хранения кнопок

# ===== Функция обработки клика =====


def on_click(index):
    global current_player
    if buttons[index]["text"] == "":  # Проверяем, пустая ли клетка
        buttons[index]["text"] = current_player  # Записываем "X" или "O"

        # Меняем игрока
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# ===== Создаём игровое поле =====
for i in range(9):  # Создаём 9 кнопок (от 0 до 8)
    button = tk.Button(
        root,
        text="",  # Изначально без текста
        font=("Arial", 30),  # Крупный шрифт
        width=5,  # Ширина кнопки
        height=2,  # Высота кнопки
        command=lambda idx=i: on_click(idx)  # Привязываем обработчик клика
    )
    button.grid(row=i//3, column=i % 3)  # Размещаем кнопку в сетке 3x3
    buttons.append(button)  # Добавляем кнопку в список

# ===== Запускаем главный цикл =====
root.mainloop()
