#!/usr/bin/env python3
"""
Genera las 10 plantillas de los productos del EC1848 · Prestación de servicios de
consultoría en mercadotecnia digital con Inteligencia Artificial en la MiPyME (Ruta C).

- 9 Word (.doc) como HTML estilizado con MIME Office
- 1 Excel (.xls) como HTML estilizado con MIME Office (el reporte 4.1, que calcula)

convert-legacy-office.py las convierte después a .docx/.xlsx reales.

Caso pedagógico: Cafetería La Cuesta, café de especialidad en zona universitaria que
tuesta su propio café (6 empleados). Mariana, dueña y fundadora, es la persona
responsable de la mercadotecnia digital; Martín es el consultor. Los datos del caso
salen de la ficha única del caso del curso y no se inventan aquí.

Filosofía pedagógica: no darle la solución al aspirante. Cada plantilla muestra:
  (1) los criterios literales del EC1848 publicado en el DOF (28-oct-2026)
  (2) un ejemplo breve del caso La Cuesta (solo ilustrativo)
  (3) preguntas guía que el aspirante responde con los datos de la MiPyME con la
      que trabaja

Los criterios se copian tal cual del EC; solo se quitan la coma y la «y»/«e» con que
el EC encadena cada criterio con el siguiente, porque aquí van en lista con letra.

Uso:
    python -X utf8 scripts/generate-templates-c.py

Salida: estandar-c/templates/<num_con_guiones>-<slug>.{docx|xlsx}
"""

from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-c" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

EC = "EC1848"

