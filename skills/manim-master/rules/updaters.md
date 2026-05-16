# Updaters

Updaters are powerful, but easy to misuse.

## Basic updater

```python
dot.add_updater(lambda m: m.next_to(line, UP))
```

## Clear updaters

Always clear when done:

```python
dot.clear_updaters()
```

## Use with ValueTracker

```python
t = ValueTracker(0)
dot.add_updater(lambda m: m.move_to(axes.c2p(t.get_value(), 0)))
self.play(t.animate.set_value(3))
dot.clear_updaters()
```

## Avoid

- many updaters in one scene,
- updaters that depend on deleted objects,
- forgetting to clear updaters,
- using updaters when normal animations are enough.
