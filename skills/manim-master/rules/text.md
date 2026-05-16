# Text

## Use Text for normal words

```python
title = Text("Vector Addition", font_size=48)
```

## Keep text short

Screen text should be brief. Narration or subcaptions can carry longer explanation.

## Labels

```python
label = Text("result", font_size=24)
label.next_to(arrow, UP)
```

## Font size guide

```txt
Title: 42-56
Body: 26-34
Label: 20-28
Formula: 34-46
```

## Avoid

- paragraph blocks,
- tiny labels,
- low contrast text,
- too many fonts,
- text touching screen edges.
