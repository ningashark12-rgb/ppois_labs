"""Domain model for Restoration."""

class Restoration:
    """Represents a Restoration."""

    def __init__(self, book=None, restoration_date=None) -> None:
        self.book = book
        self.restoration_date = restoration_date

    def restore(self) -> None:
        """Behavior for Restoration restore."""
        pass

    def estimate_cost(self) -> None:
        """Behavior for Restoration estimate_cost."""
        pass

