"""Domain model for Review."""

class Review:
    """Represents a Review."""

    def __init__(self, rating=None, comment=None, date=None) -> None:
        self.rating = rating
        self.comment = comment
        self.date = date

    def submit(self) -> None:
        """Behavior for Review submit."""
        pass

    def edit_review(self) -> None:
        """Behavior for Review edit_review."""
        pass

