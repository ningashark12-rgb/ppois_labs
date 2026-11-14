"""Domain model for Member."""

from __future__ import annotations
from .exceptions import MaxBooksExceededException, FineNotPaidException

class Member:
    """Represents a Library Member."""

    def __init__(self, member_id: str, name: str, email: str = None, borrowed_books=None, fines: float = 0.0) -> None:
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        self.fines = fines

    def borrow_book(self, book) -> None:
        """Borrow a book, with limits and fine checks."""
        if self.fines > 0:
            raise FineNotPaidException(f"Member {self.name} has unpaid fines.")
        if len(self.borrowed_books) >= 5:
            raise MaxBooksExceededException(f"Member {self.name} has reached the 5-book limit.")
        
        book.checkout()
        self.borrowed_books.append(book)

    def return_book(self, book) -> None:
        """Return a book to the library."""
        if book in self.borrowed_books:
            book.checkin()
            self.borrowed_books.remove(book)

    def pay_fine(self, amount: float) -> None:
        """Pay off a fine."""
        self.fines = max(0.0, self.fines - amount)

    def reserve_book(self, book) -> None:
        """Reserve a book that is currently out."""
        pass