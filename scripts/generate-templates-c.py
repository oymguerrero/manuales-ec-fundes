#!/usr/bin/env python3
"""
Genera los 9 templates de los productos del Estándar C · Implementar marketing digital
con IA en MiPyMEs (Estándar C · Crear contenido de marketing digital con IA).

- 8 Word (.doc) como HTML estilizado con MIME Office
- 1 Excel (.xls) como HTML estilizado con MIME Office

Caso pedagógico: Cafetería La Cuesta — café de especialidad en zona universitaria,
6 empleados, dueña Mariana (tuesta su propio café). Publican en redes sociales de
forma irregular y sin estrategia. Quieren atraer al público universitario y posicionar
el café de especialidad frente a las cadenas.

Filosofía pedagógica: NO darle la solución al aspirante. Cada template muestra:
  (1) el criterio F21 literal
  (2) ejemplo breve del caso La Cuesta (solo ilustrativo)
  (3) preguntas guía que el aspirante responde con datos de SU MiPyME real

Uso:
    python3 scripts/generate-templates-c.py

Salida: estandar-c/templates/<num_con_guiones>-<slug>.{doc|xls}
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-c" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

PRODUCTS = [
    # -----------------------------------------------------------------------
    # ELEMENTO 1 · PLANIFICAR
    # -----------------------------------------------------------------------
    {
        "num": "1.1",
        "slug": "1-1-expediente-informacion",
        "format": "word",
        "elemento": "1 · Planificar",
        "title": "Expediente de información clave de la MiPyME, documentado",
        "intro": (
            "Es el punto de partida del proyecto: un expediente completo con el perfil "
            "empresarial, datos de contacto del responsable de marketing, productos/servicios "
            "a promover, metas comerciales, plataformas digitales activas, métricas de presencia "
            "actual, análisis de contenido existente, perfil de audiencia objetivo y el acuerdo "
            "de confidencialidad firmado."
        ),
        "f21": [
            "(a) Contiene el perfil empresarial incluyendo: el nombre de la empresa/marca comercial, "
            "giro, misión, visión, valores y ubicación",
            "(b) Incluye los datos de contacto de la persona responsable del marketing digital en la "
            "MiPyME: nombre, cargo, correo electrónico y teléfono",
            "(c) Incluye el listado de productos/servicios a promover a través del marketing digital",
            "(d) Especifica las metas comerciales por un periodo de tiempo considerando volumen de "
            "ventas/medio de captación de clientes",
            "(e) Incluye el listado de plataformas digitales en los que tiene presencia actual la MiPyME",
            "(f) Detalla las métricas de presencia digital con las que cuenta la MiPyME",
            "(g) Cuenta con el análisis del contenido existente, especificando tipo, frecuencia y nivel "
            "de interacción por cada plataforma digital",
            "(h) Contiene descrito el perfil de la audiencia objetivo, considerando al menos tres "
            "variables de segmentación: características demográficas, intereses y comportamiento digital",
            "(i) Tiene el acuerdo de confidencialidad firmado por la persona responsable de la "
            "información y el proveedor de servicios",
        ],
        "caso": (
            "Cafetería La Cuesta · zona universitaria · café de especialidad. "
            "Mariana (dueña): mariana@lacuesta.mx / 55-1234-5678. "
            "Plataformas activas: Instagram (890 seguidores, 3 posts/semana), "
            "Facebook (420 seguidores, 1-2 posts/semana). "
            "Contenido actual: fotos sin edición de cafés, textos improvisados, sin hashtags estratégicos. "
            "Audiencia: universitarios 18-28 años que buscan espacios de estudio + café de calidad. "
            "Meta: +200 seguidores/mes y +15% de visitas al local en 3 meses."
        ),
        "preguntas": [
            (
                "Perfil empresarial completo",
                "Nombre de la empresa, marca comercial, giro, misión, visión, valores y ubicación "
                "de la MiPyME con la que trabajas.",
            ),
            (
                "Contacto de la persona responsable de marketing",
                "¿Quién en la MiPyME es responsable del marketing digital? "
                "Nombre completo, cargo, correo y teléfono.",
            ),
            (
                "Productos y servicios a promover",
                "¿Qué productos o servicios vas a promover con el contenido digital? "
                "Lista al menos 3 con una descripción breve de cada uno.",
            ),
            (
                "Metas comerciales",
                "¿Qué quiere lograr la MiPyME en los próximos 3-6 meses? "
                "Define metas en términos de seguidores, alcance, clientes o ventas.",
            ),
            (
                "Plataformas digitales actuales",
                "¿En qué plataformas digitales tiene presencia la MiPyME hoy? "
                "Lista todas: redes sociales, sitio web, marketplace, WhatsApp Business.",
            ),
            (
                "Métricas de presencia digital actual",
                "Por cada plataforma: ¿cuántos seguidores tiene? ¿Cuál es su tasa de interacción "
                "promedio? ¿Con qué frecuencia publica?",
            ),
            (
                "Análisis del contenido existente",
                "¿Qué tipo de contenido publica actualmente la MiPyME? ¿Con qué frecuencia? "
                "¿Qué publicaciones han funcionado mejor y por qué?",
            ),
            (
                "Perfil de la audiencia objetivo",
                "¿A quién quiere llegar la MiPyME? Describe al menos 3 variables: "
                "características demográficas, intereses y comportamiento digital.",
            ),
            (
                "Acuerdo de confidencialidad",
                "¿Firmaste el acuerdo de confidencialidad con la MiPyME? "
                "Adjunta la evidencia o describe las condiciones acordadas.",
            ),
        ],
    },
    {
        "num": "1.2",
        "slug": "1-2-estrategia-contenido",
        "format": "word",
        "elemento": "1 · Planificar",
        "title": "Estrategia de contenido de marketing digital de la MiPyME utilizando IA, diseñada",
        "intro": (
            "Define la voz y personalidad de marca, los lineamientos de tono por plataforma, "
            "los tipos de contenido recomendados por etapa del embudo, el calendario de publicación "
            "para al menos cuatro semanas, los horarios óptimos, las temporadas comerciales relevantes, "
            "los objetivos medibles y el presupuesto de implementación. Debe contar con la aprobación "
            "documentada de la persona responsable de marketing en la MiPyME."
        ),
        "f21": [
            "(a) Especifica la definición de la voz y personalidad de marca para el contenido digital",
            "(b) Incluye los lineamientos de tono y estilo por plataforma digital",
            "(c) Precisa los tipos de contenido digital de texto/imagen/audio/video recomendados "
            "por etapa del embudo de ventas de acuerdo con la información clave recabada en el levantamiento",
            "(d) Contiene la tabla de análisis conformada por: la justificación de la(s) plataforma(s) "
            "digital(es) a utilizar por audiencia, el tipo de formato con especificaciones técnicas, "
            "las herramientas/plataformas de IA recomendadas por tipo de contenido digital y la "
            "frecuencia de publicación acorde a la capacidad operativa",
            "(e) Indica los horarios de publicación sugeridos por plataforma digital conforme a las "
            "recomendaciones de la IA y a los hábitos del público objetivo",
            "(f) Incluye la vinculación a las temporadas comerciales relevantes para el sector del negocio",
            "(g) Especifica la distribución de los tipos de contenido digital a lo largo del periodo, "
            "considerando al menos cuatro semanas de planificación",
            "(h) Incluye al menos dos objetivos medibles vinculados al negocio y sus respectivas "
            "métricas de seguimiento",
            "(i) Incluye el presupuesto/monto de inversión requerido de implementación, de acuerdo "
            "con el contexto de la MiPyME",
            "(j) Contiene la evidencia de aprobación de la estrategia de marketing digital planteada "
            "por parte de la persona responsable del marketing digital en la MiPyME",
        ],
        "caso": (
            "Voz de marca: 'el café de tu rincón favorito' — cálida, cercana, educativa sobre café "
            "de especialidad, con orgullo local. Tono por plataforma: Instagram (aspiracional + visual); "
            "Facebook (informativo + comunitario). Semana tipo: 5 posts semanales entre ambas plataformas "
            "— lunes receta/tip; miércoles origen del café de temporada; viernes invitación al local. "
            "Herramientas IA recomendadas: ChatGPT/Claude para copy de texto; Midjourney/Canva IA para "
            "imágenes; ElevenLabs para reels con narración. Temporada clave: inicio de semestre (agosto "
            "y enero), exámenes finales (noviembre y mayo). Objetivo 1: +200 seguidores/mes en Instagram. "
            "Objetivo 2: +15% de visitas al local desde redes en 3 meses."
        ),
        "preguntas": [
            (
                "Voz y personalidad de marca",
                "¿Cómo describe la MiPyME su personalidad de marca? ¿Con qué adjetivos se identifica? "
                "¿A qué marcas aspira parecerse en tono?",
            ),
            (
                "Tono y estilo por plataforma",
                "¿Cómo varía el tono en Instagram vs Facebook vs TikTok? "
                "¿Qué restricciones de estilo aplican en cada plataforma?",
            ),
            (
                "Tipos de contenido por etapa del embudo",
                "¿Qué contenido vas a usar para que te descubran (reconocimiento)? "
                "¿Para que te consideren (consideración)? ¿Para que te compren (conversión)? "
                "¿Para que te recomienden (fidelización)?",
            ),
            (
                "Tabla de análisis de plataformas",
                "Por cada plataforma elegida: justifica por qué ese público está ahí, qué formato "
                "usarás (feed/story/reel/post), qué herramienta IA usarás y con qué frecuencia publicarás.",
            ),
            (
                "Horarios de publicación",
                "¿A qué horas publicas en cada plataforma? ¿Qué te dice la IA o las analíticas "
                "sobre los mejores horarios para tu audiencia?",
            ),
            (
                "Temporadas comerciales relevantes",
                "¿Qué fechas o eventos del año son clave para el negocio? "
                "¿Cómo los integras al calendario de contenido?",
            ),
            (
                "Distribución de contenido (al menos 4 semanas)",
                "Elabora el calendario de publicación para las primeras 4 semanas: "
                "fecha, plataforma, tipo de contenido, tema.",
            ),
            (
                "Objetivos medibles",
                "Define al menos 2 objetivos con número, plazo y métrica. "
                "Ejemplo: 'Crecer 200 seguidores en Instagram en 90 días, medido con las analíticas nativas.'",
            ),
            (
                "Presupuesto de implementación",
                "¿Cuánto propones invertir? Detalla: herramientas de IA (costo mensual), "
                "publicidad pagada (presupuesto por semana), horas de trabajo estimadas.",
            ),
            (
                "Evidencia de aprobación",
                "¿Cómo documentarás que la persona responsable aprobó la estrategia? "
                "Correo de confirmación, firma en el documento, captura de pantalla de mensaje.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 2 · GENERAR
    # -----------------------------------------------------------------------
    {
        "num": "2.1",
        "slug": "2-1-portafolio-texto",
        "format": "word",
        "elemento": "2 · Generar",
        "title": "Contenido de texto del portafolio de marketing digital generado con IA, documentado",
        "intro": (
            "Documenta el proceso completo de generación de contenido de texto con IA: "
            "la herramienta utilizada, el prompt estructurado (rol, contexto, tarea, audiencia, "
            "formato, tono, restricciones), la versión final lista para publicar y la verificación "
            "de originalidad, coherencia de marca, beneficios y llamados a la acción."
        ),
        "f21": [
            "(a) Especifica la herramienta de IA utilizada para la generación contenido de texto",
            "(b) Incluye la estructura del prompt/contenido de referencia para generación de contenido "
            "de texto que incluya al menos el rol, el contexto, la tarea, la audiencia, el formato, "
            "el tono de comunicación y las restricciones",
            "(c) Contiene la versión final del texto generada con apoyo de la herramienta/plataforma "
            "de IA para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a originalidad y coherencia con la marca",
            "(e) Está redactado de forma clara, precisa y con apego a reglas de redacción y ortografía",
            "(f) Contiene los beneficios y llamados a la acción",
            "(g) Se adapta al formato de la(s) plataforma(s) digital(es) de destino",
        ],
        "caso": (
            "Herramienta: Claude claude-sonnet-4-6. "
            "Prompt estructura completa: 'Rol: eres redactor de contenido de marketing digital "
            "especializado en cafeterías de especialidad. Contexto: Cafetería La Cuesta, zona "
            "universitaria, café tostado en casa. Tarea: escribe el caption para un post de Instagram "
            "del lunes. Audiencia: universitarios 18-28 años. Formato: caption de máximo 150 palabras "
            "+ 5 hashtags. Tono: cálido, cercano, con dato de origen del café. Restricciones: sin "
            "emojis excesivos, no usar la palabra «delicioso».' "
            "Versión final: 'Hoy tostamos el Oaxaqueño de temporada. Notas de chocolate oscuro, "
            "ciruela y un final largo. Ven a probarlo entre clases — de 8 a 8. ☕ "
            "#CaféDeEspecialidad #LaCuesta #CaféOaxaqueño #ZonaUniversitaria #CaféTostado'"
        ),
        "preguntas": [
            (
                "Herramienta de IA usada",
                "¿Qué herramienta usaste para generar el texto? ¿Qué versión o modelo?",
            ),
            (
                "Estructura del prompt completo",
                "Escribe el prompt exacto que usaste, con todos sus elementos: "
                "rol, contexto, tarea, audiencia, formato, tono, restricciones.",
            ),
            (
                "Versión final del texto",
                "Copia aquí el texto final, ya editado y listo para publicar, "
                "indicando para qué plataforma es.",
            ),
            (
                "Validación de originalidad y coherencia de marca",
                "¿Cómo verificaste que el texto es original? "
                "¿Cómo comprobaste que refleja la voz de la marca?",
            ),
            (
                "Beneficios y llamados a la acción",
                "¿Qué beneficio comunica el texto al lector? "
                "¿Cuál es el llamado a la acción y dónde aparece?",
            ),
            (
                "Adaptación al formato de la plataforma",
                "¿Cumple con los límites de caracteres de la plataforma? "
                "¿Incluye hashtags, menciones u otros elementos propios del medio?",
            ),
        ],
    },
    {
        "num": "2.2",
        "slug": "2-2-portafolio-imagen",
        "format": "word",
        "elemento": "2 · Generar",
        "title": "Contenido de imagen del portafolio de marketing digital generado con IA, documentado",
        "intro": (
            "Documenta el proceso de generación de imágenes con IA: la herramienta, el prompt "
            "o imagen de referencia, la imagen final para cada plataforma, la verificación de "
            "coherencia visual con la marca, la coherencia anatómica y física, y la relación de "
            "aspecto correcta para la plataforma de destino."
        ),
        "f21": [
            "(a) Especifica la herramienta de IA utilizada para la generación del contenido de imagen",
            "(b) Incluye la estructura del prompt/imagen de referencia para la generación de contenido "
            "de imagen",
            "(c) Contiene la versión final de imagen generada con la herramienta/plataforma de IA "
            "para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a la coherencia visual con la marca, "
            "coherencia anatómica y física",
            "(e) Es congruente con el requerimiento y el contexto/realidad",
            "(f) Tiene la relación de aspecto acorde con la(s) plataforma(s) digital(es) de destino",
        ],
        "caso": (
            "Herramienta: Midjourney v6. "
            "Prompt: 'A warm specialty coffee shop interior, latte art close-up, wooden bar, "
            "glass jars with roasted coffee beans, warm golden lighting, cozy university neighborhood "
            "atmosphere, Instagram square format --ar 1:1 --style raw'. Iteraciones: 3. "
            "Imagen final: cuadrada 1:1, colores cálidos terracota y madera, sin texto sobreimpuesto "
            "(el copy va en el caption). Verificación: la imagen no muestra logos de otras marcas, "
            "el café latte art es proporcional y anatómicamente correcto, los granos son reconocibles "
            "como café."
        ),
        "preguntas": [
            (
                "Herramienta de IA para imágenes",
                "¿Qué herramienta usaste? (Midjourney, DALL-E, Adobe Firefly, Canva IA, "
                "Imagen de Google...) ¿Qué versión?",
            ),
            (
                "Prompt o parámetros de imagen",
                "Escribe el prompt completo. Si usaste una imagen de referencia, descríbela. "
                "¿Qué parámetros configuraste: estilo, relación de aspecto, nivel de detalle?",
            ),
            (
                "Imagen final y plataforma de destino",
                "Describe la imagen final o adjunta la captura. "
                "¿Para qué plataforma está optimizada y en qué formato?",
            ),
            (
                "Coherencia visual con la marca",
                "¿Cómo verificaste que la imagen es coherente con la identidad visual de la MiPyME? "
                "¿Los colores, el estilo y el ambiente coinciden?",
            ),
            (
                "Coherencia anatómica y física",
                "¿Revisaste que no haya distorsiones, objetos imposibles o personas con fisionomía "
                "incorrecta? ¿Cómo lo corregiste si fue necesario?",
            ),
            (
                "Relación de aspecto correcta",
                "¿Usaste la relación de aspecto correcta para la plataforma? "
                "(1:1 para feed de Instagram; 9:16 para stories y Reels; 16:9 para Facebook).",
            ),
        ],
    },
    {
        "num": "2.3",
        "slug": "2-3-portafolio-audio",
        "format": "word",
        "elemento": "2 · Generar",
        "title": "Contenido de audio del portafolio de marketing digital generado con IA, documentado",
        "intro": (
            "Documenta el proceso de generación de audio con IA: la herramienta y voz seleccionada, "
            "el guión o parámetros proporcionados, el audio final y su uso previsto, la verificación "
            "de calidad de voz (claridad, dicción, naturalidad) y la coherencia con la personalidad "
            "de marca de la MiPyME."
        ),
        "f21": [
            "(a) Especifica la herramienta de IA utilizada para la generación del contenido de audio",
            "(b) Incluye el prompt/los parámetros de contenido de audio de narración por voz/música "
            "en la herramienta de IA elegida",
            "(c) Contiene la versión final de audio generada con la herramienta/plataforma de IA "
            "para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a la claridad de voz/sonido, "
            "dicción/ritmo y la naturalidad de voz/sonido",
            "(e) Tiene coherencia con la marca",
        ],
        "caso": (
            "Herramienta: ElevenLabs (voz 'Rachel', español neutro). "
            "Parámetros: stability 0.65, similarity_boost 0.75, modelo eleven_multilingual_v2. "
            "Guión: 'En La Cuesta tostamos nuestro propio café. Ven a descubrir el sabor del café "
            "de especialidad hecho con cuidado, en tu zona universitaria.' Duración: 12 segundos. "
            "Uso: narración de fondo para Reel de Instagram. Verificación: se escuchó en auriculares "
            "— dicción clara, sin pausas artificiales, tono cálido y coincide con la voz de marca."
        ),
        "preguntas": [
            (
                "Herramienta de IA para audio",
                "¿Qué herramienta usaste para generar el audio? ¿Qué voz o modelo seleccionaste?",
            ),
            (
                "Prompt o parámetros de audio",
                "¿Qué guión o instrucciones proporcionaste? ¿Qué parámetros configuraste: "
                "tipo de voz, tono, ritmo, emoción?",
            ),
            (
                "Audio final y uso previsto",
                "¿Para qué plataforma y formato es el audio? "
                "(narración de reel, podcast, jingle...) ¿Cuánto dura?",
            ),
            (
                "Calidad de voz y sonido",
                "¿Verificaste la claridad, la dicción y la naturalidad? "
                "¿Hubo que hacer ajustes de velocidad, pausas o entonación?",
            ),
            (
                "Coherencia con la marca",
                "¿El tono y estilo del audio refleja la personalidad de la MiPyME? "
                "¿La voz elegida es coherente con cómo quiere percibirse la marca?",
            ),
        ],
    },
    {
        "num": "2.4",
        "slug": "2-4-portafolio-video",
        "format": "word",
        "elemento": "2 · Generar",
        "title": "Contenido de video del portafolio de marketing digital generado con IA, documentado",
        "intro": (
            "Documenta el proceso de generación de video con IA: la herramienta, el prompt "
            "por escena o referencia visual, el video final y su especificación técnica, "
            "la coherencia narrativa (inicio-desarrollo-cierre y llamado a la acción), "
            "la consistencia visual entre escenas y la calidad de audio integrado."
        ),
        "f21": [
            "(a) Especifica la herramienta de IA utilizada para la generación de contenido de video",
            "(b) Incluye la estructura del prompt/video/imagen de referencia para la generación "
            "de contenido de imagen",
            "(c) Contiene la versión final de video generada con la herramienta/plataforma de IA "
            "para la(s) plataforma(s) digital(es) de destino",
            "(d) Tiene coherencia narrativa con inicio, desarrollo y cierre definidos, así como "
            "claridad del mensaje e inclusión de llamado a la acción",
            "(e) Tiene consistencia visual y física de los elementos entre escenas y coherencia "
            "con la identidad de la marca",
            "(f) Cumple con la calidad técnica con respecto a la resolución, formato y duración "
            "adecuados a la plataforma digital",
            "(g) Tiene calidad de audio con respecto a la pronunciación/entonación/sonido(s) y claridad",
            "(h) Cumple con los criterios de calidad en cuanto a originalidad y coherencia con la marca",
        ],
        "caso": (
            "Herramienta: Higgsfield / RunwayML gen-3. "
            "Prompt por escena: 'Inicio: manos de barista moliendo café en molino manual, luz cálida "
            "de mañana, cámara lenta; Desarrollo: espresso cayendo sobre taza de cerámica artesanal, "
            "vapor ascendente, fondo café oscuro; Cierre: manos sosteniendo taza de latte art, campus "
            "universitario de fondo desenfocado, texto sobreimpuesto: «Tu café de siempre, de "
            "especialidad» 9:16, 15 segundos'. Verificación: 3 iteraciones. Video final: .mp4, "
            "1080x1920, 15 segundos, sin distorsiones temporales en el café. Audio: música de fondo "
            "ambiental suave generada con Suno, sin letra, 72 BPM."
        ),
        "preguntas": [
            (
                "Herramienta de IA para video",
                "¿Qué herramienta usaste para generar el video? "
                "(Higgsfield, RunwayML, Kling, Sora, Pika, CapCut IA...)",
            ),
            (
                "Prompt o referencia de video",
                "Describe el prompt completo por escena. ¿Usaste imagen o video de referencia? "
                "¿Qué instrucciones diste sobre movimiento, iluminación, estilo visual?",
            ),
            (
                "Video final",
                "¿Para qué plataforma es? ¿Cuánto dura? ¿Qué resolución y formato tiene? "
                "¿Cómo lo vas a publicar?",
            ),
            (
                "Coherencia narrativa",
                "¿El video tiene inicio, desarrollo y cierre claros? ¿El mensaje central es evidente? "
                "¿Dónde está el llamado a la acción?",
            ),
            (
                "Consistencia visual entre escenas",
                "¿Los personajes, objetos y colores son consistentes entre escenas? "
                "¿Hay saltos o distorsiones que corregiste?",
            ),
            (
                "Calidad técnica",
                "Resolución, formato de archivo, duración. "
                "¿Cumple con las especificaciones técnicas de la plataforma destino?",
            ),
            (
                "Calidad de audio",
                "¿El audio (música, narración, efectos) es claro y coherente con el video? "
                "¿Se escucha bien sin auriculares?",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 3 · IMPLEMENTAR
    # -----------------------------------------------------------------------
    {
        "num": "3.1",
        "slug": "3-1-bitacora-implementacion",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Bitácora de implementación del contenido de marketing digital en plataformas digitales, documentada",
        "intro": (
            "Registro cronológico de todas las publicaciones realizadas durante la campaña: "
            "fecha, hora, plataforma, tipo de contenido y estado de cada pieza. Incluye capturas "
            "de pantalla o enlaces de verificación, especificaciones técnicas aplicadas, incidencias "
            "y rechazos de plataforma, y evidencia de las herramientas de medición configuradas."
        ),
        "f21": [
            "(a) Contiene el listado de publicaciones realizadas con fecha, hora, plataforma(s) "
            "digital(es), tipo de contenido y estado de publicación: publicado/programado/rechazado",
            "(b) Incluye las capturas de pantalla/enlaces de verificación de cada publicación realizada",
            "(c) Indica la descripción de las especificaciones técnicas de cada medio utilizado "
            "conforme a la estrategia de marketing digital",
            "(d) Contiene el registro de incidencias técnicas/rechazos de plataforma(s) digital(es) "
            "y los ajustes realizados durante la implementación",
            "(e) Incluye la evidencia de las herramientas de medición y seguimiento en cada "
            "plataforma digital utilizada",
        ],
        "caso": (
            "Semana 1: lunes 9:00 → Instagram feed (imagen café, caption texto IA) → publicado; "
            "miércoles 10:00 → Facebook post (mismo contenido adaptado) → publicado; "
            "viernes 18:00 → Instagram Reel (video 15s) → programado. "
            "Incidencia: el reel del martes fue rechazado por Meta por audio con derechos de autor "
            "— se reemplazó con pista de Suno sin licencia. "
            "Herramientas de seguimiento: Meta Business Suite para ambas plataformas, "
            "Google Analytics UTM para links al menú."
        ),
        "preguntas": [
            (
                "Registro de publicaciones",
                "Por cada publicación: fecha, hora exacta, plataforma, tipo de contenido "
                "(imagen, video, texto, audio), estado (publicado / programado / rechazado).",
            ),
            (
                "Capturas de pantalla o enlaces",
                "Para cada publicación realizada: adjunta la captura de pantalla o el enlace "
                "público que confirma que se publicó.",
            ),
            (
                "Especificaciones técnicas aplicadas",
                "¿Verificaste que cada pieza cumplía con las especificaciones técnicas de la "
                "plataforma antes de publicar? ¿Qué dimensiones, formatos y pesos usaste?",
            ),
            (
                "Incidencias y ajustes",
                "¿Tuviste rechazos, errores o problemas durante la publicación? "
                "¿Cuáles fueron y cómo los resolviste?",
            ),
            (
                "Herramientas de medición instaladas",
                "¿Configuraste píxeles de seguimiento, UTMs o cualquier herramienta de analítica? "
                "¿En qué plataformas y para qué métricas?",
            ),
        ],
    },
    {
        "num": "3.2",
        "slug": "3-2-guia-operativa",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Guía operativa de publicación para la MiPyME, documentada",
        "intro": (
            "Manual práctico que le queda a la MiPyME para publicar de manera autónoma "
            "después del proyecto: procedimiento paso a paso por plataforma, especificaciones "
            "técnicas de formato, horarios recomendados, restricciones y políticas de contenido, "
            "y accesos a las herramientas de programación y gestión de redes utilizadas."
        ),
        "f21": [
            "(a) Contiene el procedimiento paso a paso de carga, programación y publicación de "
            "contenido por cada plataforma digital activa de la MiPyME",
            "(b) Incluye las especificaciones técnicas de formato por cada plataforma digital "
            "activa de la MiPyME",
            "(c) Enlista los horarios recomendados de publicación por cada plataforma digital "
            "activa de la MiPyME conforme a la estrategia",
            "(d) Contiene descritas las restricciones y políticas de contenido de cada plataforma "
            "digital activa de la MiPyME",
            "(e) Incluye los accesos y credenciales de las herramientas de programación y gestión "
            "de redes utilizadas",
        ],
        "caso": (
            "Procedimiento Instagram: 1) Abrir Meta Business Suite → seleccionar La Cuesta; "
            "2) «Crear publicación» → elegir tipo (feed/reel/historia); "
            "3) cargar el archivo (JPG ≤ 30 MB para imagen, MP4 ≤ 4 GB para video); "
            "4) agregar caption, hashtags y ubicación; 5) programar fecha y hora; "
            "6) verificar vista previa multidispositivo; 7) publicar/programar. "
            "Especificaciones técnicas: Feed cuadrado 1:1 (1080×1080), Feed horizontal 1.91:1 "
            "(1080×566), Reels 9:16 (1080×1920), Stories 9:16 (1080×1920). "
            "Restricciones clave: sin marcas de agua de competidores, sin afirmaciones de salud "
            "sin sustento, sin contenido de derechos reservados en el audio."
        ),
        "preguntas": [
            (
                "Procedimiento paso a paso por plataforma",
                "Para cada plataforma activa de la MiPyME: escribe los pasos exactos para cargar, "
                "programar y publicar contenido. Debe ser suficientemente claro para que alguien "
                "sin experiencia lo siga.",
            ),
            (
                "Especificaciones técnicas por plataforma",
                "Tabla de formatos: tipo de contenido, dimensiones recomendadas, peso máximo del "
                "archivo, duración máxima, formatos admitidos.",
            ),
            (
                "Horarios recomendados",
                "Por plataforma: ¿a qué horas publicas? ¿Qué días? Basa esto en los datos de "
                "analítica o en las recomendaciones de la IA.",
            ),
            (
                "Restricciones y políticas de contenido",
                "¿Qué tipo de contenido rechaza cada plataforma? ¿Cuáles son las principales "
                "causas de que una publicación sea rechazada o penalizada?",
            ),
            (
                "Accesos y herramientas",
                "Lista las herramientas de programación que usas (Meta Business Suite, Buffer, "
                "Hootsuite, Later...) con los datos de acceso — sin contraseñas aquí, pero indica "
                "dónde están guardadas de forma segura.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 4 · OPTIMIZAR
    # -----------------------------------------------------------------------
    {
        "num": "4.1",
        "slug": "4-1-reporte-optimizacion",
        "format": "excel",
        "elemento": "4 · Optimizar",
        "title": "Reporte de desempeño del contenido publicado de marketing digital, documentado",
        "intro": (
            "Producto integrador que combina el reporte de desempeño de la campaña concluida "
            "con el plan de optimización para el siguiente periodo. Incluye métricas por publicación "
            "y por plataforma, comparativo contra objetivos, análisis de mejor y peor desempeño, "
            "recomendaciones de ajuste y el calendario del siguiente periodo. Debe contar con la "
            "aprobación de la persona responsable de marketing en la MiPyME."
        ),
        "f21": [
            "(a) Está elaborado a partir de una campaña de marketing digital concluida",
            "(b) Tiene el resumen ejecutivo con los principales resultados alcanzados en el periodo "
            "analizado y su relación con los objetivos de la estrategia",
            "(c) Incluye las métricas de rendimiento por publicación, por tipo de contenido y por "
            "plataforma digital, así como el comparativo respecto a la línea base de la MiPyME/"
            "indicadores de referencia de mercado",
            "(d) Especifica el comparativo de resultados contra los objetivos medibles establecidos "
            "en la estrategia aprobada",
            "(e) Contiene el análisis de mayor y menor rendimiento de los contenidos por tipo, "
            "formato, horario y plataforma digital, con la identificación de patrones de "
            "comportamiento y metas establecidas",
            "(f) Incluye las capturas de pantalla/evidencias de los datos reportados por las "
            "herramientas de medición y seguimiento de las plataformas digitales",
            "(g) Especifica la fecha del periodo de análisis, la fuente de los datos presentados "
            "y la frecuencia de medición",
            "(h) Contiene las recomendaciones de continuidad/ajuste a los tipos de contenido/"
            "formatos/frecuencia de publicación por plataforma digital, con base en el análisis "
            "de resultados",
            "(i) Indica la(s) propuesta(s) de pruebas de optimización a realizar, considerando "
            "la hipótesis a validar y la métrica de éxito",
            "(j) Incluye la recomendación de continuidad/ajuste a horarios de publicación con base "
            "en los datos de rendimiento por plataforma digital y por tipo de contenido",
            "(k) Contiene la recomendación de continuidad/modificación a la segmentación de audiencia "
            "y al presupuesto de promoción de acuerdo con los resultados obtenidos",
            "(l) Incluye la propuesta de continuidad/ajuste a los prompts e instrucciones de "
            "generación de contenido con IA, considerando de los resultados de la campaña que concluyó",
            "(m) Tiene el calendario de publicación de contenidos para el siguiente periodo",
            "(n) Especifica los nuevos objetivos y métricas de seguimiento para el siguiente periodo",
            "(o) Contiene la evidencia de aprobación del plan de optimización por parte de la(s) "
            "persona(s) responsable(s) del marketing digital en la MiPyME",
        ],
        "caso": (
            "Campaña: septiembre 2025, 4 semanas. "
            "Resultados: Instagram +187 seguidores (meta: +200, -6.5%); "
            "Engagement rate promedio 4.2% (referencia mercado cafeterías: 2.8%); "
            "Alcance total: 8,420 personas. "
            "Mejor contenido: video Reel del origen del café (487 likes, 23 comentarios, 156 guardados). "
            "Peor contenido: imagen de menú con texto (12 likes, 0 comentarios). "
            "Patrón: el contenido educativo sobre café de especialidad tiene 3x más engagement que "
            "el contenido promocional directo. "
            "Plan de optimización: reducir posts de menú en un 50%, aumentar contenido educativo/"
            "origen del café, probar Reels de 30s (vs 15s actuales), publicar jueves 7pm en vez "
            "de viernes 6pm."
        ),
        "preguntas": [
            (
                "Periodo analizado y fuente de datos",
                "¿Cuándo fue la campaña que estás analizando? ¿Qué fuentes usaste para obtener "
                "los datos (Meta Insights, Google Analytics, Hootsuite)? ¿Con qué frecuencia los mediste?",
            ),
            (
                "Resumen ejecutivo",
                "En 3-5 líneas: ¿qué pasó en el periodo? ¿Qué lograste vs qué esperabas?",
            ),
            (
                "Métricas por publicación, tipo de contenido y plataforma",
                "Tabla completa: por cada publicación (o por tipo de contenido agrupado), muestra "
                "alcance, impresiones, interacciones, tasa de interacción y otros KPIs relevantes.",
            ),
            (
                "Comparativo contra objetivos de la estrategia",
                "¿Qué objetivos habías definido? ¿Los cumpliste, los superaste o quedaste por debajo? "
                "Tabla de objetivo vs resultado real.",
            ),
            (
                "Análisis de mejor y peor desempeño",
                "¿Qué publicaciones o tipos de contenido funcionaron mejor? ¿Cuáles funcionaron peor? "
                "¿Qué patrones de horario, formato o tema explican los resultados?",
            ),
            (
                "Capturas de pantalla o evidencias",
                "Adjunta o describe las capturas de las herramientas de analítica que respaldan "
                "los datos del reporte.",
            ),
            (
                "Recomendaciones de ajuste (tipos, formatos, frecuencia)",
                "Con base en los resultados: ¿qué tipos de contenido vas a continuar? "
                "¿Cuáles vas a eliminar o reducir? ¿Cambias la frecuencia?",
            ),
            (
                "Pruebas de optimización propuestas",
                "¿Qué pruebas A/B o multivariables propones para el siguiente periodo? "
                "Por cada una: qué hipótesis validas y con qué métrica.",
            ),
            (
                "Ajuste de horarios",
                "¿Cambias los horarios de publicación? ¿Por qué? ¿Qué datos respaldan el cambio?",
            ),
            (
                "Ajuste de segmentación y presupuesto",
                "¿Modificas la audiencia a la que llegas? ¿Ajustas el presupuesto de publicidad "
                "pagada? ¿Por qué?",
            ),
            (
                "Ajuste de prompts de IA",
                "¿Qué cambios harás en los prompts que usas para generar contenido? "
                "¿Qué aprendiste sobre qué tipos de prompts funcionan mejor para esta MiPyME?",
            ),
            (
                "Calendario del siguiente periodo",
                "Elabora el calendario de publicación para el siguiente mes o periodo.",
            ),
            (
                "Nuevos objetivos",
                "¿Qué objetivos y métricas defines para el siguiente periodo, basándote en lo aprendido?",
            ),
            (
                "Evidencia de aprobación",
                "¿Cómo documenta la persona responsable que aprobó el plan? "
                "Correo, firma, captura.",
            ),
        ],
    },
]


# ===========================================================================
# PLANTILLAS POR FORMATO
# (mismo sistema visual que los Estándares A y B; solo cambia la caja de caso
#  pedagógico y los textos de footer/subtitle)
# ===========================================================================

BASE_STYLES = """
@page {
  size: 21.59cm 27.94cm;
  margin: 2.2cm 1.8cm;
}
body {
  font-family: 'Calibri', 'Arial', sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #333;
}
.brand-header {
  border-bottom: 3pt solid #f7c031;
  padding-bottom: 10pt;
  margin-bottom: 18pt;
}
.brand-header table { width: 100%; border-collapse: collapse; }
.brand-header td { border: none; vertical-align: middle; padding: 0; }
.brand-block {
  background: #28467e;
  color: #f7c031;
  font-weight: bold;
  font-size: 13pt;
  padding: 12pt 8pt;
  text-align: center;
  border-radius: 6pt;
  width: 70pt;
}
.brand-header h1 { color: #28467e; font-size: 17pt; margin: 0 0 3pt 0; font-weight: bold; }
.brand-header .subtitle { color: #666; font-size: 10pt; margin: 0; }
.brand-header .meta { text-align: right; font-size: 9pt; color: #666; width: 130pt; }
.brand-header .meta strong { color: #28467e; font-size: 11pt; }

.product-data {
  background: #f5f9ff;
  border: 1pt solid #cce0f5;
  padding: 12pt 16pt;
  margin: 0 0 20pt 0;
  border-radius: 4pt;
}
.product-data table { width: 100%; border-collapse: collapse; }
.product-data td { padding: 4pt 8pt; font-size: 10pt; border: none; }
.product-data td:first-child { font-weight: bold; color: #28467e; width: 30%; }
.product-data .blank { border-bottom: 1pt solid #999; display: inline-block; min-width: 220pt; }

.intro {
  background: #FFF3CC;
  border-left: 4pt solid #f7c031;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  color: #555;
}

.f21-box {
  background: #f0f7ff;
  border-left: 4pt solid #1F4E8C;
  padding: 12pt 16pt 14pt;
  margin: 16pt 0;
  font-size: 10pt;
}
.f21-box h3 {
  margin: 0 0 8pt 0;
  font-size: 11pt;
  color: #28467e;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.f21-box ul { margin: 0; padding-left: 18pt; color: #333; }
.f21-box li { margin-bottom: 4pt; }

.caso-box {
  background: #fdf6e3;
  border: 1pt dashed #d4a40e;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  font-style: italic;
  color: #6a5208;
}
.caso-box strong { color: #28467e; font-style: normal; }

h2 {
  color: #28467e;
  font-size: 14pt;
  border-bottom: 1pt solid #f7c031;
  padding-bottom: 4pt;
  margin-top: 24pt;
  margin-bottom: 12pt;
}

.question-block {
  margin-bottom: 22pt;
  padding: 0 0 12pt 0;
  border-bottom: 1pt dotted #ddd;
}
.question-num {
  display: inline-block;
  background: #28467e;
  color: white;
  width: 22pt;
  height: 22pt;
  line-height: 22pt;
  text-align: center;
  border-radius: 50%;
  font-weight: bold;
  font-size: 11pt;
  margin-right: 8pt;
  vertical-align: middle;
}
.question-title {
  font-weight: bold;
  color: #28467e;
  font-size: 11.5pt;
}
.question-help {
  color: #666;
  font-size: 10pt;
  font-style: italic;
  margin: 6pt 0 8pt 30pt;
  line-height: 1.45;
}
.fill-area {
  border: 1pt dashed #ccc;
  background: #fafafa;
  padding: 22pt 16pt;
  margin: 6pt 0 0 30pt;
  min-height: 60pt;
  color: #aaa;
  font-style: italic;
  font-size: 10pt;
}

.footer {
  margin-top: 36pt;
  padding-top: 10pt;
  border-top: 1pt solid #ddd;
  font-size: 8pt;
  color: #999;
  text-align: center;
  font-style: italic;
}
"""

WORD_TEMPLATE = """<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:w="urn:schemas-microsoft-com:office:word"
      xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="ProgId" content="Word.Document">
<meta name="Generator" content="Microsoft Word">
<title>{num} · {title}</title>
<!--[if gte mso 9]>
<xml><w:WordDocument><w:View>Print</w:View><w:Zoom>100</w:Zoom><w:DoNotOptimizeForBrowser/></w:WordDocument></xml>
<![endif]-->
<style>{base_styles}</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;"><div class="brand-block">Mi<br>CompañIA</div></td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Manual de Marketing Digital con IA · Producto del Elemento {elemento}</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Template editable<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Tu evaluador no busca que llenes el template — busca que respondas con datos de TU MiPyME real. Las preguntas guía te orientan; las respuestas son tuyas.</div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Cafetería La Cuesta (ilustrativo, NO es tu solución):</strong> {caso}</div>

<div class="product-data">
<table>
<tr><td>MiPyME (razón social)</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Persona responsable</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Consultor responsable</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Fecha del documento</td><td><span class="blank">&nbsp;</span></td></tr>
</table>
</div>

<h2>Tu turno · preguntas guía</h2>

{questions_html}

<div class="footer">
Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org<br>
Template del Manual de Marketing Digital con IA · Para ser llenado por el aspirante con datos de su proyecto real con una MiPyME
</div>

</body>
</html>
"""

EXCEL_TEMPLATE = """<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:x="urn:schemas-microsoft-com:office:excel"
      xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="ProgId" content="Excel.Sheet">
<meta name="Generator" content="Microsoft Excel">
<title>{num} · {title}</title>
<!--[if gte mso 9]>
<xml><x:ExcelWorkbook><x:ExcelWorksheets>
<x:ExcelWorksheet><x:Name>{num}</x:Name><x:WorksheetOptions><x:Panes><x:Pane><x:Number>3</x:Number></x:Pane></x:Panes></x:WorksheetOptions></x:ExcelWorksheet>
</x:ExcelWorksheets></x:ExcelWorkbook></xml>
<![endif]-->
<style>{base_styles}
table.matrix {{ border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 10pt; }}
table.matrix th, table.matrix td {{ border: 1pt solid #999; padding: 6pt 8pt; vertical-align: top; }}
table.matrix th {{ background: #28467e; color: white; font-weight: bold; text-align: left; }}
table.matrix tr.score th {{ background: #f7c031; color: #28467e; }}
table.matrix td.fill {{ background: #fffbe6; min-height: 22pt; height: 22pt; color: #aaa; font-style: italic; }}
table.matrix tr:nth-child(even) td.fill {{ background: #fefbf0; }}
</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;"><div class="brand-block">Mi<br>CompañIA</div></td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Manual de Marketing Digital con IA · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Excel es el formato natural para esta clase de producto: te permite añadir filas conforme registres más publicaciones, ordenar por métricas y generar gráficas. <strong>Llénalo con datos de TU MiPyME real.</strong></div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Cafetería La Cuesta (ilustrativo):</strong> {caso}</div>

<div class="product-data">
<table>
<tr><td>MiPyME</td><td><span class="blank">&nbsp;</span></td><td>Fecha</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Consultor</td><td><span class="blank">&nbsp;</span></td><td>Responsable MiPyME</td><td><span class="blank">&nbsp;</span></td></tr>
</table>
</div>

<h2>Tu turno · preguntas guía</h2>

{questions_html}

{matrix_html}

<div class="footer">
Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org · Template del Manual de Marketing Digital con IA
</div>

</body>
</html>
"""


# ===========================================================================
# RENDERIZADORES
# ===========================================================================

def render_f21(criterios):
    """Genera la lista HTML de criterios F21 literales."""
    html = ""
    for c in criterios:
        html += f'<li>{c}</li>\n'
    return html


def render_questions_word(preguntas):
    """Genera los bloques de preguntas guía para templates Word."""
    html = ""
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<div class="question-block">\n'
            f'<div><span class="question-num">{i}</span>'
            f'<span class="question-title">{title}</span></div>\n'
            f'<div class="question-help">{help_text}</div>\n'
            f'<div class="fill-area">[Escribe aquí tu respuesta con datos reales de tu MiPyME. '
            f'Borra esta línea cuando empieces.]</div>\n'
            f'</div>\n'
        )
    return html


def render_questions_excel(preguntas):
    """Genera la tabla de preguntas guía para templates Excel."""
    html = (
        '<table class="matrix">\n'
        '<tr>'
        '<th style="width: 4%;">#</th>'
        '<th style="width: 28%;">Pregunta guía</th>'
        '<th>Tu respuesta (llena con datos de TU MiPyME)</th>'
        '</tr>\n'
    )
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<tr>\n'
            f'<td style="text-align: center; font-weight: bold; color: #28467e;">{i}</td>\n'
            f'<td><strong>{title}</strong><br>'
            f'<span style="color: #666; font-size: 9pt; font-style: italic;">{help_text}</span></td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    html += '</table>\n'
    return html


def render_matrix_extra(num):
    """
    Matrices estructuradas adicionales para el producto 4.1 (Excel).

    Genera tres tablas:
      - Hoja 1: métricas por publicación (10 filas)
      - Hoja 2: comparativo objetivo vs resultado (5 filas)
      - Hoja 3: calendario del siguiente periodo (7 semanas x 7 días)
    """

    # 4.1 · Reporte de desempeño y plan de optimización
    if num == "4.1":
        # --- Hoja 1: métricas por publicación ---
        metricas_rows = ""
        for i in range(1, 11):
            metricas_rows += (
                f'<tr>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Fecha
                f'<td class="fill">&nbsp;</td>\n'                              # Plataforma
                f'<td class="fill">&nbsp;</td>\n'                              # Tipo de contenido
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Alcance
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Impresiones
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Me gusta
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Comentarios
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Compartidos
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Guardados
                f'<td class="fill" style="text-align:center;color:#999;">=%</td>\n'  # Tasa interacción
                f'<td class="fill">&nbsp;</td>\n'                              # Estado
                f'</tr>\n'
            )

        # --- Hoja 2: comparativo objetivo vs resultado ---
        comparativo_rows = ""
        for i in range(1, 6):
            comparativo_rows += (
                f'<tr>\n'
                f'<td class="fill">&nbsp;</td>\n'                              # Objetivo
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Meta definida
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Resultado real
                f'<td class="fill" style="text-align:center;color:#999;">=%</td>\n'  # Variación %
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Cumplido S/N
                f'</tr>\n'
            )

        # --- Hoja 3: calendario del siguiente periodo (7 semanas x 7 días) ---
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        encabezado_dias = "".join(
            f'<th style="width: 12%;">{d}</th>' for d in dias
        )
        calendario_rows = ""
        for semana in range(1, 8):
            calendario_rows += f'<tr><td style="font-weight:bold;color:#28467e;text-align:center;background:#f0f7ff;">Semana {semana}</td>'
            for _ in dias:
                calendario_rows += '<td class="fill">&nbsp;</td>'
            calendario_rows += '</tr>\n'

        return f"""
<h2>Hoja 1 · Métricas por publicación</h2>
<p style="font-size: 10pt; color: #666;">
  Registra una fila por publicación. Añade filas según el volumen de tu campaña.
  La columna «Tasa de interacción %» se calcula como (Me gusta + Comentarios + Compartidos + Guardados) / Alcance × 100.
</p>
<table class="matrix">
<tr>
  <th style="width: 8%;">Fecha</th>
  <th style="width: 10%;">Plataforma</th>
  <th style="width: 14%;">Tipo de contenido</th>
  <th style="width: 7%;">Alcance</th>
  <th style="width: 8%;">Impresiones</th>
  <th style="width: 7%;">Me gusta</th>
  <th style="width: 8%;">Comentarios</th>
  <th style="width: 8%;">Compartidos</th>
  <th style="width: 8%;">Guardados</th>
  <th style="width: 10%;">Tasa de interacción %</th>
  <th>Estado</th>
</tr>
{metricas_rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:6pt;font-style:italic;">
  Fuente de datos recomendada: Meta Business Suite Insights / Google Analytics / herramienta de gestión de redes.
</p>

<h2>Hoja 2 · Comparativo objetivo vs resultado</h2>
<p style="font-size: 10pt; color: #666;">
  Registra cada objetivo que definiste en la estrategia aprobada y compáralo con el resultado real.
</p>
<table class="matrix">
<tr>
  <th style="width: 28%;">Objetivo</th>
  <th style="width: 18%;">Meta definida</th>
  <th style="width: 18%;">Resultado real</th>
  <th style="width: 12%;">Variación %</th>
  <th style="width: 12%;">Cumplido (S/N)</th>
</tr>
{comparativo_rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:6pt;font-style:italic;">
  Variación % = (Resultado real - Meta definida) / Meta definida × 100. Positivo = superado; negativo = por debajo.
</p>

<h2>Hoja 3 · Calendario del siguiente periodo</h2>
<p style="font-size: 10pt; color: #666;">
  Planifica el contenido del siguiente periodo. Por cada celda anota: plataforma / tipo de contenido / tema.
  Añade o elimina semanas según la duración del periodo planificado.
</p>
<table class="matrix">
<tr>
  <th style="width: 8%;">Semana</th>
  {encabezado_dias}
</tr>
{calendario_rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:6pt;font-style:italic;">
  Complementa este calendario con las fechas clave de temporada comercial definidas en la estrategia.
</p>
"""

    # Otros productos no tienen matriz extra
    return ""


def render_product(p):
    """Devuelve (contenido HTML, extensión de archivo)."""
    f21_html = render_f21(p["f21"])

    if p["format"] == "word":
        questions_html = render_questions_word(p["preguntas"])
        html = WORD_TEMPLATE.format(
            num=p["num"],
            title=p["title"],
            elemento=p["elemento"],
            intro=p["intro"],
            caso=p["caso"],
            f21_html=f21_html,
            questions_html=questions_html,
            base_styles=BASE_STYLES,
        )
        return html, "doc"

    elif p["format"] == "excel":
        questions_html = render_questions_excel(p["preguntas"])
        matrix_html = render_matrix_extra(p["num"])
        html = EXCEL_TEMPLATE.format(
            num=p["num"],
            title=p["title"],
            elemento=p["elemento"],
            intro=p["intro"],
            caso=p["caso"],
            f21_html=f21_html,
            questions_html=questions_html,
            matrix_html=matrix_html,
            base_styles=BASE_STYLES,
        )
        return html, "xls"

    raise ValueError(f"Formato desconocido: {p['format']}")


def main():
    # Limpiar archivos legacy con extensiones OOXML si los hubiera
    for ext in (".docx", ".xlsx"):
        for f in OUT.glob(f"*{ext}"):
            f.unlink()
            print(f"  [del legacy] {f.name}")
    for d in OUT.glob("*.files"):
        if d.is_dir():
            import shutil
            shutil.rmtree(d)
            print(f"  [del legacy dir] {d.name}")

    for p in PRODUCTS:
        content, ext = render_product(p)
        # Slug de archivo: usa el slug explícito del producto (ya tiene formato num-num-slug)
        filename = f"{p['slug']}.{ext}"
        filepath = OUT / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")

    print(f"\nGenerados {len(PRODUCTS)} templates en {OUT}/")


if __name__ == "__main__":
    main()
