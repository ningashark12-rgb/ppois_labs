"""Domain model for Vehicle."""

from __future__ import annotations
from .exceptions import VehicleNotAvailableException

class Vehicle:
    """Represents a Vehicle."""

    def __init__(self, plate_number: str, brand=None, model=None, year=None, is_available: bool = True, mileage=0) -> None:
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available = is_available
        self.mileage = mileage

    def start(self) -> None:
        """Vehicle starts moving, becoming unavailable."""
        if not self.is_available:
            raise VehicleNotAvailableException(f"Vehicle {self.plate_number} is already in use.")
        self.is_available = False

    def stop(self) -> None:
        """Vehicle finishes moving, becoming available."""
        self.is_available = True

    def refuel(self) -> None:
        pass

    def schedule_maintenance(self) -> None:
        self.is_available = False

    def update_mileage(self, km: int) -> None:
        self.mileage += km