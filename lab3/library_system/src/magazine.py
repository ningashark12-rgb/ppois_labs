"""Domain model for Magazine."""

class Magazine:
    """Represents a Magazine."""

    def __init__(self, issue_number=None, publisher=None, release_date=None) -> None:
        self.issue_number = issue_number
        self.publisher = publisher
        self.release_date = release_date

    def get_issue(self) -> None:
        """Behavior for Magazine get_issue."""
        pass

    def archive(self) -> None:
        """Behavior for Magazine archive."""
        pass

