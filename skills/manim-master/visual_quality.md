# Visual Quality Rules

The goal is not merely to render. The goal is to make thought visible.

## Quality checklist

A Manim scene is low quality if:

- everything appears at once,
- text is too small,
- formulas overlap,
- colors are random,
- motion has no meaning,
- camera zooms for no reason,
- the scene has no visual hierarchy,
- important objects are not highlighted,
- the viewer does not know where to look.

## Visual hierarchy

Every frame should have:

1. one main focus,
2. one supporting context,
3. minimal decoration.

If the viewer has to search for the important object, the scene failed.

## Color discipline

Use a small palette:

```txt
Background: dark navy / black
Primary: blue/cyan for main objects
Accent: yellow/orange for key insight
Secondary: green/purple for supporting objects
Error/contrast: red only when meaningful
```

Never use many saturated colors randomly.

## Spacing

Rules:
- Keep margins.
- Avoid touching screen edges.
- Leave breathing room between formulas and diagrams.
- Use `arrange`, `next_to`, and `to_edge`.

## Typography

Use:
- large titles,
- medium labels,
- readable formulas,
- short text.

Avoid paragraphs on screen. Narration can carry long explanation.

## Motion

Good motion explains.

Use motion to show:
- cause and effect,
- transformation,
- grouping,
- continuity,
- comparison,
- emergence of a pattern.

Do not move objects just to look fancy.

## Camera

Use camera movement only when it improves understanding.

Good camera use:
- zoom into a detail,
- pan from concrete example to abstraction,
- reveal a larger structure.

Bad camera use:
- constant movement,
- dramatic zooms without educational purpose,
- making text harder to read.

## Mathematical beauty

For equations:
- keep related terms spatially aligned,
- use `TransformMatchingTex` when transforming formulas,
- color the same symbol consistently,
- do not change notation mid-video.

Example:

```python
eq1 = MathTex(r"a^2 + b^2 = c^2")
eq2 = MathTex(r"c = \sqrt{a^2 + b^2}")
self.play(TransformMatchingTex(eq1, eq2))
```

## Scene rhythm

A strong explainer usually follows:

1. hook,
2. concrete example,
3. visual model,
4. symbolic form,
5. generalization,
6. final insight.

## Final frame

End with a clean final frame:
- one key formula,
- one core visual,
- one short takeaway.

Hold it long enough:

```python
self.wait(2)
```
