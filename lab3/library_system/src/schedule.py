"""Domain model for Schedule."""

class Schedule:
    """Represents a Schedule."""

    def __init__(self, start_time=None, end_time=None, day=None) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def set_hours(self) -> None:
        """Behavior for Schedule set_hours."""
        pass

    def is_open(self) -> None:
        """Behavior for Schedule is_open."""
        pass

