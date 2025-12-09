def find_short(s):
    words = s.split()  # Разбиваем строку на слова
    min_length = min(len(word) for word in words)  # Находим минимальную длину
    short_words = [word for word in words if len(word) == min_length]  # Все слова такой длины
    return min_length, short_words

# Пример использования
s = "bitcoin take over the world maybe who knows perhaps"
length, words = find_short(s)

print(f"Самая короткая длина: {length}")
print(f"Слова с этой длиной: {words}")


   


