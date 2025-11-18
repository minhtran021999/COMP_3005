This repository is a teaching/homework collection for COMP_3005 (Python). The goal of the instructions
below is to make an AI coding agent productive quickly by surfacing project-specific patterns,
conventions, and common workflows.

Key facts
- Language: Python 3 (plain .py scripts). Files live at repo root and under `Homework/` subfolders.
- No external package manager files (no requirements.txt, pyproject.toml). Assume standard library only.
- Primary workflows are small script runs and file I/O exercises (CSV/JSON). See `Homework/HW5_/`,
  `Homework/HW6_/`, `Homework/HW8_/` for canonical examples.

Repository conventions & patterns
- Student/hw files follow a homework template: a header docstring with guidelines, many small functions,
  and tests guarded by `if __name__ == '__main__':`. Preserve this structure when editing.
- Naming: homework files often end with `_minh_tran.py` or `hwX_minh_tran.py`. When adding examples or tests,
  mirror the existing file-level testing style (commented tests or `__main__`).
- I/O: code reads/writes CSV and JSON using the stdlib `open`, `csv`, and `json` modules. Paths are relative
  to the repository root. Avoid introducing complex path or environment assumptions.

Build / run / test guidance
- There is no build system. Run examples with the system Python (macOS zsh):
  ```bash
  python3 Homework/HW6_/hw6.py
  python3 Homework/HW5_/hw5_minh_tran.py
  ```
- Tests are manual: look for `if __name__ == '__main__':` blocks. Preserve commented-out tests in student files.

Project-specific advice for edits
- Keep functions pure where the homework expects return values rather than prints. Many exercises assert
  return values in teacher's tests (see `hw6.py` and `hw5_minh_tran.py`). If adding helpers, provide docstrings
  consistent with existing style.
- Error handling: homework code intentionally demonstrates defensive checks (type checks, FileNotFound). Follow
  the same explicit, simple patterns rather than introducing advanced exception hierarchies.
- Data cleaning examples: use list comprehensions to filter negatives/missing values (see `hw5_minh_tran.py`).

Integration points & important files to inspect
- `Homework/HW5_/hw5_minh_tran.py` — CSV parsing, conversion to floats, average computations, file output.
- `Homework/HW6_/hw6.py` — data casting, averaging, and input retry patterns.
- `Homework/HW8_/hw8_minh_tran.py` — dictionary & JSON handling. Shows writing JSON outputs and expected shapes.
- `demo.py` — trivial script showing top-level script style.

What a helpful code change looks like
- Small, focused edits that preserve the student's function signatures and behavior. Add unit-like checks
  inside `if __name__ == '__main__':` or separate small test scripts that call functions and print results.
- When fixing bugs, prefer conservative fixes that don't change file I/O formats or output CSV/JSON schemas.

When you are unsure
- Ask for clarification about grading constraints or whether modifying input/output formats is allowed.
- If a change requires new dependencies or a test harness, propose adding a `requirements.txt` and a small
  `tests/` folder; do not add them unrequested.

Examples to reference
- Filter negatives: `buy_floats = [p for p in buy_floats if p > 0]` in `Homework/HW5_/hw5_minh_tran.py`.
- Safe file read loop: `while True: try: with open(filename): break; except FileNotFoundError: filename = input(...)`

If you change behavior significantly, leave a short comment at the top of the edited file describing the
reason for the change and how it was validated.

---
If any part of this file is unclear or you want more examples (unit tests, small runners), tell me which
homework to focus on and I will add them.
