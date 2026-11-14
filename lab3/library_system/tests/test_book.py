import pytest
from src.book import Book
from src.exceptions import BookAlreadyBorrowedException

def test_book_checkout():
    book = Book(isbn="1", title="Test")
    book.checkout()
    assert book.is_available is False

def test_book_checkout_fails():
    book = Book(isbn="1", title="Test", is_available=False)
    with pytest.raises(BookAlreadyBorrowedException):
        book.checkout()

def test_book_checkin():
    book = Book(isbn="1", title="Test", is_available=False)
    book.checkin()
    assert book.is_available is True

def test_book_details():
    book = Book(isbn="1", title="Test", author="Author")
    assert "Test" in book.get_details()

def test_book_update_condition():
    book=Book(isbn="1", title="Test")
    book.update_condition("Good") #this covers line 32 :) 
    