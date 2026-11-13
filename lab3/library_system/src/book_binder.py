"""Domain model for BookBinder."""

class BookBinder:
    """Represents a BookBinder."""

    def __init__(self, binder_name=None, materials=None) -> None:
        self.binder_name = binder_name
        self.materials = materials

    def bind_book(self) -> None:
        """Behavior for BookBinder bind_book."""
        pass

    def repair_book(self) -> None:
        """Behavior for BookBinder repair_book."""
        pass

