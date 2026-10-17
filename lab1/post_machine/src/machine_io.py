"""File I/O helpers for the Post machine.

Two free functions:
    save_machine(machine, path)  -- write to a text file
    load_machine(path)           -- read from a text file
"""

from __future__ import annotations

from pathlib import Path

from .machine import PostMachine
from .program import Program
from .tape import Tape

TAPE_PREFIX = "TAPE:"
PROGRAM_PREFIX = "PROGRAM:"


def save_machine(machine: PostMachine, path: str | Path) -> None:
    """Write `machine` to `path` in the standard text format."""
    lines = []

    tape_cells = " ".join(str(cell) for cell in machine.tape.cells)
    lines.append("# Tape: 0 = empty, 1 = marked.")
    lines.append(f"{TAPE_PREFIX} {tape_cells}")
    lines.append("")

    lines.append("# Program: one rule per line, numbered from 1.")
    lines.append(PROGRAM_PREFIX)
    for index, rule in enumerate(machine.program, start=1):
        lines.append(f"{index}. {rule.to_string()}")

    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_machine(path: str | Path) -> PostMachine:
    """Read a machine from `path` and return a fresh `PostMachine`."""
    text = Path(path).read_text(encoding="utf-8")

    tape_cells: list[int] | None = None
    program_lines: list[str] = []
    in_program_section = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith(TAPE_PREFIX):
            cells_text = line[len(TAPE_PREFIX):].strip()
            tape_cells = [int(token) for token in cells_text.split()]
            continue

        if line.startswith(PROGRAM_PREFIX):
            in_program_section = True
            continue

        if in_program_section:
            program_lines.append(line)

    if tape_cells is None:
        raise ValueError("Missing TAPE: section in file")
    if not program_lines:
        raise ValueError("Missing or empty PROGRAM: section in file")

    program = Program()
    program.load_from_string("\n".join(program_lines))
    tape = Tape(tape_cells)

    return PostMachine(tape, program)