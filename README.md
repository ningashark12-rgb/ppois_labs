# ppoiss_labs

Labs for the *Design of Intelligent Systems Software* course.

## Structure

- `lab1/rubiks_cube/` — Lab 1: Rubik's Cube (OOP fundamentals)

## Lab 1: Rubik's Cube

Python implementation of a 3×3×3 Rubik's Cube.

- Domain model: `src/cube.py`
- File I/O: `src/cube_io.py`
- Interactive CLI: `src/main.py`
- Tests: `tests/` (100% coverage)
- Docs: generated with `pdoc` (see CI artifact)

### Setup

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt