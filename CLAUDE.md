# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repositorio

Manuales web interactivos del proyecto **Mi CompañIA** (FUNDES Latinoamérica + Google.org) sobre certificación CONOCER en IA aplicada a MiPyMEs mexicanas. Dos manuales publicados:

- **Curso introductorio** (`maestro/`): 6 capítulos sobre el sistema CONOCER (qué es, cómo evalúa, proceso, ¿es para ti?, recursos).
- **Estándar A · Implementar IA** (`estandar-a/`): 3 elementos + instrumento + ruta + recursos, con el caso pedagógico transversal "La Espiga" (panadería ficticia con Doña Beatriz + Carlos).

El contenido normativo viene de `Manual_Maestro_v2.pdf` y `Manual_Estandar_A_v2.pdf` (fuentes que NO están en el repo). Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.

## Stack y principio rector

**HTML/CSS/JS vanilla puro, sin build step.** Abrir `index.html` con doble clic debe funcionar. Sin npm, sin frameworks, sin transpiler. Single source para CSS y JS:

- `assets/styles.css` — sistema de diseño completo (~4500 líneas)
- `assets/interactive.js` — todos los componentes interactivos (~1800 líneas)

Únicas dependencias externas: Google Fonts (Afacad/Inter por CDN), y carga **condicional** de Mermaid 10 / SortableJS / Chart.js 4 vía `loadCDN()` helper — solo se inyectan cuando una página tiene el componente que las requiere.

## Cómo correr localmente

```bash
# Opción 1: doble clic en index.html (basta porque todo es estático)
# Opción 2: live server (recomendado si vas a probar audio/imágenes con paths relativos)
python -m http.server 5500
# o en VS Code: extensión Live Server → "Open with Live Server"
```

Sin tests automatizados. Antes de commit:

```bash
# Sintaxis JS
node --check assets/interactive.js

# Validar que todos los <script type="application/json"> son parseables
python -c "
import json, re, pathlib
errs = 0
for f in pathlib.Path('.').rglob('*.html'):
    text = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<script type=\"application/json\"[^>]*>(.+?)</script>', text, re.DOTALL):
        try: json.loads(m.group(1))
        except json.JSONDecodeError as e: print(f'  JSON ERROR in {f}: {e}'); errs += 1
print('JSON OK' if errs == 0 else f'{errs} errores')
"
```

## Variables de entorno y scripts

`.env` (gitignored) sostiene claves para los scripts de generación de assets en `scripts/`. Cargar con:

```bash
. ./scripts/load-env.sh        # Bash/zsh
. .\scripts\load-env.ps1       # PowerShell
```

| Script | Para qué |
|---|---|
| `tts-elevenlabs.ps1` | Genera MP3 de narración con ElevenLabs (voz Alice, modelo `eleven_multilingual_v2`). Lee `media/scripts/<nombre>.txt` y escribe `media/audio-<nombre>.mp3`. ElevenLabs free tier limita 10k chars/mes. |
| `tts-generate.ps1` | Variante con Google Cloud TTS Neural2 (fallback si ElevenLabs no disponible). |
| `generate-templates.py` | Genera los 13 templates descargables del Estándar A (`.docx`/`.xlsx`/`.pptx`) con `python-docx`, `openpyxl`, `python-pptx`. Salida en `estandar-a/templates/`. |
| `higgsfield` (CLI) | Imágenes del caso La Espiga. Modelo barato: `text2image_soul_v2` (0.12 créditos). Rate limit free tier: 4 jobs concurrentes. Después de generar, comprimir PNG → JPEG con PIL (típicamente 27 MB → 867 KB, 97% reducción) y actualizar referencias `.png` → `.jpg` en HTML. |

## Arquitectura de componentes interactivos (`assets/interactive.js`)

Patrón consistente: cada componente es `function initX(container)`, se registra al final en `init()`. Los datos pedagógicos viven **inline** en cada HTML usando `<script type="application/json" class="X__data">{...}</script>` — nunca un archivo de datos central. Razón: evita `fetch()` async, race conditions, y mantiene co-localización editorial (quien edita el HTML edita la actividad).

Componentes pedagógicos (ordenados por nivel Bloom que tocan):

| Componente | Bloom | Datos via | CDN |
|---|---|---|---|
| `.flashcard-deck` | Recordar/Comprender | JSON inline (mazo con micro-SRS) | — |
| `.flipcard` | Comprender | data-attrs en buttons | — |
| `.quiz` con `data-type=mc/vf/order/cloze` | Comprender/Aplicar | data-attrs + markup | — |
| `.case-lab` | Aplicar/Analizar | JSON inline (tabs F21 ↔ La Espiga) | — |
| `.timeline-interactive` | Comprender/Aplicar | JSON inline (hitos clicables) | — |
| `.drag-sort` | Aplicar/Analizar | markup (zonas + banco) | SortableJS |
| `.diagram-mermaid` | Comprender | `<pre class="mermaid">` | Mermaid |
| `.chart-block` | Analizar | JSON inline (config Chart.js) | Chart.js |
| `.swipe-decide` | Evaluar | JSON inline (tarjetas binarias) | — |
| `.scenario-decision` | Aplicar/Evaluar/Crear | JSON inline (ramificado ok/risk/wrong) | — |
| `.progress-skill` | (gamificación) | lee localStorage | — |

