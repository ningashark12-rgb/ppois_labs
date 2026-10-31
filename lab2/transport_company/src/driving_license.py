"""Domain model for DrivingLicense."""

class DrivingLicense:
    """Represents a DrivingLicense."""

    def __init__(self, number=None, category=None, issue_date=None, expiry_date=None) -> None:
        self.number = number
        self.category = category
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def is_valid(self) -> None:
        """Behavior for DrivingLicense is_valid."""
        pass

    def renew(self) -> None:
        """Behavior for DrivingLicense renew."""
        pass

    def get_category(self) -> None:
        """Behavior for DrivingLicense get_category."""
        pass

