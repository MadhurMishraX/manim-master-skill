---
name: manim-master
description: |
  Create production-quality Manim Community Edition animations with Claude.
  Use when the user asks for Manim code, mathematical animations, science explainers,
  equation visualizations, proof animations, algorithm visualizations, or educational videos.
  Follows Diagnose -> Plan -> Code -> Render -> Review -> Iterate -> Export.
---

# Manim Master Skill

You are helping the user create accurate, clear, and beautiful animations using Manim Community Edition.

Use this skill for:

- ManimCE code generation
- mathematical animations
- science explainers
- proof visualizations
- algorithm animations
- equation derivations
- educational videos
- debugging Manim render errors
- improving existing Manim scenes

## Main workflow

Always follow:

```txt
Diagnose -> Plan -> Code -> Render -> Review -> Iterate -> Export
```

## Framework rule

Use Manim Community Edition by default.

Use:

```python
from manim import *
```

Do not use:

```python
from manimlib import *
```

Only use ManimGL if the user explicitly asks for it.

## Project structure

Create generated animation projects in the user's current working directory, not inside this skill directory.

Use:

```txt
project-name/
|-- plan.md
|-- script.py
|-- manim.cfg
|-- concat.txt
|-- final.mp4
`-- media/
```

## Before coding

Create or update `plan.md`.

Include:

- topic
- target audience
- learning goal
- assumptions
- scene list
- visual metaphor
- formulas
- color palette
- render plan
- possible risks

If the user gives enough information, do not ask extra questions. Make reasonable assumptions and record them.

## During coding

- Use one class per scene.
- Name scenes clearly.
- Keep helper functions at the top.
- Use `VGroup` for layout.
- Use `MathTex` for formulas.
- Use `Text` for plain text.
- Use raw strings for LaTeX.
- Use subcaptions when narration is implied.
- Keep colors consistent.
- Avoid clutter.

## Rendering

Use low quality first:

```bash
manim -ql script.py Scene1_Hook
```

Render only failed or changed scenes while debugging.

Use high quality only after the scene is correct:

```bash
manim -qh script.py Scene1_Hook Scene2_CoreIdea Scene3_Conclusion
```

## Review

Before final output, check:

- no clipped text
- no overlapping labels
- readable formulas
- stable camera
- meaningful motion
- clear final frame
- correct scene order
- enough wait time after key moments

## Supporting files

Read these when relevant:

- `workflow.md`
- `manimce_rules.md`
- `visual_quality.md`
- `troubleshooting.md`
- `rules/scenes.md`
- `rules/animations.md`
- `rules/mobjects.md`
- `rules/text.md`
- `rules/latex.md`
- `rules/graphs.md`
- `rules/camera.md`
- `rules/three_d.md`
- `rules/updaters.md`
- `rules/value_trackers.md`
- `rules/performance.md`

## Error handling

When an error occurs:

1. Read the exact error.
2. Identify the failing line.
3. Fix the smallest cause.
4. Re-render only the affected scene.
5. Do not rewrite the whole file unless the structure is broken.

## Final response

Report:

- what files were created,
- render command used,
- final video path,
- any assumptions,
- any unresolved issue.
