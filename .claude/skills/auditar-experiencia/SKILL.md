---
name: auditar-experiencia
description: Ejecuta un control independiente de diseño, UX, marca y accesibilidad sobre páginas o cambios de Mi CompañIA y consolida un dictamen de publicación.
---

# /auditar-experiencia

Audita una página, conjunto de archivos o diff antes de publicar. No modifica archivos.

## Argumentos

- **`<alcance>`**: archivo, carpeta, páginas o referencia como `git diff`.
- Si no se especifica, usa los archivos modificados en el working tree.

## Workflow

1. Determina el alcance exacto y reúne la petición/brief original si existe.
2. Invoca en paralelo, compartiendo el mismo alcance:
   - `mi-compania-design-auditor`: fidelidad al brief, UI, UX, responsive y calidad integral.
   - `mi-compania-brand-reviewer`: marca, tokens, voz y consistencia visual.
   - `mi-compania-accessibility-auditor`: WCAG 2.2 AA y tecnologías de asistencia.
3. Consolida hallazgos equivalentes sin perder su evidencia ni criterio original.
4. Usa la severidad más alta cuando dos reportes discrepen sobre el mismo problema.
5. Emite un dictamen único:
   - `APROBADO`: ningún reporte tiene bloqueantes/altas.
   - `APROBADO CON OBSERVACIONES`: solo medias, bajas o pruebas manuales acotadas.
   - `BLOQUEADO`: cualquier bloqueante/alta o falta evidencia crítica.
6. Asigna cada corrección al agente dueño: UX, UI, graphic-designer, copywriter, pedagogo, frontend o asset-generator.

## Salida

```markdown
## Auditoría consolidada · <alcance>

### Bloqueantes y altas
| Fuente | Evidencia | Impacto | Responsable |
|---|---|---|---|

### Medias y bajas
| Fuente | Evidencia | Recomendación | Responsable |
|---|---|---|---|

### Verificado
- Diseño y UX:
- Marca:
- Accesibilidad:

### Pruebas manuales pendientes
- ...

## Dictamen
APROBADO | APROBADO CON OBSERVACIONES | BLOQUEADO
```

No corrijas durante la auditoría. Si el dictamen es `BLOQUEADO`, devuelve las tareas al orquestador y vuelve a auditar después de la corrección.
