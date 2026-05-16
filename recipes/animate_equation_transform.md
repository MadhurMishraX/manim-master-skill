# Animate Equation Transform

## Use when

You need to show one formula becoming another while preserving meaning.

## Pattern

```python
eq1 = MathTex(r"a^2 + b^2 = c^2")
eq2 = MathTex(r"c = \sqrt{a^2 + b^2}")

self.play(Write(eq1))
self.wait(0.5)
self.play(TransformMatchingTex(eq1, eq2))
self.wait(1)
```

## Common mistakes

- changing notation between equations,
- transforming formulas with no visual reason,
- using formulas too small to read,
- showing too many algebra steps at once.

## Render

```bash
manim -ql script.py SceneName
```
