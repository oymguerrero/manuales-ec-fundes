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

Trabajamos **tres personas** sobre este repo: Oscar, Iván y Aide. Da igual el editor (Antigravity, Claude Code o VS Code) — por debajo todos usan el mismo Git y el mismo repositorio. La rama `main` es **el archivo final**: la única versión oficial.

### Reglas de oro

1. **`git pull` antes de empezar y antes de subir.** Así trabajas siempre sobre lo último.
2. **Nunca se trabaja directo sobre `main`.** Todo cambio entra por una rama y un Pull Request (PR).
3. Un cambio es oficial **solo cuando su PR se mergea** a `main`.

### Ciclo de trabajo (por cada tarea)

```
git switch main && git pull           # 1. partes de la última versión
git switch -c ec2-conocimiento-1      # 2. creas tu rama (nómbrala por la tarea)
   ...editas el HTML...
git add ec2.html                      # 3. marcas qué entra
git commit -m "EC2: desarrollar conocimiento 1 del Elemento 1"
git push -u origin ec2-conocimiento-1 # 4. subes tu rama a GitHub
```

5. En GitHub, abre un **Pull Request** de tu rama hacia `main`.
6. Otra persona del equipo lo revisa y le da **Merge**.
7. Todos hacen `git pull` sobre `main` → todos quedan con el archivo final.

> En Claude Code (Oscar e Iván) basta con pedirle el ciclo al asistente. En Antigravity (Aide), el panel *Source Control* tiene botones para pull, commit, push y abrir el PR.

### Para no pisarse

- Repártanse el trabajo **por archivo de EC**: una persona por `ecN.html` a la vez.
- Avisen al equipo antes de tocar `index.html` o `assets/styles.css` — los comparten los 4 manuales.
- Commits pequeños y frecuentes, con mensaje claro:
  - `EC2: desarrollar conocimiento 1 del Elemento 1`
  - `EC3: corregir numeración del Elemento 2`

Para una vista visual del proceso completo, abre `flujo-trabajo.html`.

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
