# Scenes

## Use one class per scene

```python
class Scene1_Hook(Scene):
    def construct(self):
        ...
```

## Scene naming

Good:

```python
Scene1_Hook
Scene2_CoreIdea
Scene3_Derivation
Scene4_Conclusion
```

Bad:

```python
Scene1
Test
Final
Demo
```

## Scene responsibilities

A scene should usually do one job:

- introduce the question,
- build the visual model,
- transform the formula,
- show the result,
- summarize the insight.

## Scene pacing

Use short waits after important moments:

```python
self.wait(0.5)
```

Use longer waits for final frames:

```python
self.wait(2)
```

## Setup helper

Use a helper function:

```python
def apply_style(scene: Scene) -> None:
    scene.camera.background_color = "#0B1020"
```

## Avoid

- huge scenes with 200 lines of unrelated logic,
- multiple unrelated ideas in one scene,
- leaving old objects on screen without purpose,
- making every scene start from scratch if continuity matters.
