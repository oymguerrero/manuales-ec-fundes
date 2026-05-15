---
name: crear-actividad-interactiva
description: Crea una actividad interactiva nueva (flip cards, quiz, decision scenario, sort drag-drop, comparison slider, hotspot diagram) siguiendo el catálogo del agente pedagogo y los contratos HTML del agente frontend. Orquesta al pedagogo para diseño de contenido y al frontend para implementación. Use cuando el usuario quiere agregar una actividad concreta a una página, sin necesariamente partir de un muro de texto a convertir.
---

# /crear-actividad-interactiva

Crea una actividad interactiva nueva en una página, con diseño pedagógico fundamentado y código accesible.

## Argumentos

- **`<tipo>`** (requerido): patrón a crear. Valores válidos:
  - `flipcards` — pares concepto/definición que se voltean
  - `quiz` — preguntas múltiple choice con feedback inmediato
  - `scenario` — decisión profesional con outcomes ramificados
  - `sort` — drag-drop para categorizar items
  - `sequence` — drag-drop para ordenar pasos
  - `comparison` — slider antes/después
  - `hotspot` — diagrama con puntos clickeables que revelan info

- **`<archivo>`** (opcional): ruta del archivo donde insertar la actividad. Si no se pasa, pregunta.

- **`<tema>`** (opcional): tema o sección de contenido de la actividad. Si no se pasa, pregunta.

## Ejemplos

```
/crear-actividad-interactiva flipcards estandar-a/elemento-1.html "Los 8 productos"
/crear-actividad-interactiva quiz maestro/que-es.html "Tipos de evidencia"
/crear-actividad-interactiva scenario estandar-a/elemento-2.html "Capacitación"
```

## Workflow al invocarse

### Paso 1 · Diseño pedagógico (pedagogo)

Invoca al `mi-compania-pedagogo` con:

> "Diseña el contenido de una actividad tipo [tipo] sobre [tema] para insertar en [archivo]. Aplica Backward Design: declara el objetivo conductual, el nivel de Bloom y el contenido específico (preguntas, pares, opciones, distractores, feedback)."

Recibe del pedagogo:

| Para tipo... | Pedagogo entrega... |
|---|---|
| `flipcards` | 5-10 pares concepto/definición; nivel Bloom 1-2 |
| `quiz` | 3-5 preguntas con 3-4 opciones c/u + texto de feedback correcto e incorrecto; nivel Bloom 2-3 |
| `scenario` | 1 situación + 3-4 decisiones + outcome contextualizado para cada una; nivel Bloom 3-5 |
| `sort` | Lista de items + categorías destino + categoría correcta de cada item; nivel Bloom 3-4 |
| `sequence` | Lista de pasos en orden correcto (se mostrarán mezclados); nivel Bloom 3 |
| `comparison` | Contenido del lado "antes" + "después" (texto, métrica, imagen); nivel Bloom 4 |
| `hotspot` | Diagrama o imagen base + 4-8 puntos con coordenadas + info de cada punto; nivel Bloom 2-3 |

### Paso 2 · Verificación de CSS y JS

Antes de pedir al frontend que codifique, verifica si el componente ya está soportado por `assets/styles.css` y `assets/interactive.js`:

```bash
grep -c "\.flipcard" assets/styles.css
grep -c "initFlipcard\|initQuiz\|initScenario" assets/interactive.js
```

Si no está, el primer paso del frontend será agregar los estilos y la lógica al CSS/JS compartido. Si ya está, solo inserta el markup.

### Paso 3 · Implementación (frontend)

Invoca al `mi-compania-frontend` con:

> "Implementa una actividad tipo [tipo] en [archivo] § [anchor o final del main]. Usa el contrato del catálogo §"Componentes interactivos pedagógicos" del agente. Contenido a usar (provisto por pedagogo): [spec del pedagogo]. Si los estilos/JS del componente no existen aún, agrégalos a assets/styles.css y assets/interactive.js."

### Paso 4 · Revisión (brand-reviewer)

Invoca al `mi-compania-brand-reviewer` sobre el archivo y `assets/styles.css` (si cambió), validando §15 y §16 del sistema de diseño.

### Paso 5 · Reporte

Resume al usuario:
- Tipo de actividad creada y nivel de Bloom.
- Objetivo conductual que cumple.
- Ubicación en el archivo.
- Si el CSS/JS se actualizó (componente nuevo agregado a la biblioteca compartida).

## Markup base por tipo (referencia rápida)

Consulta el catálogo completo en `.claude/agents/mi-compania-frontend.md` § "Componentes interactivos pedagógicos". Aquí solo el esqueleto:

### flipcards
```html
<div class="flipcards">
  <button class="flipcard" aria-pressed="false">
    <span class="flipcard__face flipcard__face--front">Concepto</span>
    <span class="flipcard__face flipcard__face--back">Definición</span>
  </button>
</div>
```

### quiz
```html
<div class="quiz" data-correct="b">
  <p class="quiz__question">Pregunta</p>
  <div class="quiz__options">
    <button class="quiz__option" data-option="a">A</button>
    <button class="quiz__option" data-option="b">B</button>
  </div>
  <div class="quiz__feedback" aria-live="polite" hidden></div>
</div>
```

### scenario
```html
<div class="scenario">
  <p class="scenario__situation">...</p>
  <div class="scenario__choices">
    <button class="scenario__choice" data-outcome="X">...</button>
  </div>
  <div class="scenario__outcomes">
    <div class="scenario__outcome" data-outcome="X" hidden>...</div>
  </div>
</div>
```

(otros tipos en el agente frontend)

## Cuándo NO usar esto

- **No** lo uses para crear una versión simple de algo que ya cubre un componente existente (tabs, accordion, callout).
- **No** lo uses si el contenido es muy poco (1-2 items): mejor texto plano.
- **No** lo uses si el patrón requerido no existe en el catálogo de 7 — pide primero al pedagogo evaluar si vale la pena agregarlo.
