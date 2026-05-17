#!/usr/bin/env python3
"""
Create concat.txt and stitch rendered Manim scene videos.

Usage:
    python skills/manim-master/tools/stitch.py \
        --media-dir media/videos/script/480p15 \
        --output final.mp4
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--media-dir", required=True, help="Directory containing rendered scene mp4 files")
    parser.add_argument("--output", default="final.mp4", help="Output mp4 path")
    parser.add_argument("--concat", default="concat.txt", help="concat.txt path")
    parser.add_argument("--reencode", action="store_true", help="Re-encode instead of stream copy")
    args = parser.parse_args()

    media_dir = Path(args.media_dir)
    if not media_dir.exists():
        print(f"ERROR: media dir not found: {media_dir}", file=sys.stderr)
        return 1

    import re

    def natural_sort_key(path: Path) -> list[int | str]:
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", path.name)]

    videos = sorted(media_dir.glob("*.mp4"), key=natural_sort_key)
    if not videos:
        print(f"ERROR: no mp4 files found in {media_dir}", file=sys.stderr)
        return 1

    concat_path = Path(args.concat)
    concat_path.write_text(
        "\n".join(f"file '{video.as_posix()}'" for video in videos) + "\n",
        encoding="utf-8",
    )

    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path)]

    if args.reencode:
        cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac"]
    else:
        cmd += ["-c", "copy"]

    cmd.append(args.output)

    print(" ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
