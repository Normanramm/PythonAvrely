from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

# тут в идеале добавить классы и методы, отдельные методы для парсинга и сбора данных

options = webdriver.ChromeOptions()
options.add_argument("start-maximized") # аргумент для запуска в максимальном размере

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])  # параметры для сайта
options.add_experimental_option('useAutomationExtension', False)  # параметры для сайта
driver = webdriver.Chrome(options=options)  # тут можно удалить если в переменном окружении путь

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


#
#time.sleep(5)

data = {}

for page in range(1, 3):
        url = f"https://www.russiadiscovery.ru/tours/trekkingi/page/{page}/"
        driver.get(url) # переход на страницу

        # извлекаем все блоки с категориями
        blocks = driver.find_element(By.CLASS_NAME, "cat3__list")
        posts = blocks.find_elements(By.TAG_NAME, "tour3__list-i")

        for post in posts:  # перебираем все посты
                title = post.find_element(By.CLASS_NAME, "__place").find_element(By.TAG_NAME, "a").get_attribute("href")
                title_link = post.find_element(By.CLASS_NAME, "__name").find_element(By.TAG_NAME, "a").get_attribute("href")
                price = post.find_element(By.CLASS_NAME, "tour3__price-baloon --square ").find_element(By.TAG_NAME, "div").text.replace(" ",".")
                data[title] = {
                        "url": title_link,
                        "price": price
                } # добавляем данные в словарь

for post_url in data.values(): # перебираем словарь
        #print(post_url['url'])
        driver.get(post_url['url'])


                '''# открываем запись и парсим данные
                driver.get(title_link)
                group_size = driver.find_element(By.CLASS_NAME, "tour3__values-i").text
                '''




#driver.quit()
