"""Domain model for Employee."""

class Employee:
    """Represents a Employee."""

    def __init__(self, name: str, position=None, salary=None, hire_date=None) -> None:
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def work(self) -> None:
        """Behavior for Employee work."""
        pass

    def take_break(self) -> None:
        """Behavior for Employee take_break."""
        pass

    def get_payslip(self) -> None:
        """Behavior for Employee get_payslip."""
        pass

    def resign(self) -> None:
        """Behavior for Employee resign."""
        pass

