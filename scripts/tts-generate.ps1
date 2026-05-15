# =========================================================
# Mi CompaniIA - Generar audio MP3 con Google Cloud TTS
# =========================================================
# Uso:
#   .\scripts\tts-generate.ps1 -InputFile media\script-X.txt -OutputFile media\audio-X.mp3
#   .\scripts\tts-generate.ps1 -Text "Hola mundo" -OutputFile media\test.mp3
#
# Requiere:
#   - GOOGLE_API_KEY en el entorno (carga con `. .\scripts\load-env.ps1`)
#   - API Cloud Text-to-Speech habilitada en el proyecto Google Cloud
#
# Voces recomendadas para espanol mexicano:
#   - es-US-Neural2-A   femenina calida (default)
#   - es-US-Neural2-B   masculina profesional
#   - es-US-Studio-B    premium masculina narrativa
# =========================================================

param(
    [string]$InputFile,
    [string]$Text,
    [Parameter(Mandatory=$true)]
    [string]$OutputFile,
    [string]$VoiceName = $env:TTS_VOICE_NAME,
    [string]$LanguageCode = $env:TTS_LANGUAGE_CODE,
    [double]$SpeakingRate = 0.0
)

# Validar credencial
if (-not $env:GOOGLE_API_KEY) {
    Write-Host "[ERROR] GOOGLE_API_KEY no esta en el entorno." -ForegroundColor Red
    Write-Host "  Carga primero las variables: . .\scripts\load-env.ps1" -ForegroundColor Yellow
    exit 1
}

# Defaults
if (-not $VoiceName) { $VoiceName = "es-US-Neural2-A" }
if (-not $LanguageCode) { $LanguageCode = "es-MX" }
if ($SpeakingRate -eq 0.0) {
    if ($env:TTS_SPEAKING_RATE) {
        $SpeakingRate = [double]$env:TTS_SPEAKING_RATE
    } else {
        $SpeakingRate = 0.95
    }
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

# Detectar si es SSML
$inputType = "text"
if ($Text.TrimStart() -like "<speak*") {
    $inputType = "ssml"
}

# Validar longitud
if ($Text.Length -gt 5000) {
    Write-Host "[!] Texto excede 5000 chars ($($Text.Length))" -ForegroundColor Yellow
    Write-Host "    Fracciona en multiples llamadas y concatena con ffmpeg." -ForegroundColor Yellow
    exit 1
}

# Construir request
$requestBody = @{
    input = @{ $inputType = $Text }
    voice = @{
        languageCode = $LanguageCode
        name = $VoiceName
    }
    audioConfig = @{
        audioEncoding = "MP3"
        speakingRate = $SpeakingRate
        pitch = -1.0
        sampleRateHertz = 24000
    }
} | ConvertTo-Json -Depth 5

$url = "https://texttospeech.googleapis.com/v1/text:synthesize?key=$($env:GOOGLE_API_KEY)"

Write-Host "[->] Generando audio..."
Write-Host "     Voz: $VoiceName | Idioma: $LanguageCode | Velocidad: $SpeakingRate"
Write-Host "     Texto: $($Text.Length) chars | Salida: $OutputFile"

try {
    $response = Invoke-RestMethod -Uri $url -Method Post `
        -ContentType "application/json; charset=utf-8" `
        -Body ([System.Text.Encoding]::UTF8.GetBytes($requestBody))
} catch {
    Write-Host "[ERROR] Error en la API:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    if ($_.ErrorDetails.Message) {
        Write-Host $_.ErrorDetails.Message -ForegroundColor DarkRed
    }
    exit 1
}

if (-not $response.audioContent) {
    Write-Host "[ERROR] Respuesta sin audioContent" -ForegroundColor Red
    exit 1
}

# Crear directorio si no existe
$outputDir = Split-Path -Parent $OutputFile
if ($outputDir -and -not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
}

# Decodificar base64 -> MP3
$audioBytes = [Convert]::FromBase64String($response.audioContent)
[System.IO.File]::WriteAllBytes($OutputFile, $audioBytes)

$sizeKB = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)
$sizeStr = "$sizeKB KB"
Write-Host "[OK] Audio generado: $OutputFile ($sizeStr)" -ForegroundColor Green
