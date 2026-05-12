# Manuales EC — Componente 2 Fundes

Manuales interactivos en HTML de los 4 Estándares de Competencia (EC) sobre Inteligencia Artificial aplicada a MiPyMEs. Componente 2 de Fundes.

## Estructura

```
manuales-ec-fundes/
├── index.html        Landing principal con los 4 ECs
├── ec1.html          EC1 — Soluciones de IA alineadas a la MiPyME (DESARROLLADO)
├── ec2.html          EC2 — Productos y servicios con IA (borrador)
├── ec3.html          EC3 — Marketing digital con IA (borrador)
├── ec4.html          EC4 — Transformación digital con IA (borrador)
├── assets/
│   └── styles.css    Hojas de estilo compartidas
├── README.md
└── .gitignore
```

## Cómo verlo localmente

Solo abre `index.html` con doble clic en cualquier navegador (Chrome, Edge, Firefox). No requiere servidor.

## Cómo colaborar

1. **Clona o abre el repo** en Antigravity (o VS Code, o cualquier editor con Git).
2. **Edita** el archivo HTML del EC en el que estés trabajando — los placeholders están marcados con clase `.placeholder` y dicen "pendiente desarrollar".
3. **Haz commit** con mensaje claro:
   - `EC2: desarrollar conocimiento 1 del Elemento 1`
   - `EC3: corregir numeración del Elemento 2`
4. **Push** al repositorio para que el resto del equipo vea los cambios.

## Estado actual de los manuales

| EC | Elementos | Conocimientos | Estado |
|----|-----------|---------------|--------|
| EC1 | 3 | 14 | Desarrollado |
| EC2 | 4 | 18 | Estructura + placeholders |
| EC3 | 4 | 10 | Estructura + placeholders |
| EC4 | 3 (+1 sin conocimientos) | 13 | Estructura + placeholders |

## Publicar como sitio (opcional)

Para que el equipo pueda abrir el manual desde una URL sin clonar el repo, activa **GitHub Pages**:

1. Ve a *Settings → Pages* en el repo de GitHub.
2. En *Source*, selecciona la rama `main` y carpeta `/ (root)`.
3. Guarda. En ~1 minuto el sitio estará en `https://<usuario>.github.io/<nombre-repo>/`.

## Fuentes

El contenido proviene de los archivos base del proyecto Fundes Componente 2:

- `EC1 COMPLETO.docx`, `EC2 COMPLETO.docx`, `EC3 COMPLETO.docx`, `EC4 COMPLETO.docx`
- `Tabla de especificaciones EC1.xlsx` / `EC2.xls` / `EC3.xlsx` / `EC4.xlsx`
- `Todos los conocimientos.xlsx`

Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.
