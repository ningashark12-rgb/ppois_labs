"""Domain model for Genre."""

class Genre:
    """Represents a Genre."""

    def __init__(self, name: str, description=None) -> None:
        self.name = name
        self.description = description

    def get_category(self) -> None:
        """Behavior for Genre get_category."""
        pass

