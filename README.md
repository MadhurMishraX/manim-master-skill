# Manim Master Skill

A production-grade Claude Skill for creating accurate, beautiful, and reliable Manim Community Edition animations.

This repository helps Claude plan, code, render, debug, review, and refine mathematical and scientific animations using a disciplined workflow.

```txt
Diagnose -> Plan -> Code -> Render -> Review -> Iterate -> Export
```

## What this is

Manim Master Skill is built for people who want Manim animations that are not just renderable, but actually useful as explanations.

It gives Claude:

- a structured animation workflow,
- ManimCE-specific coding rules,
- visual design rules,
- debugging playbooks,
- tested starter templates,
- reusable recipes,
- example projects,
- CI checks,
- and review checklists.

## Why it exists

Most generated Manim code has at least one of these problems:

1. It does not render.
2. It mixes ManimCE and ManimGL syntax.
3. It looks cluttered.
4. It teaches the concept unclearly.
5. It has no debugging strategy.
6. It has no review loop.
7. It ignores LaTeX, ffmpeg, path, and version problems.

This skill fixes those problems by giving Claude a practical operating system for Manim work.

## Features

- Manim Community Edition first
- Planning templates
- Scene-by-scene workflow
- Render helpers
- ffmpeg stitching helper
- Visual quality rules
- Math correctness checks
- LaTeX troubleshooting
- Camera and 3D guidance
- Recipes for common animation patterns
- Example projects
- Smoke tests
- GitHub Actions CI
- Contribution guidelines

## Repository structure

```txt
manim-master-skill/
|-- README.md
|-- LICENSE
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- CHANGELOG.md
|-- ROADMAP.md
|-- pyproject.toml
|-- requirements-dev.txt
|-- .gitignore
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- docs/
|   |-- architecture.md
|   |-- benchmarks.md
|   |-- claude-prompts.md
|   |-- design-principles.md
|   |-- manimce-vs-manimgl.md
|   `-- release-checklist.md
|-- examples/
|   |-- derivative_sine/
|   |-- vector_addition/
|   `-- binary_search/
|-- recipes/
|   |-- animate_equation_transform.md
|   |-- create_graph_scene.md
|   |-- debug_latex.md
|   |-- make_subtitles.md
|   |-- stitch_scenes.md
|   |-- use_updaters_safely.md
|   `-- use_value_tracker.md
|-- skills/
|   `-- manim-master/
|       |-- SKILL.md
|       |-- workflow.md
|       |-- troubleshooting.md
|       |-- visual_quality.md
|       |-- manimce_rules.md
|       |-- rules/
|       |   |-- animations.md
|       |   |-- camera.md
|       |   |-- colors.md
|       |   |-- graphs.md
|       |   |-- latex.md
|       |   |-- mobjects.md
|       |   |-- performance.md
|       |   |-- scenes.md
|       |   |-- text.md
|       |   |-- three_d.md
|       |   |-- updaters.md
|       |   `-- value_trackers.md
|       |-- templates/
|       |   |-- manim.cfg
|       |   |-- plan.template.md
|       |   |-- review.checklist.md
|       |   `-- script.template.py
|       `-- tools/
|           |-- render_all.py
|           `-- stitch.py
`-- tests/
    |-- smoke_scene.py
    |-- test_no_hidden_unicode.py
    |-- test_skill_structure.py
    `-- test_python_syntax.py
```

## Install the skill

```bash
npx skills add MadhurMishraX/manim-master-skill/skills/manim-master
```

## Install ManimCE locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install manim
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install manim
```

Verify:

```bash
python --version
manim --version
ffmpeg -version
```

For `MathTex`, install LaTeX:

- macOS: MacTeX
- Linux: TeX Live
- Windows: MiKTeX

## Quick start prompt

```txt
Create a Manim animation explaining why the derivative of sin(x) is cos(x).
Use a unit circle visual first, then connect it to the limit idea.
Make it 16:9, about 90 seconds, with clean subtitles.
```

Claude should create:

```txt
project-name/
|-- plan.md
|-- script.py
|-- manim.cfg
|-- concat.txt
|-- final.mp4
`-- media/
```

## Development render

```bash
manim -ql script.py Scene1_Hook
```

## Final render

```bash
manim -qh script.py Scene1_Hook Scene2_CoreIdea Scene3_Conclusion
```

## Stitch scenes

```bash
python skills/manim-master/tools/stitch.py --media-dir media/videos/script/480p15 --output final.mp4
```

## Run tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Design philosophy

A good mathematical animation is not decoration. It is a controlled sequence of attention.

This skill treats animation like explanation:

- define the confusion,
- build a visual model,
- connect the visual to notation,
- reveal the pattern,
- finish with a clean takeaway.

## License

MIT License.
