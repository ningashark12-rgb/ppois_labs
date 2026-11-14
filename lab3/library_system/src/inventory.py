"""Domain model for Inventory."""

class Inventory:
    """Represents a Inventory."""

    def __init__(self, total_books=None, missing_books=None) -> None:
        self.total_books = total_books
        self.missing_books = missing_books

    def audit(self) -> None:
        """Behavior for Inventory audit."""
        pass

    def add_inventory(self) -> None:
        """Behavior for Inventory add_inventory."""
        pass

