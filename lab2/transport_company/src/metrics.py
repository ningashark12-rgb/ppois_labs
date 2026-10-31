"""Domain model for Metrics."""

class Metrics:
    """Represents a Metrics."""

    def __init__(self, total_distance=None, avg_speed=None, fuel_used=None, time_elapsed=None) -> None:
        self.total_distance = total_distance
        self.avg_speed = avg_speed
        self.fuel_used = fuel_used
        self.time_elapsed = time_elapsed

    def calculate_efficiency(self) -> None:
        """Behavior for Metrics calculate_efficiency."""
        pass

    def track_progress(self) -> None:
        """Behavior for Metrics track_progress."""
        pass

    def reset_metrics(self) -> None:
        """Behavior for Metrics reset_metrics."""
        pass

    def get_summary(self) -> None:
        """Behavior for Metrics get_summary."""
        pass

