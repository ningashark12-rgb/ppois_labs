"""Unit tests for the Tape class."""

import pytest

from src.tape import EMPTY, MARKED, Tape


def test_default_tape_has_one_empty_cell() -> None:
    tape = Tape()
    assert tape.cells == [EMPTY]
    assert tape.head == 0
    assert tape.read() == EMPTY


def test_tape_from_cells_normalizes_values() -> None:
    tape = Tape([0, 2, 0, 5])
    assert tape.cells == [0, 1, 0, 1]


def test_write_marks_current_cell() -> None:
    tape = Tape()
    tape.write(MARKED)
    assert tape.read() == MARKED


def test_write_unmarks_current_cell() -> None:
    tape = Tape([MARKED])
    tape.write(EMPTY)
    assert tape.read() == EMPTY


def test_move_right_advances_head() -> None:
    tape = Tape()
    tape.move_right()
    assert tape.head == 1


def test_move_right_extends_tape_when_needed() -> None:
    tape = Tape([1])
    tape.move_right()
    assert tape.cells == [1, 0]
    assert tape.head == 1


def test_move_left_moves_head_back() -> None:
    tape = Tape([0, 1])
    tape.move_right()
    tape.move_left()
    assert tape.head == 0


def test_move_left_from_start_raises() -> None:
    tape = Tape()
    with pytest.raises(IndexError):
        tape.move_left()


def test_head_position_is_readable() -> None:
    tape = Tape([0, 1, 1])
    tape.move_right()
    assert tape.head == 1


def test_cells_returns_a_copy() -> None:
    tape = Tape([1, 0])
    snapshot = tape.cells
    snapshot.append(99)
    assert tape.cells == [1, 0]


def test_equality() -> None:
    a = Tape([1, 0, 1])
    b = Tape([1, 0, 1])
    assert a == b
    assert hash(a) == hash(b)


def test_equality_accounts_for_head_position() -> None:
    a = Tape([1, 0])
    b = Tape([1, 0])
    b.move_right()
    assert a != b


def test_not_equal_to_other_type() -> None:
    assert Tape() != "not a tape"


def test_str_marks_head_position() -> None:
    tape = Tape([1, 0, 1])
    tape.move_right()
    text = str(tape)
    assert "[0]" in text


def test_repr_contains_cells_and_head() -> None:
    tape = Tape([1, 0])
    text = repr(tape)
    assert "cells" in text
    assert "head" in text