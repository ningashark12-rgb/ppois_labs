"""Unit tests for the Rule class."""

import pytest

from src.rule import Rule


def test_create_simple_rule() -> None:
    rule = Rule("MARK")
    assert rule.command == "MARK"
    assert rule.argument is None
    assert not rule.has_argument()


def test_create_jump_rule() -> None:
    rule = Rule("JUMP", 5)
    assert rule.command == "JUMP"
    assert rule.argument == 5
    assert rule.has_argument()


def test_unknown_command_raises() -> None:
    with pytest.raises(ValueError):
        Rule("DANCE")


def test_jump_without_argument_raises() -> None:
    with pytest.raises(ValueError):
        Rule("JUMP")


def test_simple_rule_with_argument_raises() -> None:
    with pytest.raises(ValueError):
        Rule("MARK", 3)


def test_jump_target_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Rule("JUMP", 0)


def test_command_is_case_insensitive() -> None:
    rule = Rule("mark")
    assert rule.command == "MARK"


def test_command_is_trimmed() -> None:
    rule = Rule("  RIGHT  ")
    assert rule.command == "RIGHT"


def test_to_string_simple() -> None:
    assert Rule("LEFT").to_string() == "LEFT"


def test_to_string_jump() -> None:
    assert Rule("JUMP", 4).to_string() == "JUMP 4"


def test_load_from_string_simple() -> None:
    rule = Rule("MARK")
    rule.load_from_string("RIGHT")
    assert rule.command == "RIGHT"
    assert rule.argument is None


def test_load_from_string_jump() -> None:
    rule = Rule("MARK")
    rule.load_from_string("JUMP 3")
    assert rule.command == "JUMP"
    assert rule.argument == 3


def test_load_from_string_rejects_empty() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("   ")


def test_load_from_string_rejects_non_integer_argument() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("JUMP abc")


def test_load_from_string_rejects_too_many_tokens() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("JUMP 1 2")


def test_equality() -> None:
    assert Rule("MARK") == Rule("MARK")
    assert Rule("JUMP", 3) == Rule("JUMP", 3)
    assert hash(Rule("MARK")) == hash(Rule("MARK"))


def test_inequality() -> None:
    assert Rule("MARK") != Rule("UNMARK")
    assert Rule("JUMP", 3) != Rule("JUMP", 4)


def test_not_equal_to_other_type() -> None:
    assert Rule("MARK") != "MARK"


def test_str_matches_to_string() -> None:
    rule = Rule("JZ", 7)
    assert str(rule) == "JZ 7"


def test_repr_contains_command_and_argument() -> None:
    text = repr(Rule("JUMP", 2))
    assert "JUMP" in text
    assert "2" in text
def test_load_from_string_rejects_unknown_command() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("FLY")


def test_load_from_string_rejects_no_argument_for_jump() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("JUMP")


def test_load_from_string_rejects_argument_for_simple_command() -> None:
    rule = Rule("MARK")
    with pytest.raises(ValueError):
        rule.load_from_string("RIGHT 5")