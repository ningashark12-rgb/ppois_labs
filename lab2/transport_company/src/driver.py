"""Domain model for Driver."""

from __future__ import annotations
from .exceptions import DriverNotAvailableException

class Driver:
    """Represents a Driver."""

    def __init__(self, name: str, license=None, is_available: bool = True, experience_years=0, rating=5.0) -> None:
        self.name = name
        self.license = license
        self.is_available = is_available
        self.experience_years = experience_years
        self.rating = rating

    def accept_order(self) -> None:
        """Driver accepts an order, making them unavailable."""
        if not self.is_available:
            raise DriverNotAvailableException(f"Driver {self.name} is already on a delivery.")
        self.is_available = False

    def decline_order(self) -> None:
        """Driver declines, status remains unchanged."""
        pass

    def update_status(self, available: bool) -> None:
        """Manually update driver availability."""
        self.is_available = available

    def get_rating(self) -> float:
        return self.rating