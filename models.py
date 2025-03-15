import uuid


class Book:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
        self.id = uuid.uuid4()

    def __str__(self):
        return f"<Book {self.title} by {self.author} - ID: {self.id}>"


class Library:
    def __str__(self):
        return f"<Library {self.name}-Books: {len(self.books)}>"

    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book_by_id(self, book_id: uuid.UUID):
        self.books = [book for book in self.books if book.id != book_id]

    def find_book_by_id(self, book_id: uuid.UUID):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
