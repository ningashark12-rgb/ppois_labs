"""Domain model for Cargo."""

class Cargo:
    """Represents a Cargo."""

    def __init__(self, weight=None, volume=None, description=None, is_fragile=None) -> None:
        self.weight = weight
        self.volume = volume
        self.description = description
        self.is_fragile = is_fragile

    def calculate_cost(self) -> None:
        """Behavior for Cargo calculate_cost."""
        pass

    def validate_weight(self) -> None:
        """Behavior for Cargo validate_weight."""
        pass

    def get_description(self) -> None:
        """Behavior for Cargo get_description."""
        pass

