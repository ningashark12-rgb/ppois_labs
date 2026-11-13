"""Domain model for SearchEngine."""

class SearchEngine:
    """Represents a SearchEngine."""

    def __init__(self, query=None, results=None) -> None:
        self.query = query
        self.results = results

    def search_by_title(self) -> None:
        """Behavior for SearchEngine search_by_title."""
        pass

    def search_by_author(self) -> None:
        """Behavior for SearchEngine search_by_author."""
        pass

    def filter(self) -> None:
        """Behavior for SearchEngine filter."""
        pass

