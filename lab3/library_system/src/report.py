"""Domain model for Report."""

class Report:
    """Represents a Report."""

    def __init__(self, report_id=None, date_generated=None, content=None) -> None:
        self.report_id = report_id
        self.date_generated = date_generated
        self.content = content

    def generate(self) -> None:
        """Behavior for Report generate."""
        pass

    def export_pdf(self) -> None:
        """Behavior for Report export_pdf."""
        pass

