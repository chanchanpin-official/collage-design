#!/usr/bin/env python3
"""Prepare installable fonts outside the skill's upload directory."""
import argparse
from pathlib import Path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    skill = Path(__file__).resolve().parent.parent
    source = skill / "assets" / "fonts"
    output = args.output_dir.expanduser().resolve()
    if output == skill or skill in output.parents:
        parser.error("Choose an output directory outside the skill upload folder.")
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        parser.exit(1, "Install the dependency in your Python environment: pip install 'fonttools[woff]'\n")

    names = ["NotoSansSC-VF.ttf", "SpaceGrotesk-VF.ttf", "Anton-Regular.ttf",
             "NotoSansSC-OFL.txt", "SpaceGrotesk-OFL.txt", "Anton-OFL.txt"]
    conflicts = [name for name in names if (output / name).exists()]
    if conflicts:
        parser.error("Output files already exist; choose an empty folder: " + ", ".join(conflicts))
    output.mkdir(parents=True, exist_ok=True)
    try:
        with TTFont(source / "NotoSansSC-VF.woff2") as font:
            font.flavor = None
            font.save(output / names[0])
    except ImportError:
        parser.exit(1, "WOFF2 support requires: pip install 'fonttools[woff]'\n")
    for name in names[1:]:
        shutil.copyfile(source / name, output / name)
    for name in names:
        print(output / name)


if __name__ == "__main__":
    main()
