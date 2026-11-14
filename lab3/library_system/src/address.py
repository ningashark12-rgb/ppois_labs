"""Domain model for Address."""

class Address:
    """Represents a Address."""

    def __init__(self, street=None, city=None, zip_code=None, country=None) -> None:
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country

    def validate(self) -> None:
        """Behavior for Address validate."""
        pass

    def to_string(self) -> None:
        """Behavior for Address to_string."""
        pass

