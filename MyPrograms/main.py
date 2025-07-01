# Получаем ввод от пользователя
sentence = input("Введите предложение: ")
old_word = input("Введите слово для поиска: ")
new_word = input("Введите слово для замены: ")

# Разделяем предложение на слова
words = sentence.split()

# Инициализируем индекс для цикла while
i = 0

# Используем цикл while для поиска и замены
while i < len(words):
    if old_word in words:
        index = words.index(old_word)
        words[index] = new_word
    i += 1

# Собираем предложение обратно в строку
result = ' '.join(words)

# Выводим результат
print("Измененное предложение:", result)