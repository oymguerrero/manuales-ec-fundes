---
name: pre-publicacion
description: Ejecuta el checklist completo del proyecto Mi CompañIA antes de hacer commit/push: tamaño de imágenes, links rotos, brand audit en todas las páginas, validación HTML básica, cumplimiento de accesibilidad. Devuelve un go/no-go con la lista de problemas a resolver. Use al cerrar una sesión de trabajo o antes de publicar cambios.
---

# /pre-publicacion

Checklist completo antes de publicar. Garantiza que el sitio cumple los mínimos del sistema de diseño y que no se rompió nada en cambios recientes.

## Sin argumentos

Esta skill no recibe argumentos. Audita el repo completo en su estado actual (working tree).

## Workflow al invocarse

Ejecuta en este orden, deteniéndote en el primer 🔴 que requiera atención del usuario:

### Fase 1 · Estado del repo

```bash
git status
git diff --stat
```

Identifica qué archivos cambiaron desde el último commit. Esto define el alcance de las verificaciones siguientes.

### Fase 2 · Peso de imágenes

```bash
ls -la img/ | awk 'NR>3 {total += $5; if ($5 > 400000) print "  ⚠️", $9, $5/1024 "KB"} END {print "Total:", total/1024/1024 "MB"}'
```

Verifica:
- Cada imagen JPG/PNG individual ≤ 400 KB → si excede, 🟡 recomendado comprimir
- Total carpeta `img/` ≤ 5 MB → si excede, 🔴 bloqueante (delega a `mi-compania-asset-generator` para recomprimir)

### Fase 3 · Validación HTML básica

Verifica con `grep` problemas comunes:

```bash
# Imágenes sin alt
grep -nE '<img[^>]*>' *.html | grep -v 'alt='

# Múltiples h1 por página
for f in *.html; do
  count=$(grep -c '<h1' "$f")
  if [ "$count" -ne 1 ]; then echo "⚠️ $f tiene $count h1"; fi
done

# Tags abiertos sin cerrar (heurística simple)
for f in *.html; do
  for tag in section article div; do
    open=$(grep -oE "<$tag[^>]*>" "$f" | wc -l)
    close=$(grep -oE "</$tag>" "$f" | wc -l)
    if [ "$open" -ne "$close" ]; then
      echo "⚠️ $f: <$tag> abre $open, cierra $close"
    fi
  done
done
```

### Fase 4 · Links rotos internos

```bash
# Verifica que cada href interno apunta a un archivo o anchor existente
for f in *.html; do
  grep -oE 'href="[^"]*"' "$f" | while read href; do
    target=$(echo "$href" | sed 's/href="//;s/"//;s/#.*//')
    if [ -n "$target" ] && [[ "$target" != http* ]] && [ ! -f "$target" ]; then
      echo "❌ $f → $target"
    fi
  done
done
```

### Fase 5 · Brand audit completo

Invoca la skill `/revisar-marca` (o directamente al agente `mi-compania-brand-reviewer`) sobre todos los HTML + CSS:

```
/revisar-marca *.html assets/styles.css
```

Captura el reporte y agrega los bloqueantes/recomendados al sumario final.

### Fase 6 · Verificación de marca uniforme

Usa `grep` para confirmar consistencia:

```bash
# Todas las páginas deben tener "Mi CompañIA" en el title
grep -L "Mi CompañIA" *.html

# Todas las páginas deben enlazar al logo
grep -L 'src="img/logo.png"' *.html

# Ninguna debe tener referencia al branding viejo
grep -nE 'Componente 2|Fundes\b' *.html | grep -v 'FUNDES Latinoamérica'
```

### Fase 7 · Reporte final go/no-go

Genera un reporte con esta estructura:

```markdown
# Pre-publicación · 2026-XX-XX

## Resumen
- ✅ Listo para publicar / ⚠️ Listo con observaciones / ❌ Bloqueado

## Cambios desde último commit
- archivo1.html (modificado)
- archivo2.css (modificado)

## 🔴 Bloqueantes (X)
[lista]

## 🟡 Recomendados (X)
[lista, con marca opcional]

## 🟢 Verificado
- Peso de imágenes
- Validación HTML
- Links internos
- Marca uniforme

## Siguiente paso
[Si bloqueado: lista los agentes a invocar para arreglar]
[Si listo: comando git de commit sugerido]
```

## Salida esperada

Un solo mensaje al usuario con el reporte completo. Después de eso, el usuario decide si corre `/commit` o si delega arreglos.

## Cuándo NO usar esto

- **No** lo uses durante una sesión de desarrollo activo — está pensado para el cierre/handoff
- **No** lo uses si solo cambiaste documentación (`README.md`, `.claude/`) — esos no afectan el sitio público

## Notas para el implementador

Si los comandos `grep` con awk fallan en PowerShell, usa equivalentes:

```powershell
Get-ChildItem img/ | Where-Object { $_.Length -gt 400000 } | Select-Object Name, @{N='KB';E={[int]($_.Length/1KB)}}
```

Como esta skill puede correr en Bash o PowerShell, verifica primero el shell disponible y adapta los comandos.
