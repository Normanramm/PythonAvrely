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

    def play_one(self,book):
        for en, ru in self.info.items():
            print(f"{ru}: {self.book.get(en, 'Неизвестно')}")
        print()

    def play(self):
        for book in self.books:
            self.play_one(book)


if __name__ == '__main__':
   
    public = Book()
    public.play()