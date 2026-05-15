---
name: convertir-muro-de-texto
description: Analiza una sección de texto largo y propone (y opcionalmente ejecuta) su conversión a un formato pedagógicamente más activo: tabs, flip cards, quiz, scenario, drag-drop, comparison slider, microvideo o audio. Orquesta a los agentes pedagogo + frontend + asset-generator. Use cuando una página tenga secciones >500 palabras sin componentes interactivos, o cuando el usuario pida hacer una sección menos densa visualmente.
---

# /convertir-muro-de-texto

Analiza una sección de texto largo y la transforma en una experiencia de aprendizaje activo. Aplica el marco pedagógico de Mi CompañIA (andragogía + Bloom + cognitive load + UDL + microlearning) y orquesta a los agentes técnicos para implementarla.

## Argumentos

- **`<archivo>`** (opcional): ruta del archivo HTML. Si no se pasa, usa el archivo abierto en el IDE.
- **`<anchor>`** (opcional): id de la sección a convertir (ej. `#evidencias`). Si no se pasa, lista los muros detectados para que el usuario elija.

## Ejemplos

```
/convertir-muro-de-texto
/convertir-muro-de-texto maestro/que-es.html
/convertir-muro-de-texto maestro/que-es.html #competencia
```

## Workflow al invocarse

### Paso 1 · Detección de muros

Lee el archivo y aplica las heurísticas de detección (§16.1 del sistema de diseño):

- Sección con >500 palabras seguidas sin componente interactivo
- Lista de >7 items sin agrupación visual
- Definiciones de >5 términos en párrafos seguidos
- Procedimiento de >5 pasos sin numeración visual
- Comparación que se hace en prosa cuando debería ser tabla/diagrama

Reporta cada muro con: id de la sección, núm. de palabras, núm. de items, patrón sugerido.

### Paso 2 · Diagnóstico pedagógico (delegar al pedagogo)

Para la sección elegida, invoca al `mi-compania-pedagogo` con esta pregunta:

> "Analiza la sección [#anchor] de [archivo]. Aplicando Backward Design: ¿cuál debería ser el objetivo de aprendizaje? ¿En qué nivel de Bloom opera? ¿Qué patrón del catálogo de 20 (§"Catálogo" del agente pedagogo) es óptimo para esta conversión?"

El pedagogo regresa:
- Objetivo conductual de la sección.
- Nivel de Bloom.
- Patrón recomendado (1 principal + 1 alternativo).
- Esqueleto de contenido para la actividad (preguntas, distractores, feedback, secuencia).

### Paso 3 · Implementación

Según el patrón recomendado:

**Si es patrón de UI puro** (flip card, quiz, scenario, drag-drop, comparison, hotspot):
→ Delega al `mi-compania-frontend` con la spec del pedagogo.

**Si es patrón que requiere asset** (microvideo, audio narrado):
→ Pregunta al usuario sobre el costo (créditos higgsfield / API calls TTS).
→ Si aprueba: delega al `mi-compania-asset-generator` para generar el asset; luego al `mi-compania-frontend` para integrar.

**Si es patrón mixto** (ej. diagrama interactivo SVG): pedagogo + frontend coordinados.

### Paso 4 · Revisión

Invoca al `mi-compania-brand-reviewer` sobre el archivo modificado, validando §15 (diagramas) y §16 (aprendizaje activo) del sistema de diseño.

### Paso 5 · Reporte al usuario

Cierra con un resumen de:
- Qué muro de texto se convirtió y a qué patrón.
- Qué archivos cambiaron.
- Qué pendientes quedan (ej. crear el video / audio si aprobó pero requiere tiempo de generación).
- Próxima sección sugerida para conversión.

## Cuándo NO usar esto

- **No** lo uses sobre secciones que ya tienen componentes interactivos (tabs, accordion, etc.) — esas ya están convertidas.
- **No** lo uses sobre documentación técnica del repo (`.claude/`, README) — está diseñada para lectura lineal.
- **No** lo uses si el objetivo de la sección es deliberadamente largo y narrativo (ej. bienvenida emocional del Maestro) — algunos textos largos son funcionales pedagógicamente.

## Salida esperada

Un mensaje al usuario con:

```
## Conversión propuesta · [archivo] § [anchor]

**Muro detectado:** [X] palabras, [Y] items, sin componente interactivo.

**Objetivo (Backward Design):** [objetivo conductual]
**Nivel Bloom:** [1-6]
**Patrón recomendado:** [nombre del catálogo §"Catálogo de 20"]
**Patrón alternativo:** [otro nombre]

**Plan:**
- Pedagogo diseña contenido: [N] flip cards / [N] preguntas / etc.
- Frontend implementa componente
- [Si aplica:] Asset-generator produce video/audio en [duración] · costo [N] créditos

**Pendientes para usuario:**
- Aprobar costo de [generación de asset, si aplica]
- Revisar el contenido propuesto por el pedagogo
```

Solo después de aprobación del usuario, ejecuta los Pasos 3 y 4.
