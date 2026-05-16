# Manim Master Workflow

## Phase 0 - Diagnose

Before creating a serious animation, check the environment:

```bash
python --version
manim --version
ffmpeg -version
```

For MathTex-heavy projects, check LaTeX availability:

```bash
latex --version
```

Record results in `plan.md`:

```markdown
## Environment
- Python:
- Manim:
- FFmpeg:
- LaTeX:
- OS:
```

If any tool is missing, continue with a fallback only when possible:
- no LaTeX -> use `Text`, simpler formulas, or tell the user the exact install requirement.
- no ffmpeg -> render scenes but do not stitch.
- no Manim -> create files but state that rendering cannot be verified.

## Phase 1 - Plan

Create `plan.md`.

A strong plan must include:

- topic
- audience
- exact learning goal
- prerequisite knowledge
- hook
- core intuition
- scene list
- visual metaphor
- formulas
- color palette
- camera strategy
- expected duration
- implementation risks
- assumptions

Good animation is not decoration. It is thought becoming visible.

## Phase 2 - Code

Create `script.py`.

Use this structure:

```python
from manim import *

BACKGROUND = "#0b1020"
PRIMARY = BLUE_B
ACCENT = YELLOW
SECONDARY = GREEN_B

class Scene1_Hook(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        ...
```

Rules:
- Use one class per scene.
- Keep scene code readable.
- Prefer helper functions over repeated styling.
- Avoid overusing random movement.
- Keep formulas stable in the same screen region.
- Use color consistently.

## Phase 3 - Render

Start with low quality:

```bash
manim -ql script.py Scene1_Hook
```

Then render all scenes:

```bash
manim -ql script.py Scene1_Hook Scene2_CoreIdea Scene3_Conclusion
```

Use high quality only at the end:

```bash
manim -qh script.py Scene1_Hook Scene2_CoreIdea Scene3_Conclusion
```

## Phase 4 - Review

Inspect:
- readability
- pacing
- object overlap
- mathematical correctness
- transition smoothness
- scene continuity
- final frame hold

Use `templates/review.checklist.md`.

## Phase 5 - Iterate

When feedback arrives:

1. identify affected scene,
2. update only necessary code,
3. render only changed scenes,
4. restitch final video,
5. summarize changes.

Do not rewrite the whole project unless the structure is broken.

## Phase 6 - Export

Create `concat.txt`:

```txt
file 'media/videos/script/480p15/Scene1_Hook.mp4'
file 'media/videos/script/480p15/Scene2_CoreIdea.mp4'
file 'media/videos/script/480p15/Scene3_Conclusion.mp4'
```

Stitch:

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

If quality was high, paths usually use `1080p60` instead of `480p15`.

## Final response format

When done, tell the user:

- files created,
- render status,
- final video path,
- any assumptions,
- any unresolved issue.

Keep it practical. Do not over-explain.
