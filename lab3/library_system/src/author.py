"""Domain model for Author."""

class Author:
    """Represents a Author."""

    def __init__(self, name: str, biography=None, nationality=None) -> None:
        self.name = name
        self.biography = biography
        self.nationality = nationality

    def write_book(self) -> None:
        """Behavior for Author write_book."""
        pass

    def get_bio(self) -> None:
        """Behavior for Author get_bio."""
        pass

