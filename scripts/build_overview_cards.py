#!/usr/bin/env python
"""Build manuals-overview card images at images/overview/ from Louie's renders.

10 render-derived files + onecable composite = 11 outputs, each exactly 1600x900 RGBA.
"""
import os
from PIL import Image, ImageDraw, ImageFont

# Canonical source for the render-derived cards. These PNGs live in the
# repo-root "manual images last.zip" archive; extract it to this folder before
# running. (The loose "manual images last/" extraction folder is disposable and
# may be absent — re-extract from the zip to reproduce.)
SRC_DIR_NAME = "manual images last"

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(REPO, SRC_DIR_NAME)
OUT = os.path.join(REPO, "images", "overview")

# flip.png ships with its device floating high in the source render (alpha-bbox
# vertical center ~0.344). Every other card sits at cy ~0.46-0.50, so flip.png
# is re-centered to this target after the resize (pure vertical translation on a
# transparent canvas — no scaling, no horizontal shift, content never clips).
FLIP_RECENTER_CY = 0.475
ONECABLE_SRC = os.path.join(
    REPO, "images", "Screenmate - OneCable - Handleiding images",
    "Screenmate OneCable Image for 'In The Box'.png")

os.makedirs(OUT, exist_ok=True)

TARGET = (1600, 900)

# source filename -> list of output basenames
RENDER_MAP = [
    ("dual flip.png", ["dual-flip.png"]),
    ("expand.png", ["expand.png"]),
    ("flip-png.png", ["flip.png"]),
    ("infinity-png.png", ["infinity.png"]),
    ("infinity lite-png.png", ["infinity-lite.png"]),
    ("lite & lite-touchscreen & lite 144hz.png", ["lite.png", "lite-144hz.png"]),
    ("One 4k - one 4k oled-png.png", ["one-4k.png", "one-4k-oled.png"]),
    ("panorama.png", ["panorama.png"]),
]


def to_16x9_3840(im):
    """Center-crop (or pad) an RGBA image to exactly 3840x2160."""
    w, h = im.size
    if (w, h) == (3840, 2160):
        return im
    # center-crop width/height to 3840x2160 if larger; pad if smaller
    left = (w - 3840) // 2
    top = (h - 2160) // 2
    if w >= 3840 and h >= 2160:
        return im.crop((left, top, left + 3840, top + 2160))
    # pad path (not expected here)
    canvas = Image.new("RGBA", (3840, 2160), (0, 0, 0, 0))
    canvas.paste(im, (-left, -top), im)
    return canvas


def alpha_bbox_fraction(im):
    """Return (wfrac, hfrac, cx_frac, cy_frac) of the alpha bbox."""
    alpha = im.split()[-1]
    bbox = alpha.getbbox()
    if bbox is None:
        return None
    l, t, r, b = bbox
    W, H = im.size
    wfrac = (r - l) / W
    hfrac = (b - t) / H
    cx = ((l + r) / 2) / W
    cy = ((t + b) / 2) / H
    return wfrac, hfrac, cx, cy


def recenter_vertically(im, target_cy):
    """Return a copy of RGBA `im` with its alpha bbox vertically translated so
    the bbox center lands at target_cy (fraction of height). Horizontal position
    and scale are untouched. Raises if the shift would clip content off-canvas.
    """
    W, H = im.size
    l, t, r, b = im.split()[-1].getbbox()
    cur_center = (t + b) / 2
    dy = int(round(target_cy * H - cur_center))
    if t + dy < 0 or b + dy > H:
        raise ValueError(
            "recenter dy=%d would clip bbox (t=%d b=%d H=%d)" % (dy, t, b, H))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.paste(im, (0, dy), im)
    return canvas


def median(vals):
    s = sorted(vals)
    n = len(s)
    if n % 2:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


outputs = {}  # basename -> PIL image (final 1600x900)

# --- Process the 10 render-derived files ---
for src_name, out_names in RENDER_MAP:
    im = Image.open(os.path.join(SRC, src_name)).convert("RGBA")
    im = to_16x9_3840(im)
    im = im.resize(TARGET, Image.LANCZOS)
    for out_name in out_names:
        outputs[out_name] = im.copy()

# --- flip.png: vertical re-center so it doesn't float high in its card ---
outputs["flip.png"] = recenter_vertically(outputs["flip.png"], FLIP_RECENTER_CY)

# --- Measure fractions for onecable sizing ---
# width fraction median from dual-flip / flip / expand outputs
width_srcs = ["dual-flip.png", "flip.png", "expand.png"]
wfracs = [alpha_bbox_fraction(outputs[n])[0] for n in width_srcs]
median_wfrac = median(wfracs)

