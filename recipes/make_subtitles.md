# Make Subtitles

## Use when

The animation has narration or educational explanation.

## Code

```python
self.add_subcaption("We start with the unit circle.", duration=2)
self.play(Create(circle))
```

Or:

```python
self.play(
    Write(title),
    subcaption="Here is the question we want to answer.",
    subcaption_duration=2,
)
```

## Tips

- keep subtitles short,
- sync them with animation,
- avoid repeating the exact same on-screen text,
- use subtitles to carry explanation while visuals stay clean.
