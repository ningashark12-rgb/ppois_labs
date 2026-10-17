"""An ordered list of Post machine rules.

Rules are numbered starting from 1 to match jump targets used by
`JUMP` and `JZ` commands.
"""

from __future__ import annotations

from .rule import Rule


class Program:
    """An ordered list of Post machine rules."""

    def __init__(self, rules: list[Rule] | None = None) -> None:
        """Create a program, optionally from a list of rules."""
        self._rules: list[Rule] = list(rules) if rules else []

    # ------------------------------------------------------------------
    # Size and access
    # ------------------------------------------------------------------

    def size(self) -> int:
        """Return the number of rules."""
        return len(self._rules)

    def is_empty(self) -> bool:
        """Return True if the program has no rules."""
        return not self._rules

    def get(self, number: int) -> Rule:
        """Return the rule at 1-based `number`.

        Raises IndexError if the number is out of range.
        """
        if number < 1 or number > len(self._rules):
            raise IndexError(f"No rule at position {number}")
        return self._rules[number - 1]

    # ------------------------------------------------------------------
    # Modification
    # ------------------------------------------------------------------

    def add(self, rule: Rule) -> None:
        """Append `rule` to the end of the program."""
        self._rules.append(rule)

    def remove(self, number: int) -> None:
        """Remove the rule at 1-based `number`.

        Raises IndexError if the number is out of range.
        """
        if number < 1 or number > len(self._rules):
            raise IndexError(f"No rule at position {number}")
        del self._rules[number - 1]

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_string(self) -> str:
        """Return the rules as a newline-separated numbered list."""
        lines = []
        for index, rule in enumerate(self._rules, start=1):
            lines.append(f"{index}. {rule.to_string()}")
        return "\n".join(lines)

    def load_from_string(self, text: str) -> None:
        """Replace this program's rules by parsing `text`.

        Each non-empty, non-comment line must be of the form
        `N. COMMAND [ARG]`.  Line numbers are ignored — the order of
        the lines is what defines the program.
        """
        rules: list[Rule] = []
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            # Strip the leading "N. " if present.
            if ". " in line:
                _, _, rest = line.partition(". ")
                line = rest.strip()
            rule = Rule("MARK")
            rule.load_from_string(line)
            rules.append(rule)
        self._rules = rules

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __iter__(self):
        return iter(self._rules)

    def __len__(self) -> int:
        return len(self._rules)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Program):
            return NotImplemented
        return self._rules == other._rules

    def __hash__(self) -> int:
        return hash(tuple(self._rules))

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"Program(rules={self._rules!r})"