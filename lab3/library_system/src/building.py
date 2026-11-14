"""Domain model for Building."""

class Building:
    """Represents a Building."""

    def __init__(self, building_name=None, address=None, floors=None) -> None:
        self.building_name = building_name
        self.address = address
        self.floors = floors

    def open(self) -> None:
        """Behavior for Building open."""
        pass

    def close(self) -> None:
        """Behavior for Building close."""
        pass

    def get_info(self) -> None:
        """Behavior for Building get_info."""
        pass

