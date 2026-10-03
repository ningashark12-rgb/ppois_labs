"""Console interface for the Rubik's Cube domain.

This module only handles user interaction.  All cube logic lives in
`cube.py`; all persistence lives in `cube_io.py`.
"""

from __future__ import annotations

from pathlib import Path

from .cube import MOVE_FACES, RubiksCube
from .cube_io import CubeIO

MENU_OPTIONS = (
    ("1", "Show cube"),
    ("2", "Shuffle"),
    ("3", "Rotate a face"),
    ("4", "Check solved"),
    ("5", "Save to file"),
    ("6", "Load from file"),
    ("0", "Exit"),
)

SHUFFLE_MOVES = 20


def _prompt_int(prompt: str) -> int:
    """Ask the user for an integer, retrying on bad input."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def _show_cube(cube: RubiksCube) -> None:
    print()
    print(cube)
    print(f"Solved: {cube.is_solved()}")
    print()


def _rotate_menu(cube: RubiksCube) -> None:
    face = input(f"Face to rotate {MOVE_FACES}: ").strip().upper()
    if face not in MOVE_FACES:
        print("Unknown face.")
        return
    times = _prompt_int("Times (negative = counter-clockwise): ")
    cube.rotate_face(face, times)
    print("Rotated.")


def _shuffle_menu(cube: RubiksCube) -> None:
    cube.shuffle(moves=SHUFFLE_MOVES)
    print(f"Shuffled with {SHUFFLE_MOVES} random moves.")


def _save_menu(cube: RubiksCube) -> None:
    path = input("Path to save: ").strip()
    CubeIO.save(cube, path)
    print(f"Saved to {path}.")


def _load_menu(cube: RubiksCube) -> RubiksCube:
    path = input("Path to load: ").strip()
    if not Path(path).exists():
        print("File does not exist.")
        return cube
    return CubeIO.load(path)


def _print_menu() -> None:
    print("\n=== Rubik's Cube ===")
    for key, label in MENU_OPTIONS:
        print(f"{key}. {label}")


def main() -> None:
    """Run the interactive menu loop."""
    cube = RubiksCube()

    while True:
        _print_menu()
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            return
        if choice == "1":
            _show_cube(cube)
        elif choice == "2":
            _shuffle_menu(cube)
        elif choice == "3":
            _rotate_menu(cube)
        elif choice == "4":
            print("Solved:", cube.is_solved())
        elif choice == "5":
            _save_menu(cube)
        elif choice == "6":
            cube = _load_menu(cube)
        else:
            print("Invalid choice.")


if __name__ == "__main__":  # pragma: no cover
    main()