# Performance

## Draft first

Use:

```bash
manim -ql script.py SceneName
```

Only render high quality when the scene works.

## Reduce render cost

- reduce surface resolution,
- avoid unnecessary updaters,
- avoid thousands of tiny objects,
- render only changed scenes,
- keep animations simple.

## Cache

Manim caching helps repeated renders. Do not disable it unless debugging cache issues.

## Heavy scenes

For heavy scenes:

- split into multiple scenes,
- reduce object count,
- use lower resolution while drafting,
- avoid complex 3D rotations.
