"""Domain model for BankAccount."""

class BankAccount:
    """Represents a BankAccount."""

    def __init__(self, account_number: str, balance=None, owner_name=None, currency=None) -> None:
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.currency = currency

    def deposit(self) -> None:
        """Behavior for BankAccount deposit."""
        pass

    def withdraw(self) -> None:
        """Behavior for BankAccount withdraw."""
        pass

    def transfer(self) -> None:
        """Behavior for BankAccount transfer."""
        pass

    def get_balance(self) -> None:
        """Behavior for BankAccount get_balance."""
        pass

