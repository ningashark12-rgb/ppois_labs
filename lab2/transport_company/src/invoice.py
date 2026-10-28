"""Domain model for Invoice."""

class Invoice:
    """Represents a Invoice."""

    def __init__(self, invoice_number=None, amount=None, issue_date=None, is_paid=None) -> None:
        self.invoice_number = invoice_number
        self.amount = amount
        self.issue_date = issue_date
        self.is_paid = is_paid

    def mark_paid(self) -> None:
        """Behavior for Invoice mark_paid."""
        pass

    def generate_pdf(self) -> None:
        """Behavior for Invoice generate_pdf."""
        pass

    def apply_discount(self) -> None:
        """Behavior for Invoice apply_discount."""
        pass

