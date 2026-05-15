# Manuales EC — Componente 2 Fundes

Manuales interactivos en HTML de los 4 Estándares de Competencia (EC) sobre Inteligencia Artificial aplicada a MiPyMEs. Componente 2 de Fundes.

## Estructura

```
manuales-ec-fundes/
├── index.html              Landing principal con los 4 ECs
├── ec1.html                EC1 — Soluciones de IA alineadas a la MiPyME
├── ec2.html                EC2 — Productos y servicios con IA
├── ec3.html                EC3 — Marketing digital con IA
├── ec4.html                EC4 — Transformación digital con IA
├── flujo-trabajo.html      Infografía del flujo de trabajo en equipo
├── flujo-trabajo.png       Infografía exportada como imagen (para compartir)
├── assets/
│   └── styles.css          Hojas de estilo compartidas
├── img/
│   └── logo.png            Logo del manual
├── MiCompañIA_SistemaDiseno_Web.md   Sistema de diseño web (paleta, tipografía)
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

- **Repártanse por archivo de EC**: una persona por `ecN.html` a la vez. Si nadie edita el mismo archivo, nunca hay choques.
- **Avisen** antes de tocar `index.html` o `assets/styles.css` — los comparten los 4 manuales.
- **Suban seguido**, en cambios chicos: mientras menos tiempo pase entre traer y subir, menos posibilidad de cruzarse.
- Si dos editan el mismo archivo casi a la vez, la IA junta el trabajo sola; solo pedirá ayuda en el caso raro de que dos cambien exactamente la misma línea.

Para una vista visual del proceso, abre `flujo-trabajo.html`.

## Estado actual de los manuales

| EC | Elementos | Conocimientos | Estado |
|----|-----------|---------------|--------|
| EC1 | 3 | 14 | Desarrollado |
| EC2 | 4 | 18 | Estructura + placeholders |
| EC3 | 4 | 10 | Estructura + placeholders |
| EC4 | 3 (+1 sin conocimientos) | 13 | Estructura + placeholders |

## Visibilidad del repositorio

Este repositorio es **privado**: solo el equipo (Oscar, Iván y Aide) puede verlo y editarlo. Para sumar a alguien más, el dueño lo agrega en *Settings → Collaborators*.

GitHub Pages (publicar el manual en una URL) requiere un plan de pago para repos privados, así que por ahora el manual se revisa abriéndolo localmente.

## Fuentes

El contenido proviene de los archivos base del proyecto Fundes Componente 2:

- `EC1 COMPLETO.docx`, `EC2 COMPLETO.docx`, `EC3 COMPLETO.docx`, `EC4 COMPLETO.docx`
- `Tabla de especificaciones EC1.xlsx` / `EC2.xls` / `EC3.xlsx` / `EC4.xlsx`
- `Todos los conocimientos.xlsx`

Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.
