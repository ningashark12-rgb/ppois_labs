"""Domain model for Member."""

class Member:
    """Represents a Member."""

    def __init__(self, member_id: str, name: str, email=None, borrowed_books=None, fines=None) -> None:
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books
        self.fines = fines

    def borrow_book(self) -> None:
        """Behavior for Member borrow_book."""
        pass

    def return_book(self) -> None:
        """Behavior for Member return_book."""
        pass

    def pay_fine(self) -> None:
        """Behavior for Member pay_fine."""
        pass

    def reserve_book(self) -> None:
        """Behavior for Member reserve_book."""
        pass

