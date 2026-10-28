"""Domain model for TrackingSystem."""

class TrackingSystem:
    """Represents a TrackingSystem."""

    def __init__(self, active_trackings=None, history=None) -> None:
        self.active_trackings = active_trackings
        self.history = history

    def start_tracking(self) -> None:
        """Behavior for TrackingSystem start_tracking."""
        pass

    def update_location(self) -> None:
        """Behavior for TrackingSystem update_location."""
        pass

    def stop_tracking(self) -> None:
        """Behavior for TrackingSystem stop_tracking."""
        pass

    def get_history(self) -> None:
        """Behavior for TrackingSystem get_history."""
        pass

