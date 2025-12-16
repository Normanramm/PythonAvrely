import tkinter as tk
from tkinter import font
import pyautogui
import random
import threading
import time


class MouseWigglerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Скайнет")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Фон 
        self.root.configure(bg="#f8f9fa")

        self.center_window()
        self.wiggling = False

        # Верхняя панель (заголовок)
        header_frame = tk.Frame(root, bg="#343a40", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)  # сохраняем высоту

        header_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.header_label = tk.Label(
            header_frame,
            text="🖱️ Автоматическое движение курсора",
            font=header_font,
            fg="white",
            bg="#343a40"
        )
        self.header_label.pack(pady=20)

        # Основное содержимое 
        main_frame = tk.Frame(root, bg="#f8f9fa")
        main_frame.pack(fill="both", expand=True, padx=40, pady=30)

        # Статус
        self.status_var = tk.StringVar(
            value="Готово к запуску. Нажмите кнопку ниже.")
        status_font = font.Font(family="Segoe UI", size=14)
        self.status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=status_font,
            bg="#f8f9fa",
            fg="#495057",
            wraplength=700,
            justify="center"
        )
        self.status_label.pack(pady=(0, 40))

        # Кнопка "НАЧАТЬ"
        start_font = font.Font(family="Segoe UI", size=22, weight="bold")
        self.start_button = tk.Button(
            main_frame,
            text="▶ ЗАПУСТИТЬ ШЕВЕЛЕНИЕ",
            font=start_font,
            bg="#28a745",          # зелёный Material
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            width=30,
            command=self.start_wiggling,
            cursor="hand2"
        )
        self.start_button.pack(pady=(0, 25))

        # Кнопка "ОСТАНОВИТЬ" 
        stop_font = font.Font(family="Segoe UI", size=24, weight="bold")
        self.stop_button = tk.Button(
            main_frame,
            text="⏹ ЭКСТРЕННАЯ ОСТАНОВКА",
            font=stop_font,
            bg="#dc3545",          # красный Material
            fg="white",
            activebackground="#c82333",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            width=32,
            command=self.stop_wiggling,
            state="disabled",
            cursor="hand2"
        )
        self.stop_button.pack(pady=(0, 0))

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"800x500+{x}+{y}")

    def wiggle_mouse(self):
        screen_width, screen_height = pyautogui.size()
        while self.wiggling:
            dx = random.randint(-40, 40)
            dy = random.randint(-40, 40)
            x, y = pyautogui.position()
            new_x = max(0, min(screen_width - 1, x + dx))
            new_y = max(0, min(screen_height - 1, y + dy))
            pyautogui.moveTo(new_x, new_y, duration=0.03)
            time.sleep(0.1)

    def start_wiggling(self):
        if not self.wiggling:
            self.wiggling = True
            self.status_var.set(
                "✅ КУРСОР АКТИВНО ШЕВЕЛИТСЯ! "
                "Для немедленной остановки нажмите КРАСНУЮ КНОПКУ ниже."
            )
            self.start_button.config(state="disabled", bg="#6c757d")
            self.stop_button.config(state="normal", bg="#dc3545")
            threading.Thread(target=self.wiggle_mouse, daemon=True).start()

    def stop_wiggling(self):
        self.wiggling = False
        self.status_var.set(
            "⏹ Движение успешно остановлено. Система в безопасности!")
        self.start_button.config(state="normal", bg="#28a745")
        self.stop_button.config(state="disabled", bg="#6c757d")


def main():
    root = tk.Tk()
    # Поддержка DPI для Windows
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    app = MouseWigglerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()