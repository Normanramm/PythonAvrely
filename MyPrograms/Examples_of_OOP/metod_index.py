# Вариант обычный ____________________________________________________________________________________________

# Запрашиваем у пользователя данные
sentence = input("Введите предложение: ")
old_word = input("Введите слово для поиска: ")
new_word = input("Введите слово для замены: ")

# Разбиваем предложение на список слов
words = sentence.split()

# Используем цикл while для замены всех вхождений old_word на new_word
i = 0
while i < len(words):
    if words[i] == old_word:
        words[i] = new_word
    i += 1

# Выводим изменённое предложение
print("Измененное предложение:", ' '.join(words))

# Вариант функция_____________________________________________________________________________________________

def replace_word(sentence, old_word, new_word):

    words = sentence.split()
    i = 0
    while i < len(words):
        if words[i] == old_word:
            words[i] = new_word
        i += 1
    print("Измененное предложение:", ' '.join(words))


replace_word(sentence=input("Введите предложение: "), 
             old_word=input("Введите слово для поиска: "), 
             new_word=input("Введите слово для замены: "))

# Вариант в классе____________________________________________________________________________________________

class SentenceReplacer:
    def __init__(self):
        self.sentence = ""
        self.old_word = ""
        self.new_word = ""
        self.words = []

    def get_input(self):
        """Запрашивает у пользователя данные"""
        self.sentence = input("Введите предложение: ")
        self.old_word = input("Введите слово для поиска: ")
        self.new_word = input("Введите слово для замены: ")

    def split_sentence(self):
        """Разбивает предложение на список слов"""
        self.words = self.sentence.split()

    def replace_words(self):
        """Заменяет все вхождения слова в списке"""
        i = 0
        while i < len(self.words):
            if self.words[i] == self.old_word:
                self.words[i] = self.new_word
            i += 1

    def output_result(self):
        """Выводит изменённое предложение"""
        print("Измененное предложение:", ' '.join(self.words))

# === Основная часть программы ===
if __name__ == "__main__":
    replacer = SentenceReplacer()
    replacer.get_input()
    replacer.split_sentence()
    replacer.replace_words()
    replacer.output_result()