# =========================================================
# Mi CompaniIA - Generar audio MP3 con ElevenLabs TTS
# =========================================================
# Uso:
#   .\scripts\tts-elevenlabs.ps1 -InputFile media\scripts\X.txt -OutputFile media\audio-X.mp3
#   .\scripts\tts-elevenlabs.ps1 -Text "Hola mundo" -OutputFile media\test.mp3
#
# Requiere:
#   - ELEVENLABS_API_KEY en el entorno (carga con `. .\scripts\load-env.ps1`)
#
# ElevenLabs maneja texto plano y SSML parcial (etiquetas <break/>, <emphasis/>).
# Modelo recomendado: eleven_multilingual_v2 (mejor calidad en espanol).
# =========================================================

param(
    [string]$InputFile,
    [string]$Text,
    [Parameter(Mandatory=$true)]
    [string]$OutputFile,
    [string]$VoiceId = $env:ELEVENLABS_VOICE_ID,
    [string]$ModelId = $env:ELEVENLABS_MODEL_ID,
    [double]$Stability = -1.0,
    [double]$SimilarityBoost = -1.0,
    [double]$Style = -1.0
)

# Validar credencial
if (-not $env:ELEVENLABS_API_KEY -or $env:ELEVENLABS_API_KEY -eq "tu-elevenlabs-key-aqui") {
    Write-Host "[ERROR] ELEVENLABS_API_KEY no esta configurada." -ForegroundColor Red
    Write-Host "  1. Pega tu key en .env (linea ELEVENLABS_API_KEY=...)" -ForegroundColor Yellow
    Write-Host "  2. Carga las variables: . .\scripts\load-env.ps1" -ForegroundColor Yellow
    exit 1
}

# Defaults
if (-not $VoiceId) { $VoiceId = "21m00Tcm4TlvDq8ikWAM" }
if (-not $ModelId) { $ModelId = "eleven_multilingual_v2" }

if ($Stability -lt 0) {
    if ($env:ELEVENLABS_STABILITY) { $Stability = [double]$env:ELEVENLABS_STABILITY } else { $Stability = 0.5 }
}
if ($SimilarityBoost -lt 0) {
    if ($env:ELEVENLABS_SIMILARITY_BOOST) { $SimilarityBoost = [double]$env:ELEVENLABS_SIMILARITY_BOOST } else { $SimilarityBoost = 0.75 }
}
if ($Style -lt 0) {
    if ($env:ELEVENLABS_STYLE) { $Style = [double]$env:ELEVENLABS_STYLE } else { $Style = 0.0 }
}

# Obtener texto
if ($InputFile) {
    if (-not (Test-Path $InputFile)) {
        Write-Host "[ERROR] Archivo no encontrado: $InputFile" -ForegroundColor Red
        exit 1
    }
    $Text = Get-Content -Raw -Path $InputFile -Encoding UTF8
}

if (-not $Text) {
    Write-Host "[ERROR] Se requiere -InputFile o -Text" -ForegroundColor Red
    exit 1
}

# ElevenLabs maneja SSML parcial. Si viene en <speak>...</speak>, lo
# despojamos del wrapper porque ElevenLabs no lo requiere (acepta <break/>
# y <emphasis/> dentro de texto plano).
$Text = $Text -replace '<speak>\s*', '' -replace '\s*</speak>', ''

# Reemplaza <emphasis level="moderate">X</emphasis> por X
# (ElevenLabs interpreta enfasis con sus voice_settings, no SSML literal)
$Text = $Text -replace '<emphasis[^>]*>', '' -replace '</emphasis>', ''

# Construir request
$requestBody = @{
    text = $Text
    model_id = $ModelId
    voice_settings = @{
        stability = $Stability
        similarity_boost = $SimilarityBoost
        style = $Style
        use_speaker_boost = $true
    }
} | ConvertTo-Json -Depth 5

$url = "https://api.elevenlabs.io/v1/text-to-speech/$VoiceId"

Write-Host "[->] Generando audio (ElevenLabs)..."
Write-Host "     Voz: $VoiceId | Modelo: $ModelId"
Write-Host "     Stability: $Stability | Similarity: $SimilarityBoost | Style: $Style"
Write-Host "     Texto: $($Text.Length) chars | Salida: $OutputFile"

# Crear directorio si no existe
$outputDir = Split-Path -Parent $OutputFile
if ($outputDir -and -not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
}

try {
    $headers = @{
        "xi-api-key" = $env:ELEVENLABS_API_KEY
        "Accept" = "audio/mpeg"
    }

    Invoke-WebRequest -Uri $url -Method Post `
        -Headers $headers `
        -ContentType "application/json; charset=utf-8" `
        -Body ([System.Text.Encoding]::UTF8.GetBytes($requestBody)) `
        -OutFile $OutputFile -ErrorAction Stop | Out-Null
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

if (-not (Test-Path $OutputFile)) {
    Write-Host "[ERROR] El archivo de salida no se creo" -ForegroundColor Red
    exit 1
}

$sizeKB = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)
$sizeStr = "$sizeKB KB"
Write-Host "[OK] Audio generado: $OutputFile ($sizeStr)" -ForegroundColor Green
