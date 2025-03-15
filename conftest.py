import pytest
from models import Book, Library


@pytest.fixture(scope="function")
def library():
    return Library("Central Library")


@pytest.fixture(scope="function")
def book():
    return Book("Harper Lee", "To Kill a Mockingbird")


@pytest.fixture(scope="function")
def another_book():
    return Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone")
