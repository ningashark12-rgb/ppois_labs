"""Domain model for Janitor."""

class Janitor:
    """Represents a Janitor."""

    def __init__(self, shift=None, cleaning_supplies=None) -> None:
        self.shift = shift
        self.cleaning_supplies = cleaning_supplies

    def clean_area(self) -> None:
        """Behavior for Janitor clean_area."""
        pass

    def restock_supplies(self) -> None:
        """Behavior for Janitor restock_supplies."""
        pass

