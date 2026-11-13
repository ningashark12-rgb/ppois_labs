"""Domain model for Notification."""

class Notification:
    """Represents a Notification."""

    def __init__(self, message=None, recipient=None, is_read=None) -> None:
        self.message = message
        self.recipient = recipient
        self.is_read = is_read

    def send(self) -> None:
        """Behavior for Notification send."""
        pass

    def mark_read(self) -> None:
        """Behavior for Notification mark_read."""
        pass

