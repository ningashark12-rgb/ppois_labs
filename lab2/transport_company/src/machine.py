"""Domain model for Machine."""

class Machine:
    """Represents a Machine."""

    def __init__(self, machine_id=None, type=None, status=None) -> None:
        self.machine_id = machine_id
        self.type = type
        self.status = status

    def start(self) -> None:
        """Behavior for Machine start."""
        pass

    def stop(self) -> None:
        """Behavior for Machine stop."""
        pass

    def check_status(self) -> None:
        """Behavior for Machine check_status."""
        pass

    def repair(self) -> None:
        """Behavior for Machine repair."""
        pass

