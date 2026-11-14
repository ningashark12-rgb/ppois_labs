"""Domain model for Accountant."""

class Accountant:
    """Represents a Accountant."""

    def __init__(self, employee_id=None, tax_id=None) -> None:
        self.employee_id = employee_id
        self.tax_id = tax_id

    def calculate_taxes(self) -> None:
        """Behavior for Accountant calculate_taxes."""
        pass

    def process_payroll(self) -> None:
        """Behavior for Accountant process_payroll."""
        pass

