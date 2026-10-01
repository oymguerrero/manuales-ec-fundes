# Mi CompañIA — Manuales de los cuatro estándares

Manuales interactivos en HTML del proyecto **Mi CompañIA** (iniciativa de FUNDES México con apoyo de Google.org) sobre Inteligencia Artificial aplicada a las MiPyMEs mexicanas. Este repositorio publica **cinco cursos**: el introductorio sobre el sistema CONOCER y uno por cada una de las cuatro propuestas de estándar, que aún no han sido publicadas oficialmente.

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
├── diagnostico/                     Finder: qué estándar le corresponde a cada perfil
├── estandar-a/                      Adopción de soluciones de IA en los procesos
│   ├── index.html                   Bienvenida + ficha técnica del estándar
│   ├── elemento-1.html              Elemento 1 · Planear
│   ├── elemento-2.html              Elemento 2 · Adoptar
│   ├── elemento-3.html              Elemento 3 · Evaluar
│   ├── ruta-preparacion.html        Ruta de preparación
│   ├── recursos.html                FAQ, glosario y referencias R1-R24
│   └── templates/                   12 plantillas descargables de los productos
├── estandar-b/                      Creación de soluciones comerciales con IA
├── estandar-c/                      Consultoría en mercadotecnia digital con IA
├── estandar-d/                      Soluciones tecnológicas de modernización digital
│                                    (los tres con 4 elementos, ruta, recursos y templates)
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

- **Repártanse por archivo**: una persona por `maestro/Xxx.html` o `estandar-<x>/Xxx.html` a la vez. Si nadie edita el mismo archivo, nunca hay choques.
- **Avisen** antes de tocar `index.html`, `assets/styles.css` o `assets/interactive.js` — los comparten todos los manuales.
- **Suban seguido**, en cambios chicos: mientras menos tiempo pase entre traer y subir, menos posibilidad de cruzarse.
- Si dos editan el mismo archivo casi a la vez, la IA junta el trabajo sola; solo pedirá ayuda en el caso raro de que dos cambien exactamente la misma línea.

Para una vista visual del proceso, abre `flujo-trabajo.html`.

## Estado actual de los manuales

Las cifras son las del documento final de cada estándar (el F21), cotejadas
elemento por elemento con lo que publica el sitio.

| Curso | Elementos y evidencias | Caso |
|---|---|---|
| **Curso introductorio** | 6 capítulos · audios narrados · quizzes · diagramas SVG | — |
| **A — Adopción de IA en los procesos** | 3 elementos · 12 productos · 4 desempeños · 14 conocimientos | La Espiga |
| **B — Creación de soluciones comerciales** | 4 elementos · 14 productos · 5 desempeños · 15 conocimientos | Tonalli |
| **C — Consultoría en mercadotecnia digital** | 4 elementos · 10 productos · 8 desempeños · 10 conocimientos | La Cuesta |
| **D — Modernización digital** | 4 elementos · 16 productos · 1 desempeño · 12 conocimientos | El Surtido |

Las cuatro propuestas de estándar **aún no están publicadas por CONOCER**; su
contenido puede cambiar.

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

- El F21 (estándar de competencia) de cada una de las cuatro propuestas
- `Manual_Maestro_v2.pdf` (base del curso introductorio)
- Tablas de especificaciones, conocimientos y referencias de cada estándar

El F22 (instrumento de evaluación) **no** se usa como fuente de contenido: los
materiales deben ayudar a pasar la evaluación, no resolverla.

Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.
