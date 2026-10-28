"""Domain model for Route."""

class Route:
    """Represents a Route."""

    def __init__(self, start_address=None, end_address=None, distance_km=None, estimated_time=None) -> None:
        self.start_address = start_address
        self.end_address = end_address
        self.distance_km = distance_km
        self.estimated_time = estimated_time

    def calculate_distance(self) -> None:
        """Behavior for Route calculate_distance."""
        pass

    def optimize_for_traffic(self) -> None:
        """Behavior for Route optimize_for_traffic."""
        pass

    def get_eta(self) -> None:
        """Behavior for Route get_eta."""
        pass

    def add_waypoint(self) -> None:
        """Behavior for Route add_waypoint."""
        pass

