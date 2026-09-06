# Stage One Produções — sítio web

Site institucional de uma página para a Stage One Produções (produção de eventos,
contratação de artistas e aluguer técnico).

## Ficheiros

| Ficheiro             | Descrição                                                     |
|----------------------|------------------------------------------------------------- |
| `index.html`         | O site completo (HTML + CSS + JS num só ficheiro). Sem build. |
| `robots.txt`         | Permite indexação; aponta para o sitemap.                     |
| `sitemap.xml`        | Mapa do site (1 página).                                      |
| `logo.jpg`           | Logótipo completo em alta resolução (1254×1254).              |
| `logo-wordmark.png`  | Só o wordmark, recortado — usado no cabeçalho do site.        |
| `icon.png`           | Favicon / ícone (512×512).                                    |
| `og.jpg`             | Imagem de partilha (1200×630) — WhatsApp, Facebook, etc.      |
| `LogoStageONE.jpeg`  | Logótipo original enviado (fonte dos assets acima).           |
| `logo_assets.py`     | Recria `logo.jpg` / `logo-wordmark.png` / `icon.png` / `og.jpg` a partir do original. Corre: `python logo_assets.py` |

## Antes de publicar — trocar o domínio

Onde aparece `https://stageoneproducoes.pt`, mete o domínio real. Fica em 3 sítios:

1. `index.html` — comentário no `<head>` marca: `og:url`, `og:image`, `twitter:image`, `canonical`, JSON-LD
2. `robots.txt` — linha `Sitemap:`
3. `sitemap.xml` — `<loc>` (e atualiza `<lastmod>`)

Sem domínio o site funciona na mesma — só a partilha e o SEO é que ficam à espera.
Depois de online: submete `sitemap.xml` no Google Search Console.

## Ver localmente

Abre `index.html` no navegador (duplo clique). É tudo — não precisa de servidor.

## Publicar (grátis)

Qualquer um destes serve, sem configuração:

- **Netlify Drop** — arrasta a pasta `StageOne` para <https://app.netlify.com/drop>
- **GitHub Pages** — cria um repositório, faz push destes ficheiros, ativa Pages
- **Vercel / Cloudflare Pages** — importa a pasta como projeto estático

Para um domínio próprio (ex.: `stageoneproducoes.pt`), aponta o DNS para o serviço escolhido.

## Personalizar

Tudo o que muda com frequência está no topo do `<style>` do `index.html`,
no bloco `:root` (cores, tipos de letra, espaçamentos). Os textos estão
directamente no HTML, por secção: hero, Sobre, Serviços, Como trabalhamos, Contacto.

- **Logo maior/melhor:** substitui `Logo.jpg` (o atual tem só 150×150 px).
  O nome do ficheiro pode ficar igual e não é preciso mexer no HTML.
- **Imagem de partilha:** substitui `og.jpg` (mantém 1200×630 px). É o que
  aparece quando o link é partilhado. Testa em opengraph.dev depois de publicar.
- **Contactos:** procura `932 091 099` e `stageone-prod@hotmail.com` no HTML.
- **WhatsApp:** procura `wa.me/351932091099` (o número e a mensagem pré-escrita).
- **Formulário:** envia os pedidos por **Formspree** (`https://formspree.io/f/mrpgadwq`)
  via AJAX — o visitante **fica no site** e vê um painel de confirmação animado
  (visto certo a desenhar-se). Erros aparecem inline com um leve "shake".
  Sem JavaScript, faz POST normal e o Formspree mostra a sua página de agradecimento.
  - A **1ª submissão** de cada domínio novo tem de ser confirmada por email
    (o Formspree envia para o dono da conta).
  - Plano grátis do Formspree = **50 pedidos/mês**.
  - Para mudar o destino, cria outro form no Formspree e troca o `action` no HTML.
  - Anti-spam: campo-armadilha `_gotcha` (escondido) + validação de email.

## Notas técnicas

- Tema escuro assumido (ambiente de palco). Acessível: navegação por teclado,
  `prefers-reduced-motion` respeitado, contraste AA.
- Tipos de letra: Archivo, Manrope e IBM Plex Mono (Google Fonts).
- A animação de fundo é um `<canvas>` leve (luz de palco); desliga sozinha
  com o separador em segundo plano ou com movimento reduzido.
- Dados estruturados `LocalBusiness` (JSON-LD) no `<head>` — valida em
  search.google.com/test/rich-results depois de pôres o domínio.
