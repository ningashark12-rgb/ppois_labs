"""Domain model for Order."""

class Order:
    """Represents a Order."""

    def __init__(self, order_id: str, client=None, cargo=None, driver=None, vehicle=None, status=None, price=None) -> None:
        self.order_id = order_id
        self.client = client
        self.cargo = cargo
        self.driver = driver
        self.vehicle = vehicle
        self.status = status
        self.price = price

    def assign_driver(self) -> None:
        """Behavior for Order assign_driver."""
        pass

    def assign_vehicle(self) -> None:
        """Behavior for Order assign_vehicle."""
        pass

    def calculate_price(self) -> None:
        """Behavior for Order calculate_price."""
        pass

    def complete_order(self) -> None:
        """Behavior for Order complete_order."""
        pass

    def cancel_order(self) -> None:
        """Behavior for Order cancel_order."""
        pass

