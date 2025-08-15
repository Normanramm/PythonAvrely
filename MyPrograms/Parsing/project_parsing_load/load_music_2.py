import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm


# Папка для сохранения аудио
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Настройки Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск без интерфейса
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Автоматически устанавливаем chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL для входа и поиска
login_url = "https://rus.hitmotop.com/login"
search_url = "https://rus.hitmotop.com/search?q=free%20flow%20flava"

try:
    # Переходим на страницу логина
    driver.get(login_url)
    print("⏳ Открываем страницу входа...")

    # Вводим логин и пароль
    username = "ваш_логин"
    password = "ваш_пароль"

    driver.find_element(By.NAME, "email").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    print("⏳ Ждём загрузки страницы после входа...")
    time.sleep(5)  # Дайте время на обработку формы

    # Теперь переходим на страницу поиска
    driver.get(search_url)
    print("⏳ Ждём загрузки страницы с треками...")
    time.sleep(10)  # Ожидаем JS-контент

    # Получаем HTML после выполнения JS
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Ищем элементы с треками
    tracks = soup.find_all('div', class_='track-item')  # Может отличаться — проверьте структуру!

    if not tracks:
        print("❌ Нет найденных треков.")
    else:
        print(f"✅ Найдено {len(tracks)} треков.")

        for i, track in enumerate(tracks):
            title = track.find('h3') or track.find('a')
            artist = track.find('p') or track.find('span')

            title_text = title.text.strip() if title else f"трек_{i+1}"
            artist_text = artist.text.strip() if artist else "Неизвестен"

            print(f"\n{i + 1}. {title_text} - {artist_text}")

            # Ищем ссылку на аудио
            audio_tag = track.find('audio')
            if audio_tag:
                src = audio_tag.get('src')
                if not src.startswith('http'):
                    src = "https://rus.hitmotop.com" + src

                filename = os.path.basename(src)
                file_path = os.path.join(DOWNLOAD_DIR, f"{i+1}_{filename}")

                print(f"Скачиваю: {src}")
                response = requests.get(src, stream=True)
                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    with open(file_path, 'wb') as f, tqdm(
                        desc=f"Скачивание: {title_text}",
                        total=total_size,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024
                    ) as bar:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                                bar.update(len(chunk))
                    print(f"✅ Сохранён как: {file_path}")
                else:
                    print(f"❌ Не удалось скачать трек: {src}")
            else:
                print("❌ Нет ссылки на аудио.")

finally:
    driver.quit()
