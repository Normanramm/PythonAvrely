import qrcode
from PIL import Image

# 1. Ввод данных от пользователя
data = input("Введите текст или ссылку: ")

# 2. Создание QR-кода с увеличенной версией и высокой коррекцией ошибок
qr = qrcode.QRCode(
    version=2,  # Чуть больше места для логотипа
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Максимальная коррекция — до 30%
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# 3. Генерация изображения QR-кода
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# 4. Загрузка логотипа
logo = Image.open("logo.png")  # Убедитесь, что файл есть в той же папке

# 5. Масштаб логотипа — 20% от ширины QR-кода
qr_width, qr_height = img.size  # Получаем размеры QR-кода
logo_size = qr_width // 5  # 50% от ширины QR-кода

# изменяем размер логотипа, используя высококачественный метод ресайза LANCZOS, который дает наилучшие результаты при уменьшении изображений.
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# 6. Расчёт позиции логотипа (по центру)
logo_pos = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2
)

# 7. Вставка логотипа
img.paste(logo, logo_pos)

# 8. Сохранение результата и показ
img.save("qr_with_logo.png", quality=95)  # Добавлен параметр качества
img.show()

print("✅ QR-код с логотипом успешно создан!")
