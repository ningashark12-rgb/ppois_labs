"""Command-line interface for the Library Management System."""

from __future__ import annotations
from .library import Library
from .book import Book
from .member import Member
from .exceptions import LibraryException

MENU_OPTIONS = (
    ("1", "Add a book"),
    ("2", "Register a member"),
    ("3", "Borrow a book"),
    ("4", "Return a book"),
    ("5", "Library report"),
    ("0", "Exit"),
)

def _print_menu() -> None:
    print("\n=== Library Management ===")
    for key, label in MENU_OPTIONS:
        print(f"{key}. {label}")

def _add_book(library: Library) -> None:
    isbn = input("Book ISBN: ").strip()
    title = input("Book Title: ").strip()
    author = input("Author: ").strip()
    library.add_book(Book(isbn=isbn, title=title, author=author))
    print(f"Book '{title}' added to catalog.")

def _register_member(library: Library) -> None:
    m_id = input("Member ID: ").strip()
    name = input("Member Name: ").strip()
    library.register_member(Member(member_id=m_id, name=name))
    print(f"Member '{name}' registered.")

def _borrow_book(library: Library) -> None:
    m_id = input("Member ID: ").strip()
    isbn = input("Book ISBN: ").strip()
    try:
        library.process_loan(m_id, isbn)
        print("Book borrowed successfully.")
    except LibraryException as exc:
        print(f"Error: {exc}")

def _return_book(library: Library) -> None:
    m_id = input("Member ID: ").strip()
    isbn = input("Book ISBN: ").strip()
    library.return_loan(m_id, isbn)
    print("Book returned.")

def main() -> None:
    """Run the interactive menu."""
    library = Library("City Central Library")

    handlers = {
        "1": lambda: _add_book(library),
        "2": lambda: _register_member(library),
        "3": lambda: _borrow_book(library),
        "4": lambda: _return_book(library),
        "5": lambda: print(library.generate_report()),
    }

    while True:
        _print_menu()
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            return

        handler = handlers.get(choice)
        if handler is None:
            print("Invalid choice.")
            continue
        handler()

if __name__ == "__main__":  # pragma: no cover
    main()