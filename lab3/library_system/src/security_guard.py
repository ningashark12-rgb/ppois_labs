"""Domain model for SecurityGuard."""

class SecurityGuard:
    """Represents a SecurityGuard."""

    def __init__(self, badge_number=None, patrol_area=None) -> None:
        self.badge_number = badge_number
        self.patrol_area = patrol_area

    def patrol(self) -> None:
        """Behavior for SecurityGuard patrol."""
        pass

    def check_id(self) -> None:
        """Behavior for SecurityGuard check_id."""
        pass

