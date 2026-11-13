"""Domain model for Staff."""

class Staff:
    """Represents a Staff."""

    def __init__(self, name: str, position=None, salary=None) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    def clock_in(self) -> None:
        """Behavior for Staff clock_in."""
        pass

    def clock_out(self) -> None:
        """Behavior for Staff clock_out."""
        pass

