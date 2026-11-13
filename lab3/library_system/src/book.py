"""Domain model for Book."""

from __future__ import annotations
from .exceptions import BookAlreadyBorrowedException

class Book:
    """Represents a Book in the library."""

    def __init__(self, isbn: str, title: str, author: str = None, publisher: str = None, genre: str = None, is_available: bool = True) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.is_available = is_available

    def checkout(self) -> None:
        """Mark the book as borrowed."""
        if not self.is_available:
            raise BookAlreadyBorrowedException(f"Book '{self.title}' is already borrowed.")
        self.is_available = False

    def checkin(self) -> None:
        """Mark the book as returned."""
        self.is_available = True

    def get_details(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def update_condition(self, condition: str) -> None:
        """Update the book's physical condition."""
        pass