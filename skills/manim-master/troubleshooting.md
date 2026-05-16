# Troubleshooting ManimCE

## Command not found: manim

Check:

```bash
python -m pip show manim
python -m manim --version
```

Use:

```bash
python -m manim -ql script.py Scene1_Hook
```

## FFmpeg missing

Check:

```bash
ffmpeg -version
```

Install ffmpeg using the OS package manager.

## LaTeX error

Symptoms:
- `MathTex` fails.
- Error mentions `latex`, `dvisvgm`, `standalone`, or missing packages.

Fix:
- Install a full LaTeX distribution.
- Use raw strings in MathTex.
- Simplify formulas.
- Temporarily replace `MathTex` with `Text` to continue visual work.

Bad:

```python
MathTex("\frac{a}{b}")
```

Good:

```python
MathTex(r"\frac{a}{b}")
```

## Scene does not appear in output

Check class name and command:

```bash
manim -ql script.py Scene1_Hook
```

The class name must exactly match.

## Text clipped

Fix:
- reduce `font_size`,
- use `.scale(0.8)`,
- use `.to_edge()`,
- use `.arrange()`,
- split text into multiple objects.

## Objects overlap

Use:

```python
group = VGroup(a, b, c).arrange(DOWN, buff=0.4)
```

Or:

```python
b.next_to(a, DOWN, buff=0.3)
```

## TransformMatchingTex behaves strangely

This happens when LaTeX substrings do not match cleanly.

Fix:
- use consistent tokens,
- split formulas into parts,
- use `Transform` or `ReplacementTransform` instead.

## Updater keeps running

Clear it:

```python
mobject.clear_updaters()
```

## final.mp4 not created

Check:
- `concat.txt` paths,
- quality folder name,
- scene files exist,
- ffmpeg is installed.

Use:

```bash
find media/videos -name "*.mp4"
```

## ffmpeg concat fails with codec issue

Use re-encode:

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c:v libx264 -pix_fmt yuv420p -c:a aac final.mp4
```

## Render is too slow

Use:
- `-ql` during development,
- fewer particles,
- fewer updaters,
- simpler surfaces,
- lower frame rate in config.

## 3D scene looks flat

Use:

```python
self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
```

Add axes and labels for orientation.
