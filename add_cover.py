"""Add (or replace) a persona's cover: any image in, covers/<slug>.webp out.

    python add_cover.py <slug> <image.png>

Resizes to at most 720px wide (never upscales), WebP quality 80. Commit and
push the result; the Pages workflow publishes it within a couple of minutes.
Needs Pillow (`pip install pillow`).
"""
import re
import sys
from pathlib import Path

from PIL import Image

SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")  # = Roundtable's persona slug rule


def main(slug: str, src: str) -> Path:
    if not SLUG.match(slug):
        raise SystemExit(f"bad slug {slug!r}: lowercase letters, digits and hyphens only")
    im = Image.open(src).convert("RGB")
    w = min(720, im.width)
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    out = Path(__file__).parent / "covers" / f"{slug}.webp"
    im.save(out, "WEBP", quality=80, method=6)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    print(main(sys.argv[1], sys.argv[2]))
