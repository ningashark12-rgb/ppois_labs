"""Domain model for Procurement."""

class Procurement:
    """Represents a Procurement."""

    def __init__(self, supplier=None, order_date=None) -> None:
        self.supplier = supplier
        self.order_date = order_date

    def order_books(self) -> None:
        """Behavior for Procurement order_books."""
        pass

    def track_delivery(self) -> None:
        """Behavior for Procurement track_delivery."""
        pass

