import pyautogui
import random
import time
import keyboard  # для обнаружения нажатий клавиш

# Отключаем failsafe (осторожно! лучше оставить включённым при отладке)
# pyautogui.FAILSAFE = False

def wiggle_mouse():
    print("Шевелю мышкой! Нажмите 'Esc' чтобы остановить...")
    screen_width, screen_height = pyautogui.size()
    while True:
        # Случайное смещение
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        # Получаем текущую позицию мыши
        x, y = pyautogui.position()
        # Новая позиция
        new_x = max(0, min(screen_width - 1, x + dx))
        new_y = max(0, min(screen_height - 1, y + dy))
        # Перемещаем мышь
        pyautogui.moveTo(new_x, new_y, duration=0.01)
        # Небольшая пауза между движениями
        time.sleep(0.1)
        # Проверка: если нажат Esc — выйти
        if keyboard.is_pressed('esc'):
            print("Остановлено.")
            break

def main():
    print("Нажмите пробел, чтобы начать 'шевелить' мышкой.")
    print("Нажмите 'Esc' в любой момент, чтобы остановить.")
    keyboard.wait('space')  # ждём нажатия пробела
    wiggle_mouse()

if __name__ == "__main__":
    main()