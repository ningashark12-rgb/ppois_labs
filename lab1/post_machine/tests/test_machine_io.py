"""Unit tests for the file I/O layer."""

import pytest

from src.machine import PostMachine
from src.machine_io import load_machine, save_machine
from src.program import Program
from src.rule import Rule
from src.tape import Tape


def _build_simple_machine() -> PostMachine:
    tape = Tape([0, 1, 0])
    program = Program()
    program.add(Rule("MARK"))
    program.add(Rule("RIGHT"))
    program.add(Rule("STOP"))
    return PostMachine(tape, program)


def test_save_writes_tape_and_program(tmp_path) -> None:
    machine = _build_simple_machine()
    target = tmp_path / "machine.txt"

    save_machine(machine, target)

    text = target.read_text(encoding="utf-8")
    assert "TAPE: 0 1 0" in text
    assert "PROGRAM:" in text
    assert "1. MARK" in text
    assert "2. RIGHT" in text
    assert "3. STOP" in text


def test_save_load_roundtrip(tmp_path) -> None:
    original = _build_simple_machine()
    target = tmp_path / "machine.txt"

    save_machine(original, target)
    loaded = load_machine(target)

    assert loaded.tape == original.tape
    assert loaded.program == original.program


def test_load_missing_tape_raises(tmp_path) -> None:
    target = tmp_path / "bad.txt"
    target.write_text("PROGRAM:\n1. MARK\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_machine(target)


def test_load_missing_program_raises(tmp_path) -> None:
    target = tmp_path / "bad.txt"
    target.write_text("TAPE: 0 0 0\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_machine(target)


def test_load_ignores_comments_and_blanks(tmp_path) -> None:
    target = tmp_path / "machine.txt"
    target.write_text(
        "# a comment\n"
        "TAPE: 1 0\n"
        "\n"
        "PROGRAM:\n"
        "# another comment\n"
        "1. MARK\n"
        "2. STOP\n",
        encoding="utf-8",
    )

    machine = load_machine(target)
    assert machine.tape.cells == [1, 0]
    assert machine.program.size() == 2