Componentes de layout/navegación (no pedagógicos pero críticos): `.tabs` (ARIA roving tabindex), `.checklist` (persistencia local), `.audio-narration` (mini-bar flotante scoped al módulo activo), `.lesson-tabs` (LMS sidebar + progress por módulo), `.glossary--rich` (búsqueda + índice alfabético), `.printable-checklist` (PDF via `window.print`).

### Métricas y persistencia

Wrapper único `recordEvent(type, payload)` escribe a `mi-compania-metrics::v1` (array circular, últimos 500 eventos). Todas las claves localStorage llevan prefijo `mi-compania-` y versión `::v1::` para poder invalidar limpiamente si cambia el esquema. `.progress-skill` lee todas estas claves y reconstruye un dashboard del usuario.

### Drag-sort: dos detalles que se rompen fácil

Si rehaces `initDragSort`:
1. **Pasa opts FRESCOS a cada `Sortable.create()`** (no reutilizar la misma referencia). SortableJS muta `group: 'name'` → `group: {name, pull, put}` internamente al primer create. Si reutilizas el objeto, las zonas creadas después reciben un group ya transformado y la comunicación bidireccional se rompe.
2. Usa `emptyInsertThreshold: 20` para permitir drop en contenedores casi vacíos.

## Sistema de agentes y skills (`.claude/`)

**Importante:** `.claude/` está en `.gitignore` global del usuario pero **este repo lo trackea explícitamente** (es trabajo colaborativo entre 3 personas que necesitan los mismos agentes/skills).

Agentes especializados (`.claude/agents/`), cada uno con un rol estricto que no se solapa:

| Agente | Hace | NO hace |
|---|---|---|
| `mi-compania-orchestrator` | **Coordina** a los demás: recibe petición vaga, decide qué agentes invocar, en qué orden, integra resultados, propone commit | No modifica archivos directamente — solo coordina |
| `mi-compania-content-developer` | Vuelca contenido normativo de PDFs/DOCX a HTML | Copy persuasivo, ejercicios pedagógicos |
| `mi-compania-copywriter` | Copy de UI: hero, CTAs, microcopy, headlines | Contenido normativo largo, ejercicios |
| `mi-compania-pedagogo` | Diseña ejercicios, callouts, secuencias andragógicas | Implementa JS/CSS, escribe contenido factual |
| `mi-compania-frontend` | HTML semántico, CSS con tokens, JS vanilla | Contenido, copy, imágenes |
| `mi-compania-asset-generator` | Imágenes/videos/audio (Higgsfield, ElevenLabs) | UI, contenido |
| `mi-compania-brand-reviewer` | **Solo audita** contra el sistema de diseño | No modifica nada — solo reporta |
| `mi-compania-backend` | Deploy, CI/CD, hosting, optimización pipeline | UI |

Skills (`.claude/skills/`) son comandos slash que orquestan agentes:

- `/orquestar <petición>` → invoca `mi-compania-orchestrator` para peticiones vagas que cruzan disciplinas. Útil cuando no sabes qué skill específica usar.
- `/revisar-marca [archivos...]` → invoca `brand-reviewer` y devuelve reporte categorizado (🔴 bloqueante / 🟡 recomendado / 🟢 verificado).
- `/convertir-muro-de-texto` → toma una sección densa y la fracciona pedagógicamente.
- `/crear-actividad-interactiva` → pedagogo diseña + frontend implementa.
- `/nueva-seccion-ec` → inserta sección en `estandar-a/elemento-*.html` con plantillas.
- `/pre-publicacion` → checklist antes de publicar.

**Cuándo usar el orchestrator vs invocar un agente directo:**

- Usa `/orquestar` o invoca `mi-compania-orchestrator` cuando la petición **mezcla 2+ disciplinas** (ej. contenido normativo + componente interactivo + revisión) y no sabes qué agentes elegir ni en qué orden.
- Invoca un agente directo cuando la petición **claramente** es de una sola disciplina (ej. "audita la marca de X" → llama a brand-reviewer; "implementa este componente" → llama a frontend).
- NO uses el orquestador para cambios de 1-2 líneas — el main loop los hace directo.

## Sistema de diseño

Fuente canónica: `design.md` (~62k chars). Resumen operativo:

