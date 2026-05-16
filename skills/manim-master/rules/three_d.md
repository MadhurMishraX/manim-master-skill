# 3D Scenes

## Basic 3D scene

```python
class Scene3_Surface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
```

## Surface

```python
surface = Surface(
    lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
    u_range=[-3, 3],
    v_range=[-3, 3],
    resolution=(24, 24),
)
```

## Tips

- use fewer polygons during drafts,
- label axes,
- avoid dense text in 3D scenes,
- keep camera movement slow.

## Avoid

- complex 3D before 2D intuition,
- high resolution surfaces during testing,
- unexplained camera rotations.
