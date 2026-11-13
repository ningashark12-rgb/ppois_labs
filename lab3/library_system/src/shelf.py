"""Domain model for Shelf."""

class Shelf:
    """Represents a Shelf."""

    def __init__(self, shelf_id=None, capacity=None, current_books=None) -> None:
        self.shelf_id = shelf_id
        self.capacity = capacity
        self.current_books = current_books

    def add_book(self) -> None:
        """Behavior for Shelf add_book."""
        pass

    def remove_book(self) -> None:
        """Behavior for Shelf remove_book."""
        pass

    def check_capacity(self) -> None:
        """Behavior for Shelf check_capacity."""
        pass

