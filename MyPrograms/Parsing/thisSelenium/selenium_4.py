from selenium import webdriver
import time
import pickle

# Работа с куки

# 1 сначала это делаем, тут регаемся на сайте и сохраняем куки
browser = webdriver.Firefox()
browser.get('https://www.google.com/')

time.sleep(100)

pickle.dump(browser.get_cookies(), open('cookies', 'wb'))# сохраняем куки
print('Куки сохранены')

'''
# 2 далее делаем это, нужно открыть сохраненный файл и открыть его
browser = webdriver.Firefox()
browser.get('https://www.google.com/')

for cookie in pickle.load(open('cookies', 'rb')):
    browser.add_cookie(cookie)

print('Куки загружены')
browser.get('https://www.google.com/') # или написать browser.refresh()
'''