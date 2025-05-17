from selenium import webdriver
from selenium_stealth import stealth
import time

# тут в идеале добавить классы и методы, отдельные методы для парсинга и сбора данных

options = webdriver.ChromeOptions()
options.add_argument("start-maximized") # аргумент для запуска в максимальном размере

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"]) # параметры для сайта
options.add_experimental_option('useAutomationExtension', False) # параметры для сайта
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\DIPRAJ\Programming\adclick_bot\chromedriver.exe") # тут можно удалить если в переменном окружении путь

stealth(driver, #параметры для сайта и браузера
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://bot.sannysoft.com/"
driver.get(url)
time.sleep(5)
driver.quit()