# Configuración de Claude Code · Mi CompañIA

Esta carpeta `.claude/` contiene la configuración de Claude Code específica para este proyecto. Cuando alguien abre el repo con Claude Code, estos archivos se cargan automáticamente y dan acceso a un equipo de **agentes especializados** + **slash commands** que conocen el proyecto a fondo.

> **Propósito educativo:** este folder está diseñado también como ejemplo. Cada archivo lleva comentarios explicando *por qué* se hizo así, no solo *qué* hace. Léelo antes de modificar para mantener la coherencia.

---

## ¿Agente o Skill? La diferencia

| | **Agente** | **Skill** |
|---|---|---|
| **Cómo se invoca** | El agente principal lo delega solo (lee la `description` para decidir) o el usuario pide explícitamente | El usuario lo invoca con `/nombre` |
| **Qué tan grande es la tarea** | Multi-paso, requiere razonamiento dedicado | Un workflow concreto, idealmente <10 pasos |
| **Tiene su propia ventana de contexto** | Sí — protege el contexto del agente principal | No — corre en el contexto actual |
| **Cuándo elegirlo** | Tareas que necesitan investigar/leer mucho, o que se repiten con variaciones | Comandos repetitivos con plantilla clara |

**Regla práctica:** si el resultado depende de leer 5+ archivos o de interpretar contenido nuevo cada vez, usa **agente**. Si es "haz X paso a paso siempre igual", usa **skill**.

---

## El equipo de agentes

El equipo tiene **16 especialistas y 1 orquestador general**. Cada agente conserva un dominio estrecho para que el routing automático sea preciso.

### Producción de contenido

| Agente | Cuándo se invoca | Dominio |
|---|---|---|
| [`mi-compania-content-developer`](agents/mi-compania-content-developer.md) | Hay material fuente (DOCX, tabla de especificaciones, notas) que hay que volver HTML del proyecto | Contenido normativo: elementos, conocimientos, descripciones técnicas |
| [`mi-compania-learning-content-generator`](agents/mi-compania-learning-content-generator.md) | Hay fuentes y objetivo aprobados y se necesita desarrollar una lección | Explicaciones, ejemplos, casos, guiones y práctica guiada |
| [`mi-compania-pedagogo`](agents/mi-compania-pedagogo.md) | El contenido factual ya existe → falta el envoltorio pedagógico (ejercicios, callouts, secuencia de aprendizaje, evaluación formativa) | Diseño instruccional CONOCER + andragogía para MiPyMEs |
| [`mi-compania-copywriter`](agents/mi-compania-copywriter.md) | Hay que escribir copy persuasivo o de UI (CTAs, hero, microcopy, mensajes de error) aplicando voz de marca | Voz, tono, microcopy, español mexicano |

### Implementación técnica

| Agente | Cuándo se invoca | Dominio |
|---|---|---|
| [`mi-compania-frontend`](agents/mi-compania-frontend.md) | Implementar HTML/CSS/JS, responsive, componentes interactivos, performance | Stack actual: HTML+CSS+JS vanilla, mobile-first |
| [`mi-compania-backend`](agents/mi-compania-backend.md) | Deploy, CI/CD, build pipelines, optimización de assets, integración futura de formularios/API | GitHub Pages, Cloudflare Pages, Vercel, GitHub Actions |
| [`mi-compania-image-producer`](agents/mi-compania-image-producer.md) | Producir una imagen individual desde un brief aprobado | Generación, selección, optimización, alt y recortes |
| [`mi-compania-audio-producer`](agents/mi-compania-audio-producer.md) | Producir una narración o clip desde un guion aprobado | TTS voz Leda, control de calidad, MP3 y transcripción |
| [`mi-compania-asset-generator`](agents/mi-compania-asset-generator.md) | Producir video o un paquete que combina varios medios | Pipeline multimedia coordinado y optimización |

### Experiencia y diseño

| Agente | Cuándo se invoca | Dominio |
|---|---|---|
| [`mi-compania-ux-architect`](agents/mi-compania-ux-architect.md) | Hay que reorganizar recorridos, navegación, jerarquía de información o reducir fricción | UX, arquitectura de información, estados y pruebas de usabilidad |
| [`mi-compania-elearning-specialist`](agents/mi-compania-elearning-specialist.md) | Hay que diseñar una experiencia asincrónica, ruta, medios, progreso o retorno | Educación en línea, microlearning, feedback y aprendizaje móvil |
| [`mi-compania-ui-designer`](agents/mi-compania-ui-designer.md) | Una vista o componente necesita especificación visual y responsive | UI, sistema de diseño, tokens, estados y handoff |
| [`mi-compania-graphic-designer`](agents/mi-compania-graphic-designer.md) | Se requiere dirección de arte, infografía, iconografía, diagrama o brief de imagen | Diseño gráfico, composición y especificación de assets |

### Calidad

| Agente | Cuándo se invoca | Dominio |
|---|---|---|
| [`mi-compania-brand-reviewer`](agents/mi-compania-brand-reviewer.md) | Auditar archivo contra reglas del sistema de diseño antes de commit | Tokens, voz, contraste WCAG AA, accesibilidad básica |
| [`mi-compania-accessibility-auditor`](agents/mi-compania-accessibility-auditor.md) | Verificar WCAG 2.2 AA, teclado, lector de pantalla, reflow o multimedia | Accesibilidad especializada con evidencia y severidad |
| [`mi-compania-design-auditor`](agents/mi-compania-design-auditor.md) | Cerrar un cambio visual sustantivo antes de publicar | Auditoría independiente de brief, UI, UX, responsive y calidad |

### Coordinación

