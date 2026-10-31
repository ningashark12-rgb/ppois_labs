"""Domain model for Van."""

class Van:
    """Represents a Van."""

    def __init__(self, max_volume=None, sliding_door=None) -> None:
        self.max_volume = max_volume
        self.sliding_door = sliding_door

    def open_door(self) -> None:
        """Behavior for Van open_door."""
        pass

    def load_packages(self) -> None:
        """Behavior for Van load_packages."""
        pass

    def deliver_parcel(self) -> None:
        """Behavior for Van deliver_parcel."""
        pass

    def refuel(self) -> None:
        """Behavior for Van refuel."""
        pass

