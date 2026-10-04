"""File I/O helpers for the Rubik's Cube domain.

Kept in a separate module so that the domain class stays independent
from any storage mechanism.
"""

from __future__ import annotations

from pathlib import Path

from .cube import RubiksCube


def save_cube(cube: RubiksCube, path: str | Path) -> None:
    """Write the cube's serialized form to `path`."""
    Path(path).write_text(cube.to_string(), encoding="utf-8")


def load_cube(path: str | Path) -> RubiksCube:
    """Read a cube from `path` and return it."""
    text = Path(path).read_text(encoding="utf-8")
    cube = RubiksCube()
    cube.load_from_string(text)
    return cube