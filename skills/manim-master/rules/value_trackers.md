# ValueTrackers

Use `ValueTracker` to animate changing numbers.

## Basic pattern

```python
t = ValueTracker(0)

dot = always_redraw(lambda: Dot(axes.c2p(t.get_value(), np.sin(t.get_value()))))

self.add(dot)
self.play(t.animate.set_value(PI), run_time=3)
```

## Dynamic labels

```python
label = always_redraw(
    lambda: MathTex(f"x={t.get_value():.2f}").next_to(dot, UP)
)
```

## Use when

- a point moves along a graph,
- a parameter changes,
- a tangent line updates,
- a numerical display follows an animation.

## Avoid

- using trackers for simple one-time movement,
- too many dynamic labels,
- high precision values on screen.
