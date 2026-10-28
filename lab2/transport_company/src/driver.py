"""Domain model for Driver."""

class Driver:
    """Represents a Driver."""

    def __init__(self, name: str, license=None, is_available=None, experience_years=None, rating=None) -> None:
        self.name = name
        self.license = license
        self.is_available = is_available
        self.experience_years = experience_years
        self.rating = rating

    def accept_order(self) -> None:
        """Behavior for Driver accept_order."""
        pass

    def decline_order(self) -> None:
        """Behavior for Driver decline_order."""
        pass

    def update_status(self) -> None:
        """Behavior for Driver update_status."""
        pass

    def get_rating(self) -> None:
        """Behavior for Driver get_rating."""
        pass

