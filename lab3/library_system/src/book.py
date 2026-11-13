"""Domain model for Book."""

class Book:
    """Represents a Book."""

    def __init__(self, isbn: str, title: str, author=None, publisher=None, genre=None, is_available=None) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.is_available = is_available

    def checkout(self) -> None:
        """Behavior for Book checkout."""
        pass

    def checkin(self) -> None:
        """Behavior for Book checkin."""
        pass

    def get_details(self) -> None:
        """Behavior for Book get_details."""
        pass

    def update_condition(self) -> None:
        """Behavior for Book update_condition."""
        pass

