"""Domain model for DVD."""

class DVD:
    """Represents a DVD."""

    def __init__(self, duration_minutes=None, age_rating=None) -> None:
        self.duration_minutes = duration_minutes
        self.age_rating = age_rating

    def play(self) -> None:
        """Behavior for DVD play."""
        pass

    def check_compatibility(self) -> None:
        """Behavior for DVD check_compatibility."""
        pass

