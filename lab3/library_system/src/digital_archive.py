"""Domain model for DigitalArchive."""

class DigitalArchive:
    """Represents a DigitalArchive."""

    def __init__(self, file_format=None, storage_size=None) -> None:
        self.file_format = file_format
        self.storage_size = storage_size

    def upload(self) -> None:
        """Behavior for DigitalArchive upload."""
        pass

    def download(self) -> None:
        """Behavior for DigitalArchive download."""
        pass

    def compress(self) -> None:
        """Behavior for DigitalArchive compress."""
        pass

