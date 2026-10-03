"""Unit tests for the Rubik's Cube domain class."""

import copy

import pytest

from src.cube import CUBE_SIZE, Color, RubiksCube


@pytest.fixture
def solved_cube() -> RubiksCube:
    return RubiksCube()


def test_new_cube_is_solved(solved_cube: RubiksCube) -> None:
    assert solved_cube.is_solved()


def test_each_face_has_correct_size(solved_cube: RubiksCube) -> None:
    for face in ("U", "D", "F", "B", "L", "R"):
        grid = solved_cube.get_face(face)
        assert len(grid) == CUBE_SIZE
        assert all(len(row) == CUBE_SIZE for row in grid)


def test_rotate_face_once_breaks_solved(solved_cube: RubiksCube) -> None:
    solved_cube.rotate_face("U")
    assert not solved_cube.is_solved()


def test_rotate_face_four_times_restores(solved_cube: RubiksCube) -> None:
    for _ in range(4):
        solved_cube.rotate_face("F")
    assert solved_cube.is_solved()


def test_rotate_counter_clockwise_inverts_clockwise(solved_cube: RubiksCube) -> None:
    original = solved_cube.to_string()
    solved_cube.rotate_face("R", 1)
    solved_cube.rotate_face("R", -1)
    assert solved_cube.to_string() == original


def test_invalid_face_raises(solved_cube: RubiksCube) -> None:
    with pytest.raises(ValueError):
        solved_cube.rotate_face("X")


def test_from_string_roundtrip(solved_cube: RubiksCube) -> None:
    text = solved_cube.to_string()
    assert RubiksCube.from_string(text) == solved_cube


def test_from_string_rejects_wrong_face_count() -> None:
    with pytest.raises(ValueError):
        RubiksCube.from_string("WWW/WWW")


def test_from_string_rejects_invalid_symbol() -> None:
    bad = "WWWWWWWWW/" + "X" * 9 + "/" + "/".join(["WWWWWWWWW"] * 4)
    with pytest.raises(ValueError):
        RubiksCube.from_string(bad)


def test_equality_and_hash(solved_cube: RubiksCube) -> None:
    clone = RubiksCube.from_string(solved_cube.to_string())
    assert solved_cube == clone
    assert hash(solved_cube) == hash(clone)


def test_not_equal_after_rotation(solved_cube: RubiksCube) -> None:
    other = RubiksCube.from_string(solved_cube.to_string())
    other.rotate_face("U")
    assert solved_cube != other


def test_not_equal_to_other_type(solved_cube: RubiksCube) -> None:
    assert solved_cube != "not a cube"


def test_str_contains_all_faces(solved_cube: RubiksCube) -> None:
    text = str(solved_cube)
    for face in ("U", "D", "F", "B", "L", "R"):
        assert f"{face}:" in text


def test_repr_contains_serialized_form(solved_cube: RubiksCube) -> None:
    assert solved_cube.to_string() in repr(solved_cube)


def test_copy_is_independent(solved_cube: RubiksCube) -> None:
    clone = copy.deepcopy(solved_cube)
    clone.rotate_face("U")
    assert clone != solved_cube
    assert solved_cube.is_solved()


def test_shallow_copy_is_independent(solved_cube: RubiksCube) -> None:
    clone = copy.copy(solved_cube)
    clone.rotate_face("D")
    assert clone != solved_cube
    assert solved_cube.is_solved()


def test_shuffle_with_seed_is_deterministic() -> None:
    a = RubiksCube()
    b = RubiksCube()
    a.shuffle(moves=10, seed=42)
    b.shuffle(moves=10, seed=42)
    assert a == b


def test_get_color_returns_expected(solved_cube: RubiksCube) -> None:
    assert solved_cube.get_color("U", 0, 0) is Color.WHITE


def test_get_color_out_of_range(solved_cube: RubiksCube) -> None:
    with pytest.raises(IndexError):
        solved_cube.get_color("U", 5, 5)


def test_get_color_unknown_face(solved_cube: RubiksCube) -> None:
    with pytest.raises(ValueError):
        solved_cube.get_color("X", 0, 0)


def test_get_face_unknown_face(solved_cube: RubiksCube) -> None:
    with pytest.raises(ValueError):
        solved_cube.get_face("X")


def test_rotate_all_faces_keeps_solvable(solved_cube: RubiksCube) -> None:
    for face in ("U", "D", "F", "B", "L", "R"):
        for _ in range(4):
            solved_cube.rotate_face(face)
    assert solved_cube.is_solved()


def test_from_string_rejects_wrong_cell_count() -> None:
    bad = "WWWWWWWW/" + "/".join(["WWWWWWWWW"] * 5)
    with pytest.raises(ValueError):
        RubiksCube.from_string(bad)


def test_read_strips_rejects_unknown_face(solved_cube: RubiksCube) -> None:
    with pytest.raises(ValueError):
        solved_cube._read_strips("X")


def test_write_strips_rejects_unknown_face(solved_cube: RubiksCube) -> None:
    with pytest.raises(ValueError):
        solved_cube._write_strips("X", [])