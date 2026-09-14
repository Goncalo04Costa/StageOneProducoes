# -*- coding: utf-8 -*-
"""Gera os visuais de marca (placeholder) para o site da Liliana Oliveira:
   - icon.png   (favicon / ícone, 512x512)
   - og.jpg     (imagem de partilha, 1200x630)

Inspirados no logótipo real (script "Liliana Oliveira" em magenta com
contorno azul-marinho, chapéu de aba larga e coração de filigrana) — mas
recriados aqui a partir de formas simples, não são o ficheiro oficial.
Assim que tiveres o logótipo definitivo em alta resolução, o mais simples
é SUBSTITUIR diretamente `icon.png` (quadrado, 512x512+) e `og.jpg`
(1200x630) por exportações desse ficheiro — não é preciso correr nada.

Este script só é útil se quiseres voltar a gerar a versão placeholder
(por ex. depois de ajustar cores). Precisa de Playwright + Chromium:

    pip install playwright
    playwright install chromium
    python assets.py
"""
import pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).resolve().parent

HAT_HEART = """
<g transform="rotate(-10 68 40)">
  <ellipse cx="68" cy="46" rx="46" ry="9" fill="none" stroke="#3A4B9E" stroke-width="3"/>
  <path d="M40,44 Q40,12 68,12 Q96,12 96,40 L96,44" fill="none" stroke="#3A4B9E" stroke-width="3" stroke-linecap="round"/>
  <rect x="42" y="32" width="52" height="9" rx="3" fill="#E6127D" stroke="#3A4B9E" stroke-width="2"/>
</g>
<g transform="translate(96,48) scale(0.85)">
  <path d="M12 21s-7.5-4.8-10-9.3C0.3 8.6 2 5 5.5 5c2 0 3.5 1.2 4.5 3 1-1.8 2.5-3 4.5-3 3.5 0 5.2 3.6 3.5 6.7C19.5 16.2 12 21 12 21z" fill="#E6127D" stroke="#3A4B9E" stroke-width="1.6" stroke-linejoin="round"/>
</g>
"""

ICON_HTML = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  html,body{{margin:0;padding:0;}}
  body{{
    width:512px;height:512px;
    background:
      radial-gradient(70% 55% at 20% 10%, rgba(230,18,125,.30), transparent 70%),
      radial-gradient(65% 55% at 85% 90%, rgba(58,75,158,.35), transparent 70%),
      #121A3D;
    display:flex; align-items:center; justify-content:center;
  }}
  svg{{ width:340px; height:340px; overflow:visible; }}
</style></head>
<body><svg viewBox="0 0 130 74">{HAT_HEART}</svg></body></html>"""

OG_HTML = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Yellowtail&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
  html,body{{margin:0;padding:0;}}
  body{{
    width:1200px;height:630px;
    background:
      radial-gradient(60% 60% at 12% -10%, rgba(230,18,125,.28), transparent 70%),
      radial-gradient(55% 60% at 100% 0%, rgba(58,75,158,.32), transparent 70%),
      radial-gradient(70% 55% at 60% 120%, rgba(58,75,158,.24), transparent 70%),
      #121A3D;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    font-family:"IBM Plex Mono",monospace;
  }}
  .kicker{{ color:#FF8FC7; font-size:26px; letter-spacing:8px; text-transform:uppercase; margin-bottom:18px; }}
  svg{{ width:150px; height:86px; overflow:visible; margin-bottom:6px; }}
  h1{{
    margin:0; font-family:"Yellowtail",cursive; font-weight:400;
    font-size:150px; line-height:0.86; text-align:center;
    color:#E6127D; -webkit-text-stroke:3px #3A4B9E;
  }}
</style></head>
<body>
  <p class="kicker">CANTORA &middot; PORTUGAL</p>
  <svg viewBox="0 0 130 74">{HAT_HEART}</svg>
  <h1>Liliana</h1>
  <h1>Oliveira</h1>
</body></html>"""

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--ignore-certificate-errors"])

    page = browser.new_page(viewport={"width": 512, "height": 512})
    page.set_content(ICON_HTML)
    page.wait_for_timeout(200)
    page.screenshot(path=str(OUT / "icon.png"))
    page.close()

    page2 = browser.new_page(viewport={"width": 1200, "height": 630})
    page2.set_content(OG_HTML)
    page2.wait_for_load_state("networkidle")
    page2.wait_for_timeout(300)
    page2.screenshot(path=str(OUT / "og.jpg"), type="jpeg", quality=92)
    page2.close()

    browser.close()

print("OK: icon.png + og.jpg gerados em", OUT)
