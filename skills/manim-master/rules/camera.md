# Camera

## Use default camera when possible

Most scenes do not need camera movement.

## Moving camera

Use:

```python
class Scene2_Zoom(MovingCameraScene):
    def construct(self):
        self.play(self.camera.frame.animate.scale(0.6).move_to(target))
```

## Camera movement should explain

Use camera movement to:

- focus on detail,
- reveal structure,
- compare regions,
- move from example to abstraction.

## Avoid

- constant zooming,
- fast camera motion,
- moving camera while many objects move,
- making text hard to read.
