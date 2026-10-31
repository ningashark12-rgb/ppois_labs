"""Domain model for Order."""

from __future__ import annotations
from .driver import Driver
from .vehicle import Vehicle

class Order:
    """Represents an Order."""

    def __init__(self, order_id: str, client=None, cargo=None, driver=None, vehicle=None, status="Pending", price=0.0) -> None:
        self.order_id = order_id
        self.client = client
        self.cargo = cargo
        self.driver = driver
        self.vehicle = vehicle
        self.status = status
        self.price = price

    def assign_driver(self, driver: Driver) -> None:
        """Assign a driver to this order."""
        driver.accept_order()
        self.driver = driver

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        """Assign a vehicle to this order."""
        vehicle.start()
        self.vehicle = vehicle

    def calculate_price(self, base_rate: float = 10.0) -> float:
        """Calculate price based on cargo weight (if cargo is set)."""
        if self.cargo:
            self.price = base_rate * getattr(self.cargo, 'weight', 1)
        else:
            self.price = base_rate
        return self.price

    def complete_order(self) -> None:
        """Mark the order as complete and free up driver and vehicle."""
        self.status = "Completed"
        if self.driver:
            self.driver.update_status(True)
        if self.vehicle:
            self.vehicle.stop()

    def cancel_order(self) -> None:
        self.status = "Cancelled"