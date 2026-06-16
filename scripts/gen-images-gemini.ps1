# =========================================================
# Mi CompañIA - Generar imagenes con Google Imagen 4 (Gemini)
# =========================================================
# Uso:
#   .\scripts\gen-images-gemini.ps1 -Prompt "texto..." -OutputFile img/escenas/x.png
#   .\scripts\gen-images-gemini.ps1 -Prompt "..." -OutputFile img/x.png -AspectRatio "16:9"
#
# Requiere:
#   - GOOGLE_API_KEY en el entorno (carga con `. .\scripts\load-env.ps1`)
#
# Modelos disponibles (Google Generative Language API):
#   - imagen-4.0-fast-generate-001  (mas rapido, calidad alta)
#   - imagen-4.0-generate-001       (calidad superior)
#   - imagen-4.0-ultra-generate-001 (maxima calidad, mas costo/tiempo)
# Aspect ratios: 1:1, 9:16, 16:9, 3:4, 4:3
# =========================================================

param(
    [Parameter(Mandatory=$true)]
    [string]$Prompt,
    [Parameter(Mandatory=$true)]
    [string]$OutputFile,
    [string]$Model = "imagen-4.0-fast-generate-001",
    [ValidateSet("1:1", "9:16", "16:9", "3:4", "4:3")]
    [string]$AspectRatio = "1:1",
    [int]$SampleCount = 1
)

if (-not $env:GOOGLE_API_KEY -or $env:GOOGLE_API_KEY -eq "tu-api-key-aqui") {
    Write-Host "[ERROR] GOOGLE_API_KEY no esta configurada." -ForegroundColor Red
    Write-Host "  Carga el .env primero: . .\scripts\load-env.ps1" -ForegroundColor Yellow
    exit 1
}

# Crear directorio si no existe
$outputDir = Split-Path -Parent $OutputFile
if ($outputDir -and -not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
}

$endpoint = "https://generativelanguage.googleapis.com/v1beta/models/$Model" + ":predict?key=$($env:GOOGLE_API_KEY)"

$requestBody = @{
    instances = @(@{ prompt = $Prompt })
    parameters = @{
        sampleCount = $SampleCount
        aspectRatio = $AspectRatio
        personGeneration = "allow_adult"
    }
} | ConvertTo-Json -Depth 10

Write-Host "[->] Generando imagen con Imagen 4 ($Model)..."
Write-Host "     AspectRatio: $AspectRatio | Salida: $OutputFile"
Write-Host "     Prompt: $($Prompt.Substring(0, [Math]::Min(100, $Prompt.Length)))..."

try {
    $response = Invoke-RestMethod -Uri $endpoint -Method Post `
        -ContentType "application/json; charset=utf-8" `
        -Body ([System.Text.Encoding]::UTF8.GetBytes($requestBody)) `
        -ErrorAction Stop
} catch {
    Write-Host "[ERROR] Error en la API:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host $reader.ReadToEnd() -ForegroundColor DarkRed
    }
    exit 1
}

if (-not $response.predictions -or $response.predictions.Count -eq 0) {
    Write-Host "[ERROR] La API no devolvio imagenes (posible filtro de safety)" -ForegroundColor Red
    Write-Host ($response | ConvertTo-Json -Depth 5) -ForegroundColor DarkRed
    exit 1
}

# La respuesta trae las imagenes como base64 en .bytesBase64Encoded
$bytes = [System.Convert]::FromBase64String($response.predictions[0].bytesBase64Encoded)
[System.IO.File]::WriteAllBytes($OutputFile, $bytes)

$sizeKB = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)
Write-Host "[OK] Imagen generada: $OutputFile ($sizeKB KB)" -ForegroundColor Green
