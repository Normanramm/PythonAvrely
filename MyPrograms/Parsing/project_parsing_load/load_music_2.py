import os
import time
import requests
from bs4 import BeautifulSoup

# Проверяем установку необходимых библиотек
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
except ImportError as e:
    print(f"❌ Ошибка импорта Selenium: {e}")
    print("Установите: pip install selenium")
    exit(1)

try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("❌ Установите webdriver-manager: pip install webdriver-manager")
    exit(1)

try:
    from tqdm import tqdm
except ImportError:
    print("❌ Установите tqdm: pip install tqdm")
    exit(1)

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

# Автоматически устанавливаем chromedriver с обработкой ошибок
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("✅ Chrome WebDriver успешно инициализирован")
except Exception as e:
    print(f"❌ Ошибка инициализации Chrome: {e}")
    print("Убедитесь, что Chrome браузер установлен")
    exit(1)

# URL для входа и поиска
login_url = "https://rus.hitmotop.com/login"
search_url = "https://rus.hitmotop.com/search?q=free%20flow%20flava"

# Получаем учетные данные из переменных окружения или используем placeholder'ы
username = os.getenv("HITMOTOP_USERNAME", "ваш_логин")
password = os.getenv("HITMOTOP_PASSWORD", "ваш_пароль")

# Проверяем, что учетные данные не являются placeholder'ами
if username == "ваш_логин" or password == "ваш_пароль":
    print("⚠️  ВНИМАНИЕ: Используются placeholder'ы для логина и пароля!")
    print("Установите переменные окружения HITMOTOP_USERNAME и HITMOTOP_PASSWORD")
    print("Или замените значения в коде на реальные данные")

try:
    # Переходим на страницу логина
    driver.get(login_url)
    print("⏳ Открываем страницу входа...")

    # Вводим логин и пароль
    try:
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        email_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()
        print("✅ Данные для входа введены")
    except Exception as e:
        print(f"❌ Ошибка при вводе данных: {e}")
        print("Возможно, изменилась структура страницы входа")

    print("⏳ Ждём загрузки страницы после входа...")
    time.sleep(5)  # Дайте время на обработку формы

    # Теперь переходим на страницу поиска
    driver.get(search_url)
    print("⏳ Ждём загрузки страницы с треками...")
    time.sleep(10)  # Ожидаем JS-контент

    # Получаем HTML после выполнения JS
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Анализируем структуру страницы для диагностики
    print("🔍 Анализируем структуру страницы...")
    all_divs = soup.find_all('div')
    print(f"Найдено {len(all_divs)} div элементов")
    
    # Выводим первые несколько классов для анализа
    classes = set()
    for div in all_divs[:20]:
        if div.get('class'):
            classes.update(div.get('class'))
    print(f"Найденные классы (первые 20): {list(classes)[:20]}")

    # Ищем элементы с треками - пробуем разные селекторы
    tracks = []
    possible_selectors = [
        'div.track-item',
        'div.track',
        'div.song-item',
        'div.music-item',
        'div[class*="track"]',
        'div[class*="song"]',
        'div[class*="music"]'
    ]
    
    for selector in possible_selectors:
        try:
            tracks = soup.select(selector)
            if tracks:
                print(f"✅ Найдены треки с селектором: {selector}")
                break
        except:
            continue
    
    # Если не нашли по селекторам, ищем по содержимому
    if not tracks:
        print("🔍 Ищем треки по содержимому...")
        # Ищем div'ы, которые могут содержать информацию о треках
        for div in all_divs:
            text = div.get_text().lower()
            if any(keyword in text for keyword in ['трек', 'песня', 'музыка', 'song', 'track', 'music']):
                tracks.append(div)
                if len(tracks) >= 5:  # Ограничиваем поиск
                    break

    if not tracks:
        print("❌ Нет найденных треков.")
        print("Возможные причины:")
        print("1. Изменилась структура сайта")
        print("2. Требуется авторизация")
        print("3. Сайт блокирует автоматизированный доступ")
        
        # Сохраняем HTML для анализа
        debug_file = os.path.join(DOWNLOAD_DIR, "debug_page.html")
        with open(debug_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"📄 HTML страницы сохранен в {debug_file} для анализа")
    else:
        print(f"✅ Найдено {len(tracks)} треков.")

        for i, track in enumerate(tracks):
            # Ищем заголовок и исполнителя разными способами
            title = None
            artist = None
            
            # Пробуем разные селекторы для заголовка
            title_selectors = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'span', 'div']
            for selector in title_selectors:
                title = track.find(selector)
                if title and title.get_text().strip():
                    break
            
            # Пробуем разные селекторы для исполнителя
            artist_selectors = ['p', 'span', 'div', 'a']
            for selector in artist_selectors:
                artist = track.find(selector)
                if artist and artist.get_text().strip() and artist != title:
                    break

            title_text = title.get_text().strip() if title else f"трек_{i+1}"
            artist_text = artist.get_text().strip() if artist else "Неизвестен"

            print(f"\n{i + 1}. {title_text} - {artist_text}")

            # Ищем ссылку на аудио разными способами
            audio_src = None
            
            # Способ 1: тег audio
            audio_tag = track.find('audio')
            if audio_tag:
                audio_src = audio_tag.get('src')
            
            # Способ 2: ссылка с расширением аудио
            if not audio_src:
                audio_links = track.find_all('a', href=True)
                for link in audio_links:
                    href = link['href']
                    if any(ext in href.lower() for ext in ['.mp3', '.wav', '.ogg', '.m4a']):
                        audio_src = href
                        break
            
            # Способ 3: data-атрибуты
            if not audio_src:
                for attr in track.attrs:
                    if 'src' in attr.lower() or 'url' in attr.lower():
                        audio_src = track.get(attr)
                        break

            if audio_src:
                if not audio_src.startswith('http'):
                    audio_src = "https://rus.hitmotop.com" + audio_src

                filename = os.path.basename(audio_src)
                if not filename or '.' not in filename:
                    filename = f"track_{i+1}.mp3"
                
                file_path = os.path.join(DOWNLOAD_DIR, f"{i+1}_{filename}")

                print(f"Скачиваю: {audio_src}")
                try:
                    response = requests.get(audio_src, stream=True, timeout=30)
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
                        print(f"❌ Не удалось скачать трек: {audio_src} (код: {response.status_code})")
                except Exception as e:
                    print(f"❌ Ошибка при скачивании: {e}")
            else:
                print("❌ Нет ссылки на аудио.")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")
    import traceback
    traceback.print_exc()

finally:
    try:
        driver.quit()
        print("✅ WebDriver закрыт")
    except:
        pass
