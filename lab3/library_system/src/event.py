"""Domain model for Event."""

class Event:
    """Represents a Event."""

    def __init__(self, event_name=None, date=None, location=None) -> None:
        self.event_name = event_name
        self.date = date
        self.location = location

    def schedule(self) -> None:
        """Behavior for Event schedule."""
        pass

    def cancel_event(self) -> None:
        """Behavior for Event cancel_event."""
        pass

