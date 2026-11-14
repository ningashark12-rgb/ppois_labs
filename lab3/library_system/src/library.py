"""The main library class that manages catalog, members, and loans."""

from __future__ import annotations
from .member import Member
from .book import Book
from .loan import Loan
from .exceptions import BookNotFoundException, MemberNotFoundException

class Library:
    """Represents the central Library system."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.catalog: list[Book] = []
        self.members: list[Member] = []
        self.staff = []
        self.loans: list[Loan] = []

    def register_member(self, member: Member) -> None:
        self.members.append(member)

    def add_book(self, book: Book) -> None:
        self.catalog.append(book)

    def process_loan(self, member_id: str, isbn: str) -> None:
        """Process a book checkout."""
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            raise MemberNotFoundException(f"Member {member_id} not found.")
        
        book = next((b for b in self.catalog if b.isbn == isbn), None)
        if not book:
            raise BookNotFoundException(f"Book {isbn} not found.")
        
        member.borrow_book(book)
        loan = Loan(loan_id=f"L-{len(self.loans)+1}", book=book, member=member)
        self.loans.append(loan)

    def return_loan(self, member_id: str, isbn: str) -> None:
        """Process a book return."""
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
            if book:
                member.return_book(book)

    def generate_report(self) -> str:
        return f"Library '{self.name}': {len(self.catalog)} books, {len(self.members)} members, {len(self.loans)} loans."