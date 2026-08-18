---
name: crear-leccion-multimedia
description: Diseña y produce una lección en línea completa de Mi CompañIA coordinando pedagogía, e-learning, contenido, imagen, audio, frontend y auditorías según el alcance.
---

# /crear-leccion-multimedia

Convierte un tema y sus fuentes aprobadas en una lección digital completa, accesible y lista para integrarse al sitio.

## Argumentos

- **`<tema o archivo destino>`**: requerido.
- **`[fuentes]`**: material factual aprobado o rutas locales.
- **`[duración]`**: opcional; si falta, el especialista e-learning la estima.

## Workflow

1. Confirma objetivo, audiencia aspirante, archivo destino y fuentes. No inventes contenido normativo faltante.
2. Invoca `mi-compania-pedagogo` para definir resultado, Bloom, evidencia, práctica y evaluación formativa.
3. Pasa esa salida a `mi-compania-elearning-specialist` para crear ruta, segmentación, selección de medios, progreso y criterios de finalización.
4. Con el blueprint aprobado, ejecuta en paralelo cuando no comparten archivo:
   - `mi-compania-learning-content-generator`: explicaciones, casos, guiones y práctica guiada.
   - `mi-compania-graphic-designer`: brief de los visuales necesarios.
5. Produce solo los medios justificados:
   - `mi-compania-image-producer` para imágenes.
   - `mi-compania-audio-producer` para narraciones.
   - `mi-compania-asset-generator` si hay video o paquete multimedia combinado.
6. Invoca `mi-compania-ux-architect` y `mi-compania-ui-designer` si la lección introduce navegación, layout o componentes nuevos.
7. `mi-compania-frontend` integra contenido y assets respetando degradación sin JS.
8. Ejecuta `/auditar-experiencia` sobre los archivos modificados.
9. Si el dictamen queda bloqueado, devuelve cada hallazgo a su agente responsable y repite únicamente la auditoría afectada.

## Salida esperada

```markdown
## Lección producida
- Objetivo y evidencia:
- Ruta y duración:
- Archivos modificados/creados:
- Medios y alternativas accesibles:
- Actividades y feedback:
- Resultado de auditorías:
- Pendientes:
```

No agregues audio, imagen, video o interacción solo para “hacerlo dinámico”. Cada medio debe resolver una necesidad de comprensión, práctica, contexto o accesibilidad.
