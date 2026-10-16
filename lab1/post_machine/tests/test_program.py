"""Unit tests for the Program class."""

import pytest

from src.program import Program
from src.rule import Rule


def test_empty_program() -> None:
    program = Program()
    assert program.is_empty()
    assert program.size() == 0
    assert len(program) == 0


def test_program_from_rules() -> None:
    program = Program([Rule("MARK"), Rule("RIGHT")])
    assert program.size() == 2


def test_add_appends_rule() -> None:
    program = Program()
    program.add(Rule("MARK"))
    program.add(Rule("STOP"))
    assert program.size() == 2


def test_get_returns_rule_by_number() -> None:
    program = Program([Rule("MARK"), Rule("RIGHT")])
    assert program.get(1) == Rule("MARK")
    assert program.get(2) == Rule("RIGHT")


def test_get_out_of_range_raises() -> None:
    program = Program([Rule("MARK")])
    with pytest.raises(IndexError):
        program.get(5)
    with pytest.raises(IndexError):
        program.get(0)


def test_remove_by_number() -> None:
    program = Program([Rule("MARK"), Rule("RIGHT"), Rule("STOP")])
    program.remove(2)
    assert program.size() == 2
    assert program.get(2) == Rule("STOP")


def test_remove_out_of_range_raises() -> None:
    program = Program([Rule("MARK")])
    with pytest.raises(IndexError):
        program.remove(2)


def test_iteration() -> None:
    program = Program([Rule("MARK"), Rule("STOP")])
    commands = [rule.command for rule in program]
    assert commands == ["MARK", "STOP"]


def test_to_string() -> None:
    program = Program([Rule("MARK"), Rule("JUMP", 1)])
    assert program.to_string() == "1. MARK\n2. JUMP 1"


def test_load_from_string() -> None:
    text = """# a comment
1. MARK
2. RIGHT

3. JZ 1
"""
    program = Program()
    program.load_from_string(text)
    assert program.size() == 3
    assert program.get(1) == Rule("MARK")
    assert program.get(2) == Rule("RIGHT")
    assert program.get(3) == Rule("JZ", 1)


def test_load_from_string_without_numbers() -> None:
    program = Program()
    program.load_from_string("MARK\nSTOP")
    assert program.size() == 2
    assert program.get(2) == Rule("STOP")


def test_equality() -> None:
    a = Program([Rule("MARK"), Rule("STOP")])
    b = Program([Rule("MARK"), Rule("STOP")])
    assert a == b
    assert hash(a) == hash(b)


def test_inequality() -> None:
    a = Program([Rule("MARK")])
    b = Program([Rule("RIGHT")])
    assert a != b


def test_not_equal_to_other_type() -> None:
    assert Program() != "not a program"


def test_str_matches_to_string() -> None:
    program = Program([Rule("MARK")])
    assert str(program) == program.to_string()


def test_repr_contains_rules() -> None:
    program = Program([Rule("MARK")])
    assert "rules" in repr(program)