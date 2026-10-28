"""Domain model for Manager."""

class Manager:
    """Represents a Manager."""

    def __init__(self, name: str, department=None, team_size=None) -> None:
        self.name = name
        self.department = department
        self.team_size = team_size

    def assign_task(self) -> None:
        """Behavior for Manager assign_task."""
        pass

    def review_performance(self) -> None:
        """Behavior for Manager review_performance."""
        pass

    def approve_budget(self) -> None:
        """Behavior for Manager approve_budget."""
        pass

    def conduct_meeting(self) -> None:
        """Behavior for Manager conduct_meeting."""
        pass

