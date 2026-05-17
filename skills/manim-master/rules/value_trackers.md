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

Avoid compiling LaTeX (`MathTex`) inside updaters or `always_redraw()` dynamically, as it spawns external LaTeX subprocesses on every single frame and severely slows down rendering.

Instead, use `DecimalNumber` (or `Variable`), which dynamically updates vector text directly in memory:

```python
# Create the decimal label once
label = DecimalNumber(t.get_value(), num_decimal_places=2)
label.next_to(dot, UP)

# Update value and keep it positioned next to the moving dot
label.add_updater(lambda d: d.set_value(t.get_value()))
label.add_updater(lambda d: d.next_to(dot, UP))
```

Or for simple, non-equation labels, use `always_redraw` with standard `Text` (which does not trigger the LaTeX compiler):

```python
label = always_redraw(
    lambda: Text(f"x = {t.get_value():.2f}", font_size=24).next_to(dot, UP)
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
