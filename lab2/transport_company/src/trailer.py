"""Domain model for Trailer."""

class Trailer:
    """Represents a Trailer."""

    def __init__(self, max_weight=None, volume=None, number_of_axles=None) -> None:
        self.max_weight = max_weight
        self.volume = volume
        self.number_of_axles = number_of_axles

    def attach_to_truck(self) -> None:
        """Behavior for Trailer attach_to_truck."""
        pass

    def detach(self) -> None:
        """Behavior for Trailer detach."""
        pass

    def check_load(self) -> None:
        """Behavior for Trailer check_load."""
        pass

    def get_capacity(self) -> None:
        """Behavior for Trailer get_capacity."""
        pass

