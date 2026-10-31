"""Domain model for PerishableCargo."""

class PerishableCargo:
    """Represents a PerishableCargo."""

    def __init__(self, expiry_time=None, temperature_required=None, spoilage_risk=None) -> None:
        self.expiry_time = expiry_time
        self.temperature_required = temperature_required
        self.spoilage_risk = spoilage_risk

    def check_temperature(self) -> None:
        """Behavior for PerishableCargo check_temperature."""
        pass

    def is_expired(self) -> None:
        """Behavior for PerishableCargo is_expired."""
        pass

    def calculate_time_left(self) -> None:
        """Behavior for PerishableCargo calculate_time_left."""
        pass

