import time
from selenium import webdriver


# Юзер-Агенты, работа в фоне и обход детекта селениума
# options.add_argument("--disable-blink-features=AutomationControlled") Отключение видимости авоматизации для хрома
# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html сайт проверки браузера


''' C этим кодом можно узнать, открыт ли браузер селениумом
в Firefox ввести about:config и далее найти dom.webdriver.enabled и поставить false больше не работает'''

'''
option = webdriver.FirefoxOptions()
option.set_preference("dom.webdriver.enabled", False)
browser = webdriver.Firefox(options=option)
browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
'''


option = webdriver.FirefoxOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.set_preference("dom.webdriver.enabled", False)
option.set_preference("dom.webnotifications.enabled", False)
option.set_preference("dom.volume_scale", '0,0')
option.headless = True # для работы браузера в фоне

browser = webdriver.Firefox(options=option)
browser.get('https://nick-name.ru/generate/')


while True:
    button_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element_xpath(button_xpath).click()
    link = browser.find_element('register').get_attribute('href')[36:]
    print(f'Nickname: {link}')

# '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
# browser.find_element_by_xpath(button_xpath).click()
# link = browser.find_element_by_xpath('register').get_attribute('href')[36:]