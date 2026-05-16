# Graphs and Axes

## Basic axes

```python
axes = Axes(
    x_range=[-3, 3, 1],
    y_range=[-2, 2, 1],
    x_length=7,
    y_length=4,
)
```

## Plot function

```python
graph = axes.plot(lambda x: np.sin(x), color=BLUE)
```

## Labels

```python
labels = axes.get_axis_labels(x_label="x", y_label="y")
```

## Coordinate point

```python
point = axes.c2p(1, np.sin(1))
dot = Dot(point, color=YELLOW)
```

## Good graph animation

```python
self.play(Create(axes), Write(labels))
self.play(Create(graph))
self.play(FadeIn(dot))
```

## Avoid

- unlabeled axes,
- too many graphs at once,
- colors without meaning,
- graph lines too thin to see.
