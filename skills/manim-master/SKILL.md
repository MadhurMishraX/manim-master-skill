---
name: manim-master
description: |
  Create production-quality Manim Community Edition animations with Claude.
  Use for mathematical animations, science explainers, equation visualizations,
  proof animations, algorithm visualizations, educational videos, and Manim code.
  Follows Diagnose -> Plan -> Code -> Render -> Review -> Iterate.
---

# Manim Master Skill

You are helping the user create accurate, beautiful, production-grade animations using Manim Community Edition.

Use this skill for:
- ManimCE code generation
- mathematical animations
- science explainers
- proof visualizations
- algorithm animations
- equation derivations
- educational videos

Use Manim Community Edition unless the user explicitly asks for ManimGL. ManimCE and ManimGL are different frameworks and their code should not be mixed.

## Prime directive

Make the animation:

1. Correct - conceptually and mathematically accurate.
2. Renderable - works in real ManimCE.
3. Clear - one idea at a time.
4. Beautiful - strong spacing, pacing, color, typography, and motion.
5. Iterative - render, inspect, fix, then improve.

## Mandatory workflow

Follow this sequence:

```txt
Diagnose -> Plan -> Code -> Render -> Review -> Iterate -> Export
```

Read the supporting files when needed:

- `workflow.md` - full operating procedure
- `manimce_rules.md` - ManimCE coding rules and safe API patterns
- `visual_quality.md` - visual design rules
- `troubleshooting.md` - common render/debug fixes
- `templates/plan.template.md` - planning structure
- `templates/script.template.py` - starter ManimCE script
- `templates/review.checklist.md` - final QA checklist

## Core rules

Use:

```python
from manim import *
```

Do not use:

```python
from manimlib import *
```

Create a dedicated project folder in the user's current working directory:

```txt
<project-name>/
|-- plan.md
|-- script.py
|-- manim.cfg
|-- concat.txt
|-- final.mp4
`-- media/
```

Never write project files inside the skill directory.

Before coding, create or update `plan.md`.

If details are missing, make reasonable assumptions and record them under:

```markdown
## Assumptions
```

Do not block the task unless a missing detail makes the video impossible.

## Coding rules

- Use one class per scene.
- Use descriptive scene class names.
- Use helper functions for repeated styling.
- Use `VGroup` for grouped objects.
- Use `.animate` for simple transformations.
- Use `Transform`, `ReplacementTransform`, and `TransformMatchingTex` carefully.
- Add `self.wait()` after important visual moments.
- Add subcaptions when narration is implied.

## Rendering

Use low quality first:

```bash
manim -ql script.py Scene1_Hook
```

Render only failed or changed scenes while debugging.

Use high quality only after all scenes are correct:

```bash
manim -qh script.py Scene1_Hook Scene2_CoreIdea Scene3_Derivation
```

## Stitching

After all scenes render, create `concat.txt` and use ffmpeg:

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

If codec copying fails, re-encode:

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c:v libx264 -pix_fmt yuv420p -c:a aac final.mp4
```

## Quality control

Before final answer, check:

- all scene files exist,
- final video exists,
- no clipped text,
- no overlapping labels,
- formulas are readable,
- camera framing is stable,
- subtitles are present when needed,
- scene order is correct,
- final frame holds long enough.

## Style guidance

Use clear educational visualization principles:
- build intuition visually,
- reveal information gradually,
- use spatial metaphors,
- keep notation alive on screen,
- connect symbols to geometry.

## When errors happen

Never guess blindly.

Read the error message, identify the exact failing line, fix the smallest cause, and re-render only the affected scene.

Use `troubleshooting.md`.
