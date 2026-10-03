"""Tests for the interactive CLI in main.py.

We simulate user input by patching `builtins.input`, and check
the printed output via the `capsys` fixture.
"""

from __future__ import annotations

from unittest.mock import patch

from src import main as main_module


def _feed(*inputs: str):
    """Return a fake input() that yields each string once."""
    iterator = iter(inputs)
    return lambda _prompt="": next(iterator)


def test_show_cube_then_exit(capsys) -> None:
    with patch("builtins.input", _feed("1", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "U:" in out
    assert "Goodbye!" in out


def test_shuffle_then_exit(capsys) -> None:
    with patch("builtins.input", _feed("2", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Shuffled with" in out


def test_rotate_face_then_exit(capsys) -> None:
    with patch("builtins.input", _feed("3", "U", "1", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Rotated." in out


def test_rotate_with_bad_face(capsys) -> None:
    with patch("builtins.input", _feed("3", "Z", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Unknown face." in out


def test_rotate_retries_on_non_integer(capsys) -> None:
    with patch("builtins.input", _feed("3", "U", "abc", "2", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Please enter a valid integer." in out


def test_check_solved_then_exit(capsys) -> None:
    with patch("builtins.input", _feed("4", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Solved: True" in out


def test_save_then_exit(capsys, tmp_path) -> None:
    target = tmp_path / "cube.txt"
    with patch("builtins.input", _feed("5", str(target), "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Saved to" in out
    assert target.exists()


def test_load_existing_file(capsys, tmp_path) -> None:
    target = tmp_path / "cube.txt"
    target.write_text("WWWWWWWWW/" * 5 + "WWWWWWWWW", encoding="utf-8")
    with patch("builtins.input", _feed("6", str(target), "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Goodbye!" in out


def test_load_missing_file(capsys, tmp_path) -> None:
    missing = tmp_path / "nope.txt"
    with patch("builtins.input", _feed("6", str(missing), "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "File does not exist." in out


def test_invalid_menu_choice_then_exit(capsys) -> None:
    with patch("builtins.input", _feed("99", "0")):
        main_module.main()
    out = capsys.readouterr().out
    assert "Invalid choice." in out