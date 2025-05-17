import tkinter as tk
from tkinter import messagebox

class IMTclass:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_imt(self):
        return self.weight / ((self.height / 100) ** 2)

    def interpret(self, imt):
        if imt < 18.5:
            return "Недостаточный вес"
        elif imt >= 18.5 and imt < 25:
            return "Нормальный вес"
        elif imt >= 25 and imt < 30:
            return "Избыточный вес"
        elif imt >= 30:
            return "Ожирение"
        else:
            return "Вызывай врача"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x250")
        self.title("Индекс массы тела VAI")

        self.weight_label = tk.Label(self, text="Вес в килограммах:")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        self.height_label = tk.Label(self, text="Рост в сантиметрах:")
        self.height_label.pack()

        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        self.calculate_button = tk.Button(self, text="Рассчитать", command=self.calculate)
        self.calculate_button.pack()

        # Центрируем окно
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (self.winfo_reqwidth() / 2))
        y_coordinate = int((screen_height / 2) - (self.winfo_reqheight() / 2))
        self.geometry("+{}+{}".format(x_coordinate, y_coordinate)) # self.geometry(f'400x250+{x_coordinate}+{y_coordinate}')


    def calculate(self):
        try:
            weight = float(self.weight_entry.get().replace(',', '.'))
            height = float(self.height_entry.get().replace(',', '.'))
            imt = IMTclass(weight, height)
            messagebox.showinfo("Результат", imt.interpret(imt.calculate_imt()))
        except ValueError:
            messagebox.showerror("Ошибка", "Введите число.")

app = App()
app.mainloop()
