"""Domain model for Truck."""

class Truck:
    """Represents a Truck."""

    def __init__(self, max_weight=None, axles=None) -> None:
        self.max_weight = max_weight
        self.axles = axles

    def start_engine(self) -> None:
        """Behavior for Truck start_engine."""
        pass

    def stop_engine(self) -> None:
        """Behavior for Truck stop_engine."""
        pass

    def load_cargo(self) -> None:
        """Behavior for Truck load_cargo."""
        pass

    def unload_cargo(self) -> None:
        """Behavior for Truck unload_cargo."""
        pass

