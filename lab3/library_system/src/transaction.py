"""Domain model for Transaction."""

class Transaction:
    """Represents a Transaction."""

    def __init__(self, transaction_id: str, amount=None, type=None) -> None:
        self.transaction_id = transaction_id
        self.amount = amount
        self.type = type

    def process(self) -> None:
        """Behavior for Transaction process."""
        pass

    def rollback(self) -> None:
        """Behavior for Transaction rollback."""
        pass

