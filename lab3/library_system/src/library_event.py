"""Domain model for LibraryEvent."""

class LibraryEvent:
    """Represents a LibraryEvent."""

    def __init__(self, event_type=None, attendees=None) -> None:
        self.event_type = event_type
        self.attendees = attendees

    def register_attendee(self) -> None:
        """Behavior for LibraryEvent register_attendee."""
        pass

    def cancel_event(self) -> None:
        """Behavior for LibraryEvent cancel_event."""
        pass

