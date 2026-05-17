#!/usr/bin/env python3
"""
Render all Scene classes in a ManimCE script.

Usage:
    python skills/manim-master/tools/render_all.py script.py -q l
    python skills/manim-master/tools/render_all.py script.py -q h
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path

SCENE_BASES = {
    "Scene",
    "MovingCameraScene",
    "ThreeDScene",
    "ZoomedScene",
    "GraphScene",
}


def get_scene_classes(script_path: Path) -> list[str]:
    tree = ast.parse(script_path.read_text(encoding="utf-8"))
    scenes: list[str] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue

        for base in node.bases:
            if isinstance(base, ast.Name) and base.id in SCENE_BASES:
                scenes.append(node.name)
            elif isinstance(base, ast.Attribute) and base.attr in SCENE_BASES:
                scenes.append(node.name)

    return scenes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", help="Path to Manim script.py")
    parser.add_argument("-q", "--quality", default="l", choices=["l", "m", "h", "k"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    script_path = Path(args.script)
    if not script_path.exists():
        print(f"ERROR: script not found: {script_path}", file=sys.stderr)
        return 1

    scenes = get_scene_classes(script_path)
    if not scenes:
        print("ERROR: no Scene classes found.", file=sys.stderr)
        return 1

    cmd = ["manim", f"-q{args.quality}", str(script_path), *scenes]
    print(" ".join(cmd))

    if args.dry_run:
        return 0

    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
