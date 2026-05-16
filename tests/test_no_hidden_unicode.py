from pathlib import Path

BAD_CHARS = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\ufeff": "BOM",
    "\u2060": "WORD JOINER",
}


def test_no_hidden_unicode_characters():
    root = Path(__file__).resolve().parents[1]
    problems = []

    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for char, name in BAD_CHARS.items():
            if char in text:
                problems.append(f"{path.relative_to(root)} contains {name}")

    assert not problems, "\n".join(problems)
