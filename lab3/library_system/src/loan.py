"""Domain model for Loan."""

class Loan:
    """Represents a Loan."""

    def __init__(self, loan_id: str, book=None, member=None, issue_date=None, due_date=None) -> None:
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.due_date = due_date

    def extend_loan(self) -> None:
        """Behavior for Loan extend_loan."""
        pass

    def calculate_fine(self) -> None:
        """Behavior for Loan calculate_fine."""
        pass

    def complete_loan(self) -> None:
        """Behavior for Loan complete_loan."""
        pass

