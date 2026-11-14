"""Domain model for Receipt."""

class Receipt:
    """Represents a Receipt."""

    def __init__(self, receipt_id=None, amount=None, date=None) -> None:
        self.receipt_id = receipt_id
        self.amount = amount
        self.date = date

    def print_receipt(self) -> None:
        """Behavior for Receipt print_receipt."""
        pass

    def get_details(self) -> None:
        """Behavior for Receipt get_details."""
        pass

