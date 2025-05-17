import requests
from bs4 import BeautifulSoup

url = 'https://www.playground.ru/lord_of_the_rings_the_battle_for_middle-earth/file/maps'
responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = 'postListContainer')
block_2 = block.find_all('div', 'post-title')
print(block_2)





