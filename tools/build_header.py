"""Build the essential semicolon profile header as a self-contained SVG.

All text is converted to vector paths, so rendering does not depend on the
viewer having Geist installed. Only one element animates: the terminal
cursor after the tagline.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textpath import text_path, measure

NAVY = "#0A0E1A"
AMBER = "#F59E0B"
LIGHT = "#F8FAFC"
MUTED = "#8A93A6"
RED = "#EF4444"

W, H = 1200, 340

NAME = "Amirhossein Akhoondzadeh"
ROLE = "SENIOR MOBILE ENGINEER    BERLIN"
LINE1 = "real code that looks correct,"
LINE2 = "shown failing on screen."

# Left column: the semicolon mark. Right column: the type.
MARK_X = 96
TEXT_X = 232

parts = []
add = parts.append

add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" role="img" '
    f'aria-label="Amirhossein Akhoondzadeh, senior mobile engineer, Berlin. '
    f'Real code that looks correct, shown failing on screen.">')

# Background
add(f'<rect width="{W}" height="{H}" rx="18" fill="{NAVY}"/>')

# Faint dot grid, brand texture at very low opacity
add('<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">'
    f'<circle cx="1.5" cy="1.5" r="1.5" fill="{LIGHT}" opacity="0.05"/></pattern></defs>')
add(f'<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>')

# The semicolon mark: square dot over a curved tail, matching the avatar.
# The tail runs mostly vertical and hooks left only near the tip, which is
# what keeps it reading as a semicolon rather than a blob.
DOT = 46
dot_y = 104
add(f'<rect x="{MARK_X}" y="{dot_y}" width="{DOT}" height="{DOT}" fill="{AMBER}"/>')
cxm = MARK_X + DOT / 2
t = dot_y + DOT + 28
r = DOT / 2 - 1
# Filled tapered comma: rounded cap at the top, outer edge sweeping down and
# left, inner edge returning. The taper is what separates a comma from a blob.
add(f'<path d="M{cxm - r} {t} '
    f'A {r} {r} 0 0 1 {cxm + r} {t} '
    f'C {cxm + r + 5} {t + 52}, {cxm + r - 6} {t + 88}, {cxm - 26} {t + 108} '
    f'C {cxm - 8} {t + 74}, {cxm - r + 8} {t + 42}, {cxm - r} {t} Z" '
    f'fill="{AMBER}"/>')

# Name
name_size = 52
d, _ = text_path(NAME, "black", name_size, TEXT_X, 138)
add(f'<path d="{d}" fill="{LIGHT}"/>')

# Role line, mono, letterspaced
role_size = 15
d, role_w = text_path(ROLE, "monomed", role_size, TEXT_X, 176, tracking=0.14)
add(f'<path d="{d}" fill="{MUTED}"/>')

# Amber rule under the role
add(f'<rect x="{TEXT_X}" y="200" width="72" height="4" fill="{AMBER}"/>')

# Tagline. "failing" carries the amber so the eye lands on the one word
# the whole channel is about.
tag_size = 26
d, w1 = text_path(LINE1, "medium", tag_size, TEXT_X, 250)
add(f'<path d="{d}" fill="{LIGHT}"/>')

cur = TEXT_X
for chunk, colour in (("shown ", LIGHT), ("failing", AMBER), (" on screen.", LIGHT)):
    d, adv = text_path(chunk, "medium", tag_size, cur, 286)
    add(f'<path d="{d}" fill="{colour}"/>')
    cur += adv
w2 = cur - TEXT_X

# The one animated element: a terminal cursor after the last word.
cx = TEXT_X + w2 + 10
add(f'<rect x="{cx:.1f}" y="266" width="13" height="26" fill="{AMBER}">'
    '<animate attributeName="opacity" values="1;1;0;0;1" dur="1.2s" '
    'repeatCount="indefinite" calcMode="discrete"/></rect>')

# Right side: a real failing test receipt. This is the premise of the whole
# channel, so the banner states it rather than only describing it.
PX, PY, PW, PH = 706, 202, 418, 104
add(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="10" '
    f'fill="#121A2B" stroke="#1F293D" stroke-width="1"/>')

m = 15
d, adv = text_path("$ ", "mono", m, PX + 24, PY + 42)
add(f'<path d="{d}" fill="{MUTED}"/>')
d, _ = text_path("flutter test", "mono", m, PX + 24 + adv, PY + 42)
add(f'<path d="{d}" fill="{LIGHT}"/>')

cur = PX + 24
for chunk, colour in (("00:02 ", MUTED), ("+5 ", LIGHT), ("-1", RED),
                      (": Some tests failed.", RED)):
    d, adv = text_path(chunk, "mono", m, cur, PY + 76)
    add(f'<path d="{d}" fill="{colour}"/>')
    cur += adv

add('</svg>')

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "amirhosseinakhoondzadeh", "assets", "header.svg")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    f.write("\n".join(parts))
print("wrote", out, os.path.getsize(out), "bytes")
