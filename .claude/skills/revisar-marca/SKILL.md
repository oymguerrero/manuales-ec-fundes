---
name: revisar-marca
description: Audita rápidamente uno o más archivos del proyecto Mi CompañIA contra las reglas del sistema de diseño (tokens, voz, contraste, accesibilidad, peso de imágenes). Delega al agente mi-compania-brand-reviewer y devuelve el reporte. Use antes de hacer commit cuando se modificaron archivos del sitio.
---

# /revisar-marca

Audita uno o más archivos del proyecto contra las reglas del sistema de diseño Mi CompañIA. Devuelve un reporte con findings categorizados (bloqueantes, recomendados, verificados).

## Argumentos

- **`[archivos...]`** (opcional, múltiples): rutas a archivos específicos. Si no se pasan, audita todos los `.html` en la raíz del proyecto + `assets/styles.css`.

## Ejemplos

```
/revisar-marca
/revisar-marca ec2.html
/revisar-marca index.html ec1.html assets/styles.css
```

## Workflow al invocarse

1. **Identifica los archivos a auditar:**
   - Si se pasaron argumentos → úsalos
   - Si no → corre `Glob` para `*.html` en raíz + lee `assets/styles.css`
   - Verifica que existen; si alguno no existe, repórtalo y continúa con los que sí

2. **Invoca al agente `mi-compania-brand-reviewer`** vía la herramienta Agent, pasándole:
   - La lista de archivos a revisar
   - El comando: "Audita estos archivos contra el sistema de diseño Mi CompañIA. Aplica el checklist completo. Devuelve el reporte en formato estandarizado."

3. **Recibe el reporte** del agente y muéstraselo al usuario tal cual (no resumir — el reporte ya está condensado en categorías).

4. **Después del reporte**, ofrece el siguiente paso al usuario:
   - Si hay 🔴 bloqueantes → propón delegar el arreglo al agente correspondiente (`copywriter` para problemas de voz, `frontend` para HTML/CSS, `asset-generator` para imágenes pesadas)
   - Si solo hay 🟡 → confirma que el archivo está listo para commit pero hay mejoras opcionales
   - Si todo es 🟢 → confirma que pasa y propón commit

## Cuándo NO usar esto

- **No** lo uses para arreglar problemas — solo para detectarlos. Si el usuario quiere que arregles directo, mejor invoca al agente correspondiente sin pasar por esta skill.
- **No** lo uses sobre archivos de documentación (`README.md`, `MiCompañIA_SistemaDiseno_Web.md`) — el brand reviewer está calibrado para HTML/CSS, no para markdown de docs.

## Salida esperada

Un reporte con esta estructura, por archivo:

```
## Auditoría · ec2.html
🔴 Bloqueantes (1)
1. [Voz] "transformación digital" en línea 47 fuera de sección de aliados → pide al copywriter reescribir.

🟡 Recomendados (2)
1. [Imágenes] hero-ec2.jpg pesa 420 KB, sobre el target de 400 KB → opcional recomprimir.
2. [Accesibilidad] botón en línea 89 sin type="button" → agregar atributo.

🟢 Verificado: tokens, contraste, jerarquía headings, logo, meta básico.
```
