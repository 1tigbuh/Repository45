import uuid


def test_create_book(book):
    assert book.author == "Harper Lee"
    assert book.title == "To Kill a Mockingbird"
    assert isinstance(book.id, uuid.UUID)


def test_create_library(library):
    assert library.name == "Central Library"
    assert len(library.books) == 0


def test_add_book(library, book):
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books[0].title == "To Kill a Mockingbird"


def test_remove_book(library, book):
    library.add_book(book)
    library.remove_book_by_id(book.id)
    assert len(library.books) == 0


def test_find_book(library, book):
    library.add_book(book)
    found_book = library.find_book_by_id(book.id)
    assert found_book is not None
    assert found_book.title == "To Kill a Mockingbird"


def test_add_multiple_books(library, book, another_book):
    library.add_book(book)
    library.add_book(another_book)
    assert len(library.books) == 2
    assert library.books[1].title == "Harry Potter and the Philosopher's Stone"
