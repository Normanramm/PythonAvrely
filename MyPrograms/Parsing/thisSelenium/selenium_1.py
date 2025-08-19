from selenium import webdriver
import time

'''Установка и основные функции
(для работы нужно скачать драйвер браузера https://googlechromelabs.github.io/chrome-for-testing/)
драйвер браузера поместить в папку с питоном или куда удобно
зайти в свойства системы - переменные среды и в системных переменных найти path и добавить путь к драйверу
https://www.selenium.dev/
'''
browser = webdriver.Chrome()
browser.get('https://www.google.com') # открыть страницу
time.sleep(2)
browser.get('https://letpy.com/handbook/string-methods/join/') # открыть страницу

# делаем скриншот
browser = webdriver.Chrome()
browser.get('https://letpy.com/handbook/string-methods/join/')
browser.save_screenshot('screenshot.png')

browser.refresh() # обновляем страницу
browser.quit() # закрываем браузер

