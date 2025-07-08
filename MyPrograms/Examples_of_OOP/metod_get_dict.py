# _______________________________________________

from data_sandbox import get_random_books
books = get_random_books() # [{'title': 'Шерлок Холмс: Этюд в багровых тонах', 'author': 'Артур Конан Дойл'}, ...]
for i in books:
    print(f"Автор: {i.get("author", "Неизвестен")}")
    print(f'Название произведения - "{i.get("title", "Неизвестно")}"')
    print(f"Год выпуска: - {i.get("year", "Неизвестен")}")
    print(f"Издатель: - {i.get("publisher", "Неизвестен")}")

# ________________________________________________
from data_sandbox import get_random_books

books = get_random_books()
info_en = ['title', 'author', 'year', 'publisher']
info_ru = ['Название', 'Автор', 'Год', 'Издательство']

for book in books:
    for en, ru in zip(info_en, info_ru):
        print(f"{ru}: {book.get(en, 'Неизвестно')}")
    print()

# ________________________________________________

from data_sandbox import get_random_books

books = get_random_books()
info = {
    'title': 'Название', 
    'author': 'Автор', 
    'year': 'Год', 
    'publisher': 'Издательство'
}

for book in books:
    for en, ru in info.items():
        print(f"{ru}: {book.get(en, 'Неизвестно')}")
    print()

# В классе________________________________________________

from data_sandbox import get_random_books

class BookInfoPrinter:
    def __init__(self):
        self.books = get_random_books()
        self.field_translations = {
            'title': 'Название',
            'author': 'Автор',
            'year': 'Год',
            'publisher': 'Издательство'
        }
    
    def print_book_info(self, book):
        """Печатает информацию об одной книге"""
        for field, label in self.field_translations.items():
            print(f"{label}: {book.get(field, 'Неизвестно')}")
        print()  # Пустая строка между книгами
    
    def print_all_books(self):
        """Печатает информацию о всех книгах"""
        for book in self.books:
            self.print_book_info(book)

# Использование класса
printer = BookInfoPrinter()
printer.print_all_books()

