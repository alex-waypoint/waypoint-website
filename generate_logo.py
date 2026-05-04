#!/usr/bin/env python3
"""
Waypoint LinkedIn Assets Generator
  waypoint_linkedin.png        — 300×300px profile picture
  waypoint_linkedin_banner.png — 1128×191px banner
"""

import cairosvg, os, struct

OUT = "/Users/alexisdeclaro/Desktop/waypoint/claude-website/"

# ─── Profile picture (300×300) ──────────────────────────────────
svg_profile = """<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="300" fill="#090B0F"/>
  <circle cx="150" cy="118" r="5" fill="#5AC4DE"/>
  <text x="150" y="166"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="44" font-weight="700" letter-spacing="-0.5"
        text-anchor="middle" fill="#FFFFFF">Waypoint</text>
  <rect x="110" y="178" width="80" height="2" rx="1" fill="#0F5E7A"/>
</svg>"""

# ─── Banner (1128×191) ──────────────────────────────────────────
svg_banner = """<svg viewBox="0 0 1128 191" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Right-side teal glow -->
    <radialGradient id="rg" cx="92%" cy="50%" r="38%">
      <stop offset="0%"   stop-color="#0F5E7A" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#0F5E7A" stop-opacity="0"/>
    </radialGradient>
    <!-- Subtle dot grid -->
    <pattern id="dots" x="0" y="0" width="28" height="28"
             patternUnits="userSpaceOnUse">
      <circle cx="14" cy="14" r="0.7" fill="#FFFFFF" opacity="0.07"/>
    </pattern>
  </defs>

  <!-- Background + dot grid + glow -->
  <rect width="1128" height="191" fill="#090B0F"/>
  <rect width="1128" height="191" fill="url(#dots)"/>
  <rect width="1128" height="191" fill="url(#rg)"/>

  <!-- Top teal accent bar -->
  <rect x="0" y="0" width="1128" height="2.5" fill="#0F5E7A"/>

  <!-- ── LEFT: Waypoint wordmark ── -->
  <!-- Geo-dot -->
  <circle cx="48" cy="91" r="5" fill="#5AC4DE"/>
  <!-- Wordmark -->
  <text x="62" y="103"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="30" font-weight="700" letter-spacing="-0.3"
        fill="#FFFFFF">Waypoint</text>
  <!-- Sub-label -->
  <text x="63" y="121"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="8.5" font-weight="400" letter-spacing="2.6"
        fill="#5AC4DE">GEOSPATIAL INTELLIGENCE</text>

  <!-- Vertical divider -->
  <rect x="250" y="40" width="1.5" height="111"
        fill="#0F5E7A" opacity="0.45"/>

  <!-- ── RIGHT: Copy ── -->
  <!-- Line 1 — primary statement -->
  <text x="274" y="90"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="21" font-weight="600" letter-spacing="-0.2"
        fill="#FFFFFF">Human-validated geospatial intelligence</text>
  <!-- Em-dash connector -->
  <text x="274" y="116"
        font-family="Inter, Helvetica Neue, Arial, sans-serif"
        font-size="15" font-weight="400" letter-spacing="0"
        fill="#8A8A92">— built for organizations where data quality matters.</text>

  <!-- ── Corner coordinate marks ── -->
  <!-- top-right -->
  <path d="M1100,18 L1112,18 L1112,30"
        stroke="#5AC4DE" stroke-width="1.4" fill="none"
        stroke-linecap="round" stroke-linejoin="round" opacity="0.45"/>
  <!-- bottom-right -->
  <path d="M1100,173 L1112,173 L1112,161"
        stroke="#5AC4DE" stroke-width="1.4" fill="none"
        stroke-linecap="round" stroke-linejoin="round" opacity="0.45"/>
  <!-- top-left -->
  <path d="M18,18 L6,18 L6,30"
        stroke="#5AC4DE" stroke-width="1.4" fill="none"
        stroke-linecap="round" stroke-linejoin="round" opacity="0.25"/>
  <!-- bottom-left -->
  <path d="M18,173 L6,173 L6,161"
        stroke="#5AC4DE" stroke-width="1.4" fill="none"
        stroke-linecap="round" stroke-linejoin="round" opacity="0.25"/>

  <!-- Right-edge subtle data-layer lines -->
  <line x1="950" y1="72"  x2="1092" y2="72"
        stroke="#0F5E7A" stroke-width="1" opacity="0.35"/>
  <line x1="970" y1="86"  x2="1092" y2="86"
        stroke="#0F5E7A" stroke-width="1" opacity="0.25"/>
  <line x1="958" y1="100" x2="1092" y2="100"
        stroke="#0F5E7A" stroke-width="1" opacity="0.3"/>
  <line x1="978" y1="114" x2="1092" y2="114"
        stroke="#0F5E7A" stroke-width="1" opacity="0.2"/>
</svg>"""


def render(svg_str, path, w=None, h=None):
    kwargs = dict(bytestring=svg_str.encode(), write_to=path)
    if w: kwargs["output_width"]  = w
    if h: kwargs["output_height"] = h
    cairosvg.svg2png(**kwargs)
    with open(path, "rb") as f:
        f.read(8); f.read(4); f.read(4)
        pw = struct.unpack(">I", f.read(4))[0]
        ph = struct.unpack(">I", f.read(4))[0]
    kb = os.path.getsize(path) // 1024
    print(f"  ✓  {os.path.basename(path):38s} {pw}×{ph}px  ({kb} KB)")


if __name__ == "__main__":
    print("Generating LinkedIn assets…\n")
    render(svg_profile, OUT + "waypoint_linkedin.png",        w=300,  h=300)
    render(svg_banner,  OUT + "waypoint_linkedin_banner.png", w=1128, h=191)
    print("\nDone.")
