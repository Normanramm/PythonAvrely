from selenium import webdriver
from selenium.webdriver.common.keys import Keys

''' Работа с объектами на странице, заполнение форм(вроде как удалена из селениума)'''

browser = webdriver.Chrome()
browser.get('https://youtube.com')

xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'
browser.find_element(xpath).click()

form_xpath = '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
browser.find_element(form_xpath).send_keys('test')


# скролинг, тоже не работает в селениум

browser = webdriver.Chrome()
browser.get('https://youtube.com')
html = browser.find_element('html')

for i in range(10):
    html.send_keys(keys.DOWN)

