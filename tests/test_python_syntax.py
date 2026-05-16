import ast
from pathlib import Path


def test_python_files_parse():
    root = Path(__file__).resolve().parents[1]
    problems = []

    for path in root.rglob("*.py"):
        if ".venv" in path.parts or "venv" in path.parts:
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            problems.append(f"{path.relative_to(root)}: {exc}")

    assert not problems, "\n".join(problems)
