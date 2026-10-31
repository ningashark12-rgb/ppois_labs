"""Domain model for PerformanceMetric."""

class PerformanceMetric:
    """Represents a PerformanceMetric."""

    def __init__(self, metric_name=None, value=None, unit=None) -> None:
        self.metric_name = metric_name
        self.value = value
        self.unit = unit

    def update_value(self) -> None:
        """Behavior for PerformanceMetric update_value."""
        pass

    def compare(self) -> None:
        """Behavior for PerformanceMetric compare."""
        pass

    def get_status(self) -> None:
        """Behavior for PerformanceMetric get_status."""
        pass

