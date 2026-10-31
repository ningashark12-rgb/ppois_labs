"""Domain model for Client."""

class Client:
    """Represents a Client."""

    def __init__(self, name: str, phone=None, email=None) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def place_order(self) -> None:
        """Behavior for Client place_order."""
        pass

    def make_payment(self) -> None:
        """Behavior for Client make_payment."""
        pass

    def get_contact_info(self) -> None:
        """Behavior for Client get_contact_info."""
        pass

    def update_details(self) -> None:
        """Behavior for Client update_details."""
        pass

