"""Domain model for Fine."""

class Fine:
    """Represents a Fine."""

    def __init__(self, amount=None, reason=None, is_paid=None) -> None:
        self.amount = amount
        self.reason = reason
        self.is_paid = is_paid

    def pay(self) -> None:
        """Behavior for Fine pay."""
        pass

    def waive(self) -> None:
        """Behavior for Fine waive."""
        pass

    def get_receipt(self) -> None:
        """Behavior for Fine get_receipt."""
        pass

