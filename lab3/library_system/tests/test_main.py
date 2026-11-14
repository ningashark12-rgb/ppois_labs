"""Unit tests for the CLI main.py."""

from unittest.mock import patch
from src.main import main, _add_book, _register_member, _borrow_book, _return_book
from src.library import Library
from src.exceptions import LibraryException


def _feed(*inputs):
    """Return a fake input() that yields each string once."""
    iterator = iter(inputs)
    return lambda _prompt="": next(iterator)


def test_main_exit_immediately(capsys):
    with patch("builtins.input", _feed("0")):
        main()
    out = capsys.readouterr().out
    assert "Goodbye!" in out


def test_add_book_menu(capsys):
    library = Library("Test")
    with patch("builtins.input", _feed("123", "Title", "Author")):
        _add_book(library)
    assert len(library.catalog) == 1
    assert library.catalog[0].title == "Title"


def test_register_member_menu(capsys):
    library = Library("Test")
    with patch("builtins.input", _feed("M1", "John")):
        _register_member(library)
    assert len(library.members) == 1
    assert library.members[0].name == "John"


def test_borrow_book_menu_success(capsys):
    library = Library("Test")
    _add_book_helper(library, "123")
    _register_member_helper(library, "M1")
    with patch("builtins.input", _feed("M1", "123")):
        _borrow_book(library)
    out = capsys.readouterr().out
    assert "borrowed successfully" in out


def test_borrow_book_menu_fails(capsys):
    library = Library("Test")
    _register_member_helper(library, "M1")
    with patch("builtins.input", _feed("M1", "999")):  # Book 999 doesn't exist
        _borrow_book(library)
    out = capsys.readouterr().out
    assert "Error" in out


def test_return_book_menu(capsys):
    library = Library("Test")
    _add_book_helper(library, "123")
    _register_member_helper(library, "M1")
    library.process_loan("M1", "123")
    with patch("builtins.input", _feed("M1", "123")):
        _return_book(library)
    out = capsys.readouterr().out
    assert "Book returned" in out


def test_main_invalid_choice(capsys):
    with patch("builtins.input", _feed("99", "0")):
        main()
    out = capsys.readouterr().out
    assert "Invalid choice" in out


# Helper functions to avoid repeating setup
def _add_book_helper(library, isbn):
    from src.book import Book
    library.add_book(Book(isbn=isbn, title="Title"))

def _register_member_helper(library, m_id):
    from src.member import Member
    library.register_member(Member(member_id=m_id, name="John"))
