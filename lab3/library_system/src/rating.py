"""Domain model for Rating."""

class Rating:
    """Represents a Rating."""

    def __init__(self, stars=None, reviewer=None) -> None:
        self.stars = stars
        self.reviewer = reviewer

    def calculate_average(self) -> None:
        """Behavior for Rating calculate_average."""
        pass

