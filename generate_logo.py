#!/usr/bin/env python3
"""
Waypoint Wordmark Generator
Outputs:
  waypoint_wordmark_dark.png   — white text on dark  (2000×480)
  waypoint_wordmark_light.png  — dark text on white  (2000×480)
  waypoint_wordmark_dark.svg   — master vector (dark)
  waypoint_wordmark_light.svg  — master vector (light)
"""

import cairosvg, os, struct

OUT = "/Users/alexisdeclaro/Desktop/waypoint/claude-website/"

DARK       = "#090B0F"
WHITE      = "#FFFFFF"
TEAL       = "#0F5E7A"
TEAL_LIGHT = "#5AC4DE"
T3         = "#8A8A92"

# ─── Wordmark SVG ──────────────────────────────────────────────
# viewBox 0 0 500 120
# A small teal dot mirrors the geo-dot on the website — keeping
# continuity without adding a separate icon.
# Two variants: with tagline and without (for tight spaces).
def wordmark_svg(dark=True, tagline=True):
    bg         = DARK       if dark else WHITE
    word_color = WHITE      if dark else DARK
    dot_color  = TEAL_LIGHT if dark else TEAL
    tag_color  = T3         if dark else "#9A9AA2"

    tag_line = f"""
  <!-- Tagline -->
  <text x="30" y="88"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="11" font-weight="400" letter-spacing="3.2"
        fill="{tag_color}">GEOSPATIAL INTELLIGENCE</text>""" if tagline else ""

    h = "120" if tagline else "90"

    return f"""<svg viewBox="0 0 500 {h}" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="500" height="{h}" fill="{bg}"/>

  <!-- Geo-dot — small teal accent matching the website eyebrow -->
  <circle cx="14" cy="52" r="4.5" fill="{dot_color}"/>

  <!-- Wordmark -->
  <text x="28" y="66"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="48" font-weight="700" letter-spacing="-0.5"
        fill="{word_color}">Waypoint</text>
  {tag_line}
</svg>"""


def render(svg_str, path, scale=4):
    cairosvg.svg2png(bytestring=svg_str.encode(), write_to=path, scale=scale)
    with open(path, "rb") as f:
        f.read(8)
        f.read(4); f.read(4)
        w = struct.unpack(">I", f.read(4))[0]
        h = struct.unpack(">I", f.read(4))[0]
    kb = os.path.getsize(path) // 1024
    print(f"  ✓  {os.path.basename(path):40s} {w}×{h}px  ({kb} KB)")


if __name__ == "__main__":
    print("Generating Waypoint wordmark assets…\n")

    variants = [
        ("waypoint_wordmark_dark.png",          wordmark_svg(dark=True,  tagline=True),  4),
        ("waypoint_wordmark_light.png",         wordmark_svg(dark=False, tagline=True),  4),
        ("waypoint_wordmark_dark_notag.png",    wordmark_svg(dark=True,  tagline=False), 4),
        ("waypoint_wordmark_light_notag.png",   wordmark_svg(dark=False, tagline=False), 4),
    ]

    for filename, svg, scale in variants:
        render(svg, OUT + filename, scale=scale)

    # SVG master files
    for name, svg in [
        ("waypoint_wordmark_dark.svg",  wordmark_svg(dark=True,  tagline=True)),
        ("waypoint_wordmark_light.svg", wordmark_svg(dark=False, tagline=True)),
    ]:
        with open(OUT + name, "w") as f:
            f.write(svg)
        print(f"  ✓  {name:40s} (SVG master)")

    print("\nDone.")
