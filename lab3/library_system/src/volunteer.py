"""Domain model for Volunteer."""

class Volunteer:
    """Represents a Volunteer."""

    def __init__(self, name: str, hours_worked=None) -> None:
        self.name = name
        self.hours_worked = hours_worked

    def log_hours(self) -> None:
        """Behavior for Volunteer log_hours."""
        pass

    def assign_task(self) -> None:
        """Behavior for Volunteer assign_task."""
        pass

