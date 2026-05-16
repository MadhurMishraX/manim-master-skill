# Claude Prompt Library

Use these prompts with the skill.

## Create a full animation

```txt
Create a ManimCE animation explaining [topic].
Use a clear scene-by-scene plan first.
Make it 16:9, about [duration].
Use subtitles.
Render low quality first, then high quality only after it works.
```

## Fix a Manim error

```txt
This ManimCE script failed. Read the error carefully, identify the exact cause, and fix the smallest possible part. Do not rewrite the whole script unless necessary.

[error log]
[script]
```

## Improve visual quality

```txt
Review this Manim scene for visual clarity.
Find clutter, small text, weak pacing, bad color use, and unclear motion.
Then rewrite only the scene that needs improvement.
```

## Convert proof to animation

```txt
Convert this proof into a ManimCE explainer.
First write a plan with scenes.
Show the intuition before the formal algebra.
Keep notation consistent.

[proof]
```

## Create a recipe

```txt
Write a reusable ManimCE recipe for [pattern].
Include use cases, code, common mistakes, and render command.
```

## Make it less cluttered

```txt
This scene has too much on screen.
Refactor it so only one main idea appears at a time.
Use grouping, spacing, and progressive reveal.
```

## Render only changed scenes

```txt
Only scenes [names] changed.
Render only those scenes, then restitch final.mp4.
Do not rerender unchanged scenes.
```
