"""Domain model for Publisher."""

class Publisher:
    """Represents a Publisher."""

    def __init__(self, name: str, address=None, contact_info=None) -> None:
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def publish(self) -> None:
        """Behavior for Publisher publish."""
        pass

    def get_contact(self) -> None:
        """Behavior for Publisher get_contact."""
        pass

