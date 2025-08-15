import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Автоматически устанавливаем chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL поиска
url = "https://rus.hitmotop.com/search?q=free%20flow%20flava"

try:
    driver.get(url)
    print("⏳ Ждём загрузки страницы...")
    time.sleep(10)  # Ожидаем загрузку JS-контента

    # Получаем HTML после выполнения JS
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Ищем элементы с треками
    # Может отличаться — проверьте структуру!
    tracks = soup.find_all('div', class_='track-item')

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