# vertical center median across ALL render outputs (the 10, dedup source images)
cy_vals = []
seen = set()
for src_name, out_names in RENDER_MAP:
    n = out_names[0]
    cy_vals.append(alpha_bbox_fraction(outputs[n])[3])
median_cy = median(cy_vals)

# --- Build onecable.png ---
oc = Image.open(ONECABLE_SRC).convert("RGBA")
oc_w, oc_h = oc.size
target_w = median_wfrac * TARGET[0]
scale = target_w / oc_w
capped = False
if scale > 1.5:
    scale = 1.5
    capped = True
new_w = int(round(oc_w * scale))
new_h = int(round(oc_h * scale))
oc_scaled = oc.resize((new_w, new_h), Image.LANCZOS)

canvas = Image.new("RGBA", TARGET, (0, 0, 0, 0))
paste_x = (TARGET[0] - new_w) // 2
paste_y = int(round(median_cy * TARGET[1] - new_h / 2))
canvas.paste(oc_scaled, (paste_x, paste_y), oc_scaled)
outputs["onecable.png"] = canvas

# --- Save all outputs optimized ---
ORDER = ["dual-flip.png", "expand.png", "flip.png", "infinity.png",
         "infinity-lite.png", "lite.png", "lite-144hz.png", "one-4k.png",
         "one-4k-oled.png", "panorama.png", "onecable.png"]

for name in ORDER:
    outputs[name].save(os.path.join(OUT, name), "PNG", optimize=True)

# --- Quality gates + table ---
print("onecable sizing: median_wfrac=%.4f target_w=%.1fpx scale=%.3f%s cy=%.4f"
      % (median_wfrac, target_w, scale, " (CAPPED@1.5x)" if capped else "", median_cy))
print()
print("%-18s %10s %6s %6s %8s %8s %6s" %
      ("name", "size", "W", "H", "RGBA", "bbox_wf", "MB"))
problems = []
rows = []
for name in ORDER:
    p = os.path.join(OUT, name)
    im = Image.open(p)
    sz = os.path.getsize(p)
    frac = alpha_bbox_fraction(im.convert("RGBA"))
    wf = frac[0] if frac else 0.0
    mb = sz / 1024 / 1024
    ok_dim = im.size == TARGET
    ok_mode = im.mode == "RGBA"
    ok_bbox = frac is not None and wf > 0
    ok_size = mb < 3.5
    if not ok_dim: problems.append(f"{name}: size {im.size} != 1600x900")
    if not ok_mode: problems.append(f"{name}: mode {im.mode} != RGBA")
    if not ok_bbox: problems.append(f"{name}: empty alpha bbox")
    if not ok_size: problems.append(f"{name}: {mb:.2f}MB >= 3.5MB")
    print("%-18s %10s %6d %6d %8s %8.3f %6.2f" %
          (name, f"{im.size[0]}x{im.size[1]}", im.size[0], im.size[1],
           im.mode, wf, mb))
    rows.append((name, im.size, im.mode, wf, mb))

print()
if problems:
    print("PROBLEMS:")
    for pr in problems:
        print("  -", pr)
else:
    print("All quality gates PASSED.")

# --- Contact sheet: each output over white AND over #16181d, labeled ---
THUMB_W, THUMB_H = 360, 202
PAD = 14
LABEL_H = 22
DARK = (0x16, 0x18, 0x1d)
cell_w = THUMB_W
cell_h = LABEL_H + THUMB_H
cols = 2  # white, dark
rows_n = len(ORDER)
sheet_w = PAD + cols * (cell_w + PAD)
sheet_h = PAD + rows_n * (cell_h + PAD)
sheet = Image.new("RGB", (sheet_w, sheet_h), (90, 90, 90))
draw = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:
    font = ImageFont.load_default()

for i, name in enumerate(ORDER):
    im = Image.open(os.path.join(OUT, name)).convert("RGBA").resize(
        (THUMB_W, THUMB_H), Image.LANCZOS)
    y0 = PAD + i * (cell_h + PAD)
    for c, bg in enumerate([(255, 255, 255), DARK]):
        x0 = PAD + c * (cell_w + PAD)
        draw.rectangle([x0, y0, x0 + cell_w, y0 + LABEL_H], fill=(40, 40, 40))
        tag = name + ("  /white" if c == 0 else "  /#16181d")
        draw.text((x0 + 4, y0 + 4), tag, fill=(230, 230, 230), font=font)
        base = Image.new("RGB", (THUMB_W, THUMB_H), bg)
        base.paste(im, (0, 0), im)
        sheet.paste(base, (x0, y0 + LABEL_H))

CONTACT = os.path.join(SRC, "impl-contact-sheet.png")
sheet.save(CONTACT, "PNG", optimize=True)
print("\ncontact sheet:", CONTACT, "size", sheet.size,
      f"{os.path.getsize(CONTACT)/1024:.0f}KB")
