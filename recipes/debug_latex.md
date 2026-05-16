# Debug LaTeX

## Symptoms

- MathTex fails
- error mentions latex
- error mentions dvisvgm
- formula does not appear

## Fix checklist

1. Use raw strings.
2. Test the formula alone.
3. Simplify the formula.
4. Check LaTeX installation.
5. Replace with `Text` temporarily if needed.

## Good

```python
MathTex(r"\frac{a}{b}")
```

## Bad

```python
MathTex("\frac{a}{b}")
```

## Minimal test

```python
from manim import *

class LatexSmoke(Scene):
    def construct(self):
        self.play(Write(MathTex(r"x^2 + y^2 = z^2")))
        self.wait()
```
