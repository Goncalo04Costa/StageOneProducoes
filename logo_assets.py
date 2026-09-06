# -*- coding: utf-8 -*-
"""A partir do logótipo em alta resolução:
   - logo.jpg      (nome limpo, sem espaços)
   - icon.png      (recorte quadrado sem margens, p/ favicon / header)
   - og.jpg        (imagem de partilha 1200x630 com o wordmark real)
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PROJ = pathlib.Path(__file__).resolve().parent
SOURCE = "LogoStageONE.jpeg"   # logótipo original em alta resolução

src = Image.open(PROJ / SOURCE).convert("RGB")

# 1) nome limpo -------------------------------------------------------------
src.save(PROJ / "logo.jpg", "JPEG", quality=90, optimize=True, progressive=True)

# 2) bounding box do conteúdo (o que não é quase-preto) --------------------
g = src.convert("L")
bbox = g.point(lambda p: 255 if p > 28 else 0).getbbox()
pad = int(max(src.size) * 0.05)
l, t, r, b = bbox
l, t = max(0, l - pad), max(0, t - pad)
r, b = min(src.width, r + pad), min(src.height, b + pad)
content = src.crop((l, t, r, b))

# icon quadrado (conteúdo centrado sobre preto) --------------------------
side = max(content.size)
icon = Image.new("RGB", (side, side), (10, 9, 11))
icon.paste(content, ((side - content.width) // 2, (side - content.height) // 2))
icon = icon.resize((512, 512), Image.LANCZOS)
icon.save(PROJ / "icon.png", "PNG", optimize=True)

# tira do wordmark p/ o cabeçalho (proporção real, ~2.75:1) --------------
content.save(PROJ / "logo-wordmark.png", "PNG", optimize=True)

# 3) imagem OG -----------------------------------------------------------
W, H = 1200, 630
BG = (11, 10, 12)
GOLD = (231, 178, 76)
TEXT = (237, 234, 227)
MUTE = (120, 116, 128)
img = Image.new("RGB", (W, H), BG)


def glow(cx, cy, rx, ry, colour, alpha):
    layer = Image.new("L", (W, H), 0)
    ImageDraw.Draw(layer).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=alpha)
    layer = layer.filter(ImageFilter.GaussianBlur(150))
    img.paste(Image.new("RGB", (W, H), colour), (0, 0), layer)


glow(140, -30, 540, 430, (231, 178, 76), 92)
glow(1170, 40, 470, 430, (127, 96, 196), 66)
glow(1010, 730, 640, 470, (110, 51, 32), 52)

# wordmark real (o recorte de conteúdo), escalado para a largura alvo.
# O recorte tem fundo preto -> "screen" com o fundo funde sem deixar caixa.
from PIL import ImageChops
target_w = 900
wm = content.resize((target_w, round(content.height * target_w / content.width)), Image.LANCZOS)
px, py = 92, (H - wm.height) // 2 + 6
region = img.crop((px, py, px + wm.width, py + wm.height))
img.paste(ImageChops.screen(region, wm), (px, py))

d = ImageDraw.Draw(img)
F = "C:/Windows/Fonts/"
f_eyebrow = ImageFont.truetype(F + "segoeuisl.ttf", 24)
f_tag = ImageFont.truetype(F + "segoeui.ttf", 33)
f_kw = ImageFont.truetype(F + "segoeuisl.ttf", 23)


def tracked(xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking


tracked((px + 6, py - 46), "PRODUÇÃO DE EVENTOS  ·  PORTUGAL", f_eyebrow, GOLD, 4)
d.text((px + 6, py + wm.height + 6), "Produzimos momentos. Conectamos talentos.",
       font=f_tag, fill=TEXT)
tracked((px + 6, H - 78),
        "SOM   ·   LUZ   ·   LEDWALL   ·   GERADORES   ·   PALCOS   ·   CAMARINS",
        f_kw, MUTE, 3)
d.rectangle([W - 90, H - 46, W - 46, H - 43], fill=GOLD)
d.rectangle([W - 49, H - 90, W - 46, H - 43], fill=GOLD)

img.save(PROJ / "og.jpg", "JPEG", quality=86, optimize=True, progressive=True)

import os
for n in ("logo.jpg", "icon.png", "logo-wordmark.png", "og.jpg"):
    print(n, os.path.getsize(PROJ / n), "bytes")
print("bbox:", bbox, "-> content", content.size)
