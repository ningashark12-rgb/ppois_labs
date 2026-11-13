"""Domain model for BookCondition."""

class BookCondition:
    """Represents a BookCondition."""

    def __init__(self, condition_level=None, notes=None) -> None:
        self.condition_level = condition_level
        self.notes = notes

    def update_condition(self) -> None:
        """Behavior for BookCondition update_condition."""
        pass

