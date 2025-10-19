import subprocess
import sys
import importlib

def update_speedtest():
    try:
        # Обновление через pip
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "--upgrade", "speedtest-cli"
        ])
        print("✅ Speedtest успешно обновлен")
        
        # Перезагрузка модуля
        import speedtest
        importlib.reload(speedtest)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка обновления: {e}")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False

# Проверка и обновление при необходимости
def check_and_update():
    try:
        import speedtest
        print(f"Текущая версия: {getattr(speedtest, '__version__', 'Неизвестно')}")
        
        # Спросить пользователя об обновлении
        response = input("Хотите обновить speedtest? (y/n): ")
        if response.lower() == 'y':
            if update_speedtest():
                print("Обновление завершено успешно!")
            else:
                print("Не удалось обновить speedtest")
                
    except ImportError:
        print("Speedtest не установлен. Устанавливаю...")
        update_speedtest()

if __name__ == "__main__":
    check_and_update()