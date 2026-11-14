"""Domain model for Budget."""

class Budget:
    """Represents a Budget."""

    def __init__(self, total_amount=None, spent_amount=None, fiscal_year=None) -> None:
        self.total_amount = total_amount
        self.spent_amount = spent_amount
        self.fiscal_year = fiscal_year

    def allocate_funds(self) -> None:
        """Behavior for Budget allocate_funds."""
        pass

    def check_balance(self) -> None:
        """Behavior for Budget check_balance."""
        pass

