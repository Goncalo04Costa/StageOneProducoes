# Liliana Oliveira — sítio web

Site de artista, de uma página, para a cantora portuguesa Liliana Oliveira
(música, vídeos, agenda de espetáculos e contactos para reservas/imprensa).

## ⚠️ Antes de publicar — é um site-modelo

Não havia biografia, fotografias, discografia, vídeos, datas nem contactos
reais disponíveis para este projeto, por isso **todo o conteúdo é de
exemplo/placeholder**. Antes de publicar, substitui:

| O quê                        | Onde                                                         |
|-------------------------------|--------------------------------------------------------------|
| Biografia (secção Sobre)      | Texto entre `[colchetes]` no `index.html`, secção `#sobre`.  |
| Fotografias                   | Os 6 blocos "Foto — substituir" na secção `#galeria`; troca cada `<div class="ph">` por um `<img>` real. |
| Ícone / imagem de partilha    | `icon.png` e `og.jpg` foram recriados a partir do logótipo (script + chapéu + coração), não são o ficheiro oficial (ver abaixo). Substitui pelo logótipo real assim que possível. |
| Discografia / streaming       | Lista de faixas e links (Spotify, Apple Music, Deezer) em `#musica`. |
| Player do Spotify             | `SUBSTITUIR` no `src` do `iframe` — usa "Partilhar → Incorporar" no Spotify for Artists/Web Player para obteres o código real. |
| Vídeos                        | `SUBSTITUIR` nos dois `src="https://www.youtube.com/embed/SUBSTITUIR"`. |
| Datas de espetáculos           | Linhas `.agenda-row` em `#agenda`. |
| Contactos e redes sociais     | Email `booking@lilianaoliveira.pt` e os links de Instagram/YouTube/TikTok/Facebook (procura por `lilianaoliveira` no HTML). |
| Formulário de contacto        | `SUBSTITUIR` na `action` do `<form>` — cria uma conta grátis em [formspree.io](https://formspree.io) e cola o teu form ID. |
| Domínio                       | Onde aparece `https://lilianaoliveira.pt`: `index.html` (`og:url`, `og:image`, `twitter:image`, `canonical`, JSON-LD), `robots.txt` (`Sitemap:`) e `sitemap.xml` (`<loc>`). |

Sem estas alterações o site funciona e tem bom aspeto, mas mostra
informação de exemplo — não publiques antes de rever tudo.

## Ficheiros

| Ficheiro       | Descrição                                                          |
|----------------|---------------------------------------------------------------------|
| `index.html`   | O site completo (HTML + CSS + JS num só ficheiro). Sem build.       |
| `robots.txt`   | Permite indexação; aponta para o sitemap.                           |
| `sitemap.xml`  | Mapa do site (1 página).                                            |
| `icon.png`     | Favicon / ícone (512×512) — recriado a partir do logótipo, placeholder. |
| `og.jpg`       | Imagem de partilha (1200×630) — recriada a partir do logótipo, placeholder. |
| `assets.py`    | Recria `icon.png` / `og.jpg`. Precisa de Playwright + Chromium — ver comentário no topo do ficheiro. Só é preciso se quiseres voltar a gerar a versão placeholder. |

## Ícone e imagem de partilha (placeholder, mas já com as cores certas)

O logótipo oficial (script "Liliana Oliveira" em magenta com contorno
azul-marinho, chapéu de aba larga e coração de filigrana) foi partilhado
na conversa, mas **não cheguei a receber o ficheiro em si** — só o vi como
imagem. Por isso `icon.png` e `og.jpg` são uma recriação (mesmas cores,
tipo de letra script e motivo do chapéu+coração), não o ficheiro oficial.

O site inteiro (cores `--rose`/`--navy-accent` no `<style>`, tipo de letra
`Yellowtail` no wordmark, e o ícone SVG `#hatheart` embutido no HTML) já
segue essa identidade. Para ficar 100% fiel:

1. Guarda o ficheiro do logótipo oficial (PNG/SVG em alta resolução) nesta pasta.
2. Substitui `icon.png` (recorte quadrado, 512×512+, fundo sólido) e
   `og.jpg` (1200×630, logótipo centrado) por versões geradas a partir
   desse ficheiro — não precisas de correr nada, é só substituir.
3. Se as cores exatas do logótipo oficial diferirem um pouco do que aqui
   está, ajusta `--rose` / `--rose-hi` / `--rose-deep` / `--navy-accent`
   no topo do `<style>` do `index.html` para bater certo (código hex).

## Ver localmente

Abre `index.html` no navegador (duplo clique). É tudo — não precisa de servidor.

## Publicar (grátis)

Qualquer um destes serve, sem configuração:

- **Netlify Drop** — arrasta esta pasta para <https://app.netlify.com/drop>
- **GitHub Pages** — cria um repositório, faz push destes ficheiros, ativa Pages
- **Vercel / Cloudflare Pages** — importa a pasta como projeto estático

Para um domínio próprio (ex.: `lilianaoliveira.pt`), aponta o DNS para o serviço escolhido.

## Personalizar

Tudo o que muda com frequência está no topo do `<style>` do `index.html`,
no bloco `:root` (cores, tipos de letra, espaçamentos). Os textos estão
diretamente no HTML, por secção: hero, Sobre, Música, Vídeos, Agenda,
Galeria, Contacto.

- **Formulário:** envia os pedidos por **Formspree** via AJAX — o
  visitante fica no site e vê um painel de confirmação animado. Sem
  JavaScript, faz POST normal e o Formspree mostra a página de
  agradecimento.
  - A **1ª submissão** de cada domínio novo tem de ser confirmada por email.
  - Plano grátis do Formspree = **50 pedidos/mês**.
  - Anti-spam: campo-armadilha `_gotcha` (escondido) + validação de email.

## Notas técnicas

- Tema escuro assumido (azul-marinho + magenta, do logótipo). Acessível:
  navegação por teclado, `prefers-reduced-motion` respeitado, contraste AA.
- Tipos de letra: Yellowtail (nome/wordmark, script), Italiana (restantes
  títulos), Nunito (texto corrido) e IBM Plex Mono (rótulos), via Google Fonts.
- A animação de fundo é um `<canvas>` leve (luz de palco); desliga
  sozinha com o separador em segundo plano ou com movimento reduzido.
- Dados estruturados `MusicGroup` (JSON-LD) no `<head>` — valida em
  search.google.com/test/rich-results depois de pôres o domínio e a
  informação real.
