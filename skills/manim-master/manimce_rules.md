# ManimCE Rules

Use these rules when writing Manim Community Edition code.

## Correct framework

Use:

```python
from manim import *
```

Do not use:

```python
from manimlib import *
```

ManimCE and ManimGL are different frameworks.

## Scene classes

Use:

```python
class Scene1_Intro(Scene):
    def construct(self):
        ...
```

For moving camera:

```python
class Scene2_Zoom(MovingCameraScene):
    def construct(self):
        ...
```

For 3D:

```python
class Scene3_Surface(ThreeDScene):
    def construct(self):
        ...
```

## Reliable imports

Usually this is enough:

```python
from manim import *
```

For math helpers:

```python
import numpy as np
```

## Text

Use `Text` for normal text:

```python
title = Text("Vector Addition", font_size=48)
```

Use `MathTex` for formulas:

```python
formula = MathTex(r"\vec{a} + \vec{b} = \vec{c}")
```

Use raw strings for LaTeX:

```python
MathTex(r"\frac{d}{dx}\sin x = \cos x")
```

## Positioning

Preferred methods:

```python
obj.to_edge(UP)
obj.next_to(other, DOWN, buff=0.3)
obj.move_to(ORIGIN)
obj.shift(RIGHT * 2)
```

Avoid magic coordinates when relative positioning works better.

## Groups

Use `VGroup`:

```python
group = VGroup(title, formula, diagram).arrange(DOWN, buff=0.5)
```

## Animations

Reliable creation animations:

```python
self.play(Create(circle))
self.play(Write(formula))
self.play(FadeIn(label))
self.play(DrawBorderThenFill(square))
```

Reliable transformations:

```python
self.play(Transform(old, new))
self.play(ReplacementTransform(old, new))
self.play(TransformMatchingTex(eq1, eq2))
```

Reliable removal:

```python
self.play(FadeOut(group))
```

## Timing

Use clear pacing:

```python
self.play(Write(title), run_time=1.2)
self.wait(0.5)
```

Avoid extremely fast animations unless used intentionally.

## Updaters

Use updaters only when necessary.

Always remove updaters when done:

```python
dot.add_updater(lambda m: m.move_to(path.point_from_proportion(t.get_value())))
...
dot.clear_updaters()
```

## Graphs and axes

Use `Axes`:

```python
axes = Axes(
    x_range=[-3, 3, 1],
    y_range=[-2, 2, 1],
    x_length=7,
    y_length=4,
)
graph = axes.plot(lambda x: np.sin(x), color=BLUE)
```

Label axes:

```python
labels = axes.get_axis_labels(x_label="x", y_label="y")
```

## Tables

For dense data, use simplified visuals instead of huge tables. Manim videos are not textbooks.

## Subcaptions

Use:

```python
self.add_subcaption("We start with a unit circle.", duration=2)
```

Or:

```python
self.play(Write(title), subcaption="Here is the central question.", subcaption_duration=2)
```

## Config

Use `manim.cfg` for project-level defaults:

```ini
[CLI]
quality = low_quality
preview = false
background_color = #0b1020
```

## Avoid these mistakes

Do not:
- mix ManimGL syntax with ManimCE,
- use undefined colors or imaginary classes,
- overfill the screen,
- create 10 formulas at once,
- animate every object at the same speed,
- rely on exact media paths without checking quality folder,
- render high quality before low-quality testing.
