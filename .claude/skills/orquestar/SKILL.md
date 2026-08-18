---
name: orquestar
description: Delega una petición vaga al agente orquestador, que selecciona y coordina especialistas de contenido, pedagogía, e-learning, UX/UI, diseño gráfico, imagen, audio, multimedia, frontend, accesibilidad, marca, auditoría y backend.
---

# /orquestar

Manda una petición vaga al agente orquestador del proyecto. Te ahorra elegir qué skill o agente invocar cuando la tarea cruza disciplinas.

## Argumentos

- **`<petición en lenguaje natural>`**: lo que quieres lograr, en tus propias palabras.

## Ejemplos

```
/orquestar Agrega un módulo nuevo al Elemento 2 sobre seguridad LFPDPPP con ejercicio práctico
/orquestar Quiero refrescar todo el capítulo "¿Es para ti?" con mejor copy y un audio nuevo
/orquestar Hay un PDF nuevo de la fuente CONOCER, vuélcalo al manual y revisa que no rompa la marca
/orquestar El Elemento 3 está denso, conviértelo en algo más activo
```

## Workflow al invocarse

1. **Lee la petición** (todo lo que viene después de `/orquestar`).

2. **Invoca al agente `mi-compania-orchestrator`** vía la herramienta Agent, pasándole:
   - La petición literal del usuario.
   - El contexto adicional relevante si lo hay (ej. archivos que el usuario tiene abiertos, último commit, decisiones previas en la sesión).
   - La instrucción: "Eres el orquestador. Analiza, planea, delega, integra. Responde siguiendo el formato obligatorio de tu prompt (Análisis → Plan → Ejecución → Integración → Cierre)."

3. **Recibe el reporte estructurado** del orquestador y muéstraselo al usuario tal cual. NO resumir — el orquestador ya redacta para el usuario final.

4. **Después del reporte**, propón los siguientes pasos:
   - Si el orquestador propuso un commit: ofrece commitear y pushear.
   - Si hay 🔴 bloqueantes o un dictamen `BLOQUEADO`: asigna la corrección al agente correspondiente y vuelve a auditar antes de proponer commit.
   - Si quedó pendiente algo (ej. el orquestador detectó que falta un dato externo): márcalo y ofrece guardarlo como TODO.

## Cuándo NO usar esto

- **No** lo uses para peticiones de 1-2 líneas (typo, fix de href, agregar atributo). Edita directo, es más rápido.
- **No** lo uses si la petición claramente cae en una sola disciplina (ej. "audita la marca de X" → usa `/revisar-marca` directo, no orquestes).
- **No** lo uses si ya hay una skill específica que lo cubre (`/crear-actividad-interactiva`, `/nueva-seccion-ec`, `/convertir-muro-de-texto`). El orquestador es para tareas que NO encajan en ninguna skill predefinida.
- **No** lo uses para consultas (ej. "¿qué hay en el commit X?", "¿cuántos componentes pedagógicos tenemos?"). El orquestador es para trabajo que produce cambios.

## Salida esperada

El reporte del orquestador siempre tiene esta estructura (no resumas, pásalo tal cual al usuario):

```
## Análisis
<qué interpretó>

## Plan
1. <agente A> · <input> · <razón>
2. ⚡ paralelo · <agente B> · ...
3. (espera #1 y #2) · <agente C>

## Ejecución
<resumen de lo que pasó al invocar cada agente>

## Cierre
- Modificado: <archivos · líneas>
- Brand reviewer: <🟢/🟡/🔴 · detalle>
- Commit propuesto: "<mensaje>"
- Pendientes: <si aplica>
```
