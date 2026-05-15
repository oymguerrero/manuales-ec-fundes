# Mi CompañIA — Manuales de los 4 Estándares de Competencia

Manuales interactivos en HTML de los 4 Estándares de Competencia (EC) sobre Inteligencia Artificial aplicada a MiPyMEs. Iniciativa de **FUNDES Latinoamérica** con el apoyo de **Google.org**.

> La IA que acompaña a las MiPyMEs mexicanas. Paso a paso, a tu ritmo, con compañIA.

## Estructura

```
manuales-ec-fundes/
├── index.html        Landing principal con los 4 ECs
├── ec1.html          EC1 — Soluciones de IA alineadas a la MiPyME (DESARROLLADO)
├── ec2.html          EC2 — Productos y servicios con IA (borrador)
├── ec3.html          EC3 — Marketing digital con IA (borrador)
├── ec4.html          EC4 — Transformación digital con IA (borrador)
├── assets/
│   └── styles.css    Sistema de diseño Mi CompañIA
├── img/
│   └── logo.png      Logo Mi CompañIA
├── MiCompañIA_SistemaDiseno_Web.md   Documentación del sistema de diseño
├── README.md
└── .gitignore
```

## Cómo verlo localmente

Solo abre `index.html` con doble clic en cualquier navegador (Chrome, Edge, Firefox). No requiere servidor.

## Configuración de credenciales (solo para generación de assets)

El sitio web NO requiere ninguna API key para verse o publicarse. Las credenciales solo son necesarias si vas a generar **audio narrado** (Google Cloud TTS), **imágenes Imagen** o **video Veo** desde scripts locales.

### 1. Copia el template de variables de entorno

```powershell
Copy-Item .env.example .env
```

```bash
cp .env.example .env
```

### 2. Completa `.env` con tu API key de Google Cloud

Edita `.env` y reemplaza `tu-api-key-aqui` por tu clave real. Para obtenerla:

1. Ve a <https://console.cloud.google.com/apis/credentials>
2. Crea o selecciona un proyecto
3. Habilita las APIs que necesites: **Cloud Text-to-Speech API**, **Imagen** (Vertex AI), **Veo** (Vertex AI)
4. *Crear credenciales* → *Clave de API*
5. *Restringir clave* (recomendado): limita a las APIs habilitadas y a tu IP

### 3. Carga las variables en tu sesión

**PowerShell** (Windows):
```powershell
. .\scripts\load-env.ps1
```

**Bash** (macOS / Linux / WSL):
```bash
source ./scripts/load-env.sh
```

Verás un resumen con las variables cargadas (las que parecen secretas aparecen enmascaradas como `AIza****abcd`).

### 4. Usa el helper de TTS (ejemplo)

Genera un MP3 a partir de un script:

```powershell
.\scripts\tts-generate.ps1 -InputFile media\script-bienvenida.txt -OutputFile media\audio-bienvenida.mp3
```

O con texto directo:

```powershell
.\scripts\tts-generate.ps1 -Text "Hola, soy Mi CompañIA" -OutputFile media\test.mp3
```

### ⚠ Seguridad

- `.env` está en `.gitignore` — **nunca** lo commitees.
- `.env.example` SÍ se commitea (es plantilla sin valores reales).
- Restringe tu API key en la consola de Google Cloud (por API y por IP/referer).
- Si una clave se filtra, **revócala inmediatamente** en la consola de Google Cloud y genera una nueva.

## Cómo colaborar

1. **Clona o abre el repo** en Antigravity (o VS Code, o cualquier editor con Git).
2. **Edita** el archivo HTML del EC en el que estés trabajando — los placeholders están marcados con clase `.placeholder` y dicen "pendiente desarrollar".
3. **Haz commit** con mensaje claro:
   - `EC2: desarrollar conocimiento 1 del Elemento 1`
   - `EC3: corregir numeración del Elemento 2`
4. **Push** al repositorio para que el resto del equipo vea los cambios.

## Estado actual de los manuales

| EC | Elementos | Conocimientos | Estado |
|----|-----------|---------------|--------|
| EC1 | 3 | 14 | Desarrollado |
| EC2 | 4 | 18 | Estructura + placeholders |
| EC3 | 4 | 10 | Estructura + placeholders |
| EC4 | 3 (+1 sin conocimientos) | 13 | Estructura + placeholders |

## Sistema de diseño

El sitio sigue el sistema de diseño **Mi CompañIA** documentado en [`MiCompañIA_SistemaDiseno_Web.md`](MiCompañIA_SistemaDiseno_Web.md). Resumen de tokens principales:

- **Tipografía:** Inter (Google Fonts)
- **Color principal:** `#1F4E8C` (azul) y `#FFC233` (amarillo IA)
- **Color autoridad:** `#0B2E63` (azul profundo)
- **Fondo:** `#FAFCFF` (blanco cálido)
- **Bordes:** `border-radius: 20px`
- **Estilo:** cercano, claro, mucho espacio en blanco, sin tecnicismos.

## Publicar como sitio (opcional)

Para que el equipo pueda abrir el manual desde una URL sin clonar el repo, activa **GitHub Pages**:

1. Ve a *Settings → Pages* en el repo de GitHub.
2. En *Source*, selecciona la rama `main` y carpeta `/ (root)`.
3. Guarda. En ~1 minuto el sitio estará en `https://<usuario>.github.io/<nombre-repo>/`.

## Fuentes

El contenido proviene de los archivos base del proyecto:

- `EC1 COMPLETO.docx`, `EC2 COMPLETO.docx`, `EC3 COMPLETO.docx`, `EC4 COMPLETO.docx`
- `Tabla de especificaciones EC1.xlsx` / `EC2.xls` / `EC3.xlsx` / `EC4.xlsx`
- `Todos los conocimientos.xlsx`

Si encuentras una inconsistencia entre el manual y la fuente, **la fuente manda**.
