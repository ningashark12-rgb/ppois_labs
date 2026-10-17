"""Tests for the file I/O layer of the Rubik's Cube domain."""

from src.cube import RubiksCube
from src.cube_io import load_cube, save_cube


def test_save_and_load_roundtrip(tmp_path) -> None:
    original = RubiksCube()
    original.rotate_face("U")
    file_path = tmp_path / "cube.txt"

    save_cube(original, file_path)
    loaded = load_cube(file_path)

    assert loaded == original


def test_save_writes_serialized_text(tmp_path) -> None:
    cube = RubiksCube()
    file_path = tmp_path / "cube.txt"

    save_cube(cube, file_path)

    assert file_path.read_text(encoding="utf-8") == cube.to_string()