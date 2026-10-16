"""A single rule (command) in a Post machine program.

Each rule is one of:
    MARK, UNMARK, LEFT, RIGHT, STOP        -- no argument
    JUMP N, JZ N                            -- N is a rule number
"""

from __future__ import annotations

VALID_COMMANDS = frozenset(
    {"MARK", "UNMARK", "LEFT", "RIGHT", "STOP", "JUMP", "JZ"}
)

COMMANDS_WITH_ARGUMENT = frozenset({"JUMP", "JZ"})


class Rule:
    """A single Post machine instruction."""

    def __init__(self, command: str, argument: int | None = None) -> None:
        """Create a rule from a command string and optional argument.

        Raises ValueError if the command is unknown or if the argument
        does not match the command (e.g. STOP with a number).
        """
        self._command = self._parse_command(command)
        self._argument = self._parse_argument(self._command, argument)

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def command(self) -> str:
        return self._command

    @property
    def argument(self) -> int | None:
        return self._argument

    def has_argument(self) -> bool:
        """Return True if this rule takes a jump target."""
        return self._argument is not None

    # ------------------------------------------------------------------
    # Parsing helpers
    # ------------------------------------------------------------------

    def _parse_command(self, command: str) -> str:
        """Return the normalized command string, or raise ValueError."""
        command = command.strip().upper()
        if command not in VALID_COMMANDS:
            raise ValueError(f"Unknown command '{command}'")
        return command

    def _parse_argument(
        self, command: str, argument: int | None
    ) -> int | None:
        """Return the validated argument, or raise ValueError."""
        if command in COMMANDS_WITH_ARGUMENT:
            if argument is None:
                raise ValueError(f"Command '{command}' requires an argument")
            if argument < 1:
                raise ValueError("Jump target must be 1 or greater")
            return argument
        if argument is not None:
            raise ValueError(f"Command '{command}' takes no argument")
        return None

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_string(self) -> str:
        """Return a human-readable form like 'JUMP 5' or 'MARK'."""
        if self._argument is None:
            return self._command
        return f"{self._command} {self._argument}"

    def load_from_string(self, text: str) -> None:
        """Overwrite this rule from a string like 'JUMP 5'."""
        parts = text.strip().split()
        if not parts:
            raise ValueError("Empty rule string")

        command = self._parse_command(parts[0])
        argument: int | None = None

        if len(parts) == 2:
            try:
                argument = int(parts[1])
            except ValueError as exc:
                raise ValueError(f"Invalid argument '{parts[1]}'") from exc
        elif len(parts) > 2:
            raise ValueError(f"Rule has too many tokens: '{text}'")

        self._command = command
        self._argument = self._parse_argument(command, argument)

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rule):
            return NotImplemented
        return (
            self._command == other._command
            and self._argument == other._argument
        )

    def __hash__(self) -> int:
        return hash((self._command, self._argument))

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"Rule({self._command!r}, {self._argument!r})"