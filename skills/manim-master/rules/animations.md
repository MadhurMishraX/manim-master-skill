# Animations

## Creation

Use:

```python
self.play(Create(circle))
self.play(Write(formula))
self.play(FadeIn(label))
```

## Removal

Use:

```python
self.play(FadeOut(group))
```

## Transformations

Use:

```python
self.play(Transform(old, new))
self.play(ReplacementTransform(old, new))
self.play(TransformMatchingTex(eq1, eq2))
```

## Animation timing

Good:

```python
self.play(Write(title), run_time=1.2)
self.wait(0.5)
```

Avoid making everything too fast.

## Meaningful motion

Motion should show:

- an object becoming another object,
- a quantity changing,
- a relation appearing,
- a group forming,
- a comparison.

## Avoid

- random movement,
- excessive simultaneous animations,
- moving the camera and many objects at the same time,
- decorative motion that does not explain.
