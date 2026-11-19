"""Draws the pixel-art icon buttons and frames in buttons/icons/.

The shapes copy the edge, corner and shadow pattern of buttons/start.png so
the new controls look like the hand-drawn ones. Run from the repo root:
    python3 tools/make_icons.py
"""
from pathlib import Path
from PIL import Image

SCALE = 3  # each art pixel becomes 3x3 image pixels
OUT = Path("buttons/icons")

# Palettes: outline, fill, shadow, light shade, glyph
PALETTES = {
    "cream":    dict(r=(178, 89, 89), c=(232, 226, 205), d=(135, 58, 58), l=(203, 153, 144), g=(178, 89, 89)),
    "selected": dict(r=(135, 58, 58), c=(178, 89, 89), d=(94, 36, 36), l=(160, 76, 76), g=(232, 226, 205)),
    "timer":    dict(r=(109, 25, 0), c=(161, 43, 0), d=(74, 17, 0), l=(140, 37, 0), g=(255, 230, 156)),
}

# Edges traced from start.png: 5-column caps, 4-row top, 7-row bottom.
LEFT = ["...rr", "..rcc", ".rrcc", ".rccc", "rcccc",
        "rcccc", "rlccc", ".llcc", ".drcc", ".dddr", "..ddd", "....d"]
RIGHT = ["rr...", "ccr..", "ccrr.", "cccr.", "ccccr",
         "cccld", "cclrd", "ccrld", "ccrdd", "rrdd.", "ddd..", "dd..."]
MID = ["r", "c", "c", "c", "c", "c", "c", "c", "c", "r", "d", "d"]
TOP, BOTTOM = 4, 7  # rows above / below the single repeatable row


def frame(inner_w, inner_rows):
    """Rows of the button shape with inner_w middle columns and inner_rows middle rows."""
    rows = []
    for i in range(len(LEFT)):
        row = LEFT[i] + MID[i] * inner_w + RIGHT[i]
        reps = inner_rows if i == TOP else 1
        rows.extend([row] * reps)
    return rows


GLYPHS = {
    "play":   ["X.....", "XXX...", "XXXXX.", "XXXXXX", "XXXXX.", "XXX...", "X....."],
    "pause":  ["XX.XX", "XX.XX", "XX.XX", "XX.XX", "XX.XX", "XX.XX", "XX.XX"],
    "reset":  ["..XXX.X", ".X...XX", "X...XXX", "X......", "X.....X", ".X...X.", "..XXX.."],
    "remove": ["X.....X", ".X...X.", "..X.X..", "...X...", "..X.X..", ".X...X.", "X.....X"],
    "check":  [".......", "......X", ".....X.", "X...X..", ".X.X...", "..X....", "......."],
    "save":   ["XXXXXX.", "X.XX.XX", "XXXXXXX", "XXXXXXX", "X.....X", "X.....X", "XXXXXXX"],
    "sound":  ["...X..X.", "..XX...X", "XXXX.X.X", "XXXX.X.X", "XXXX.X.X", "..XX...X", "...X..X."],
    "bell":   ["...X...", "..XXX..", ".XXXXX.", ".XXXXX.", ".XXXXX.", "XXXXXXX", "...X..."],
    "moon":   ["..XXX..", ".XX....", "XX.....", "XX.....", "XX.....", ".XX....", "..XXX.."],
    "sun":    ["X..X..X", ".X.X.X.", "..XXX..", "XXXXXXX", "..XXX..", ".X.X.X.", "X..X..X"],
}


def render(rows, palette, path):
    w, h = len(rows[0]), len(rows)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in palette:
                img.putpixel((x, y), palette[ch] + (255,))
    img.resize((w * SCALE, h * SCALE), Image.NEAREST).save(path)


def icon(name, palette_name="cream", off=False):
    glyph = GLYPHS[name]
    rows = [list(r) for r in frame(7, 5)]  # 17 x 16 art pixels
    gw = len(glyph[0])
    x0, y0 = (len(rows[0]) - gw) // 2, 3
    ink = "l" if off else "g"
    for gy, line in enumerate(glyph):
        for gx, ch in enumerate(line):
            if ch == "X":
                rows[y0 + gy][x0 + gx] = ink
                below = y0 + gy + 1
                # soft shade under the glyph, like the letters on start.png
                if not off and (gy + 1 == len(glyph) or glyph[gy + 1][gx] != "X") and rows[below][x0 + gx] == "c":
                    rows[below][x0 + gx] = "l"
    if off:  # diagonal strike-through for "off"
        for i in range(8):
            rows[y0 - 1 + i][x0 - 1 + i * (gw + 1) // 7] = "g"
    suffix = "-off" if off else ""
    render(["".join(r) for r in rows], PALETTES[palette_name], OUT / f"{name}{suffix}.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in GLYPHS:
        icon(name)
    icon("sound", off=True)
    icon("bell", off=True)
    # 9-slice frames for text buttons, panels and the timer (used with CSS border-image)
    for pal in PALETTES:
        render(frame(1, 1), PALETTES[pal], OUT / f"frame-{pal}.png")


if __name__ == "__main__":
    main()
