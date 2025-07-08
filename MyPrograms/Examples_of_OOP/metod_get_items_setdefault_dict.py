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

# Еще в классе ________________________________________________

from data_sandbox import get_random_books

class Book:
    def __init__(self):
        self.books = get_random_books()
        self.info = {
            'title': 'Название',
            'author': 'Автор',
            'year': 'Год',
            'publisher': 'Издательство'
        }

    def __str__(self):
        """Возвращает строковое представление всех книг"""
        result = []
        for book in self.books:
            book_info = []
            for en, ru in self.info.items():
                book_info.append(f"{ru}: {book.get(en, 'Неизвестно')}")
            result.append('\n'.join(book_info))
        return '\n\n'.join(result)

    def print_books(self):
        """Печатает информацию о всех книгах"""
        print(self.__str__())


if __name__ == '__main__':
    book_collection = Book()
    book_collection.print_books()


# Посчитать сколько одинаковых книг в списке______________________

from data_sandbox import get_random_search_queries

# Получаем список запросов
queries = get_random_search_queries()

# Создаем словарь для подсчета
query_counts = {}

# Подсчитываем количество каждого запроса
for query in queries:
    query_counts[query] = query_counts.get(query, 0) + 1

# Выводим результаты (необязательно для проверки)
for query, count in query_counts.items():
    print(f"Запрос '{query}' встречается {count} раз(а)")


# В классе посчитать сколько одинаковых книг в словаре____________________

from data_sandbox import get_random_search_queries


class QueryClass:
    def __init__(self):
        self.queries = get_random_search_queries()
        self.my_dict = {}

    def get_queries(self):
        for query in self.queries:
            self.my_dict[query] = self.my_dict.get(query, 0) + 1

    def get_dict(self):
        for query, count in self.my_dict.items():
            print(f"Запрос: ({query}) - {count} шт.")


if __name__ == '__main__':
    query_class = QueryClass()
    query_class.get_queries()
    query_class.get_dict()

# Еще вариант колличества одинаковых книг_____________________________

from data_sandbox import get_random_search_queries

queries = get_random_search_queries()
my_dict = {}

for query in queries:
    my_dict.setdefault(query, 0)
    my_dict[query] += 1

print(query)
