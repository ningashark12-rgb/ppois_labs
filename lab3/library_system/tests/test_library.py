import pytest
from src.library import Library
from src.book import Book
from src.member import Member
from src.exceptions import BookNotFoundException, MemberNotFoundException

def test_library_add_book():
    lib = Library(name="City")
    book = Book(isbn="1", title="Test")
    lib.add_book(book)
    assert len(lib.catalog) == 1

def test_library_register_member():
    lib = Library(name="City")
    member = Member(member_id="M1", name="John")
    lib.register_member(member)
    assert len(lib.members) == 1

def test_library_process_loan():
    lib = Library(name="City")
    lib.add_book(Book(isbn="1", title="Test"))
    lib.register_member(Member(member_id="M1", name="John"))
    lib.process_loan("M1", "1")
    assert len(lib.loans) == 1

def test_library_process_loan_missing_member():
    lib = Library(name="City")
    lib.add_book(Book(isbn="1", title="Test"))
    with pytest.raises(MemberNotFoundException):
        lib.process_loan("M99", "1")

def test_library_process_loan_missing_book():
    lib = Library(name="City")
    lib.register_member(Member(member_id="M1", name="John"))
    with pytest.raises(BookNotFoundException):
        lib.process_loan("M1", "99")

def test_library_return_loan():
    lib = Library(name="City")
    lib.add_book(Book(isbn="1", title="Test"))
    lib.register_member(Member(member_id="M1", name="John"))
    lib.process_loan("M1", "1")
    lib.return_loan("M1", "1")
    # Check book returned
    member = lib.members[0]
    assert len(member.borrowed_books) == 0

def test_library_report():
    lib = Library(name="City")
    assert "City" in lib.generate_report()