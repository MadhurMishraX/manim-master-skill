# Create Graph Scene

## Use when

You need axes, a function graph, and a highlighted point.

## Code

```python
from manim import *
import numpy as np

class GraphSceneExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=4,
        )
        labels = axes.get_axis_labels("x", "y")
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        dot = Dot(axes.c2p(1, np.sin(1)), color=YELLOW)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.play(FadeIn(dot))
        self.wait(1)
```

## Common mistakes

- forgetting `import numpy as np`,
- making axes too large,
- not labeling axes,
- plotting too many functions at once.
