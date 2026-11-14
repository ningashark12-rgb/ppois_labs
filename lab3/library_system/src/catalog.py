"""Domain model for Catalog."""

class Catalog:
    """Represents a Catalog."""

    def __init__(self, categories=None, last_updated=None) -> None:
        self.categories = categories
        self.last_updated = last_updated

    def search(self) -> None:
        """Behavior for Catalog search."""
        pass

    def sort_alphabetically(self) -> None:
        """Behavior for Catalog sort_alphabetically."""
        pass

    def filter_by_genre(self) -> None:
        """Behavior for Catalog filter_by_genre."""
        pass

