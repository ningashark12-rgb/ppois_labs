"""Domain model for Payment."""

class Payment:
    """Represents a Payment."""

    def __init__(self, amount=None, payment_method=None, date=None, is_successful=None) -> None:
        self.amount = amount
        self.payment_method = payment_method
        self.date = date
        self.is_successful = is_successful

    def process_payment(self) -> None:
        """Behavior for Payment process_payment."""
        pass

    def refund(self) -> None:
        """Behavior for Payment refund."""
        pass

    def validate_card(self) -> None:
        """Behavior for Payment validate_card."""
        pass

    def get_receipt(self) -> None:
        """Behavior for Payment get_receipt."""
        pass

