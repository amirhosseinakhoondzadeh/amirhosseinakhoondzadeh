"""Convert a string to an SVG path using a local font, so the rendered
banner does not depend on the viewer having the font installed."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

FONTS = {
    "black":    "/Users/amirhosseinakhoondzadeh/Library/Fonts/Geist-Black.ttf",
    "bold":     "/Users/amirhosseinakhoondzadeh/Library/Fonts/Geist-Bold.ttf",
    "semibold": "/Users/amirhosseinakhoondzadeh/Library/Fonts/Geist-SemiBold.ttf",
    "medium":   "/Users/amirhosseinakhoondzadeh/Library/Fonts/Geist-Medium.ttf",
    "regular":  "/Users/amirhosseinakhoondzadeh/Library/Fonts/Geist-Regular.ttf",
    "mono":     "/Users/amirhosseinakhoondzadeh/Library/Fonts/GeistMono-Regular.ttf",
    "monomed":  "/Users/amirhosseinakhoondzadeh/Library/Fonts/GeistMono-Medium.ttf",
    "monobold": "/Users/amirhosseinakhoondzadeh/Library/Fonts/GeistMono-Bold.ttf",
}

_cache = {}


def _font(weight):
    if weight not in _cache:
        _cache[weight] = TTFont(FONTS[weight])
    return _cache[weight]


def text_path(s, weight="bold", size=48, x=0, y=0, tracking=0.0):
    """Return (svg_path_d, advance_width) for string s baselined at (x, y).

    tracking is extra letter spacing in em units (0.02 = 2% of size).
    """
    font = _font(weight)
    upem = font["head"].unitsPerEm
    scale = size / upem
    cmap = font.getBestCmap()
    glyphset = font.getGlyphSet()
    hmtx = font["hmtx"]

    try:
        kern = font["kern"].kernTables[0].kernTable
    except Exception:
        kern = {}

    pen_out = SVGPathPen(glyphset, ntos=lambda v: f"{v:.2f}")
    cursor = 0.0
    prev = None
    for ch in s:
        gname = cmap.get(ord(ch))
        if gname is None:
            cursor += upem * 0.35
            prev = None
            continue
        if prev is not None:
            cursor += kern.get((prev, gname), 0)
        # flip y: font space is y-up, SVG is y-down
        t = Transform(scale, 0, 0, -scale, x + cursor * scale, y)
        tpen = TransformPen(pen_out, t)
        glyphset[gname].draw(tpen)
        cursor += hmtx[gname][0] + tracking * upem
        prev = gname

    return pen_out.getCommands(), cursor * scale


def measure(s, weight="bold", size=48, tracking=0.0):
    return text_path(s, weight, size, 0, 0, tracking)[1]
