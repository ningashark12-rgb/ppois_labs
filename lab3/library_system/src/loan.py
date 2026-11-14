"""Domain model for Loan."""

from __future__ import annotations
from .exceptions import LoanExpiredException

class Loan:
    """Represents a borrowing transaction."""

    def __init__(self, loan_id: str, book=None, member=None, issue_date: str = None, due_date: str = None) -> None:
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.due_date = due_date
        self.is_returned = False

    def extend_loan(self, extra_days: int) -> None:
        """Extend the due date."""
        pass

    def calculate_fine(self, days_late: int) -> float:
        """Calculate a fine for late returns."""
        return days_late * 1.5

    def complete_loan(self) -> None:
        """Mark the loan as finished."""
        self.is_returned = True
        if self.member and self.book:
            self.member.return_book(self.book)