import tkinter as tk


class TicTacToe:
    def __init__(self):
        # Создаём окно
        self.root = tk.Tk()
        self.root.title("Крестики нолики")
        # self.root.geometry("400x400")  # Отключаем фиксированный размер
        self.root.iconbitmap("icon1.ico")  # создает иконку
        self.current_player = "X"  # Обработка хода, первым ходит "X" (крестик)
        self.buttons = []  # Сюда будем сохранять все кнопки

        # Предназначен для внутреннего использования при инициализации. Принцип инкапсуляции: объект должен быть готов к работе сразу после создания.
        # Пользователь класса (или ты сам завтра) не должен помнить, что нужно дополнительно вызывать create_widgets().
        # Так объект будет готов к работе сразу после создания.
        self.create_widgets()

    def check_winner(self):
        """Проверка победителя."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
            [0, 4, 8], [2, 4, 6]              # Диагональные линии
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.buttons[a]["text"] == self.buttons[b]["text"] == self.buttons[c]["text"] != "":
                return True
        return False

    def on_click(self, index):
        """Функция обработки клика, отвечает за ход игрока. 
            Она получает на вход номер кнопки index, которую нажали, и выполняет три важных действия:
            Проверяет, свободна ли клетка.
            Записывает символ текущего игрока ("X" или "O") в текст кнопки.
            Передаёт ход другому игроку."""
        # global current_player  # Используем глобальную переменную(Удалено — используется self.current_player)!!!

        # Проверяем, пустая ли кнопка
        if self.buttons[index]["text"] == "":
            # Записываем X или O
            self.buttons[index]["text"] = self.current_player

            # Проверяем, есть ли победитель
            if self.check_winner():
                # Временный вывод в консоль(позже заменить на всплывающее окно.)
                print(f"Победил {self.current_player}!")

            # Меняем игрока
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

    def create_widgets(self):
        """Создаёт игровое поле из 9 кнопок."""
        for i in range(9):  # Создаём 9 кнопок (от 0 до 8)
            button = tk.Button(
                self.root,
                text="",  # Пока без текста
                font=("Arial", 30),  # Крупный шрифт
                width=5,  # Ширина кнопки
                height=2,  # Высота кнопки
                # При клике вызываем метод on_click с нужным индексом
                command=lambda idx=i: self.on_click(idx)
            )
            # Размещаем кнопку в сетке(номер строки, номер столбца)
            # Размещаем кнопку в сетке, тут можно добавить другие параметры
            button.grid(row=i//3, column=i % 3)
            self.buttons.append(button)  # Добавляем кнопку в список

    def run(self):
        """Запускает главное окно."""
        self.root.mainloop()


if __name__ == '__main__':
    game = TicTacToe()
    # game.create_widgets() можно размеместить в конструкторе
    game.run()
