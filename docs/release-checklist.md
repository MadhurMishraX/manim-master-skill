# Release Checklist

Before making a release:

## Repository

- [ ] README is current
- [ ] LICENSE is present
- [ ] CHANGELOG is updated
- [ ] ROADMAP is updated
- [ ] No generated media committed
- [ ] No hidden Unicode
- [ ] CI passes

## Skill

- [ ] `skills/manim-master/SKILL.md` has valid frontmatter
- [ ] Rule files are linked
- [ ] Templates are present
- [ ] Tools are present
- [ ] Examples still render or at least pass syntax checks

## Docs

- [ ] Install command is correct
- [ ] Examples have render commands
- [ ] Troubleshooting is updated
- [ ] Recipes are clear

## Tag

```bash
git tag v0.1.0
git push origin v0.1.0
```
