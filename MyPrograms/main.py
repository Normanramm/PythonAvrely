import tkinter as tk

root = tk.Tk()
root.title("Крестики-нолики")
root.iconbitmap("icon.ico")

# ===== Глобальные переменные =====
current_player = "X"  # Начинают крестики
buttons = []  # Список для хранения всех кнопок

# ===== Функция проверки победы =====


def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
        [0, 4, 8], [2, 4, 6]              # Диагональные линии
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            return True
    return False


# ===== Функция обработки клика =====
def on_click(index):
    global current_player  # Используем глобальную переменную

    # Проверяем, пустая ли кнопка
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player  # Записываем X или O

        # Проверяем, есть ли победитель
        if check_winner():
            print(f"Победил {current_player}!")  # Временный вывод в консоль

        # Меняем игрока
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# ===== Создание кнопок =====
for i in range(9):
    button = tk.Button(
        root,
        text="",  # Изначально пустая
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)  # Привязываем функцию к кнопке
    )
    button.grid(row=i//3, column=i % 3)  # Размещаем в сетке 3x3
    buttons.append(button)  # Добавляем кнопку в список

root.mainloop()
