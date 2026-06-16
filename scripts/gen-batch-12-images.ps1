# Genera las 12 imágenes pendientes del backlog visual con Gemini Imagen 4
# Secuencial para evitar rate limit

. .\scripts\load-env.ps1

$images = @(
    @{
        out = "img/escenas/sesion-evaluacion.png"; ratio = "16:9"
        prompt = "A Mexican professional consultant, woman in her late 30s, sitting across a table from a male evaluator, late 40s, in a formal meeting room. The consultant presents a portfolio binder of documents to the evaluator who reviews them attentively with a pen in hand. The table has organized printed documents, a coffee cup, and a small notebook. Warm natural lighting from a window on the left. Editorial documentary photography style. Realistic Mexican business setting. No visible text on screens. No logos. Neutral background. Professional attire."
    }
    @{
        out = "img/escenas/entrevista-usuario-tonalli.png"; ratio = "4:3"
        prompt = "A young Mexican man in his late 20s, Diego, sits across from a craftsperson at a wooden workshop table covered with handmade clay pottery pieces in earthy terracotta tones. Diego holds a notebook and pen, taking notes attentively while the artisan shows him a ceramic piece. The workshop background has wooden shelves with colorful pottery. Warm afternoon light from a side window. Editorial documentary style. Realistic scene, no stock photo poses. No text visible on any surface. No logos or brand marks."
    }
    @{
        out = "img/escenas/consultor-implementacion-herramientas.png"; ratio = "4:3"
        prompt = "A Mexican male consultant, early 30s, Carlos, sits at a small wooden table inside a traditional Mexican bakery. He has a laptop open, taking notes in a notebook while speaking with the bakery owner, a Mexican woman in her 50s wearing an apron, who stands nearby. The bakery shelves behind them have traditional pan dulce — conchas, polvorones, cuernos — in warm golden-brown tones. Natural warm lighting. Editorial documentary style. No visible text on screens or signs. No logos."
    }
    @{
        out = "img/escenas/sesion-ideacion-prototipo.png"; ratio = "16:9"
        prompt = "Two Mexican professionals working together on a product innovation session. A young man in his late 20s and a woman artisan in her 50s stand in front of a large whiteboard with sticky notes and hand-drawn diagrams. The man holds a marker and is drawing a simple flow diagram. The woman points to one section with curiosity and engagement. A clay pottery piece sits on the table next to a laptop. Warm workshop lighting. Editorial style. Realistic Mexican creative workspace. No text visible on the whiteboard or screens. No logos."
    }
    @{
        out = "img/escenas/construccion-prototipo-ia.png"; ratio = "4:3"
        prompt = "A young Mexican man in his late 20s, seated at a desk with two monitors, building a digital tool. One screen shows a simple web interface or app prototype with photo upload functionality. His hands are on the keyboard in active development mode. On the desk: a handwritten notebook with UI sketches, a coffee mug, and a small clay figurine as inspiration object. Warm indoor lighting, slight blue glow from screens. Editorial documentary photography. No visible code text on screens. No logos."
    }
    @{
        out = "img/escenas/mariana-revision-metricas.png"; ratio = "4:3"
        prompt = "A Mexican woman in her mid-30s, Mariana, sits at a small cafe table with a laptop showing a social media analytics dashboard — bar charts and engagement metrics visible as abstract shapes without specific text. She holds a coffee cup and takes notes on a spiral notebook beside the laptop. The cafe background is warm and cozy with brick walls and soft lighting. Morning light setting. She looks thoughtful and analytical. Editorial documentary photography style. No visible text or numbers on the screen. No logos."
    }
    @{
        out = "img/escenas/mariana-publicacion-contenido.png"; ratio = "4:3"
        prompt = "A Mexican woman in her mid-30s stands behind a cafe counter with a smartphone in her hands, about to publish a social media post. The phone screen glows but has no readable text — just the abstract form of a social media interface. The cafe counter has a coffee machine, fresh pastries under glass, and warm wood tones. Natural morning light fills the space. She smiles at the phone with satisfaction. Editorial documentary style. No text visible on the phone screen or any signage. No logos."
    }
    @{
        out = "img/escenas/raul-dashboard-optimizacion.png"; ratio = "4:3"
        prompt = "A Mexican man in his late 40s, Raul, stands in a distribution warehouse office area with a large monitor showing abstract data charts and system performance graphs — visible as geometric shapes without readable numbers or text. He points at the screen while speaking with a younger woman developer in her 30s who takes notes on a tablet. Warehouse shelving with products is visible through a glass partition in the background. Practical industrial lighting. Editorial documentary photography. No logos, no brand names, no readable screen text."
    }
    @{
        out = "img/personajes/equipo-la-cuesta.png"; ratio = "1:1"
        prompt = "A young Mexican woman in her mid-20s, barista and social media manager of a specialty coffee shop, stands behind the counter with a tablet in her hands. She wears a casual cafe apron and has a friendly, professional expression. The background is a warm cafe interior with coffee equipment and soft lighting. Square composition, centered portrait, editorial documentary style. Natural warm light. No text visible on the tablet. No logos."
    }
    @{
        out = "img/escenas/carlos-resultados-espiga.png"; ratio = "4:3"
        prompt = "A young Mexican man in his early 30s, Carlos, sits across a small wooden table from a Mexican woman in her 50s, Dona Beatriz, bakery owner wearing an apron. Carlos shows her a tablet — the document shows abstract bar graphs without readable numbers. Both look at the data together with a satisfied expression. The bakery interior is visible in the background with warm golden light and bread on shelves. Editorial documentary style. No text visible on the tablet or documents. No logos."
    }
    @{
        out = "img/personajes/consultor-preparacion-evaluacion.png"; ratio = "1:1"
        prompt = "A Mexican professional in their early 30s, gender-neutral presentation, sits at a desk with a notebook and pen, thoughtfully reviewing a printed checklist or self-assessment document. The person looks focused and reflective. Simple home office background. Warm natural light from a window. Editorial documentary portrait, square composition, centered. No text readable on documents. No logos."
    }
    @{
        out = "img/escenas/raul-instalacion-sistema.png"; ratio = "4:3"
        prompt = "A Mexican woman developer in her early 30s kneels next to a warehouse computer terminal or ruggedized tablet mounted on a stand near shelving. She configures the system — hands on keyboard, focused expression. A warehouse worker in his 40s stands nearby observing the setup. The background shows organized shelving with boxes and products. Industrial fluorescent lighting with warm accent. Editorial documentary photography. No readable text on screens or labels. No logos."
    }
)

$total = $images.Count
$idx = 0
foreach ($img in $images) {
    $idx++
    Write-Host ""
    Write-Host "=== [$idx/$total] $($img.out) ===" -ForegroundColor Cyan
    .\scripts\gen-images-gemini.ps1 -Prompt $img.prompt -OutputFile $img.out -AspectRatio $img.ratio
}

Write-Host ""
Write-Host "=== Generacion completa ===" -ForegroundColor Green
Get-ChildItem img/escenas/*.png, img/personajes/*.png -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host (" - " + $_.FullName.Replace("$pwd\", "") + " (" + [math]::Round($_.Length / 1KB) + " KB)")
}
