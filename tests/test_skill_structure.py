from pathlib import Path


def test_required_files_exist():
    root = Path(__file__).resolve().parents[1]

    required = [
        "README.md",
        "LICENSE",
        "skills/manim-master/SKILL.md",
        "skills/manim-master/workflow.md",
        "skills/manim-master/manimce_rules.md",
        "skills/manim-master/visual_quality.md",
        "skills/manim-master/troubleshooting.md",
        "skills/manim-master/templates/script.template.py",
        "skills/manim-master/templates/plan.template.md",
        "skills/manim-master/tools/render_all.py",
        "skills/manim-master/tools/stitch.py",
    ]

    missing = [path for path in required if not (root / path).exists()]
    assert not missing, "Missing files: " + ", ".join(missing)


def test_skill_frontmatter():
    skill = Path(__file__).resolve().parents[1] / "skills/manim-master/SKILL.md"
    text = skill.read_text(encoding="utf-8")
    assert text.startswith("---")
    assert "name: manim-master" in text
    assert "description:" in text
