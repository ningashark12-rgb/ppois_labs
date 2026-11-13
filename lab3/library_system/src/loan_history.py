"""Domain model for LoanHistory."""

class LoanHistory:
    """Represents a LoanHistory."""

    def __init__(self, past_loans=None) -> None:
        self.past_loans = past_loans

    def add_record(self) -> None:
        """Behavior for LoanHistory add_record."""
        pass

    def get_history(self) -> None:
        """Behavior for LoanHistory get_history."""
        pass

