"""The main company class that manages drivers, vehicles, and orders."""

from __future__ import annotations
from .driver import Driver
from .vehicle import Vehicle
from .order import Order

class TransportCompany:
    """Represents the central transport company."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.fleet: list[Vehicle] = []
        self.employees: list[Driver] = []
        self.clients = []
        self.orders: list[Order] = []

    def hire_staff(self, driver: Driver) -> None:
        self.employees.append(driver)

    def buy_vehicle(self, vehicle: Vehicle) -> None:
        self.fleet.append(vehicle)

    def register_client(self, client) -> None:
        self.clients.append(client)

    def process_order(self, order: Order) -> None:
        """Automatically find an available driver and vehicle and assign them."""
        available_driver = next((d for d in self.employees if d.is_available), None)
        available_vehicle = next((v for v in self.fleet if v.is_available), None)

        if available_driver and available_vehicle:
            order.assign_driver(available_driver)
            order.assign_vehicle(available_vehicle)
            order.calculate_price()
            self.orders.append(order)
        else:
            raise Exception("No available drivers or vehicles for this order.")

    def generate_report(self) -> str:
        return f"Company {self.name} has {len(self.fleet)} vehicles, {len(self.employees)} drivers, and {len(self.orders)} orders."