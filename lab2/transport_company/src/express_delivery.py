"""Domain model for ExpressDelivery."""

class ExpressDelivery:
    """Represents a ExpressDelivery."""

    def __init__(self, speed_priority=None, guaranteed_time=None, extra_fee=None, order=None) -> None:
        self.speed_priority = speed_priority
        self.guaranteed_time = guaranteed_time
        self.extra_fee = extra_fee
        self.order = order

    def upgrade_speed(self) -> None:
        """Behavior for ExpressDelivery upgrade_speed."""
        pass

    def calculate_extra_cost(self) -> None:
        """Behavior for ExpressDelivery calculate_extra_cost."""
        pass

    def track_eta(self) -> None:
        """Behavior for ExpressDelivery track_eta."""
        pass

