"""Domain model for FragileCargo."""

class FragileCargo:
    """Represents a FragileCargo."""

    def __init__(self, fragility_level=None, special_packaging=None, handling_instructions=None) -> None:
        self.fragility_level = fragility_level
        self.special_packaging = special_packaging
        self.handling_instructions = handling_instructions

    def apply_packaging(self) -> None:
        """Behavior for FragileCargo apply_packaging."""
        pass

    def warn_handler(self) -> None:
        """Behavior for FragileCargo warn_handler."""
        pass

    def charge_fragile_fee(self) -> None:
        """Behavior for FragileCargo charge_fragile_fee."""
        pass

