"""Build the social link buttons as self-contained SVGs in brand colours.

YouTube is the primary action, so it gets the solid amber fill. The rest are
navy with an amber keyline. Labels are converted to paths like the header.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textpath import text_path

NAVY = "#0A0E1A"
AMBER = "#F59E0B"
LIGHT = "#F8FAFC"

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "amirhosseinakhoondzadeh", "assets")
os.makedirs(OUT, exist_ok=True)

H = 46
PAD_X = 18
ICON_W = 22
GAP = 11
FONT_SIZE = 16


def icon_youtube(colour, x, y):
    # Rounded screen with a play triangle knocked out.
    return (f'<g transform="translate({x},{y})">'
            f'<rect x="0" y="2.5" width="22" height="16" rx="5" fill="{colour}"/>'
            f'<path d="M8.8 6.6 L15.2 10.5 L8.8 14.4 Z" fill="{NAVY if colour == AMBER else AMBER}"/>'
            f'</g>')


def icon_linkedin(colour, x, y):
    d, _ = text_path("in", "bold", 13, 4.2, 15.2)
    return (f'<g transform="translate({x},{y})">'
            f'<rect x="0" y="1.5" width="19" height="19" rx="4" fill="{colour}"/>'
            f'<path d="{d}" fill="{NAVY if colour == AMBER else AMBER}"/>'
            f'</g>')


def icon_mail(colour, x, y):
    return (f'<g transform="translate({x},{y})">'
            f'<rect x="0" y="3" width="22" height="15.5" rx="3.5" fill="none" '
            f'stroke="{colour}" stroke-width="2"/>'
            f'<path d="M1.6 5.4 L11 12.4 L20.4 5.4" fill="none" stroke="{colour}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'</g>')


def build(name, label, icon_fn, primary):
    d, adv = text_path(label, "semibold", FONT_SIZE, 0, 0)
    w = int(PAD_X * 2 + ICON_W + GAP + adv)

    fill = AMBER if primary else NAVY
    stroke = "" if primary else f' stroke="{AMBER}" stroke-width="1.6"'
    text_col = NAVY if primary else LIGHT
    icon_col = NAVY if primary else AMBER
    inset = 0 if primary else 0.8

    tx = PAD_X + ICON_W + GAP
    ty = H / 2 + FONT_SIZE * 0.36
    dpath, _ = text_path(label, "semibold", FONT_SIZE, tx, ty)

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" '
           f'viewBox="0 0 {w} {H}" role="img" aria-label="{label}">'
           f'<rect x="{inset}" y="{inset}" width="{w - inset * 2}" '
           f'height="{H - inset * 2}" rx="10" fill="{fill}"{stroke}/>'
           f'{icon_fn(icon_col, PAD_X, (H - 21) / 2)}'
           f'<path d="{dpath}" fill="{text_col}"/>'
           f'</svg>')
    p = os.path.join(OUT, name)
    open(p, "w").write(svg)
    print(f"{name}  {w}x{H}  {os.path.getsize(p)}b")


build("btn-youtube.svg", "essential semicolon", icon_youtube, True)
build("btn-linkedin.svg", "LinkedIn", icon_linkedin, False)
build("btn-email.svg", "Email", icon_mail, False)