- **Paleta brandbook**: `--color-azul-profundo: #28467e`, `--color-azul-claro: #529ed7`, `--color-amarillo: #f7c031`, `--color-naranja: #f29100`. Token utilitario `--color-azul: #1F4E8C` (medio, no brandbook).
- **Tipografía**: Afacad primaria, Open Sans Condensed secundaria, Inter fallback. Cargadas con `display=swap` desde Google Fonts.
- **Tokens semánticos de callout** (no son colores brand sino marcadores tipológicos): `.callout--important`, `--tip`, `--example`, `--reflection`, `--template`. Cada uno tiene su paleta consistente — no sustituir por colores brand.
- **Contraste**: todos los pares texto+fondo pasan WCAG AA ≥ 4.5:1. El reviewer valida en cada audit.
- **Sparkles** (decorativos): SVG inline en eyebrows de hero, usan `--color-amarillo` o `--color-naranja`.
- **Hex fuera de paleta con significado pedagógico**: `#9F2929` (rojo "antes/negativo" en SVGs comparativos), `#7C3AED` (morado "categoría distinta"). NO auto-reemplazar — alteran el mensaje visual.

## Flujo de trabajo del equipo

**Tres personas** trabajan sobre `main` directamente — sin ramas, sin PRs. Repartirse por archivo evita conflictos. Antes de tocar `index.html`, `assets/styles.css` o `assets/interactive.js`, avisar al equipo (son compartidos por todos los manuales).

El idioma del repo es **español mexicano**. Voz de marca: cercana, práctica, esperanzadora, honesta, empoderadora. "Hablamos como un amigo que sabe: claro, humano, útil y sin tecnicismos innecesarios."

## Convenciones editoriales del Curso introductorio (`maestro/`)

Patrones consolidados que conviene respetar al editar páginas de `maestro/`:

- **Eyebrow del hero**: formato `Tema N. <Nombre>` (ej. `Tema 1. Marco Institucional`, `Tema 3. El recorrido completo`). El número de Tema coincide con la posición del capítulo en el flujo del curso, NO con el número del archivo en `accordion__num`.
- **Primer módulo de cada capítulo**: siempre `0. Visión general` (`id="vision-general"`, `open` por default) con un párrafo de contexto + un `callout--example` titulado "Objetivo específico" que enuncia qué será capaz de hacer el aspirante al terminar el tema. El callout abre con un SVG de target (`circle` triple) en azul.
- **Numeración de módulos restantes**: empieza en `<N>.1` donde N es el número de Tema. Cuando se renumeran capítulos (ej. al eliminar un módulo intermedio), actualizar **todos** los `accordion__num` siguientes y los `id` si vienen referenciados desde otras páginas.
- **Notas editoriales temporales en rojo**: pueden aparecer como `<p style="color: red;">` o `<span style="background: #fff0f0;">` durante refactors colaborativos. Son trabajo en curso, NO contenido final. El reviewer de marca las marca como bloqueantes; al cierre de un sprint conviene eliminarlas.

## Templates ofimáticos del Estándar A

13 templates descargables (`estandar-a/templates/`) generados con `generate-templates.py`. Distribución elegida por naturaleza del producto, no por uniformidad:

- **9 Word (.docx)**: reportes, informes, propuestas, actas.
- **3 Excel (.xlsx)**: 1.4.5 matriz impacto/viabilidad (con fórmulas), 1.4.6 hoja de ruta tipo Gantt, 4.4.1 reporte resultados (con variación %).
- **1 PowerPoint (.pptx)**: 3.4.3 material de capacitación, 16:9, ~12 slides.

Cada template trae **criterio F21 literal + caso La Espiga (ejemplo) + preguntas guía (no respuestas)** — pedagógicamente, deben ayudar a pasar la evaluación, no resolverla.

## Convenciones de commits

- Mensaje en imperativo + descripción de qué cambió y por qué.
- Co-Authored-By cuando aplique (Claude, Antigravity).
- Suben seguido, en cambios chicos; cualquier diff > 500 líneas conviene partirlo.
- Direct push a `oymguerrero/main`. Si encuentras conflicto, `git pull --rebase` antes de push.

## Carpeta local `extras/`

Cualquier cosa que vivas en `extras/` queda fuera de git (entrada en `.gitignore`). Úsala para drafts, PDFs fuente del brandbook, materiales de referencia internos, audios crudos antes de optimizar, etc. Nada de ahí se sube al repositorio compartido.

## Pendientes conocidos

- README.md está desactualizado en algunos puntos (menciona `cuatro-estandares.html`; ahora es `es-para-ti.html`). No es bloqueante pero conviene actualizar al cerrar un sprint.
- Hex `#9F2929` y `#7C3AED` en SVGs son decisión editorial pendiente — el brand reviewer los marca cada vez.
- Cuando agregues un componente interactivo nuevo, actualiza `design.md §16.9` (tabla del catálogo) **en el mismo commit**. El propio §16.9 lo explicita: "*Cuando se implemente un componente nuevo, mueve su fila de pendiente a implementado y actualiza esta tabla.*"
