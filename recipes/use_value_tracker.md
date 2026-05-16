# Use ValueTracker

## Pattern

```python
t = ValueTracker(0)

number = always_redraw(
    lambda: DecimalNumber(t.get_value()).to_edge(UP)
)

self.add(number)
self.play(t.animate.set_value(10), run_time=2)
self.wait()
```

## Use for

- moving points,
- changing angles,
- updating labels,
- dynamic graph demonstrations.

## Avoid

- showing too many changing numbers,
- using high precision values,
- animating values without explaining what they mean.
