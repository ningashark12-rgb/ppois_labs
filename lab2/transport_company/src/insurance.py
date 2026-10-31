"""Domain model for Insurance."""

class Insurance:
    """Represents a Insurance."""

    def __init__(self, policy_number=None, premium=None, coverage_amount=None, expiry_date=None) -> None:
        self.policy_number = policy_number
        self.premium = premium
        self.coverage_amount = coverage_amount
        self.expiry_date = expiry_date

    def file_claim(self) -> None:
        """Behavior for Insurance file_claim."""
        pass

    def calculate_premium(self) -> None:
        """Behavior for Insurance calculate_premium."""
        pass

    def renew_policy(self) -> None:
        """Behavior for Insurance renew_policy."""
        pass

