"""Domain model for Reservation."""

class Reservation:
    """Represents a Reservation."""

    def __init__(self, reservation_id=None, book=None, member=None, status=None) -> None:
        self.reservation_id = reservation_id
        self.book = book
        self.member = member
        self.status = status

    def cancel(self) -> None:
        """Behavior for Reservation cancel."""
        pass

    def confirm(self) -> None:
        """Behavior for Reservation confirm."""
        pass

    def check_status(self) -> None:
        """Behavior for Reservation check_status."""
        pass

