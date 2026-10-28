"""Domain model for Address."""

class Address:
    """Represents a Address."""

    def __init__(self, street=None, city=None, zip_code=None, country=None) -> None:
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country

    def to_string(self) -> None:
        """Behavior for Address to_string."""
        pass

    def validate_address(self) -> None:
        """Behavior for Address validate_address."""
        pass

    def get_gps(self) -> None:
        """Behavior for Address get_gps."""
        pass

    def distance_to(self) -> None:
        """Behavior for Address distance_to."""
        pass

