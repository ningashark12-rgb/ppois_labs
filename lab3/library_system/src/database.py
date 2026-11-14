"""Domain model for Database."""

class Database:
    """Represents a Database."""

    def __init__(self, connection_string=None, is_connected=None) -> None:
        self.connection_string = connection_string
        self.is_connected = is_connected

    def connect(self) -> None:
        """Behavior for Database connect."""
        pass

    def disconnect(self) -> None:
        """Behavior for Database disconnect."""
        pass

    def execute_query(self) -> None:
        """Behavior for Database execute_query."""
        pass

