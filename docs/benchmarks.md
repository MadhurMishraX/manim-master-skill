# Benchmarks

This document defines how to measure whether the skill is actually useful.

## Metrics

### Render success

Percentage of generated projects that render without manual edits.

### Debug success

Percentage of failed renders fixed after reading the error.

### Scene clarity

Human review score from 1 to 5:

1. confusing
2. partially clear
3. understandable
4. clear
5. excellent

### Visual quality

Review:

- spacing,
- typography,
- color discipline,
- motion purpose,
- final frame clarity.

### Time to final video

Measure:

```txt
prompt -> plan -> first render -> final render
```

## Suggested benchmark set

- derivative of sin(x)
- vector addition
- binary search
- Bayes theorem
- gradient descent
- Fourier series
- complex multiplication
- Riemann sum
- electric field lines
- eigenvectors

## Baseline comparison

Compare:

```txt
plain Claude prompt
vs
Claude with Manim Master Skill
```

Record:

- number of render attempts,
- number of syntax errors,
- number of visual review issues,
- final quality score.
