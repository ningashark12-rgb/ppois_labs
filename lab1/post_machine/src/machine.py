"""The Post machine interpreter.

Ties together a `Tape`, a `Program`, and a current rule index.
Each call to `step()` executes exactly one rule.
"""

from __future__ import annotations

from .program import Program
from .rule import Rule
from .tape import MARKED, Tape

DEFAULT_MAX_STEPS = 10_000


class PostMachine:
    """A Post machine: tape + program + current rule index."""

    def __init__(self, tape: Tape, program: Program) -> None:
        """Create a machine from a tape and a program."""
        self._tape = tape
        self._program = program
        self._line = 1 if not program.is_empty() else 0
        self._halted = program.is_empty()

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def tape(self) -> Tape:
        return self._tape

    @property
    def program(self) -> Program:
        return self._program

    @property
    def line(self) -> int:
        """Current rule number (1-based) or 0 if halted."""
        return self._line

    @property
    def is_halted(self) -> bool:
        return self._halted

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def step(self) -> None:
        """Execute the current rule once."""
        if self._halted:
            return
        rule = self._program.get(self._line)
        self._execute(rule)

    def run(self, max_steps: int = DEFAULT_MAX_STEPS) -> int:
        """Execute rules until STOP or `max_steps` iterations.

        Returns the number of steps actually executed.
        """
        executed = 0
        while not self._halted and executed < max_steps:
            self.step()
            executed += 1
        return executed

    def _execute(self, rule: Rule) -> None:
        """Apply a single rule to the machine's state."""
        command = rule.command

        if command == "MARK":
            self._tape.write(MARKED)
            self._advance()
        elif command == "UNMARK":
            self._tape.write(0)
            self._advance()
        elif command == "LEFT":
            self._tape.move_left()
            self._advance()
        elif command == "RIGHT":
            self._tape.move_right()
            self._advance()
        elif command == "JUMP":
            self._jump_to(rule.argument)
        elif command == "JZ":
            if self._tape.read() == 0:
                self._jump_to(rule.argument)
            else:
                self._advance()
        elif command == "STOP":
            self._halted = True
        else:
            raise ValueError(f"Unsupported command '{command}'")

    def _advance(self) -> None:
        """Move to the next rule, halting if past the end."""
        next_line = self._line + 1
        if next_line > self._program.size():
            self._halted = True
        else:
            self._line = next_line

    def _jump_to(self, target: int | None) -> None:
        """Jump to a 1-based rule number."""
        if target is None:
            raise ValueError("Jump target cannot be None")
        if target < 1 or target > self._program.size():
            raise IndexError(f"Jump target {target} out of range")
        self._line = target

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PostMachine):
            return NotImplemented
        return (
            self._tape == other._tape
            and self._program == other._program
            and self._line == other._line
            and self._halted == other._halted
        )

    def __str__(self) -> str:
        status = "halted" if self._halted else f"line {self._line}"
        return f"{self._tape} | {status}"

    def __repr__(self) -> str:
        return (
            f"PostMachine(tape={self._tape!r}, "
            f"program={self._program!r}, line={self._line})"
        )