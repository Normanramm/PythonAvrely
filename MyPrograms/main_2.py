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
        for en, ru in self.info.items():
            print(f"{ru}: {self.books.get(en, 'Неизвестно')}")
        print()

    def play(self):
        for book in self.books:
            print(self.__str__(book))


if __name__ == '__main__':
    for i in range(3):
        book = Book()
        book.play()

