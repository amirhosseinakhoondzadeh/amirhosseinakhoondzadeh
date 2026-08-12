"""One wide strip listing the stack, in brand colours, as a single SVG.

A single designed object rather than a row of third-party badge images.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textpath import text_path

NAVY = "#0A0E1A"
AMBER = "#F59E0B"
LIGHT = "#F8FAFC"
MUTED = "#8A93A6"

# Breadth only. No library and no architectural school goes in this row:
# naming one narrows him, and the repo descriptions already carry the
# specifics (Bloc, get_it, Clean Architecture, fl_chart, test counts).
ITEMS = ["FLUTTER", "DART", "ANDROID", "iOS", "ARCHITECTURE", "TESTING",
         "AI-ASSISTED WORKFLOWS"]

SIZE = 14
TRACK = 0.12
GAP = 26
PAD = 28
H = 62

# Measure first so the strip is exactly as wide as its contents.
widths = [text_path(i, "monomed", SIZE, 0, 0, TRACK)[1] for i in ITEMS]
inner = sum(widths) + GAP * 2 * (len(ITEMS) - 1)
W = int(inner + PAD * 2)

parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="Stack: {", ".join(ITEMS)}">',
         f'<rect width="{W}" height="{H}" rx="10" fill="{NAVY}"/>']

x = PAD
baseline = H / 2 + SIZE * 0.37
for n, (item, w) in enumerate(zip(ITEMS, widths)):
    d, _ = text_path(item, "monomed", SIZE, x, baseline, TRACK)
    parts.append(f'<path d="{d}" fill="{LIGHT}"/>')
    x += w
    if n < len(ITEMS) - 1:
        parts.append(f'<rect x="{x + GAP - 2.5:.1f}" y="{H/2 - 2.5:.1f}" '
                     f'width="5" height="5" fill="{AMBER}"/>')
        x += GAP * 2

parts.append('</svg>')

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "amirhosseinakhoondzadeh", "assets", "stack.svg")
open(out, "w").write("".join(parts))
print("stack.svg", W, "x", H, os.path.getsize(out), "bytes")
