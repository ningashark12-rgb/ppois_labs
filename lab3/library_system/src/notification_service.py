"""Domain model for NotificationService."""

class NotificationService:
    """Represents a NotificationService."""

    def __init__(self, channel=None, messages_sent=None) -> None:
        self.channel = channel
        self.messages_sent = messages_sent

    def send_email(self) -> None:
        """Behavior for NotificationService send_email."""
        pass

    def send_sms(self) -> None:
        """Behavior for NotificationService send_sms."""
        pass