| Agente | Cuándo se invoca | Dominio |
|---|---|---|
| [`mi-compania-orchestrator`](agents/mi-compania-orchestrator.md) | La petición mezcla dos o más disciplinas o requiere diseño → implementación → auditoría | Alcance, dependencias, propiedad de archivos e integración |

---

## Los slash commands

8 skills que el usuario invoca directamente.

| Skill | Sintaxis | Hace |
|---|---|---|
| [`orquestar`](skills/orquestar/SKILL.md) | `/orquestar <petición>` | Coordina tareas que mezclan varias disciplinas |
| [`nueva-seccion-ec`](skills/nueva-seccion-ec/SKILL.md) | `/nueva-seccion-ec <tipo>` | Inserta sección nueva en EC actual (`elemento`, `conocimiento`, `callout`, `stats`) |
| [`crear-actividad-interactiva`](skills/crear-actividad-interactiva/SKILL.md) | `/crear-actividad-interactiva <tipo>` | Diseña e implementa una actividad pedagógica accesible |
| [`convertir-muro-de-texto`](skills/convertir-muro-de-texto/SKILL.md) | `/convertir-muro-de-texto <archivo>` | Convierte contenido denso en aprendizaje activo |
| [`revisar-marca`](skills/revisar-marca/SKILL.md) | `/revisar-marca [archivo]` | Audita archivo contra reglas de marca (delega a brand-reviewer) |
| [`pre-publicacion`](skills/pre-publicacion/SKILL.md) | `/pre-publicacion` | Checklist completo antes de commit/deploy: tamaño imágenes, links rotos, brand check, HTML válido |
| [`auditar-experiencia`](skills/auditar-experiencia/SKILL.md) | `/auditar-experiencia [alcance]` | Consolida auditoría de diseño/UX, marca y accesibilidad con dictamen único |
| [`crear-leccion-multimedia`](skills/crear-leccion-multimedia/SKILL.md) | `/crear-leccion-multimedia <tema>` | Coordina pedagogía, e-learning, contenido, medios, implementación y auditoría |

---

## Decisiones de diseño

### ¿Por qué tantos agentes en lugar de uno generalista?

Cada agente es más útil mientras más estrecho es su dominio. El routing automático de Claude Code lee la `description` de cada agente para decidir cuál invocar. Si dos agentes se solapan, el modelo se confunde y termina invocando uno aleatorio. Por eso:

- `content-developer` produce contenido **factual largo** desde fuentes
- `learning-content-generator` desarrolla la **explicación educativa** desde fuentes y objetivos aprobados
- `copywriter` produce **microcopy persuasivo** desde voz de marca
- Los tres escriben texto, pero su fuente, escala y propósito son distintos.

### ¿Por qué `sonnet` en todos?

Claude Sonnet 4.6 es el balance correcto para este proyecto:
- **Opus** sería sobrecosto: el contenido no requiere razonamiento profundo, solo aplicación de reglas claras
- **Haiku** sería insuficiente: hay que mantener voz/marca consistente y eso requiere atención al contexto

Si en el futuro un agente realmente necesita razonamiento más profundo (ej. arquitectura de Astro, debugging complejo), se sobrescribe con `model: opus` en su frontmatter.

### ¿Por qué project-scoped (`.claude/`) en vez de user-scoped (`~/.claude/`)?

Estos agentes y skills son **específicos a este proyecto**. Viajan con el repo: cualquier colaborador que clone el proyecto y abra Claude Code los recibe automáticamente. Esto los convierte en parte del onboarding del proyecto.

### Permisos (`tools`)

Cada agente declara explícitamente qué tools puede usar. Principio: mínimo necesario.

| Tool | Quién lo usa | Por qué |
|---|---|---|
| `Read`, `Glob`, `Grep` | Casi todos | Investigar el código antes de actuar |
| `Edit`, `Write` | Productores de contenido / código | Modificar archivos |
| `Bash` | Frontend, backend, asset-generator y auditores | Comandos shell (compresión, deploy, validación) |

Los auditores pueden leer y correr Bash para validaciones, pero **no pueden escribir**. Esto separa diseño/implementación de la aprobación final.

---

## Cómo extender el sistema

### Agregar un agente nuevo

1. Crea `agents/mi-compania-<nombre>.md` con frontmatter:
   ```markdown
   ---
   name: mi-compania-<nombre>
   description: <una línea explicando CUÁNDO invocarlo, no qué hace>
   tools: Read, Edit  # mínimo necesario
   model: sonnet
   ---
   ```
2. En el body, define: rol, qué SÍ hace, qué NO hace, ejemplos, cuándo delegar a otros agentes.
3. Agrégalo a la tabla de este README.

### Agregar un slash command

1. Crea carpeta `skills/<nombre>/` y dentro `SKILL.md` con frontmatter:
   ```markdown
   ---
   name: <nombre>
   description: <una línea>
   ---
   ```
2. Si recibe argumentos, documéntalos en `<arguments>`.
3. En el body, escribe el workflow paso a paso.

### Convenciones de nombres

- **Agentes:** `mi-compania-<rol-en-kebab-case>` — el prefijo `mi-compania-` evita colisiones con agentes globales del usuario.
- **Skills:** `<verbo-objeto>` en español, kebab-case (ej. `nueva-seccion-ec`, `revisar-marca`). Más cortos que agentes porque el usuario los teclea.

---

## Recursos del proyecto

- [`design.md`](../design.md) — Sistema de diseño canónico (colores, tipografía, voz, componentes)
- [`README.md`](../README.md) — README del repo
- [`assets/styles.css`](../assets/styles.css) — Tokens y componentes CSS implementados

Cuando un agente necesite contexto del proyecto, lee primero estos tres archivos.