PRODUCTS = [
    # -----------------------------------------------------------------------
    # ELEMENTO 1 · E5881 · PLANIFICAR
    # -----------------------------------------------------------------------
    {
        "num": "1.1",
        "slug": "1-1-expediente-informacion",
        "format": "word",
        "elemento": "1 · E5881",
        "title": "El expediente de información clave de la MiPyME, documentado",
        "intro": (
            "Es el punto de partida del servicio: reúne lo que necesitas saber de la MiPyME "
            "antes de diseñar la estrategia. Perfil empresarial, persona responsable de la "
            "mercadotecnia digital, productos o servicios a promover, metas comerciales, "
            "plataformas y métricas actuales, análisis del contenido existente, audiencia "
            "objetivo y el acuerdo de confidencialidad firmado."
        ),
        "criterios": [
            "(a) Contiene el perfil empresarial incluyendo: el nombre de la empresa/marca comercial, giro, misión, visión, valores y ubicación",
            "(b) Incluye los datos de contacto de la persona responsable de la mercadotecnia digital en la MiPyME: nombre, cargo, correo electrónico y teléfono",
            "(c) Incluye el listado de productos/servicios a promover a través de la mercadotecnia digital",
            "(d) Especifica las metas comerciales por un periodo de tiempo considerando volumen de ventas/medio de captación de clientes",
            "(e) Incluye el listado de plataformas digitales en los que tiene presencia actual la MiPyME",
            "(f) Contiene descritas y organizadas por tipo las métricas de presencia digital con las que cuenta la MiPyME",
            "(g) Cuenta con el análisis del contenido existente, especificando tipo, frecuencia y nivel de interacción por cada plataforma digital",
            "(h) Contiene descrito el perfil de la audiencia objetivo, considerando al menos tres variables de segmentación: características demográficas, intereses y comportamiento digital",
            "(i) Tiene el acuerdo de confidencialidad firmado por la persona responsable de la información y el proveedor de servicios",
        ],
        "caso": (
            "Cafetería La Cuesta: café de especialidad en zona universitaria, México; tuesta su "
            "propio café y tiene 6 empleados. Responsable de la mercadotecnia digital: Mariana, "
            "dueña y fundadora desde hace 7 años (en el expediente van su cargo, correo y "
            "teléfono). Plataformas con presencia actual: Instagram, con 1,240 seguidores y "
            "publicaciones irregulares, cuando «hay tiempo»; WhatsApp Business, que a veces "
            "atiende Sonia, la empleada de turno, y Google My Business, sin actualizar desde que "
            "cambiaron el horario hace dos años. No había misión escrita, ni perfil de audiencia, "
            "ni lineamientos de tono o de colores: el expediente es el primer lugar donde quedan "
            "por escrito. Audiencia objetivo: universitarios de 18 a 25 años que buscan un lugar "
            "para estudiar o reunirse. Reto comercial: atraer al público universitario y "
            "posicionar el café de especialidad frente a las cadenas."
        ),
        "preguntas": [
            (
                "Perfil empresarial",
                "Escribe el nombre de la empresa o marca comercial, su giro, misión, visión, "
                "valores y ubicación. Si la MiPyME no tiene misión, visión o valores por escrito, "
                "redáctalos con la persona responsable y anota que los acordaron juntos.",
            ),
            (
                "Persona responsable de la mercadotecnia digital",
                "Nombre, cargo, correo electrónico y teléfono de la persona responsable de la "
                "mercadotecnia digital en la MiPyME con la que trabajas.",
            ),
            (
                "Productos o servicios a promover",
                "¿Qué productos o servicios va a promover la MiPyME con la mercadotecnia digital? "
                "Haz el listado con una descripción breve de cada uno.",
            ),
            (
                "Metas comerciales",
                "¿Qué quiere lograr la MiPyME y en qué periodo? Exprésalo en volumen de ventas o "
                "en el medio por el que capta a sus clientes, por ejemplo pedidos por mensajería "
                "o visitas al local.",
            ),
            (
                "Plataformas digitales con presencia actual",
                "Haz el listado de las plataformas digitales donde la MiPyME tiene presencia hoy: "
                "redes sociales, mensajería, ficha de negocio, sitio web o tienda en línea.",
            ),
            (
                "Métricas de presencia digital, organizadas por tipo",
                "Agrupa por tipo las métricas con las que cuenta la MiPyME: comunidad (seguidores, "
                "contactos), alcance e impresiones, interacción y conversión (clics, mensajes, "
                "pedidos). Anota la plataforma y la fecha de cada dato.",
            ),
            (
                "Análisis del contenido existente",
                "Por cada plataforma: ¿qué tipo de contenido publica la MiPyME, con qué "
                "frecuencia y qué nivel de interacción tiene?",
            ),
            (
                "Perfil de la audiencia objetivo",
                "¿A quién quiere llegar la MiPyME? Descríbelo con al menos tres variables de "
                "segmentación: características demográficas, intereses y comportamiento digital.",
            ),
            (
                "Acuerdo de confidencialidad",
                "¿Quién firmó el acuerdo de confidencialidad por parte de la MiPyME y en qué "
                "fecha? Anexa el acuerdo firmado por la persona responsable de la información y "
                "por ti, como proveedor de servicios.",
            ),
        ],
    },
    {
        "num": "1.2",
        "slug": "1-2-estrategia-contenido",
        "format": "word",
        "elemento": "1 · E5881",
        "title": "La estrategia de contenido de mercadotecnia digital de la MiPyME utilizando IA, diseñada",
        "intro": (
            "Define cómo va a comunicar la MiPyME en sus plataformas digitales durante al menos "
            "cuatro semanas: voz y tono de la marca, contenido por etapa del embudo de ventas, "
            "tabla de análisis por plataforma, horarios, temporadas, objetivos medibles, "
            "presupuesto y la evidencia de que la persona responsable la aprobó."
        ),
        "criterios": [
            "(a) Especifica la definición de la voz y personalidad de marca para el contenido digital",
            "(b) Incluye los lineamientos de tono y estilo por plataforma digital",
            "(c) Precisa los tipos de contenido digital de texto/imagen/audio/video recomendados por etapa del embudo de ventas de acuerdo con la información clave recabada en el levantamiento",
            "(d) Contiene la tabla de análisis conformada por: la justificación de la(s) plataforma(s) digital(es) a utilizar por audiencia, el tipo de formato con especificaciones técnicas, las herramientas/plataformas de IA recomendadas por tipo de contenido digital y la frecuencia de publicación acorde a la capacidad operativa",
            "(e) Indica los horarios de publicación sugeridos por plataforma digital conforme a las recomendaciones de la IA y a los hábitos del público objetivo",
            "(f) Incluye la vinculación a las temporadas comerciales relevantes para el sector del negocio",
            "(g) Especifica la distribución de los tipos de contenido digital a lo largo del periodo, considerando al menos cuatro semanas de planificación",
            "(h) Incluye al menos dos objetivos medibles vinculados al negocio y sus respectivas métricas de seguimiento",
            "(i) Incluye el presupuesto/monto de inversión requerido de implementación, de acuerdo con las necesidades de la MiPyME",
            "(j) Contiene la evidencia de aprobación de la estrategia de mercadotecnia digital planteada por parte de la persona responsable de la mercadotecnia digital en la MiPyME",
        ],
        "caso": (
            "Mariana eligió la ruta con Instagram y WhatsApp Business porque le importa el "
            "cliente que regresa. Distribución de 4 semanas: Reels del proceso de tueste en "
            "Instagram los lunes y jueves; posts estáticos de producto los martes; carruseles "
            "educativos sobre café de especialidad los viernes, y mensajes de difusión en "
            "WhatsApp Business cada semana. Herramientas: una herramienta de IA generativa de "
            "texto, una de imagen, una de audio y una de video, según el tipo de contenido. "
            "Temporadas vinculadas: regreso a clases, Día de Muertos, temporada navideña y Día "
            "de las Madres. Objetivos medibles: subir 20 % la interacción en Instagram y sumar "
            "50 contactos nuevos a la lista de WhatsApp, cada uno con su métrica y su "
            "presupuesto. Mariana pidió bajar la frecuencia en temporada alta a dos "
            "publicaciones más una historia; Martín ajustó la estrategia, ella firmó la hoja de "
            "aprobación y él se la envió también por correo."
        ),
        "preguntas": [
            (
                "Voz y personalidad de marca",
                "¿Cómo habla la marca y qué personalidad quiere transmitir en su contenido "
                "digital? Defínela con tres o cuatro rasgos y escribe una frase que la marca sí "
                "diría y otra que no.",
            ),
            (
                "Tono y estilo por plataforma",
                "¿Cómo se ajustan el tono y el estilo en cada plataforma digital que vas a usar? "
                "Escribe los lineamientos de cada una.",
            ),
            (
                "Tipos de contenido por etapa del embudo de ventas",
                "Con base en el expediente, ¿qué tipos de contenido de texto, imagen, audio o "
                "video recomiendas para cada etapa del embudo: reconocimiento, consideración, "
                "compra y fidelización?",
            ),
            (
                "Tabla de análisis por plataforma",
                "Llena la «Tabla de análisis por plataforma» al final de esta plantilla: por qué "
                "usar cada plataforma con esa audiencia, el formato con sus especificaciones "
                "técnicas, la herramienta de IA por tipo de contenido y la frecuencia que la "
                "MiPyME puede sostener. Aquí anota lo que no quepa en la tabla.",
            ),
            (
                "Horarios de publicación",
                "¿Qué horarios sugieres en cada plataforma? Explica cómo combinaste la "
                "recomendación de la IA con los hábitos de la audiencia objetivo.",
            ),
            (
                "Temporadas comerciales",
                "¿Qué temporadas comerciales son relevantes para el sector de la MiPyME y qué "
                "contenido se vincula con cada una?",
            ),
            (
                "Distribución del contenido en al menos cuatro semanas",
                "Llena la tabla «Distribución del contenido» al final de esta plantilla, semana "
                "por semana: día, plataforma, tipo de contenido y tema.",
            ),
            (
                "Objetivos medibles",
                "Escribe al menos dos objetivos medibles vinculados al negocio, cada uno con su "
                "métrica de seguimiento.",
            ),
            (
                "Presupuesto o monto de inversión",
                "¿Cuánto se requiere invertir para implementar la estrategia? Desglosa "
                "herramientas de IA, promoción pagada y otros costos, de acuerdo con las "
                "necesidades de la MiPyME.",
            ),
            (
                "Evidencia de aprobación",
                "¿Cómo queda documentada la aprobación de la persona responsable de la "
                "mercadotecnia digital? Usa la tabla «Aprobación de la estrategia» o anexa el "
                "correo o mensaje con que la aprobó.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 2 · E5882 · GENERAR
    # -----------------------------------------------------------------------
    {
        "num": "2.1",
        "slug": "2-1-portafolio-texto",
        "format": "word",
        "elemento": "2 · E5882",
        "title": "El contenido de texto del portafolio de mercadotecnia digital generado con IA, documentado",
        "intro": (
            "Documenta una pieza de texto generada con IA: la herramienta y por qué la elegiste, "
            "la estructura del prompt, la versión final para la plataforma de destino y cómo "
            "cumple los criterios de calidad, redacción, beneficios y llamado a la acción."
        ),
        "criterios": [
            "(a) Especifica la herramienta de IA utilizada para la generación contenido de texto y la justificación de su elección",
            "(b) Incluye la estructura del prompt/contenido de referencia para generación de contenido de texto que incluya al menos el rol, el contexto, la tarea, la audiencia, el formato, el tono de comunicación y las restricciones",
            "(c) Contiene la versión final del texto generada con apoyo de la herramienta/plataforma de IA para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a coherencia con la marca, así como congruencia con la estrategia de mercadotecnia digital aprobada",
            "(e) Está redactado de forma clara, precisa y con apego a reglas de redacción y ortografía",
            "(f) Contiene los beneficios y llamados a la acción",
            "(g) Se adapta al formato de la(s) plataforma(s) digital(es) de destino",
        ],
        "caso": (
            "Herramienta: una herramienta de IA generativa de texto, elegida porque redacta en "
            "español con el tono de la estrategia y permite iterar el prompt. Prompt: «Rol: eres "
            "redactor de mercadotecnia digital de una cafetería de especialidad. Contexto: "
            "Cafetería La Cuesta, en zona universitaria, tuesta su propio café. Tarea: escribe el "
            "texto del carrusel educativo del viernes sobre qué es el café de especialidad. "
            "Audiencia: universitarios de 18 a 25 años que buscan un lugar para estudiar o "
            "reunirse. Formato: texto para Instagram de máximo 120 palabras, con los hashtags de "
            "la cafetería. Tono: cálido, cercano y claro. Restricciones: sin datos de origen que "
            "no estén verificados y sin mencionar a otras marcas.» Iteración: la primera versión "
            "sonaba a anuncio; Martín pidió frases más cortas y una invitación a pasar a "
            "estudiar. Versión final (inicio): «¿Qué hace especial a un café de especialidad? "
            "Empieza en cómo se tuesta, y en La Cuesta lo tostamos aquí mismo.» El mensaje se "
            "adaptó después como texto breve para la difusión semanal de WhatsApp Business."
        ),
        "preguntas": [
            (
                "Herramienta de IA y por qué la elegiste",
                "¿Qué herramienta de IA usaste para generar el texto y por qué es la adecuada "
                "para este contenido?",
            ),
            (
                "Estructura del prompt",
                "Escribe el prompt completo, o el contenido de referencia, con al menos rol, "
                "contexto, tarea, audiencia, formato, tono de comunicación y restricciones.",
            ),
            (
                "Versión final del texto",
                "Copia la versión final, ya revisada, e indica para qué plataforma digital es. "
                "Anota qué cambiaste entre la primera versión y la final.",
            ),
            (
                "Coherencia con la marca y con la estrategia aprobada",
                "¿Cómo comprobaste que el texto respeta la voz de la marca y lo que pide la "
                "estrategia aprobada?",
            ),
            (
                "Redacción y ortografía",
                "¿Revisaste que el texto sea claro, preciso y sin faltas? Anota qué corregiste.",
            ),
            (
                "Beneficios y llamados a la acción",
                "¿Qué beneficio comunica el texto y cuál es su llamado a la acción?",
            ),
            (
                "Adaptación al formato de la plataforma",
                "¿Cómo adaptaste el texto a cada plataforma de destino: extensión, hashtags, "
                "enlaces y saltos de línea?",
            ),
        ],
    },
    {
        "num": "2.2",
        "slug": "2-2-portafolio-imagen",
        "format": "word",
        "elemento": "2 · E5882",
        "title": "El contenido de imagen del portafolio de mercadotecnia digital generado con IA, documentado",
        "intro": (
            "Documenta una imagen generada con IA: la herramienta y su justificación, el prompt "
            "o la imagen de referencia, la versión final y la revisión de coherencia visual, "
            "anatómica y física, de congruencia con la realidad y de relación de aspecto."
        ),
        "criterios": [
            "(a) Especifica la herramienta de IA utilizada para la generación del contenido de imagen y la justificación de su elección",
            "(b) Incluye la estructura del prompt/imagen de referencia para la generación de contenido de imagen",
            "(c) Contiene la versión final de imagen generada con la herramienta/plataforma de IA para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a la coherencia visual con la marca, coherencia anatómica y física",
            "(e) Es congruente con el requerimiento y el contexto/realidad",
            "(f) Tiene la relación de aspecto acorde con la(s) plataforma(s) digital(es) de destino",
        ],
        "caso": (
            "Herramienta: una herramienta de IA generativa de imagen, elegida porque acepta una "
            "foto de referencia y genera en formato cuadrado. Prompt: «Fotografía de producto: "
            "taza de café de especialidad sobre una barra de madera, luz cálida de mañana, granos "
            "recién tostados al fondo, estilo natural, formato cuadrado 1:1, sin texto y sin "
            "logotipos de otras marcas.» Imagen final: cuadrada de 1080 × 1080 para el post de "
            "producto de los martes en Instagram. Revisión: proporciones de la taza y del plato, "
            "vapor y reflejos creíbles, y nada que La Cuesta no venda. En el Elemento 4, estos "
            "posts sin persona fueron los de menor alcance, y el plan ajustó el prompt para "
            "incluir personas."
        ),
        "preguntas": [
            (
                "Herramienta de IA y por qué la elegiste",
                "¿Qué herramienta de IA usaste para generar la imagen y por qué es la adecuada "
                "para el tipo de imagen que pide la estrategia?",
            ),
            (
                "Prompt o imagen de referencia",
                "Escribe el prompt completo, con sujeto, estilo, formato y restricciones, o "
                "describe la imagen de referencia que usaste.",
            ),
            (
                "Versión final de la imagen",
                "Inserta la imagen final o su enlace e indica la plataforma digital de destino.",
            ),
            (
                "Coherencia visual, anatómica y física",
                "¿La imagen respeta los colores y el estilo de la marca? ¿Revisaste manos, "
                "rostros, objetos, sombras y reflejos? Anota qué corregiste.",
            ),
            (
                "Congruencia con el requerimiento y con la realidad",
                "¿La imagen muestra lo que pidió la estrategia y algo que la MiPyME sí ofrece, "
                "sin nada que pueda confundir al cliente?",
            ),
            (
                "Relación de aspecto",
                "¿Qué relación de aspecto usaste y por qué corresponde a la plataforma de "
                "destino? Por ejemplo, 1:1 para una publicación cuadrada y 9:16 para historias y "
                "Reels.",
            ),
        ],
    },
    {
        "num": "2.3",
        "slug": "2-3-portafolio-audio",
        "format": "word",
        "elemento": "2 · E5882",
        "title": "El contenido de audio del portafolio de mercadotecnia digital generado con IA, documentado",
        "intro": (
            "Documenta un audio generado con IA, de narración por voz o de música: la "
            "herramienta y su justificación, el prompt o los parámetros, la versión final y la "
            "revisión de claridad, dicción, ritmo, naturalidad y coherencia con la marca."
        ),
        "criterios": [
            "(a) Especifica la herramienta de IA utilizada para la generación del contenido de audio, y la justificación de su elección",
            "(b) Incluye el prompt/los parámetros de contenido de audio de narración por voz/música en la herramienta de IA elegida",
            "(c) Contiene la versión final de audio generada con la herramienta/plataforma de IA para la(s) plataforma(s) digital(es) de destino",
            "(d) Cumple con los criterios de calidad en cuanto a la claridad de voz/sonido, dicción/ritmo y la naturalidad de voz/sonido",
            "(e) Tiene coherencia con la marca",
        ],
        "caso": (
            "Herramienta: una herramienta de IA generativa de audio con voces en español de "
            "México, elegida porque deja ajustar ritmo, tono y emoción. Parámetros: narración por "
            "voz, tono cálido, ritmo pausado, 15 segundos, sin música con derechos de autor. "
            "Guion: «En La Cuesta tostamos nuestro propio café. Ven a estudiar, a platicar o nada "
            "más a probarlo.» Uso: narración para las Stories de Instagram. Revisión: Martín la "
            "escuchó en el celular, con y sin audífonos; en la segunda generación ajustó el ritmo "
            "para que el nombre de la cafetería se entendiera bien."
        ),
        "preguntas": [
            (
                "Herramienta de IA y por qué la elegiste",
                "¿Qué herramienta de IA usaste para generar el audio y por qué es la adecuada "
                "para narración por voz o para música, según lo que pide la estrategia?",
            ),
            (
                "Prompt o parámetros",
                "Escribe el prompt o los parámetros que configuraste: tipo de voz, guion, "
                "género, tono, ritmo, emoción, letra, duración y restricciones, según aplique.",
            ),
            (
                "Versión final del audio",
                "Anexa el archivo o su enlace e indica la plataforma de destino, el uso y la "
                "duración.",
            ),
            (
                "Claridad, dicción, ritmo y naturalidad",
                "¿Cómo verificaste la claridad de la voz o del sonido, la dicción y el ritmo, y "
                "que suene natural? Anota qué ajustaste entre una generación y otra.",
            ),
            (
                "Coherencia con la marca",
                "¿Por qué la voz o la música corresponden a la personalidad de la marca?",
            ),
        ],
    },
    {
        "num": "2.4",
        "slug": "2-4-portafolio-video",
        "format": "word",
        "elemento": "2 · E5882",
        "title": "El contenido de video del portafolio de mercadotecnia digital generado con IA, documentado",
        "intro": (
            "Documenta un video generado con IA: la herramienta y su justificación, el prompt o "
            "la referencia, la versión final y la revisión de narrativa, consistencia entre "
            "escenas, calidad técnica, audio, originalidad y coherencia con la marca."
        ),
        "criterios": [
            "(a) Especifica la herramienta de IA utilizada para la generación de contenido de video, y la justificación de su elección",
            "(b) Incluye la estructura del prompt/video/imagen de referencia para la generación de contenido de imagen",
            "(c) Contiene la versión final de video generada con la herramienta/plataforma de IA para la(s) plataforma(s) digital(es) de destino",
            "(d) Tiene coherencia narrativa con inicio, desarrollo y cierre definidos, así como claridad del mensaje e inclusión de llamado a la acción",
            "(e) Tiene consistencia visual y física de los elementos entre escenas y coherencia con la identidad de la marca",
            "(f) Cumple con la calidad técnica con respecto a la resolución, formato y duración adecuados a la plataforma digital",
            "(g) Tiene calidad de audio con respecto a la pronunciación/entonación/sonido(s) y claridad",
            "(h) Cumple con los criterios de calidad en cuanto a originalidad y coherencia con la marca",
        ],
        "caso": (
            "Herramienta: una herramienta de IA generativa de video, elegida porque genera clips "
            "verticales a partir de imágenes de referencia. Prompt por escena: inicio, granos "
            "cayendo en el tostador con luz cálida; desarrollo, el café recién tostado "
            "enfriándose en la charola; cierre, una taza servida en la barra con el texto "
            "«Tostado aquí, en La Cuesta» y el llamado a la acción «Ven a probarlo». Video final: "
            "Reel vertical 9:16 de 1080 × 1920 y 15 segundos, para Instagram los lunes y jueves. "
            "Audio: narración generada con IA, sin música con derechos de autor. Revisión: en la "
            "primera versión el tostador cambiaba de forma entre escenas; con una segunda "
            "iteración del prompt quedó consistente."
        ),
        "preguntas": [
            (
                "Herramienta de IA y por qué la elegiste",
                "¿Qué herramienta de IA usaste para generar el video y por qué es la adecuada "
                "para el tipo de video que pide la estrategia?",
            ),
            (
                "Prompt o referencia",
                "Escribe el prompt por escena (escena, sujeto, ambiente, estilo visual, "
                "iluminación, duración, restricciones y formato) e indica si usaste video o "
                "imagen de referencia.",
            ),
            (
                "Versión final del video",
                "Anexa el video o su enlace e indica la plataforma digital de destino.",
            ),
            (
                "Coherencia narrativa",
                "¿Cuál es el inicio, el desarrollo y el cierre? ¿Qué mensaje queda claro y dónde "
                "está el llamado a la acción?",
            ),
            (
                "Consistencia visual y física entre escenas",
                "¿Los objetos, las personas y los colores se mantienen entre escenas y respetan "
                "la identidad de la marca? Anota qué corregiste.",
            ),
            (
                "Calidad técnica",
                "¿La resolución, el formato y la duración corresponden a la plataforma de "
                "destino?",
            ),
            (
                "Calidad de audio",
                "¿La pronunciación, la entonación, los sonidos y la claridad del audio son "
                "correctos?",
            ),
            (
                "Originalidad y coherencia con la marca",
                "¿Cómo verificaste que el video es original, que no usa contenido de terceros "
                "sin permiso y que es coherente con la marca?",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 3 · E5883 · IMPLEMENTAR
    # -----------------------------------------------------------------------
    {
        "num": "3.1",
        "slug": "3-1-bitacora-implementacion",
        "format": "word",
        "elemento": "3 · E5883",
        "title": "La bitácora de implementación del contenido de mercadotecnia digital en plataformas digitales, documentada",
        "intro": (
            "Registro de la implementación en las plataformas digitales de la MiPyME: cada "
            "publicación con su fecha, hora, plataforma, tipo de contenido y estado, sus "
            "capturas o enlaces, las especificaciones técnicas aplicadas, las incidencias y "
            "ajustes, y la evidencia de las herramientas de medición."
        ),
        "criterios": [
            "(a) Contiene el listado de publicaciones realizadas con fecha, hora, plataforma(s) digital(es), tipo de contenido y estado de publicación: publicado/programado/rechazado",
            "(b) Incluye las capturas de pantalla/enlaces de verificación de cada publicación realizada",
            "(c) Indica la descripción de las especificaciones técnicas de cada medio utilizado conforme a la estrategia de mercadotecnia digital",
            "(d) Contiene el registro de incidencias técnicas/rechazos de plataforma(s) digital(es) y los ajustes realizados durante la implementación",
            "(e) Incluye la evidencia gráfica de las herramientas de medición y seguimiento en cada plataforma digital utilizada",
        ],
        "caso": (
            "Semana 1 en Instagram y WhatsApp Business: lunes, Reel del proceso de tueste para "
            "las 12:00, el horario de mayor tráfico en el campus → publicado; martes, post "
            "estático de producto en imagen cuadrada de 1080 × 1080 → programado; viernes, "
            "carrusel educativo → programado; mensaje de difusión semanal en WhatsApp Business "
            "→ publicado. Cada fila lleva su captura o su enlace. Incidencia y ajuste: Mariana "
            "quería publicar el Reel sin configurar los UTM del enlace al menú en línea; Martín le "
            "explicó para qué sirven, los configuraron juntos y el Reel salió un poco después de "
            "las 12:00, ya con seguimiento. Publicaciones promocionadas: 18 a 35 años, 5 km a la "
            "redonda, intereses en café de especialidad y postres artesanales, 200 pesos diarios. "
            "Evidencia de medición: capturas de las estadísticas de Instagram y de la lista de "
            "difusión de WhatsApp Business."
        ),
        "preguntas": [
            (
                "Listado de publicaciones",
                "Por cada publicación: fecha, hora, plataforma digital, tipo de contenido y "
                "estado (publicado, programado o rechazado).",
            ),
            (
                "Capturas de pantalla o enlaces de verificación",
                "Inserta la captura o el enlace que confirma cada publicación realizada.",
            ),
            (
                "Especificaciones técnicas de cada medio",
                "¿Qué especificaciones técnicas aplicaste en cada medio, según la estrategia: "
                "dimensiones, relación de aspecto, formato de archivo, peso y duración?",
            ),
            (
                "Incidencias, rechazos y ajustes",
                "¿Qué incidencias técnicas o rechazos tuviste en cada plataforma y qué ajuste "
                "hiciste en cada caso?",
            ),
            (
                "Evidencia gráfica de las herramientas de medición y seguimiento",
                "Inserta las capturas de las herramientas de medición configuradas en cada "
                "plataforma: estadísticas de la plataforma, enlaces con UTM, píxeles de "
                "seguimiento o vinculación con herramientas analíticas.",
            ),
        ],
    },
    {
        "num": "3.2",
        "slug": "3-2-guia-operativa",
        "format": "word",
        "elemento": "3 · E5883",
        "title": "La guía operativa de publicación para la MiPyME, documentada",
        "intro": (
            "Es la guía que queda en manos de la MiPyME para publicar por su cuenta: el "
            "procedimiento paso a paso por plataforma, las especificaciones técnicas de "
            "formato, los horarios recomendados, las restricciones y políticas de contenido, y "
            "los accesos a las herramientas de programación y gestión de redes. Debe ser tan "
            "clara que la persona responsable la siga sin llamarte."
        ),
        "criterios": [
            "(a) Contiene el procedimiento paso a paso de carga, programación y publicación de contenido por cada plataforma digital activa de la MiPyME",
            "(b) Incluye las especificaciones técnicas de formato por cada plataforma digital activa de la MiPyME",
            "(c) Enlista los horarios recomendados de publicación por cada plataforma digital activa de la MiPyME conforme a la estrategia",
            "(d) Contiene descritas las restricciones y políticas de contenido de cada plataforma digital activa de la MiPyME",
            "(e) Incluye los accesos y credenciales de las herramientas de programación y gestión de redes utilizadas",
        ],
        "caso": (
            "Procedimiento para Instagram: crear la publicación, elegir el tipo (post, carrusel, "
            "Reel o historia), cargar el archivo, pegar el texto complementario con los hashtags "
            "de la cafetería, revisar la vista previa y programar fecha y hora; en las "
            "promocionadas, segmentación de 18 a 35 años a 5 km a la redonda, con intereses en "
            "café de especialidad y postres artesanales, y 200 pesos diarios. Para WhatsApp "
            "Business: cómo preparar y enviar el mensaje de difusión semanal. Horario: los Reels "
            "a las 12:00, cuando hay más tráfico en el campus. Revisión previa: imagen cuadrada "
            "de 1080 × 1080 y texto complementario sin faltas. Políticas: nada de música con "
            "derechos de autor sin permiso, imágenes explícitas ni concursos sin reglas claras; "
            "la foto de un cliente con su perrito, solo con su permiso. Métricas: a las 24 horas, "
            "en «Estadísticas», revisar alcance e interacciones. Martín habilitó a Mariana con la "
            "guía en la mano y se la entregó impresa y en digital, con capturas."
        ),
        "preguntas": [
            (
                "Procedimiento paso a paso por plataforma",
                "Para cada plataforma activa de la MiPyME, escribe los pasos para cargar, "
                "programar y publicar contenido. Que alguien sin experiencia los pueda seguir.",
            ),
            (
                "Especificaciones técnicas de formato por plataforma",
                "Por cada plataforma y tipo de contenido: dimensiones, relación de aspecto, "
                "formato de archivo, peso máximo y duración.",
            ),
            (
                "Horarios recomendados de publicación",
                "Por cada plataforma: días y horas recomendados, tal como quedaron en la "
                "estrategia.",
            ),
            (
                "Restricciones y políticas de contenido",
                "¿Qué contenido restringe o rechaza cada plataforma activa de la MiPyME? "
                "Describe las políticas que más pueden afectar a este negocio.",
            ),
            (
                "Accesos y credenciales",
                "Haz el listado de las herramientas de programación y gestión de redes, con el "
                "usuario o correo de acceso y quién lo administra. Acuerda con la MiPyME una "
                "forma segura de entregar las contraseñas, por ejemplo un anexo que se entrega "
                "aparte, y anota en la guía dónde quedan.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 4 · E5884 · OPTIMIZAR
    # -----------------------------------------------------------------------
    {
        "num": "4.1",
        "slug": "4-1-reporte-desempeno",
        "format": "excel",
        "elemento": "4 · E5884",
        "title": "El reporte de desempeño del contenido publicado de mercadotecnia digital, documentado",
        # Corta a propósito: en Excel va en una celda de alto fijo de la hoja «Guía».
        "intro": (
            "Documenta los resultados de una campaña concluida: resumen ejecutivo, métricas por "
            "publicación, tipo y plataforma, comparativo contra la línea base y los objetivos, "
            "mayor y menor rendimiento, evidencias y fuente de los datos."
        ),
        "criterios": [
            "(a) Está elaborado a partir de una campaña de mercadotecnia digital concluida",
            "(b) Tiene el resumen ejecutivo con los principales resultados alcanzados en el periodo analizado y su relación con los objetivos de la estrategia",
            "(c) Incluye las métricas de rendimiento por publicación, por tipo de contenido y por plataforma digital, así como el comparativo respecto a la línea base de la MiPyME/indicadores de referencia de mercado",
            "(d) Especifica el comparativo de resultados contra los objetivos medibles establecidos en la estrategia aprobada",
            "(e) Contiene el análisis de mayor y menor rendimiento de los contenidos por tipo, formato, horario y plataforma digital, con la identificación de patrones de comportamiento y metas establecidas",
            "(f) Incluye las capturas de pantalla/evidencias de los datos reportados por las herramientas de medición y seguimiento de las plataformas digitales",
            "(g) Especifica la fecha del periodo de análisis, la fuente de los datos presentados y la frecuencia de medición",
        ],
        # También corta: la celda del caso en la hoja «Guía» mide 72 pt fijos (unas 5
        # líneas); con más texto, Excel la recorta.
        "caso": (
            "4 semanas en Instagram y WhatsApp Business. Alcance: 11,000 personas. Interacción: "
            "+23 % (meta 20 %). Contactos nuevos en WhatsApp: 68 (meta 50). Reels del tueste: 5 "
            "veces el alcance de los posts estáticos. Carrusel educativo: la tasa de interacción "
            "más alta (4.8 %). Sábados a mediodía, mejor que martes; posts de producto sin "
            "persona, lo más bajo. WhatsApp: 78 % de apertura y CTR al menú bajo."
        ),
        "preguntas": [
            (
                "Campaña concluida",
                "¿Qué campaña concluida analizas? Plataformas, fecha de inicio y fecha de cierre.",
            ),
            (
                "Resumen ejecutivo",
                "En pocas líneas: los principales resultados del periodo y su relación con los "
                "objetivos de la estrategia.",
            ),
            (
                "Métricas por publicación, tipo de contenido y plataforma",
                "Llena las hojas «Métricas por publicación» y «Resumen por tipo y plataforma», "
                "con el comparativo contra la línea base de la MiPyME o contra indicadores de "
                "referencia de mercado.",
            ),
            (
                "Comparativo contra los objetivos de la estrategia",
                "Llena la hoja «Objetivos contra resultados» con cada objetivo medible de la "
                "estrategia aprobada.",
            ),
            (
                "Mayor y menor rendimiento",
                "Llena la hoja «Mayor y menor rendimiento»: por tipo, formato, horario y "
                "plataforma, ¿qué rindió más, qué rindió menos y qué patrón de comportamiento lo "
                "explica?",
            ),
            (
                "Capturas de pantalla o evidencias",
                "Registra en la hoja «Evidencias de medición» cada captura o evidencia de las "
                "herramientas de medición y seguimiento, y anéxalas al reporte.",
            ),
            (
                "Periodo, fuente y frecuencia de medición",
                "Fecha del periodo de análisis, fuente de cada dato y frecuencia con la que "
                "mediste.",
            ),
        ],
    },
    {
        "num": "4.2",
        "slug": "4-2-plan-optimizacion",
        # Word y no Excel: el plan es sobre todo recomendaciones justificadas, ajustes de
        # prompts y una aprobación firmada; no hay nada que calcular, y sus dos tablas
        # (pruebas y calendario) caben en el documento.
        "format": "word",
        "elemento": "4 · E5884",
        "title": "El plan de optimización del contenido de mercadotecnia digital con IA para el siguiente periodo, documentado",
        "intro": (
            "Con base en el reporte de desempeño, define qué se mantiene y qué se ajusta en el "
            "siguiente periodo: tipos de contenido, formatos, frecuencia y horarios, pruebas de "
            "optimización con su hipótesis y métrica de éxito, segmentación y presupuesto de "
            "promoción, prompts, calendario, nuevos objetivos y la evidencia de aprobación de la "
            "persona responsable."
        ),
        "criterios": [
            "(a) Contiene las recomendaciones de continuidad/ajuste a los tipos de contenido/formatos/frecuencia de publicación por plataforma digital, con base en el análisis de resultados",
            "(b) Indica la(s) propuesta(s) de pruebas de optimización a realizar, considerando la hipótesis a validar y la métrica de éxito",
            "(c) Incluye la recomendación de continuidad/ajuste a horarios de publicación con base en los datos de rendimiento por plataforma digital y por tipo de contenido",
            "(d) Contiene la recomendación de continuidad/modificación a la segmentación de audiencia y al presupuesto de promoción de acuerdo con los resultados obtenidos",
            "(e) Incluye la propuesta de continuidad/ajuste a los prompts e instrucciones de generación de contenido con IA, considerando de los resultados de la campaña que concluyó",
            "(f) Tiene el calendario de publicación de contenidos para el siguiente periodo",
            "(g) Especifica los nuevos objetivos y métricas de seguimiento para el siguiente periodo",
            "(h) Contiene la evidencia de aprobación del plan de optimización por parte de la(s) persona(s) responsable(s) de la mercadotecnia digital en la MiPyME",
        ],
        "caso": (
            "Para el siguiente mes: 60 % Reels, 25 % carruseles educativos y 15 % posts de "
            "producto. Pruebas: (1) posts de producto el sábado a mediodía en vez del martes; "
            "hipótesis: el alcance sube al menos 40 %; métrica: personas alcanzadas. (2) "
            "Carruseles de proceso contra carruseles educativos, para medir cuál sostiene mejor "
            "la interacción. Segmentación y presupuesto: radio de 5 a 3 km y los mismos 200 "
            "pesos diarios, concentrados en los días de Reel. Prompts: ajustar el prompt de "
            "imagen para incluir personas. Mariana pidió contenido de temporada navideña: Martín "
            "agregó dos semanas dentro del 60 % de Reels y ajustó el calendario; ella firmó la "
            "hoja de validación y él se la envió por correo."
        ),
        "preguntas": [
            (
                "Tipos de contenido, formatos y frecuencia",
                "Con base en el reporte, ¿qué continúa y qué se ajusta en tipos de contenido, "
                "formatos y frecuencia de publicación en cada plataforma? Justifica cada "
                "recomendación con un dato del reporte.",
            ),
            (
                "Pruebas de optimización",
                "Llena la tabla «Pruebas de optimización» al final de esta plantilla: por cada "
                "prueba, qué cambia, la hipótesis a validar y la métrica de éxito.",
            ),
            (
                "Horarios de publicación",
                "¿Qué horarios continúan y cuáles se ajustan, por plataforma y por tipo de "
                "contenido? ¿Qué datos de rendimiento lo respaldan?",
            ),
            (
                "Segmentación de audiencia y presupuesto de promoción",
                "¿Se mantienen o se modifican la segmentación de audiencia y el presupuesto de "
                "promoción? ¿Por qué, según los resultados?",
            ),
            (
                "Prompts e instrucciones de generación con IA",
                "¿Qué prompts e instrucciones se mantienen y cuáles ajustas? Escribe el cambio y "
                "el resultado de la campaña que lo motiva.",
            ),
            (
                "Calendario del siguiente periodo",
                "Llena la tabla «Calendario del siguiente periodo» al final de esta plantilla, "
                "con las temporadas comerciales que caigan en ese periodo.",
            ),
            (
                "Nuevos objetivos y métricas de seguimiento",
                "¿Qué objetivos y métricas de seguimiento quedan para el siguiente periodo?",
            ),
            (
                "Evidencia de aprobación",
                "¿Cómo queda documentada la aprobación del plan? Usa la tabla «Aprobación del "
                "plan» o anexa el correo o mensaje con que la persona responsable lo aprobó.",
            ),
        ],
    },
]


# ===========================================================================
# PLANTILLAS POR FORMATO
# (mismo sistema visual que los otros estándares; convert-legacy-office.py
#  descarta este CSS y redibuja con la marca)
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
table.matrix { border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 10pt; }
table.matrix th, table.matrix td { border: 1pt solid #999; padding: 6pt 8pt; vertical-align: top; }
table.matrix th { background: #28467e; color: white; font-weight: bold; text-align: left; }

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

# La caja de criterios conserva la clase f21-box: convert-legacy-office.py, común a
# los cuatro estándares, la busca por ese nombre para la hoja «Guía» de Excel.
PIE = ("Mi CompañIA · Una iniciativa de FUNDES México con el apoyo de Google.org · "
       "Plantilla de trabajo del Estándar C (EC1848)")

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
<p class="subtitle">Curso {ec} · Producto del Elemento {elemento}</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Plantilla editable<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Quien te evalúa no busca que llenes la plantilla: busca que tu producto cumpla cada criterio del {ec} con los datos de la MiPyME con la que trabajas. Las preguntas guía te orientan; las respuestas son tuyas.</div>

<div class="f21-box">
<h3>Criterios del {ec}</h3>
<ul>{criterios_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Cafetería La Cuesta (ilustrativo, no es tu solución):</strong> {caso}</div>

<div class="product-data">
<table>
<tr><td>MiPyME (razón social)</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Persona responsable de la mercadotecnia digital</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Consultor o consultora</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Fecha del documento</td><td><span class="blank">&nbsp;</span></td></tr>
</table>
</div>

<h2>Tu turno · preguntas guía</h2>

{questions_html}

{extra_html}

<div class="footer">{pie}</div>

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
<style>{base_styles}</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;"><div class="brand-block">Mi<br>CompañIA</div></td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Curso {ec} · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Excel calcula las tasas y el avance contra cada meta, y te deja añadir filas. Llénala con los datos de la MiPyME con la que trabajas.</div>

<div class="f21-box">
<h3>Criterios del {ec}</h3>
<ul>{criterios_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Cafetería La Cuesta (ilustrativo, no es tu solución):</strong> {caso}</div>

<div class="product-data">
<table>
<tr><td>MiPyME</td><td><span class="blank">&nbsp;</span></td><td>Fecha</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Consultor o consultora</td><td><span class="blank">&nbsp;</span></td><td>Responsable en la MiPyME</td><td><span class="blank">&nbsp;</span></td></tr>
</table>
</div>

<h2>Tu turno · preguntas guía</h2>

{questions_html}

{extra_html}

<div class="footer">{pie}</div>

</body>
</html>
"""


# ===========================================================================
# RENDERIZADORES
# ===========================================================================

def render_criterios(criterios):
    """Lista HTML con los criterios literales del EC."""
    return "".join(f"<li>{c}</li>\n" for c in criterios)


def render_questions_word(preguntas):
    """Bloques de preguntas guía, cada uno con su área de respuesta."""
    html = ""
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<div class="question-block">\n'
            f'<div><span class="question-num">{i}</span>'
            f'<span class="question-title">{title}</span></div>\n'
            f'<div class="question-help">{help_text}</div>\n'
            f'<div class="fill-area">[Escribe aquí tu respuesta con los datos de la MiPyME '
            f'con la que trabajas. Borra esta línea cuando empieces.]</div>\n'
            f'</div>\n'
        )
    return html


def render_questions_excel(preguntas):
    """Tabla de preguntas guía con una columna para responder."""
    html = (
        '<table class="matrix">\n'
        '<tr>'
        '<th style="width: 4%;">#</th>'
        '<th style="width: 28%;">Pregunta guía</th>'
        '<th>Tu respuesta (con los datos de la MiPyME con la que trabajas)</th>'
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


def tabla(titulo, encabezados, filas, nota=""):
    """Tabla para llenar con su encabezado de sección.

    filas: número de filas vacías, o lista de filas donde cada celda es texto fijo,
    "" (celda vacía) o una fórmula de Excel que empieza con "=" y usa {f} para el
    número de fila (convención de convert-legacy-office.py).

    En Excel el título es el nombre de la hoja: debe caber en 31 caracteres.
    """
    if isinstance(filas, int):
        filas = [[""] * len(encabezados) for _ in range(filas)]
    th = "".join(f"<th>{e}</th>" for e in encabezados)
    cuerpo = ""
    for fila in filas:
        cuerpo += "<tr>" + "".join(
            f'<td class="fill">{c or "&nbsp;"}</td>' for c in fila) + "</tr>\n"
    parrafo = f'<p style="font-size: 10pt; color: #666;">{nota}</p>\n' if nota else ""
    return (f"<h2>{titulo}</h2>\n{parrafo}"
            f'<table class="matrix">\n<tr>{th}</tr>\n{cuerpo}</table>\n')


def aprobacion(titulo):
    return tabla(
        titulo,
        ["Persona responsable de la mercadotecnia digital", "Cargo", "Fecha", "Firma"],
        1,
        "Firma de la persona responsable de la mercadotecnia digital en la MiPyME. Si aprobó "
        "por correo o mensaje, anexa la captura.",
    )


def render_extra(num):
    """Tablas propias de cada producto, después de las preguntas guía."""
    if num == "1.2":
        return (
            tabla("Tabla de análisis por plataforma",
                  ["Plataforma digital", "Justificación por audiencia",
                   "Tipo de formato y especificaciones técnicas",
                   "Herramienta de IA por tipo de contenido",
                   "Frecuencia de publicación"], 4)
            + tabla("Distribución del contenido",
                    ["Semana", "Día y horario", "Plataforma", "Tipo de contenido",
                     "Tema o mensaje"],
                    [[f"Semana {s}", "", "", "", ""] for s in (1, 1, 2, 2, 3, 3, 4, 4)],
                    "Al menos cuatro semanas. Agrega las filas que necesites.")
            + aprobacion("Aprobación de la estrategia")
        )

    if num == "4.1":
        # Interacciones = me gusta + comentarios + compartidos + guardados (o
        # respuestas, en mensajería). Las fórmulas las escribe el conversor.
        metricas = [["", "", "", "", "", "", "", "", "",
                     '=IFERROR(ROUND(H{f}/F{f}*100,2),"")',
                     '=IFERROR(ROUND(I{f}/G{f}*100,2),"")'] for _ in range(10)]
        resumen = [["", "", "", "", "", "", "",
                    '=IF(OR(E{f}="",F{f}=""),"",E{f}-F{f})'] for _ in range(6)]
        objetivos = [["", "", "", "",
                      '=IFERROR(ROUND(D{f}/C{f}*100,1),"")',
                      '=IF(E{f}="","",IF(E{f}>=100,"Sí","No"))'] for _ in range(4)]
        dimensiones = [[d, "", "", "", ""] for d in
                       ("Tipo de contenido", "Formato", "Horario", "Plataforma digital")]
        return (
            tabla("Métricas por publicación",
                  ["Fecha", "Hora", "Plataforma", "Tipo de contenido", "Formato",
                   "Alcance", "Impresiones",
                   "Interacciones (me gusta, comentarios, compartidos y guardados)",
                   "Clics",
                   "Tasa de interacción % (interacciones ÷ alcance × 100)",
                   "Tasa de clics (CTR) % (clics ÷ impresiones × 100)"], metricas)
            + tabla("Resumen por tipo y plataforma",
                    ["Plataforma", "Tipo de contenido", "Publicaciones",
                     "Alcance promedio", "Tasa de interacción promedio %",
                     "Línea base de la MiPyME %", "Referencia de mercado %",
                     "Diferencia contra la línea base (puntos)"], resumen)
            + tabla("Objetivos contra resultados",
                    ["Objetivo medible de la estrategia", "Métrica de seguimiento", "Meta",
                     "Resultado", "Avance contra la meta % (resultado ÷ meta × 100)",
                     "¿Se cumplió?"], objetivos)
            + tabla("Mayor y menor rendimiento",
                    ["Dimensión", "Mayor rendimiento", "Menor rendimiento",
                     "Patrón de comportamiento identificado", "Meta relacionada"],
                    dimensiones)
            + tabla("Evidencias de medición",
                    ["Evidencia (captura o enlace)", "Herramienta de medición y seguimiento",
                     "Plataforma", "Dato que respalda", "Fecha de corte"], 6)
        )

    if num == "4.2":
        return (
            tabla("Pruebas de optimización",
                  ["Prueba", "Qué cambia", "Hipótesis a validar", "Métrica de éxito",
                   "Plataforma y duración"], 3)
            + tabla("Calendario del siguiente periodo",
                    ["Semana", "Día y horario", "Plataforma", "Tipo de contenido y formato",
                     "Tema o mensaje"],
                    [[f"Semana {s}", "", "", "", ""] for s in (1, 1, 2, 2, 3, 3, 4, 4)],
                    "Agrega las filas y semanas que necesites.")
            + aprobacion("Aprobación del plan")
        )

    return ""


def render_product(p):
    """Devuelve (contenido HTML, extensión de archivo)."""
    campos = dict(
        num=p["num"],
        title=p["title"],
        elemento=p["elemento"],
        intro=p["intro"],
        caso=p["caso"],
        criterios_html=render_criterios(p["criterios"]),
        extra_html=render_extra(p["num"]),
        ec=EC,
        pie=PIE,
        base_styles=BASE_STYLES,
    )
    if p["format"] == "word":
        return WORD_TEMPLATE.format(
            questions_html=render_questions_word(p["preguntas"]), **campos), "doc"
    if p["format"] == "excel":
        return EXCEL_TEMPLATE.format(
            questions_html=render_questions_excel(p["preguntas"]), **campos), "xls"
    raise ValueError(f"Formato desconocido: {p['format']}")


def main():
    # Limpiar archivos OOXML anteriores: el conversor los vuelve a generar
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
        filename = f"{p['slug']}.{ext}"
        (OUT / filename).write_text(content, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")

    print(f"\nGeneradas {len(PRODUCTS)} plantillas en {OUT}/")
    import subprocess
    import sys
    subprocess.run([sys.executable, str(ROOT / "scripts" / "convert-legacy-office.py")], check=True)


if __name__ == "__main__":
    main()
