# Manim Master Skill for Claude

A production-focused Claude Skill for creating clear, accurate, beautiful mathematical and scientific animations with Manim Community Edition.

It helps Claude follow a reliable workflow:

**Diagnose -> Plan -> Code -> Render -> Review -> Iterate -> Export**

This skill is designed for:
- Mathematical explainers
- Physics and science visualizations
- Algorithm animations
- Equation derivations
- Proof visualizations
- 3Blue1Brown-inspired educational videos without copying protected assets

## Why this skill exists

Most AI-generated Manim code fails in one of four ways:

1. It looks generic and visually cluttered.
2. It renders partially but breaks on later scenes.
3. It teaches the concept incorrectly.
4. It ignores real ManimCE constraints such as LaTeX, ffmpeg, scene paths, and version differences.

This skill fixes that by forcing Claude to:
- plan the narrative first,
- use tested ManimCE patterns,
- render incrementally,
- debug from actual errors,
- protect mathematical correctness,
- use high-quality visual design rules,
- and export a clean final video.

## Installation

### Add the skill

```bash
npx skills add <your-github-username>/manim-master-skill/skills/manim-master
```

### Install Manim Community Edition

Recommended local setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install manim
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install manim
```

Verify:

```bash
manim --version
ffmpeg -version
```

For MathTex/Tex rendering, install LaTeX:
- macOS: MacTeX
- Linux: TeX Live
- Windows: MiKTeX

## Basic usage with Claude

Ask Claude:

```txt
Create a Manim animation explaining why the derivative of sin(x) is cos(x).
Use a visual unit circle explanation, then show the limit idea.
Make it 16:9, about 90 seconds.
```

Claude should create a folder like:

```txt
derivative-sine/
|-- plan.md
|-- script.py
|-- manim.cfg
|-- concat.txt
|-- final.mp4
`-- media/
```

## Quality levels

Use low quality while developing:

```bash
manim -ql script.py Scene1_Intro
```

Use high quality only after the scene is correct:

```bash
manim -qh script.py Scene1_Intro
```

## Core rules

- Use Manim Community Edition: `from manim import *`
- Do not mix ManimCE with ManimGL syntax.
- Create one class per scene.
- Render and debug one scene at a time before stitching.
- Use subtitles with `add_subcaption()` when narration is implied.
- Keep mathematical notation consistent.
- Prefer clarity over decoration.
- Avoid copyrighted 3Blue1Brown-specific assets such as Pi creatures.
- Use 3Blue1Brown-inspired clarity, not copied identity.

## License

MIT License.
