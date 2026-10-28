"""Domain model for Rack."""

class Rack:
    """Represents a Rack."""

    def __init__(self, rack_id: str, max_weight=None, shelf_count=None) -> None:
        self.rack_id = rack_id
        self.max_weight = max_weight
        self.shelf_count = shelf_count

    def store_item(self) -> None:
        """Behavior for Rack store_item."""
        pass

    def retrieve_item(self) -> None:
        """Behavior for Rack retrieve_item."""
        pass

    def check_weight_limit(self) -> None:
        """Behavior for Rack check_weight_limit."""
        pass

