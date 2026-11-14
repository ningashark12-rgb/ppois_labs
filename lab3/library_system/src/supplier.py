"""Domain model for Supplier."""

class Supplier:
    """Represents a Supplier."""

    def __init__(self, name: str, contact_person=None) -> None:
        self.name = name
        self.contact_person = contact_person

    def supply_books(self) -> None:
        """Behavior for Supplier supply_books."""
        pass

    def get_catalog(self) -> None:
        """Behavior for Supplier get_catalog."""
        pass

