"""Domain model for ExpenseTracker."""

class ExpenseTracker:
    """Represents a ExpenseTracker."""

    def __init__(self, total_expenses=None, categories=None) -> None:
        self.total_expenses = total_expenses
        self.categories = categories

    def add_expense(self) -> None:
        """Behavior for ExpenseTracker add_expense."""
        pass

    def get_total(self) -> None:
        """Behavior for ExpenseTracker get_total."""
        pass

    def categorize(self) -> None:
        """Behavior for ExpenseTracker categorize."""
        pass

    def export_data(self) -> None:
        """Behavior for ExpenseTracker export_data."""
        pass

