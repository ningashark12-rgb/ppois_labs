"""Tape for a Post machine.

The tape is a one-dimensional strip of cells, each of which is either
empty (0) or marked (1).  A read/write head sits on one cell at a time.
The tape extends to the right on demand; moving left past the start is
an error because a Post machine has a leftmost cell.
"""

from __future__ import annotations

EMPTY = 0
MARKED = 1


class Tape:
    """A cell strip with a movable, writable head."""

    def __init__(self, cells: list[int] | None = None) -> None:
        """Create a tape from `cells` (default: one empty cell).

        The head starts at position 0.
        """
        if cells is None:
            cells = [EMPTY]
        self._cells: list[int] = [self._normalize(cell) for cell in cells]
        self._head: int = 0

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def head(self) -> int:
        """Current head position (0-based index)."""
        return self._head

    @property
    def cells(self) -> list[int]:
        """A copy of the tape's cells."""
        return self._cells[:]

    def read(self) -> int:
        """Return the symbol under the head."""
        return self._cells[self._head]

    # ------------------------------------------------------------------
    # Writing
    # ------------------------------------------------------------------

    def write(self, value: int) -> None:
        """Write `value` (0 or 1) under the head."""
        self._cells[self._head] = self._normalize(value)

    # ------------------------------------------------------------------
    # Movement
    # ------------------------------------------------------------------

    def move_left(self) -> None:
        """Move the head one cell to the left.

        Raises `IndexError` if the head is already at the leftmost cell.
        """
        if self._head == 0:
            raise IndexError("Cannot move left from the leftmost cell")
        self._head -= 1

    def move_right(self) -> None:
        """Move the head one cell to the right, extending the tape if needed."""
        self._head += 1
        if self._head == len(self._cells):
            self._cells.append(EMPTY)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _normalize(self, value: int) -> int:
        """Return 1 if `value` is truthy, otherwise 0."""
        return MARKED if value else EMPTY

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tape):
            return NotImplemented
        return self._cells == other._cells and self._head == other._head

    def __hash__(self) -> int:
        return hash((tuple(self._cells), self._head))

    def __str__(self) -> str:
        """Visualize the tape with the head marked by `[ ]`."""
        rendered = []
        for index, cell in enumerate(self._cells):
            symbol = str(cell)
            if index == self._head:
                rendered.append(f"[{symbol}]")
            else:
                rendered.append(f" {symbol} ")
        return "".join(rendered)

    def __repr__(self) -> str:
        return f"Tape(cells={self._cells!r}, head={self._head})"