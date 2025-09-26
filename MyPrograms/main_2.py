import tkinter as tk


class TicTacToe:
    def __init__(self):
        # Создаём окно
        self.root = tk.Tk()
        self.root.title("Крестики нолики")
        # self.root.geometry("400x400")  # Отключаем фиксированный размер
        self.root.iconbitmap("icon1.ico")

        self.buttons = []  # Сюда будем сохранять все кнопки

        self.create_widgets()

    def create_widgets(self):
        """Создаёт игровое поле из 9 кнопок."""
        for i in range(9):  # Создаём 9 кнопок (от 0 до 8)
            button = tk.Button(
                self.root,
                text="",  # Пока без текста
                font=("Arial", 30),  # Крупный шрифт
                width=5,  # Ширина кнопки
                height=2  # Высота кнопки
            )
            # Размещаем кнопку в сетке(номер строки, номер столбца)
            button.grid(row=i//3, column=i % 3)
            self.buttons.append(button)  # Добавляем кнопку в список

    def run(self):
        """Запускает главное окно."""
        self.root.mainloop()


if __name__ == '__main__':
    game = TicTacToe()
    # game.create_widgets() можно размеместить в конструкторе
    game.run()
