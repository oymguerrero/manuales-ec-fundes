# =========================================================
# Mi CompaniIA - Cargar .env en la sesion PowerShell actual
# =========================================================
# Uso:
#   . .\scripts\load-env.ps1        # nota el punto inicial - "dot-source"
#
# El dot-source es necesario para que las variables persistan
# en tu sesion. Sin el, se cargan en una sesion hija y se pierden.
# =========================================================

param(
    [string]$EnvFile = ".env"
)

if (-not (Test-Path $EnvFile)) {
    Write-Host "[!] No se encontro $EnvFile" -ForegroundColor Yellow
    Write-Host "Copia .env.example a .env y completa los valores:" -ForegroundColor Yellow
    Write-Host "    Copy-Item .env.example .env" -ForegroundColor Cyan
    return
}

$loaded = 0
$skipped = 0

Get-Content $EnvFile | ForEach-Object {
    $line = $_.Trim()

    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith("#")) {
        return
    }

    if ($line -match "^([A-Z_][A-Z0-9_]*)\s*=\s*(.*)$") {
        $key = $Matches[1]
        $value = $Matches[2].Trim()

        if (($value.StartsWith('"') -and $value.EndsWith('"')) -or
            ($value.StartsWith("'") -and $value.EndsWith("'"))) {
            $value = $value.Substring(1, $value.Length - 2)
        }

        if ($value -eq "tu-api-key-aqui" -or $value -eq "") {
            Write-Host "  [skip] $key (placeholder)" -ForegroundColor DarkGray
            $skipped++
            return
        }

        Set-Item -Path "env:$key" -Value $value

        if ($key -match "(KEY|TOKEN|SECRET|PASSWORD|CREDENTIALS)") {
            $masked = if ($value.Length -gt 8) {
                $value.Substring(0, 4) + "****" + $value.Substring($value.Length - 4)
            } else {
                "****"
            }
            Write-Host "  [ok] $key = $masked" -ForegroundColor Green
        } else {
            Write-Host "  [ok] $key = $value" -ForegroundColor Green
        }
        $loaded++
    }
}

Write-Host ""
Write-Host "Variables cargadas: $loaded - saltadas: $skipped" -ForegroundColor Cyan

if ($env:GOOGLE_API_KEY -and $env:GOOGLE_API_KEY -ne "tu-api-key-aqui") {
    Write-Host "[OK] GOOGLE_API_KEY disponible para TTS / Imagen / Veo" -ForegroundColor Green
}
