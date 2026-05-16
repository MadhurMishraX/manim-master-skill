# Mobjects

## Basic objects

```python
circle = Circle(radius=1.5)
square = Square(side_length=2)
dot = Dot()
line = Line(LEFT, RIGHT)
arrow = Arrow(LEFT, RIGHT)
```

## Groups

Use `VGroup` for layout:

```python
group = VGroup(title, formula, diagram).arrange(DOWN, buff=0.5)
```

## Styling

```python
circle.set_stroke(BLUE, width=4)
circle.set_fill(BLUE, opacity=0.2)
```

## Positioning

```python
obj.to_edge(UP)
obj.next_to(other, DOWN, buff=0.3)
obj.move_to(ORIGIN)
obj.shift(RIGHT * 2)
```

## Copying

Use `.copy()` when transforming while keeping the original:

```python
copy = formula.copy()
self.play(copy.animate.next_to(diagram, DOWN))
```

## Avoid

- manually hardcoding every coordinate,
- placing text without margins,
- creating duplicate objects accidentally,
- adding objects twice without needing to.
