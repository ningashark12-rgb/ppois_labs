"""Domain model for LibraryCard."""

class LibraryCard:
    """Represents a LibraryCard."""

    def __init__(self, card_number=None, member=None) -> None:
        self.card_number = card_number
        self.member = member

    def swipe(self) -> None:
        """Behavior for LibraryCard swipe."""
        pass

    def deactivate(self) -> None:
        """Behavior for LibraryCard deactivate."""
        pass

