#!/usr/bin/env bash
# =========================================================
# Mi CompañIA · Cargar .env en la sesión bash actual
# =========================================================
# Uso:
#   source ./scripts/load-env.sh
#
# El `source` es necesario para que las variables persistan
# en tu sesión actual.
# =========================================================

ENV_FILE="${1:-.env}"

if [ ! -f "$ENV_FILE" ]; then
  echo "⚠ No se encontró $ENV_FILE"
  echo "Copia .env.example a .env y completa los valores:"
  echo "    cp .env.example .env"
  return 1 2>/dev/null || exit 1
fi

loaded=0
skipped=0

while IFS= read -r line || [ -n "$line" ]; do
  # Quitar espacios al inicio/fin
  line="${line#"${line%%[![:space:]]*}"}"
  line="${line%"${line##*[![:space:]]}"}"

  # Saltar líneas vacías y comentarios
  [ -z "$line" ] && continue
  [ "${line#\#}" != "$line" ] && continue

  # Parsear KEY=VALUE
  if [[ "$line" =~ ^([A-Z_][A-Z0-9_]*)[[:space:]]*=[[:space:]]*(.*)$ ]]; then
    key="${BASH_REMATCH[1]}"
    value="${BASH_REMATCH[2]}"

    # Quitar comillas envolventes
    if [[ "$value" =~ ^\"(.*)\"$ ]] || [[ "$value" =~ ^\'(.*)\'$ ]]; then
      value="${BASH_REMATCH[1]}"
    fi

    # Saltar placeholders
    if [ "$value" = "tu-api-key-aqui" ] || [ -z "$value" ]; then
      echo "  ⊘ $key (placeholder · no cargado)"
      skipped=$((skipped + 1))
      continue
    fi

    export "$key=$value"

    # Enmascarar si parece secreto
    if [[ "$key" =~ (KEY|TOKEN|SECRET|PASSWORD|CREDENTIALS) ]]; then
      if [ ${#value} -gt 8 ]; then
        masked="${value:0:4}****${value: -4}"
      else
        masked="****"
      fi
      echo "  ✓ $key = $masked"
    else
      echo "  ✓ $key = $value"
    fi
    loaded=$((loaded + 1))
  fi
done < "$ENV_FILE"

echo ""
echo "Variables cargadas: $loaded · saltadas: $skipped"

if [ -n "$GOOGLE_API_KEY" ] && [ "$GOOGLE_API_KEY" != "tu-api-key-aqui" ]; then
  echo "✓ GOOGLE_API_KEY disponible para TTS / Imagen / Veo"
fi
