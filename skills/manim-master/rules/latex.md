# LaTeX and MathTex

## Use raw strings

Good:

```python
MathTex(r"\frac{d}{dx}\sin x = \cos x")
```

Bad:

```python
MathTex("\frac{d}{dx}\sin x = \cos x")
```

## Keep formulas readable

```python
formula = MathTex(r"a^2 + b^2 = c^2", font_size=44)
```

## Transform formulas

```python
eq1 = MathTex(r"a^2 + b^2 = c^2")
eq2 = MathTex(r"c = \sqrt{a^2 + b^2}")
self.play(TransformMatchingTex(eq1, eq2))
```

## Debugging

If MathTex fails:

1. check LaTeX installation,
2. simplify the expression,
3. test the formula alone,
4. replace with `Text` temporarily if needed.

## Avoid

- unescaped backslashes,
- huge formulas,
- changing notation mid-scene,
- using too many formulas at once.
