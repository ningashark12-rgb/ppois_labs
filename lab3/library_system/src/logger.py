"""Domain model for Logger."""

class Logger:
    """Represents a Logger."""

    def __init__(self, log_file=None, log_level=None) -> None:
        self.log_file = log_file
        self.log_level = log_level

    def log_info(self) -> None:
        """Behavior for Logger log_info."""
        pass

    def log_error(self) -> None:
        """Behavior for Logger log_error."""
        pass

