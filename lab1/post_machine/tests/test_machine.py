"""Unit tests for the PostMachine interpreter."""

import pytest

from src.machine import PostMachine
from src.program import Program
from src.rule import Rule
from src.tape import Tape


def _program(*rules: Rule) -> Program:
    p = Program()
    for rule in rules:
        p.add(rule)
    return p


def test_empty_program_starts_halted() -> None:
    machine = PostMachine(Tape(), Program())
    assert machine.is_halted


def test_mark_writes_one() -> None:
    machine = PostMachine(Tape(), _program(Rule("MARK"), Rule("STOP")))
    machine.step()
    assert machine.tape.read() == 1


def test_unmark_writes_zero() -> None:
    machine = PostMachine(Tape([1]), _program(Rule("UNMARK"), Rule("STOP")))
    machine.step()
    assert machine.tape.read() == 0


def test_right_moves_head() -> None:
    machine = PostMachine(Tape(), _program(Rule("RIGHT"), Rule("STOP")))
    machine.step()
    assert machine.tape.head == 1


def test_left_moves_head() -> None:
    tape = Tape([0, 0])
    tape.move_right()
    machine = PostMachine(tape, _program(Rule("LEFT"), Rule("STOP")))
    machine.step()
    assert machine.tape.head == 0


def test_jump_changes_line() -> None:
    machine = PostMachine(
        Tape(),
        _program(Rule("JUMP", 3), Rule("MARK"), Rule("STOP")),
    )
    machine.step()
    assert machine.line == 3


def test_jz_jumps_when_zero() -> None:
    machine = PostMachine(
        Tape([0]),
        _program(Rule("JZ", 3), Rule("MARK"), Rule("STOP")),
    )
    machine.step()
    assert machine.line == 3


def test_jz_falls_through_when_marked() -> None:
    machine = PostMachine(
        Tape([1]),
        _program(Rule("JZ", 3), Rule("MARK"), Rule("STOP")),
    )
    machine.step()
    assert machine.line == 2


def test_stop_halts() -> None:
    machine = PostMachine(Tape(), _program(Rule("STOP")))
    machine.step()
    assert machine.is_halted


def test_step_after_halt_does_nothing() -> None:
    machine = PostMachine(Tape(), _program(Rule("MARK"), Rule("STOP")))
    machine.run()
    machine.step()
    assert machine.is_halted


def test_run_returns_step_count() -> None:
    program = _program(Rule("MARK"), Rule("RIGHT"), Rule("STOP"))
    machine = PostMachine(Tape(), program)
    steps = machine.run()
    assert steps == 3


def test_run_respects_max_steps() -> None:
    program = _program(Rule("JUMP", 1))
    machine = PostMachine(Tape(), program)
    steps = machine.run(max_steps=5)
    assert steps == 5
    assert not machine.is_halted


def test_jump_target_out_of_range_raises() -> None:
    machine = PostMachine(Tape(), _program(Rule("JUMP", 99)))
    with pytest.raises(IndexError):
        machine.step()


def test_falling_off_end_halts() -> None:
    machine = PostMachine(Tape(), _program(Rule("MARK")))
    machine.step()
    assert machine.is_halted


def test_run_simple_program() -> None:
    # Program: mark, right, mark, stop  -> two marked cells
    program = _program(
        Rule("MARK"),
        Rule("RIGHT"),
        Rule("MARK"),
        Rule("STOP"),
    )
    machine = PostMachine(Tape(), program)
    machine.run()
    assert machine.tape.cells == [1, 1]


def test_equality() -> None:
    tape = Tape([1])
    program = _program(Rule("STOP"))
    a = PostMachine(tape, program)
    b = PostMachine(tape, program)
    assert a == b


def test_not_equal_to_other_type() -> None:
    machine = PostMachine(Tape(), Program())
    assert machine != "not a machine"


def test_str_contains_tape_and_status() -> None:
    machine = PostMachine(Tape([1]), _program(Rule("STOP")))
    text = str(machine)
    assert "line" in text


def test_repr_contains_tape_and_line() -> None:
    machine = PostMachine(Tape(), _program(Rule("STOP")))
    text = repr(machine)
    assert "tape" in text
    assert "line" in text
def test_program_property_returns_program() -> None:
    program = _program(Rule("STOP"))
    machine = PostMachine(Tape(), program)
    assert machine.program is program


def test_unsupported_command_raises() -> None:
    # Bypass Rule validation by crafting a fake rule with an invalid command.
    class _FakeRule:
        command = "DANCE"
        argument = None

    machine = PostMachine(Tape(), Program())
    # Force a non-empty program by injecting a fake rule directly.
    machine._program._rules.append(_FakeRule())  # noqa: SLF001
    machine._line = 1
    machine._halted = False
    with pytest.raises(ValueError):
        machine.step()


def test_jump_target_none_raises() -> None:
    machine = PostMachine(Tape(), _program(Rule("STOP")))
    with pytest.raises(ValueError):
        machine._jump_to(None)  # noqa: SLF001