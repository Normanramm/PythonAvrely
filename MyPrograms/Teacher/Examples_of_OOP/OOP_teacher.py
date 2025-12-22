# Создаём шаблон — класс Book
class Book:
    title = ""   # Атрибут (свойство) — название книги
    author = ""  # Атрибут (свойство) — автор книги

# Создаём объект (экземпляр класса Book)
book1 = Book()
book2 = Book()

# Теперь у book1 и book2 есть свои копии свойств title и author

# Присваиваем значения первому объекту
book1.title = "1984"
book1.author = "Джордж Оруэлл"

# Присваиваем значения второму объекту
book2.title = "Мастер и Маргарита"
book2.author = "Булгаков"

# Выводим данные для каждого объекта
print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)