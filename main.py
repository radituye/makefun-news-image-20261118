#!/usr/bin/env python3
"""News-image entry: write the front page to /output/entry.png.

The bundled image (entry.png, 1024x1024, 666561 bytes) sums up the
world news of Wednesday 18 November 2026 as a newspaper front page:
the masthead names the day, the lead story is the day of summits
(APEC in Shenzhen, the Quad in Manila, the Trump-Xi-Putin meeting
set for tomorrow), and six cards cover Ukraine, the Gulf, trade,
settlements, Mongolia and Cyclone Akvan.

Deterministic: the same bytes are copied on every run. No network,
standard library only.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = OUT / "entry.png"
    shutil.copyfile(src, dst)
    # Fail loudly on a short copy instead of shipping a broken image.
    assert dst.stat().st_size == src.stat().st_size, "entry.png copy mismatch"


if __name__ == "__main__":
    main()
