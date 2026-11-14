"""Domain model for ITTechnician."""

class ITTechnician:
    """Represents a ITTechnician."""

    def __init__(self, specialization=None, access_level=None) -> None:
        self.specialization = specialization
        self.access_level = access_level

    def fix_computer(self) -> None:
        """Behavior for ITTechnician fix_computer."""
        pass

    def install_software(self) -> None:
        """Behavior for ITTechnician install_software."""
        pass

    def backup_data(self) -> None:
        """Behavior for ITTechnician backup_data."""
        pass

