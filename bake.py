"""Re-bake every badge from its SVG source.

Writes 32x32/<seat>.png and 64x64/<seat>.png for each svg/<seat>.svg.

    uv run --no-project --with cairosvg python bake.py

cairosvg needs the cairo library; on macOS with Homebrew prefix the command
with DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib.
"""
import glob
import os

import cairosvg

ROOT = os.path.dirname(os.path.abspath(__file__))
SIZES = (32, 64)

for svg in sorted(glob.glob(os.path.join(ROOT, "svg", "*.svg"))):
    seat = os.path.splitext(os.path.basename(svg))[0]
    for px in SIZES:
        out_dir = os.path.join(ROOT, f"{px}x{px}")
        os.makedirs(out_dir, exist_ok=True)
        cairosvg.svg2png(url=svg, write_to=os.path.join(out_dir, f"{seat}.png"),
                         output_width=px, output_height=px)
    print(seat)
