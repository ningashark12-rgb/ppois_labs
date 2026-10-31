"""Domain model for Accountant."""

class Accountant:
    """Represents a Accountant."""

    def __init__(self, name: str, salary=None, bank_account=None, hire_date=None) -> None:
        self.name = name
        self.salary = salary
        self.bank_account = bank_account
        self.hire_date = hire_date

    def process_payment(self) -> None:
        """Behavior for Accountant process_payment."""
        pass

    def calculate_tax(self) -> None:
        """Behavior for Accountant calculate_tax."""
        pass

    def issue_invoice(self) -> None:
        """Behavior for Accountant issue_invoice."""
        pass

    def audit_books(self) -> None:
        """Behavior for Accountant audit_books."""
        pass

