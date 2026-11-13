import pytest
from src.member import Member
from src.book import Book
from src.exceptions import MaxBooksExceededException, FineNotPaidException

def test_member_borrow():
    member = Member(member_id="M1", name="John")
    book = Book(isbn="1", title="Test")
    member.borrow_book(book)
    assert len(member.borrowed_books) == 1
    assert book.is_available is False

def test_member_borrow_limit():
    member = Member(member_id="M1", name="John", borrowed_books=[1, 2, 3, 4, 5])
    book = Book(isbn="1", title="Test")
    with pytest.raises(MaxBooksExceededException):
        member.borrow_book(book)

def test_member_borrow_with_fines():
    member = Member(member_id="M1", name="John", fines=10.0)
    book = Book(isbn="1", title="Test")
    with pytest.raises(FineNotPaidException):
        member.borrow_book(book)

def test_member_return():
    member = Member(member_id="M1", name="John")
    book = Book(isbn="1", title="Test")
    member.borrow_book(book)
    member.return_book(book)
    assert len(member.borrowed_books) == 0
    assert book.is_available is True

def test_member_pay_fine():
    member = Member(member_id="M1", name="John", fines=10.0)
    member.pay_fine(5.0)
    assert member.fines == 5.0

def test_member_pay_fine_zero():
    member = Member(member_id="M1", name="John", fines=10.0)
    member.pay_fine(20.0)
    assert member.fines == 0.0

def test_member_reserve():
    member = Member(member_id="M1", name="John")
    member.reserve_book(None) # Just covers the pass