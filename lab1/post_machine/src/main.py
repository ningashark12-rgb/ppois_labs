"""Command-line interface for the Post machine.

Usage:
    python -m src.main <program_file>          # run silently
    python -m src.main <program_file> -log     # print state after each rule
"""

from __future__ import annotations

import sys

from .machine import PostMachine
from .machine_io import load_machine

LOG_FLAG = "-log"


def _print_usage() -> None:
    """Print the expected usage line."""
    print("Usage: python -m src.main <program_file> [-log]")


def run_machine(machine: PostMachine, log: bool = False) -> int:
    """Run the machine step by step, optionally logging each step.

    Returns the number of steps executed.
    """
    if not log:
        return machine.run()

    step_number = 0
    while not machine.is_halted:
        print(f"--- before step {step_number + 1}: {machine} ---")
        machine.step()
        step_number += 1
        if step_number > 10_000:
            print("Too many steps, aborting.")
            break

    print(f"--- final: {machine} ---")
    return step_number


def main(argv: list[str]) -> int:
    """Entry point. Returns a process exit code (0 = success, 1 = error)."""
    if not argv or argv[0] in ("-h", "--help"):
        _print_usage()
        return 1

    path = argv[0]
    log = LOG_FLAG in argv[1:]

    try:
        machine = load_machine(path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1

    steps = run_machine(machine, log=log)
    print(f"Executed {steps} step(s).")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))