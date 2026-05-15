---
name: nueva-seccion-ec
description: Inserta una sección nueva (elemento, conocimiento, callout, stats) en el archivo de un Estándar de Competencia (ec1-ec4.html) usando las plantillas HTML del proyecto Mi CompañIA. Use cuando el usuario pida agregar contenido estructurado a una página de EC, no cuando quiera crear una página nueva o modificar el sistema de diseño.
---

# /nueva-seccion-ec

Inserta una sección nueva en un archivo de Estándar de Competencia (`ec1.html`, `ec2.html`, `ec3.html`, `ec4.html`) usando las plantillas oficiales del proyecto.

## Argumentos

- **`<tipo>`** (requerido): qué sección agregar. Valores válidos:
  - `elemento` — un nuevo `<article class="element">` con número, título, lede y lista vacía de conocimientos
  - `conocimiento` — un nuevo `<li>` dentro de `.conocimientos` (pide número de elemento al cual agregarlo)
  - `callout` — un `<div class="callout">` (pide variante: nota, important, tip, example, template)
  - `stats` — un bloque `<div class="stats">` con stats configurables

- **`<archivo>`** (opcional): qué archivo modificar (ej. `ec2.html`). Si no se pasa, pregunta al usuario o usa el archivo abierto en el IDE.

## Ejemplos

```
/nueva-seccion-ec elemento ec2.html
/nueva-seccion-ec conocimiento ec3.html
/nueva-seccion-ec callout ec1.html
/nueva-seccion-ec stats
```

## Workflow al invocarse

1. **Identifica el archivo objetivo:**
   - Si se pasó como argumento → úsalo
   - Si hay un archivo `ec*.html` abierto en el IDE → propón ese
   - Si no → pide al usuario que especifique

2. **Lee el archivo** para ubicar el punto de inserción correcto:
   - Para `elemento` → al final de `<section id="elementos">`, antes del cierre `</section>`
   - Para `conocimiento` → dentro de la `.conocimientos` del elemento N especificado
   - Para `callout` → contextual: pide al usuario en qué `<section>` o cerca de qué heading
   - Para `stats` → contextual

3. **Pide los datos faltantes** (preguntar uno a la vez):
   - Para `elemento`: número, título, lede de una línea
   - Para `conocimiento`: en qué elemento (1-4), título, descripción, nivel cognitivo (Conocimiento/Comprensión/Aplicación)
   - Para `callout`: variante (nota/important/tip/example/template), título corto, contenido
   - Para `stats`: pares número/etiqueta (mínimo 2, máximo 4)

4. **Genera el HTML** desde la plantilla correspondiente:

### Plantilla: elemento

```html
<article class="element" id="e{N}">
  <div class="element-header">
    <span class="element-num">{N}</span>
    <h3>{TÍTULO}</h3>
  </div>
  <p class="lede">{LEDE}</p>

  <ol class="conocimientos">
    <!-- agregar conocimientos con /nueva-seccion-ec conocimiento -->
  </ol>
</article>
```

### Plantilla: conocimiento

```html
<li><div class="cono-content">
  <div class="cono-title">{TÍTULO} <span class="tag tag-{nivel-en-minúscula}">{Nivel}</span></div>
  <div class="cono-desc">{DESCRIPCIÓN}</div>
</div></li>
```

Mapeo de nivel:
- `Conocimiento` → `tag-conocimiento`
- `Comprensión` → `tag-comprension` (sin tilde en la clase)
- `Aplicación` → `tag-aplicacion` (sin tilde en la clase)

### Plantilla: callout

```html
<div class="callout callout--{variante}">
  <strong>{ETIQUETA}:</strong> {CONTENIDO}
</div>
```

Mapeo etiqueta por variante:
- `nota` → `Nota` (no agregar `--variante`, dejar `class="callout"`)
- `important` → `Importante`
- `tip` → `Para tener presente`
- `example` → `Ejemplo · La Espiga` (o el caso pedagógico que aplique)
- `template` → `Plantilla guía`

> Si la variante no es `nota` y las clases CSS `callout--{variante}` no existen aún en `assets/styles.css`, advierte al usuario y sugiere invocar al `mi-compania-frontend` para agregarlas.

### Plantilla: stats

```html
<div class="stats">
  <div class="stat"><span class="num">{NÚMERO}</span><span class="label">{ETIQUETA}</span></div>
  <!-- repetir 2-4 veces -->
</div>
```

5. **Inserta** con `Edit` en el punto identificado, conservando indentación de 2 espacios.

6. **Reporta:** qué insertaste, en qué archivo, en qué línea aproximada. Si dejaste algo pendiente (ej. callout sin clase CSS), nóta el siguiente paso.

## Si el archivo no es un EC

Si el usuario invoca esto sobre `index.html` u otro archivo no-EC, advierte que esta skill está pensada solo para `ec*.html` y sugiere alternativas (editar manualmente, o describir qué quiere y delegar al agente apropiado).
