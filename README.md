# Mi CompañIA — Manual Maestro y Estándar A

Manuales interactivos en HTML del proyecto **Mi CompañIA** (iniciativa de FUNDES Latinoamérica con apoyo de Google.org) sobre Inteligencia Artificial aplicada a las MiPyMEs mexicanas. Este repositorio publica por ahora **dos manuales**: el Manual Maestro (general) y el Manual del Estándar A · Implementación.

## Estructura

```
manuales-ec-fundes/
├── index.html                       Landing principal
├── maestro/                         Manual Maestro (6 capítulos)
│   ├── index.html                   Cap 1 · Bienvenida y diagnóstico
│   ├── que-es.html                  Cap 2 · Qué es la certificación CONOCER
│   ├── como-se-evalua.html          Cap 3 · Cómo se evalúa por evidencias
│   ├── proceso.html                 Cap 4 · Proceso paso a paso (6 etapas)
│   ├── es-para-ti.html              Cap 4 · Los 4 estándares + finder
│   └── recursos.html                Cap 6 · FAQ, glosario y referencias
├── estandar-a/                      Manual del Estándar A
│   ├── index.html                   Bienvenida + ficha técnica del Estándar A
│   ├── elemento-1.html              Elemento 1 · Planear
│   ├── elemento-2.html              Elemento 2 · Ejecutar
│   ├── elemento-3.html              Elemento 3 · Evaluar
│   ├── instrumento.html             Instrumento de Evaluación de Competencia (IEC)
│   ├── ruta-preparacion.html        Ruta de preparación de 4 semanas
│   └── recursos.html                FAQ, glosario y referencias R1-R24
├── flujo-trabajo.html               Infografía del flujo de trabajo en equipo
├── flujo-trabajo.png                Infografía exportada como imagen
├── assets/
│   ├── styles.css                   Sistema de diseño compartido
│   └── interactive.js               Componentes interactivos (lesson tabs, audio, tabs, quiz)
├── img/                             Imágenes (logo, heroes, certificado)
├── media/                           Audios narrados + scripts SSML
├── scripts/                         Helpers (TTS ElevenLabs/Google, carga de .env)
├── design.md                        Sistema de diseño (paleta, tipografía, componentes)
├── .env.example                     Plantilla de variables de entorno
├── README.md
└── .gitignore
```

## Cómo verlo localmente

Solo abre `index.html` con doble clic en cualquier navegador (Chrome, Edge, Firefox). No requiere servidor.

## Cómo colaborar

Trabajamos **tres personas** sobre este repo: Oscar, Iván y Aide. Da igual el editor (Antigravity o Claude Code) — por debajo todos usan el mismo Git y el mismo repositorio. La rama `main` es **el archivo final**: la única versión, y todos trabajan directamente sobre ella.

Tu asistente de IA (Claude Code o Antigravity) hace todo el Git por ti. Tú solo conversas:

1. **"Trae lo último"** — la IA hace `git pull`; empiezas con la versión más reciente.
2. **Pídele los cambios** — le dices qué desarrollar o corregir en el HTML; la IA edita.
3. **"Sube los cambios"** — la IA hace `git commit` y `git push`; tu aporte queda en el archivo final.

No hay ramas ni Pull Requests. Los demás verán tu aporte la próxima vez que traigan lo último.

### Para no pisarse

- **Repártanse por archivo**: una persona por `maestro/Xxx.html` o `estandar-a/Xxx.html` a la vez. Si nadie edita el mismo archivo, nunca hay choques.
- **Avisen** antes de tocar `index.html`, `assets/styles.css` o `assets/interactive.js` — los comparten todos los manuales.
- **Suban seguido**, en cambios chicos: mientras menos tiempo pase entre traer y subir, menos posibilidad de cruzarse.
- Si dos editan el mismo archivo casi a la vez, la IA junta el trabajo sola; solo pedirá ayuda en el caso raro de que dos cambien exactamente la misma línea.

Para una vista visual del proceso, abre `flujo-trabajo.html`.

## Estado actual de los manuales

| Manual | Capítulos / Elementos | Estado |
|---|---|---|
| **Manual Maestro** | 6 capítulos · audios narrados · quizzes · diagramas SVG | Desarrollado |
| **Estándar A — Implementación** | 3 elementos · 14 conocimientos · 13 productos · caso La Espiga | Desarrollado |
| **Estándar B — Desarrollar con IA** | 4 elementos · 13 productos · 7 desempeños | Publicado |
| Estándar C — Marketing digital | — | En desarrollo |
| Estándar D — Transformación digital | — | En desarrollo |

## Variables de entorno

Algunos scripts (generación de audios TTS, imágenes con Higgsfield, etc.) requieren claves de API. Copia `.env.example` a `.env` y completa tus claves:

```bash
cp .env.example .env
# Edita .env y agrega tus valores reales (NUNCA lo commitees: ya está en .gitignore)
```

## Visibilidad del repositorio

Este repositorio es **privado**: solo el equipo (Oscar, Iván y Aide) puede verlo y editarlo. Para sumar a alguien más, el dueño lo agrega en *Settings → Collaborators*.

GitHub Pages (publicar el manual en una URL) requiere un plan de pago para repos privados, así que por ahora el manual se revisa abriéndolo localmente.

## Fuentes

El contenido proviene de los documentos oficiales del proyecto FUNDES Componente 2:

- `Manual_Maestro_v2.pdf` (base del Manual Maestro)
- `Manual_Estandar_A_v2.pdf` (base del Manual del Estándar A)
- Tablas de especificaciones, conocimientos y referencias R1-R24

Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.
