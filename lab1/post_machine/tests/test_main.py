"""Unit tests for the CLI in main.py."""

from __future__ import annotations

from pathlib import Path


from src.main import main, run_machine
from src.machine import PostMachine
from src.program import Program
from src.rule import Rule
from src.tape import Tape


def _build_simple_program_file(tmp_path: Path) -> Path:
    """Create a small program file and return its path."""
    target = tmp_path / "prog.txt"
    target.write_text(
        "TAPE: 0 0\n"
        "PROGRAM:\n"
        "1. MARK\n"
        "2. RIGHT\n"
        "3. MARK\n"
        "4. STOP\n",
        encoding="utf-8",
    )
    return target


def _build_simple_machine() -> PostMachine:
    program = Program()
    program.add(Rule("MARK"))
    program.add(Rule("STOP"))
    return PostMachine(Tape([0, 0]), program)


def test_run_machine_without_log() -> None:
    machine = _build_simple_machine()
    steps = run_machine(machine, log=False)
    assert steps > 0
    assert machine.is_halted


def test_run_machine_with_log_prints_steps(capsys) -> None:
    machine = _build_simple_machine()
    run_machine(machine, log=True)
    out = capsys.readouterr().out
    assert "before step" in out
    assert "final" in out


def test_main_prints_usage_when_no_args(capsys) -> None:
    code = main([])
    out = capsys.readouterr().out
    assert "Usage" in out
    assert code == 1


def test_main_prints_usage_for_help_flag(capsys) -> None:
    code = main(["-h"])
    out = capsys.readouterr().out
    assert "Usage" in out
    assert code == 1


def test_main_runs_program(tmp_path, capsys) -> None:
    path = _build_simple_program_file(tmp_path)
    code = main([str(path)])
    out = capsys.readouterr().out
    assert "Executed" in out
    assert code == 0


def test_main_with_log_flag(tmp_path, capsys) -> None:
    path = _build_simple_program_file(tmp_path)
    code = main([str(path), "-log"])
    out = capsys.readouterr().out
    assert "before step" in out
    assert code == 0


def test_main_handles_missing_file(capsys) -> None:
    code = main(["/this/file/does/not/exist.txt"])
    out = capsys.readouterr().out
    assert "Error" in out
    assert code == 1


def test_main_handles_invalid_file(tmp_path, capsys) -> None:
    path = tmp_path / "bad.txt"
    path.write_text("no tape here\n", encoding="utf-8")
    code = main([str(path)])
    out = capsys.readouterr().out
    assert "Error" in out
    assert code ==1
def test_run_machine_with_log_aborts_on_too_many_steps(capsys, monkeypatch) -> None:
    # A program that never halts: an infinite self-jump.
    program = Program()
    program.add(Rule("JUMP", 1))
    machine = PostMachine(Tape([0]), program)

    # Prevent an actual 10,000-step loop from running in test.
    original_step = machine.step

    def fast_step() -> None:
        # Calling JUMP 1 forever.
        machine._line = 1  # noqa: SLF001
        original_step()

    monkeypatch.setattr(machine, "step", fast_step)

    # Override the internal limit indirectly: run with log=True.
    run_machine(machine, log=True)
    out = capsys.readouterr().out
    assert "Too many steps" in out