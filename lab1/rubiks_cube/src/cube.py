"""Rubik's Cube domain model.

This module contains only the domain logic of a 3x3x3 Rubik's Cube.
It has no dependency on the console interface or on file I/O.
"""

from __future__ import annotations

import copy
import random
from enum import Enum

MOVE_FACES = ("U", "D", "F", "B", "L", "R")
CUBE_SIZE = 3

# Number of times a single clockwise rotation must be applied to a face
# to return the cube to its previous state.
FULL_TURN = 4

# Valid characters that may appear in a serialized cube string.
VALID_SYMBOLS = frozenset("WYROBG")


class Color(Enum):
    """Colors used by the Rubik's Cube."""

    WHITE = "W"
    YELLOW = "Y"
    RED = "R"
    ORANGE = "O"
    BLUE = "B"
    GREEN = "G"


class RubiksCube:
    """Represents a standard 3x3x3 Rubik's Cube.

    A cube is stored as six faces (U, D, F, B, L, R).  Each face is a
    2D list of `Color` values, indexed as `face[row][col]`.
    """

    SIZE = CUBE_SIZE

    def __init__(self) -> None:
        """Create a solved Rubik's Cube."""
        self._faces: dict[str, list[list[Color]]] = {
            "U": self._create_face(Color.WHITE),
            "D": self._create_face(Color.YELLOW),
            "F": self._create_face(Color.GREEN),
            "B": self._create_face(Color.BLUE),
            "L": self._create_face(Color.ORANGE),
            "R": self._create_face(Color.RED),
        }

    # ------------------------------------------------------------------
    # Construction helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _create_face(color: Color) -> list[list[Color]]:
        """Return a fresh `SIZE x SIZE` face filled with `color`."""
        return [
            [color for _ in range(RubiksCube.SIZE)]
            for _ in range(RubiksCube.SIZE)
        ]

    @classmethod
    def from_string(cls, text: str) -> "RubiksCube":
        """Build a cube from a serialized string (see `to_string`).

        The format is six faces separated by `/`, each face being 9
        characters (row-major) taken from the set of color symbols.
        """
        cube = cls()
        faces = text.strip().split("/")
        if len(faces) != len(MOVE_FACES):
            raise ValueError(
                f"Expected {len(MOVE_FACES)} faces, got {len(faces)}"
            )

        expected_cells = cls.SIZE * cls.SIZE
        for name, block in zip(MOVE_FACES, faces):
            if len(block) != expected_cells:
                raise ValueError(
                    f"Face {name} must have {expected_cells} cells"
                )
            if any(symbol not in VALID_SYMBOLS for symbol in block):
                raise ValueError(f"Face {name} contains invalid symbols")

            cube._faces[name] = [
                [Color(block[row * cls.SIZE + col]) for col in range(cls.SIZE)]
                for row in range(cls.SIZE)
            ]

        return cube

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_string(self) -> str:
        """Serialize the cube to a string usable with `from_string`."""
        blocks = []
        for name in MOVE_FACES:
            block = "".join(
                cell.value for row in self._faces[name] for cell in row
            )
            blocks.append(block)
        return "/".join(blocks)

    # ------------------------------------------------------------------
    # Basic queries
    # ------------------------------------------------------------------

    def get_face(self, name: str) -> list[list[Color]]:
        """Return a deep copy of the named face."""
        if name not in self._faces:
            raise ValueError(f"Unknown face '{name}'")
        return copy.deepcopy(self._faces[name])

    def get_color(self, face: str, row: int, col: int) -> Color:
        """Return the color at `(row, col)` on `face`."""
        self._validate_position(face, row, col)
        return self._faces[face][row][col]

    def is_solved(self) -> bool:
        """Return True if every face is a single uniform color."""
        for face in self._faces.values():
            first = face[0][0]
            if any(cell != first for row in face for cell in row):
                return False
        return True

    @staticmethod
    def _validate_position(face: str, row: int, col: int) -> None:
        if face not in MOVE_FACES:
            raise ValueError(f"Unknown face '{face}'")
        if not 0 <= row < CUBE_SIZE or not 0 <= col < CUBE_SIZE:
            raise IndexError("Row or column out of range")

    # ------------------------------------------------------------------
    # Rotations
    # ------------------------------------------------------------------

    def rotate_face(self, face: str, times: int = 1) -> None:
        """Rotate a face clockwise `times` times (negative = counter-clockwise)."""
        if face not in MOVE_FACES:
            raise ValueError(f"Unknown face '{face}'")

        turns = times % FULL_TURN
        for _ in range(turns):
            self._rotate_face_once(face)

    def _rotate_face_once(self, face: str) -> None:
        """Rotate a single face clockwise once, including adjacent edges."""
        self._faces[face] = self._rotate_grid_clockwise(self._faces[face])
        self._rotate_adjacent_strips(face)

    @staticmethod
    def _rotate_grid_clockwise(
        grid: list[list[Color]],
    ) -> list[list[Color]]:
        """Return a new grid rotated 90 degrees clockwise."""
        size = len(grid)
        return [
            [grid[size - 1 - col][row] for col in range(size)]
            for row in range(size)
        ]

    def _rotate_adjacent_strips(self, face: str) -> None:
        """Rotate the four strips of the cube that touch `face`."""
        # Each entry: (face_name, row_or_col_index, orientation)
        # For simplicity we read the four relevant strips, rotate the
        # list of strips clockwise, and write them back.
        strips = self._read_strips(face)
        rotated = [strips[-1]] + strips[:-1]
        self._write_strips(face, rotated)

    def _read_strips(self, face: str) -> list[list[Color]]:
        """Read the four strips around `face` in clockwise order."""
        if face == "U":
            return [
                self._faces["B"][0][:],
                self._faces["R"][0][:],
                self._faces["F"][0][:],
                self._faces["L"][0][:],
            ]
        if face == "D":
            return [
                self._faces["F"][-1][:],
                self._faces["R"][-1][:],
                self._faces["B"][-1][:],
                self._faces["L"][-1][:],
            ]
        if face == "F":
            return [
                self._faces["U"][-1][:],
                [self._faces["R"][r][0] for r in range(CUBE_SIZE)],
                self._faces["D"][0][:],
                [self._faces["L"][r][-1] for r in range(CUBE_SIZE)],
            ]
        if face == "B":
            return [
                self._faces["U"][0][:],
                [self._faces["L"][r][0] for r in range(CUBE_SIZE)],
                self._faces["D"][-1][:],
                [self._faces["R"][r][-1] for r in range(CUBE_SIZE)],
            ]
        if face == "L":
            return [
                [self._faces["U"][r][0] for r in range(CUBE_SIZE)],
                [self._faces["F"][r][0] for r in range(CUBE_SIZE)],
                [self._faces["D"][r][0] for r in range(CUBE_SIZE)],
                [self._faces["B"][r][-1] for r in range(CUBE_SIZE)],
            ]
        if face == "R":
            return [
                [self._faces["U"][r][-1] for r in range(CUBE_SIZE)],
                [self._faces["B"][r][0] for r in range(CUBE_SIZE)],
                [self._faces["D"][r][-1] for r in range(CUBE_SIZE)],
                [self._faces["F"][r][-1] for r in range(CUBE_SIZE)],
            ]
        raise ValueError(f"Unknown face '{face}'")

    def _write_strips(self, face: str, strips: list[list[Color]]) -> None:
        """Write the four rotated strips back around `face`."""
        if face == "U":
            self._faces["B"][0] = strips[0][:]
            self._faces["R"][0] = strips[1][:]
            self._faces["F"][0] = strips[2][:]
            self._faces["L"][0] = strips[3][:]
        elif face == "D":
            self._faces["F"][-1] = strips[0][:]
            self._faces["R"][-1] = strips[1][:]
            self._faces["B"][-1] = strips[2][:]
            self._faces["L"][-1] = strips[3][:]
        elif face == "F":
            self._faces["U"][-1] = strips[0][:]
            for r in range(CUBE_SIZE):
                self._faces["R"][r][0] = strips[1][r]
            self._faces["D"][0] = strips[2][:]
            for r in range(CUBE_SIZE):
                self._faces["L"][r][-1] = strips[3][r]
        elif face == "B":
            self._faces["U"][0] = strips[0][:]
            for r in range(CUBE_SIZE):
                self._faces["L"][r][0] = strips[1][r]
            self._faces["D"][-1] = strips[2][:]
            for r in range(CUBE_SIZE):
                self._faces["R"][r][-1] = strips[3][r]
        elif face == "L":
            for r in range(CUBE_SIZE):
                self._faces["U"][r][0] = strips[0][r]
            for r in range(CUBE_SIZE):
                self._faces["F"][r][0] = strips[1][r]
            for r in range(CUBE_SIZE):
                self._faces["D"][r][0] = strips[2][r]
            for r in range(CUBE_SIZE):
                self._faces["B"][r][-1] = strips[3][r]
        elif face == "R":
            for r in range(CUBE_SIZE):
                self._faces["U"][r][-1] = strips[0][r]
            for r in range(CUBE_SIZE):
                self._faces["B"][r][0] = strips[1][r]
            for r in range(CUBE_SIZE):
                self._faces["D"][r][-1] = strips[2][r]
            for r in range(CUBE_SIZE):
                self._faces["F"][r][-1] = strips[3][r]
        else:
            raise ValueError(f"Unknown face '{face}'")

    # ------------------------------------------------------------------
    # Shuffling
    # ------------------------------------------------------------------

    def shuffle(self, moves: int = 20, seed: int | None = None) -> None:
        """Apply `moves` random face rotations (clockwise or counter)."""
        rng = random.Random(seed)
        for _ in range(moves):
            face = rng.choice(MOVE_FACES)
            direction = rng.choice((-1, 1))
            self.rotate_face(face, direction)

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RubiksCube):
            return NotImplemented
        return self._faces == other._faces

    def __hash__(self) -> int:
        # Faces are nested lists, so we must convert to a hashable form.
        flat = tuple(
            cell.value for name in MOVE_FACES for row in self._faces[name] for cell in row
        )
        return hash(flat)

    def __str__(self) -> str:
        lines = []
        for name in MOVE_FACES:
            lines.append(f"{name}:")
            for row in self._faces[name]:
                lines.append("  " + " ".join(cell.value for cell in row))
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"RubiksCube({self.to_string()!r})"

    def __copy__(self) -> "RubiksCube":
        return RubiksCube.from_string(self.to_string())

    def __deepcopy__(self, memo: dict) -> "RubiksCube":
        return self.__copy__()