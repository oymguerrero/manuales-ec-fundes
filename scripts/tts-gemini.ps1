# =========================================================
# Mi CompaniIA - Generar audio con Gemini TTS nativo
# =========================================================
# Uso:
#   .\scripts\tts-gemini.ps1 -InputFile media\scripts\X.txt -OutputFile media\audio-X.wav
#   .\scripts\tts-gemini.ps1 -Text "Hola mundo" -OutputFile media\test.wav -VoiceName "Leda"
#
# Requiere:
#   - GOOGLE_API_KEY (la misma de Imagen 4)
#
# Voces recomendadas (femeninas calidas, narrativa):
#   - Leda (default · calida, narradora)
#   - Kore (clara, articulada)
#   - Aoede (suave, melodica)
#   - Callirhoe (firme pero amable)
#
# La respuesta de Gemini TTS viene como PCM 24kHz mono 16-bit.
# Si ffmpeg esta disponible, convierte a MP3; si no, envuelve en WAV.
# =========================================================

param(
    [string]$InputFile,
    [string]$Text,
    [Parameter(Mandatory=$true)]
    [string]$OutputFile,
    [string]$VoiceName = "Leda",
    [string]$Model = "gemini-2.5-flash-preview-tts",
    [string]$Style = ""
)

if (-not $env:GOOGLE_API_KEY) {
    Write-Host "[ERROR] GOOGLE_API_KEY no esta en el entorno. Carga: . .\scripts\load-env.ps1" -ForegroundColor Red
    exit 1
}

if ($InputFile) {
    if (-not (Test-Path $InputFile)) { Write-Host "[ERROR] No encontrado: $InputFile" -ForegroundColor Red; exit 1 }
    $Text = Get-Content -Raw -Path $InputFile -Encoding UTF8
}
if (-not $Text) { Write-Host "[ERROR] -InputFile o -Text requerido" -ForegroundColor Red; exit 1 }
if ($Style) { $Text = "$Style`n$Text" }

$outputDir = Split-Path -Parent $OutputFile
if ($outputDir -and -not (Test-Path $outputDir)) { New-Item -ItemType Directory -Force -Path $outputDir | Out-Null }

$endpoint = "https://generativelanguage.googleapis.com/v1beta/models/$Model" + ":generateContent?key=$($env:GOOGLE_API_KEY)"
$requestBody = @{
    contents = @( @{ parts = @(@{ text = $Text }) } )
    generationConfig = @{
        responseModalities = @("AUDIO")
        speechConfig = @{
            voiceConfig = @{
                prebuiltVoiceConfig = @{ voiceName = $VoiceName }
            }
        }
    }
} | ConvertTo-Json -Depth 10

Write-Host "[->] Gemini TTS ($Model) | Voz: $VoiceName | Texto: $($Text.Length) chars | Salida: $OutputFile"
try {
    $response = Invoke-RestMethod -Uri $endpoint -Method Post -ContentType "application/json; charset=utf-8" -Body ([System.Text.Encoding]::UTF8.GetBytes($requestBody)) -ErrorAction Stop
} catch {
    Write-Host "[ERROR] API:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host $reader.ReadToEnd() -ForegroundColor DarkRed
    }
    exit 1
}

$audioPart = $response.candidates[0].content.parts[0].inlineData
if (-not $audioPart -or -not $audioPart.data) {
    Write-Host "[ERROR] Sin inlineData.data en la respuesta" -ForegroundColor Red
    exit 1
}

$audioBytes = [Convert]::FromBase64String($audioPart.data)
$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue

if ($ffmpeg) {
    $pcmFile = $OutputFile -replace '\.(mp3|wav)$', '.pcm'
    [System.IO.File]::WriteAllBytes($pcmFile, $audioBytes)
    & ffmpeg -y -f s16le -ar 24000 -ac 1 -i $pcmFile -codec:a libmp3lame -b:a 128k $OutputFile 2>&1 | Out-Null
    Remove-Item $pcmFile -ErrorAction SilentlyContinue
    if (Test-Path $OutputFile) {
        $kb = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)
        Write-Host "[OK] $OutputFile ($kb KB)" -ForegroundColor Green
    }
} else {
    # Envolver PCM 24kHz mono 16-bit en WAV header de 44 bytes
    $wavOut = $OutputFile -replace '\.mp3$', '.wav'
    $dataSize = $audioBytes.Length
    $riffSize = $dataSize + 36
    $h = New-Object byte[] 44
    [System.Text.Encoding]::ASCII.GetBytes("RIFF").CopyTo($h, 0)
    [BitConverter]::GetBytes([uint32]$riffSize).CopyTo($h, 4)
    [System.Text.Encoding]::ASCII.GetBytes("WAVE").CopyTo($h, 8)
    [System.Text.Encoding]::ASCII.GetBytes("fmt ").CopyTo($h, 12)
    [BitConverter]::GetBytes([uint32]16).CopyTo($h, 16)
    [BitConverter]::GetBytes([uint16]1).CopyTo($h, 20)
    [BitConverter]::GetBytes([uint16]1).CopyTo($h, 22)
    [BitConverter]::GetBytes([uint32]24000).CopyTo($h, 24)
    [BitConverter]::GetBytes([uint32]48000).CopyTo($h, 28)
    [BitConverter]::GetBytes([uint16]2).CopyTo($h, 32)
    [BitConverter]::GetBytes([uint16]16).CopyTo($h, 34)
    [System.Text.Encoding]::ASCII.GetBytes("data").CopyTo($h, 36)
    [BitConverter]::GetBytes([uint32]$dataSize).CopyTo($h, 40)
    $full = New-Object byte[] (44 + $audioBytes.Length)
    [Array]::Copy($h, 0, $full, 0, 44)
    [Array]::Copy($audioBytes, 0, $full, 44, $audioBytes.Length)
    [System.IO.File]::WriteAllBytes($wavOut, $full)
    $kb = [math]::Round((Get-Item $wavOut).Length / 1KB, 1)
    Write-Host "[OK] $wavOut ($kb KB · WAV · ffmpeg no disponible para .mp3)" -ForegroundColor Green
}
