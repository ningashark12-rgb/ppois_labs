"""Domain model for Vehicle."""

class Vehicle:
    """Represents a Vehicle."""

    def __init__(self, plate_number: str, brand=None, model=None, year=None, is_available=None, mileage=None) -> None:
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available = is_available
        self.mileage = mileage

    def start(self) -> None:
        """Behavior for Vehicle start."""
        pass

    def stop(self) -> None:
        """Behavior for Vehicle stop."""
        pass

    def refuel(self) -> None:
        """Behavior for Vehicle refuel."""
        pass

    def schedule_maintenance(self) -> None:
        """Behavior for Vehicle schedule_maintenance."""
        pass

    def update_mileage(self) -> None:
        """Behavior for Vehicle update_mileage."""
        pass

