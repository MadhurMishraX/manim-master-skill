# Architecture

Manim Master Skill is split into four layers.

## 1. Skill entrypoint

```txt
skills/manim-master/SKILL.md
```

This file tells Claude when and how to use the skill.

It should stay focused and not become a giant textbook. It points to rule files and templates.

## 2. Rule library

```txt
skills/manim-master/rules/
```

These files teach Claude safe ManimCE patterns:

- scenes
- animations
- mobjects
- text
- LaTeX
- graphs
- camera
- 3D
- updaters
- performance

## 3. Templates and tools

```txt
skills/manim-master/templates/
skills/manim-master/tools/
```

Templates help create a consistent project structure.

Tools help render and stitch videos.

## 4. Public learning layer

```txt
docs/
recipes/
examples/
```

This layer helps humans understand and trust the repo.

## Why progressive disclosure matters

A skill should not put every rule into one huge file. Claude should load the most relevant document for the current task.

Good pattern:

```txt
SKILL.md -> workflow.md -> specific rule file -> template/tool
```

## Project output architecture

A generated Manim project should look like:

```txt
project-name/
|-- plan.md
|-- script.py
|-- manim.cfg
|-- concat.txt
|-- final.mp4
`-- media/
```

The skill files should never be modified inside a generated project.
