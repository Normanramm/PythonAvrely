import tkinter as tk
import speedtest


class SkorostinetClass:
    def __init__(self, master):
        self.st = speedtest.Speedtest()
        self.master = master
        self.master.title("Skorost inet v2.3")
        self.master.geometry('400x200')
        # Выводим окно по середине экрана
        w = 400
        h = 200
        ws = self.master.winfo_screenwidth()  # ширина экрана
        hs = self.master.winfo_screenheight()  # высота экрана
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.create_widgets()

    def create_widgets(self):
        self.ds_label = tk.Label(self.master, text='Скорость загрузки:')
        self.ds_label.grid(row=0, column=0)

        self.us_label = tk.Label(self.master, text='Скорость отдачи:')
        self.us_label.grid(row=1, column=0)

        self.ping_label = tk.Label(self.master, text='Задержка (ping):')
        self.ping_label.grid(row=2, column=0)

        self.ping_label = tk.Label(self.master, text='Нажми и жди!')  # стоит тут поменять местоположение
        self.ping_label.grid(row=4, column=1)

        self.ds_text = tk.Text(self.master, height=1, width=20)
        self.ds_text.grid(row=0, column=1)

        self.us_text = tk.Text(self.master, height=1, width=20)
        self.us_text.grid(row=1, column=1)

        self.ping_text = tk.Text(self.master, height=1, width=20)
        self.ping_text.grid(row=2, column=1)

        self.run_button = tk.Button(self.master, text='Запустить тест', command=self.run_test)
        self.run_button.grid(row=3, column=1)

    def test(self):
        self.ds = self.st.download()
        self.us = self.st.upload()
        self.ping = self.st.results.ping

        return self.ds, self.us, self.ping

    def humansize(self, nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    def print_results(self):
        ds, us, ping = self.test()
        self.ds_text.delete('1.0', 'end')
        self.ds_text.insert('end', self.humansize(ds))

        self.us_text.delete('1.0', 'end')
        self.us_text.insert('end', self.humansize(us))

        self.ping_text.delete('1.0', 'end')
        self.ping_text.insert('end', ping)

    def run_test(self):
        self.ping_label.config(text='Идет загрузка...')
        self.master.update_idletasks()  # Обновите графический интерфейс, чтобы отобразить сообщение о загрузке
        self.print_results()
        self.ping_label.config(text='Загрузка завершена')


root = tk.Tk()
app = SkorostinetClass(root)
root.mainloop()
