"""Domain model for FuelConsumption."""

class FuelConsumption:
    """Represents a FuelConsumption."""

    def __init__(self, liters_used=None, distance_covered=None, fuel_type=None) -> None:
        self.liters_used = liters_used
        self.distance_covered = distance_covered
        self.fuel_type = fuel_type

    def calculate_mpg(self) -> None:
        """Behavior for FuelConsumption calculate_mpg."""
        pass

    def estimate_cost(self) -> None:
        """Behavior for FuelConsumption estimate_cost."""
        pass

    def track_refill(self) -> None:
        """Behavior for FuelConsumption track_refill."""
        pass

