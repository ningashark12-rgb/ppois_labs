"""Domain model for MemberCard."""

class MemberCard:
    """Represents a MemberCard."""

    def __init__(self, card_number=None, expiry_date=None) -> None:
        self.card_number = card_number
        self.expiry_date = expiry_date

    def renew(self) -> None:
        """Behavior for MemberCard renew."""
        pass

    def is_valid(self) -> None:
        """Behavior for MemberCard is_valid."""
        pass

