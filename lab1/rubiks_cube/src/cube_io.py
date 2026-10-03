"""File I/O for the Rubik's Cube domain.

Kept in a separate module so that the domain class stays independent
from any storage mechanism.
"""

from __future__ import annotations

from pathlib import Path

from .cube import RubiksCube


class CubeIO:
    """Load and save cubes to text files."""

    @staticmethod
    def save(cube: RubiksCube, path: str | Path) -> None:
        """Write the cube's serialized form to `path`."""
        Path(path).write_text(cube.to_string(), encoding="utf-8")

    @staticmethod
    def load(path: str | Path) -> RubiksCube:
        """Read a cube from `path` and return it."""
        text = Path(path).read_text(encoding="utf-8")
        return RubiksCube.from_string(text)