import tkinter as tk
from tkinter import font
import pyautogui
import random
import threading
import time


class MouseWigglerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Скайнет Pro")
        self.root.geometry("900x550")
        self.root.resizable(False, False)

        # Фон
        self.root.configure(bg="#f8f9fa")

        self.center_window()
        self.wiggling = False
        self.clicking = False

        # Верхняя панель (заголовок)
        header_frame = tk.Frame(root, bg="#343a40", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        header_font = font.Font(family="Segoe UI", size=22, weight="bold")
        self.header_label = tk.Label(
            header_frame,
            text="🖱️ Автоматическое движение и клики курсора",
            font=header_font,
            fg="white",
            bg="#343a40"
        )
        self.header_label.pack(pady=20)

        # Основное содержимое
        main_frame = tk.Frame(root, bg="#f8f9fa")
        main_frame.pack(fill="both", expand=True, padx=40, pady=20)

        # Настройки кликов
        settings_frame = tk.Frame(main_frame, bg="#f8f9fa")
        settings_frame.pack(pady=(0, 20))

        # Интервал кликов
        self.click_interval_var = tk.DoubleVar(value=5.0)
        tk.Label(settings_frame, text="Интервал кликов (сек):", 
                bg="#f8f9fa", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=(0, 10))
        
        self.interval_spinbox = tk.Spinbox(
            settings_frame,
            from_=1,
            to=60,
            increment=0.5,
            textvariable=self.click_interval_var,
            width=10,
            font=("Segoe UI", 12),
            state="normal"
        )
        self.interval_spinbox.pack(side=tk.LEFT)

        # Тип клика
        self.click_type_var = tk.StringVar(value="left")
        tk.Label(settings_frame, text="   Тип клика:", 
                bg="#f8f9fa", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=(20, 10))
        
        click_frame = tk.Frame(settings_frame, bg="#f8f9fa")
        click_frame.pack(side=tk.LEFT)
        
        tk.Radiobutton(click_frame, text="Левый", variable=self.click_type_var, 
                      value="left", bg="#f8f9fa", font=("Segoe UI", 11)).pack(side=tk.LEFT)
        tk.Radiobutton(click_frame, text="Правый", variable=self.click_type_var, 
                      value="right", bg="#f8f9fa", font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=(10, 0))
        tk.Radiobutton(click_frame, text="Двойной", variable=self.click_type_var, 
                      value="double", bg="#f8f9fa", font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=(10, 0))

        # Статус
        self.status_var = tk.StringVar(
            value="Готово к запуску. Настройте параметры и нажмите кнопку ниже.")
        status_font = font.Font(family="Segoe UI", size=14)
        self.status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=status_font,
            bg="#f8f9fa",
            fg="#495057",
            wraplength=800,
            justify="center"
        )
        self.status_label.pack(pady=(0, 30))

        # Кнопки управления
        buttons_frame = tk.Frame(main_frame, bg="#f8f9fa")
        buttons_frame.pack()

        # Кнопка "НАЧАТЬ"
        start_font = font.Font(family="Segoe UI", size=22, weight="bold")
        self.start_button = tk.Button(
            buttons_frame,
            text="▶ ЗАПУСТИТЬ ШЕВЕЛЕНИЕ И КЛИКИ",
            font=start_font,
            bg="#28a745",
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            width=35,
            command=self.start_wiggling,
            cursor="hand2"
        )
        self.start_button.pack(pady=(0, 15))

        # Кнопка "ОСТАНОВИТЬ"
        stop_font = font.Font(family="Segoe UI", size=24, weight="bold")
        self.stop_button = tk.Button(
            buttons_frame,
            text="⏹ ЭКСТРЕННАЯ ОСТАНОВКА",
            font=stop_font,
            bg="#dc3545",
            fg="white",
            activebackground="#c82333",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            width=35,
            command=self.stop_wiggling,
            state="disabled",
            cursor="hand2"
        )
        self.stop_button.pack()

        # Информация
        info_font = font.Font(family="Segoe UI", size=10)
        self.info_label = tk.Label(
            main_frame,
            text="Программа эмулирует движение мыши и периодические клики для предотвращения неактивности системы.",
            font=info_font,
            bg="#f8f9fa",
            fg="#6c757d",
            wraplength=800,
            justify="center"
        )
        self.info_label.pack(pady=(20, 0))

    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (900 // 2)
        y = (self.root.winfo_screenheight() // 2) - (550 // 2)
        self.root.geometry(f"900x550+{x}+{y}")

    def wiggle_mouse(self):
        screen_width, screen_height = pyautogui.size()
        click_counter = 0
        
        try:
            while self.wiggling:
                # Движение мыши
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                x, y = pyautogui.position()
                new_x = max(10, min(screen_width - 10, x + dx))
                new_y = max(10, min(screen_height - 10, y + dy))
                pyautogui.moveTo(new_x, new_y, duration=0.03)
                
                # Проверяем, нужно ли сделать клик
                if self.clicking:
                    click_counter += 1
                    time_since_last_click = click_counter * 0.1  # так как sleep 0.1
                    
                    if time_since_last_click >= self.click_interval_var.get():
                        self.perform_click()
                        click_counter = 0
                        # Обновляем статус в GUI
                        self.root.after(0, self.update_click_status)
                
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Ошибка: {e}")
            self.stop_wiggling()

    def perform_click(self):
        try:
            click_type = self.click_type_var.get()
            
            if click_type == "left":
                pyautogui.click()
            elif click_type == "right":
                pyautogui.rightClick()
            elif click_type == "double":
                pyautogui.doubleClick()
                
        except Exception as e:
            print(f"Ошибка при клике: {e}")

    def update_click_status(self):
        current_time = time.strftime("%H:%M:%S")
        self.status_var.set(
            f"✅ КУРСОР АКТИВНО ШЕВЕЛИТСЯ! Последний клик в {current_time}. "
            f"Следующий клик через {self.click_interval_var.get()} сек."
        )

    def start_wiggling(self):
        if not self.wiggling:
            self.wiggling = True
            self.clicking = True
            
            # Блокируем настройки при запуске
            self.interval_spinbox.config(state="disabled")
            
            self.status_var.set(
                f"✅ КУРСОР АКТИВНО ШЕВЕЛИТСЯ И КЛИКАЕТ! "
                f"Интервал кликов: {self.click_interval_var.get()} сек. "
                f"Для остановки нажмите КРАСНУЮ КНОПКУ ниже."
            )
            
            self.start_button.config(state="disabled", bg="#6c757d")
            self.stop_button.config(state="normal", bg="#dc3545")
            
            # Запускаем поток
            thread = threading.Thread(target=self.wiggle_mouse)
            thread.daemon = True
            thread.start()

    def stop_wiggling(self):
        self.wiggling = False
        self.clicking = False
        
        # Разблокируем настройки
        self.interval_spinbox.config(state="normal")
        
        self.status_var.set(
            "⏹ Движение и клики успешно остановлены. Система в безопасности!")
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