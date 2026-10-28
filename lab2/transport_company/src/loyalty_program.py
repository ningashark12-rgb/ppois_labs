"""Domain model for LoyaltyProgram."""

class LoyaltyProgram:
    """Represents a LoyaltyProgram."""

    def __init__(self, points=None, tier=None) -> None:
        self.points = points
        self.tier = tier

    def add_points(self) -> None:
        """Behavior for LoyaltyProgram add_points."""
        pass

    def redeem_points(self) -> None:
        """Behavior for LoyaltyProgram redeem_points."""
        pass

    def upgrade_tier(self) -> None:
        """Behavior for LoyaltyProgram upgrade_tier."""
        pass

