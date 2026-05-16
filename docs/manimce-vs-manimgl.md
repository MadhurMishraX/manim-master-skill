# ManimCE vs ManimGL

Manim has two major branches that people often confuse.

## Manim Community Edition

Use:

```python
from manim import *
```

Render with:

```bash
manim -ql script.py SceneName
```

Best for:

- stable educational videos,
- documentation-backed development,
- community support,
- reproducible rendering,
- beginner to advanced projects.

## ManimGL

Use:

```python
from manimlib import *
```

Render with:

```bash
manimgl script.py SceneName
```

Best for:

- interactive work,
- 3Blue1Brown-style internal workflows,
- OpenGL-heavy projects,
- advanced users who know the differences.

## Do not mix them

These are wrong in a ManimCE project:

```python
from manimlib import *
class Demo(InteractiveScene):
    ...
```

These are right in a ManimCE project:

```python
from manim import *
class Demo(Scene):
    ...
```

## Skill policy

This repository focuses on Manim Community Edition.

Only use ManimGL if the user explicitly requests it.
