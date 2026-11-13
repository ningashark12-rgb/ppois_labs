"""Domain model for Librarian."""

class Librarian:
    """Represents a Librarian."""

    def __init__(self, name: str, employee_id=None, shift=None, is_available=None) -> None:
        self.name = name
        self.employee_id = employee_id
        self.shift = shift
        self.is_available = is_available

    def issue_book(self) -> None:
        """Behavior for Librarian issue_book."""
        pass

    def receive_return(self) -> None:
        """Behavior for Librarian receive_return."""
        pass

    def check_member(self) -> None:
        """Behavior for Librarian check_member."""
        pass

    def manage_shelf(self) -> None:
        """Behavior for Librarian manage_shelf."""
        pass

