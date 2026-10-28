"""Domain model for GPSPosition."""

class GPSPosition:
    """Represents a GPSPosition."""

    def __init__(self, latitude=None, longitude=None, timestamp=None) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def update_position(self) -> None:
        """Behavior for GPSPosition update_position."""
        pass

    def get_distance(self) -> None:
        """Behavior for GPSPosition get_distance."""
        pass

    def is_same_location(self) -> None:
        """Behavior for GPSPosition is_same_location."""
        pass

