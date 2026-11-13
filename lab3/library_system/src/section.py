"""Domain model for Section."""

class Section:
    """Represents a Section."""

    def __init__(self, section_name=None, shelves=None) -> None:
        self.section_name = section_name
        self.shelves = shelves

    def add_shelf(self) -> None:
        """Behavior for Section add_shelf."""
        pass

    def get_shelf(self) -> None:
        """Behavior for Section get_shelf."""
        pass

