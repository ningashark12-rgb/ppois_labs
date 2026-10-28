"""Domain model for TrafficInfo."""

class TrafficInfo:
    """Represents a TrafficInfo."""

    def __init__(self, severity=None, location=None, delay_minutes=None) -> None:
        self.severity = severity
        self.location = location
        self.delay_minutes = delay_minutes

    def get_delay(self) -> None:
        """Behavior for TrafficInfo get_delay."""
        pass

    def is_critical(self) -> None:
        """Behavior for TrafficInfo is_critical."""
        pass

    def suggest_alternate(self) -> None:
        """Behavior for TrafficInfo suggest_alternate."""
        pass

