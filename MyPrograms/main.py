import os
import requests


DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

url = "https://rus.hitmotop.com/search?q=free%20flow%20flava"

response = requests.get(url, stream=True)

if response.status_code == 200:
    # Попробуем получить имя файла из Content-Disposition
    content_disposition = response.headers.get('Content-Disposition')
    filename = "трек.mp3"  # значение по умолчанию

    if content_disposition:
        # Извлекаем имя файла из строки вида: attachment; filename="example.mp3"
        import re
        match = re.search(r'filename="?(.+)"?', content_disposition)
        if match:
            filename = match.group(1)

    file_path = os.path.join(DOWNLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print(f"✅ Трек успешно скачан и сохранён как: {file_path}")
else:
    print("❌ Ошибка: файл не найден или доступ запрещён")
