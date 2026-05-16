# Contributing

Thanks for improving Manim Master Skill.

This project welcomes:

- new ManimCE rules,
- tested recipes,
- example projects,
- troubleshooting notes,
- visual design improvements,
- test coverage,
- documentation fixes.

## Contribution standards

Every contribution should be:

1. useful in real ManimCE projects,
2. clear enough for an agent to follow,
3. tested where possible,
4. free from hidden Unicode characters,
5. written in plain Markdown or Python.

## Good contribution types

### Add a recipe

Place it in:

```txt
recipes/
```

Use this structure:

```markdown
# Recipe Name

## Use when

## Pattern

## Code

## Common mistakes

## Render command
```

### Add a rule file

Place it in:

```txt
skills/manim-master/rules/
```

Keep rules practical. Prefer examples over theory.

### Add an example

Place it in:

```txt
examples/example_name/
```

Each example should include:

```txt
plan.md
script.py
README.md
```

Do not commit generated `media/` outputs.

## Local checks

```bash
pip install -r requirements-dev.txt
pytest
```

## Style

Use clear writing. Avoid filler. Give commands that work.

## Pull request checklist

- [ ] No generated media committed
- [ ] Python syntax passes
- [ ] Markdown is readable
- [ ] No hidden Unicode
- [ ] New examples include render commands
- [ ] New rules include working code snippets
