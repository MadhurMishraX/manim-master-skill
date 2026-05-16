# Use Updaters Safely

## Pattern

```python
tracker = ValueTracker(0)
dot = Dot()

dot.add_updater(lambda m: m.move_to(RIGHT * tracker.get_value()))

self.add(dot)
self.play(tracker.animate.set_value(3))
dot.clear_updaters()
```

## Rules

- clear updaters after use,
- keep updater logic simple,
- avoid depending on deleted objects,
- prefer `always_redraw` for dynamic geometry.

## Common mistakes

- forgetting `clear_updaters`,
- using too many updaters,
- making the scene slow,
- creating objects inside updater functions unnecessarily.
