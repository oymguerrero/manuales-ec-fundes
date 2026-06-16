#!/usr/bin/env python3
"""
Genera los 13 templates de los productos del estándar Desarrollar con IA
(Estándar B · Desarrollar productos/servicios con IA en MiPyMEs).

- 9 Word (.doc) como HTML estilizado con MIME Office
- 4 Excel (.xls) como HTML estilizado con MIME Office
- Sin PowerPoint en este estándar

Caso pedagógico: Artesanías Tonalli (taller familiar de cerámica de barro
bruñido, Lucía + Diego). El caso ilustra el TIPO de contenido; el aspirante
responde con datos de SU proyecto real.

Filosofía pedagógica: NO darle la solución al aspirante. Cada template muestra:
  (1) el criterio F21 literal
  (2) ejemplo breve del caso Tonalli (solo ilustrativo)
  (3) preguntas guía que el aspirante responde con su MiPyME real

Uso:
    python3 scripts/generate-templates-b.py

Salida: estandar-b/templates/<num_con_guiones>-<slug>.{doc|xls}
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-b" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

PRODUCTS = [
    # -----------------------------------------------------------------------
    # ELEMENTO 1 · IDENTIFICAR
    # -----------------------------------------------------------------------
    {
        "num": "1.1", "slug": "reporte-inicial", "format": "word",
        "elemento": "1 · Identificar", "title": "Reporte inicial documentado del levantamiento de información con el cliente",
        "intro": "Es el primer producto del proyecto: documentación de la sesión inicial con el emprendedor, el perfil de la empresa, los problemas identificados y la sentencia del problema/oportunidad.",
        "f21": [
            "(a) Contiene el resumen de la sesión inicial realizada con el emprendedor o persona responsable de la empresa/contexto empresarial y tecnológico actual de la empresa",
            "(b) Incluye el perfil empresarial: nombre de la empresa, ubicación, giro o actividad económica, número de empleados, datos de contacto de la persona responsable",
            "(c) Contiene la descripción de los problemas, necesidades/oportunidades de mejora identificadas desde la perspectiva del cliente",
            "(d) Contiene la descripción de los procesos, actividades/áreas donde se identifican oportunidades de mejora/innovación",
            "(e) Contiene la definición del alcance preliminar del proyecto",
            "(f) Contiene la definición de la sentencia del problema/oportunidad en un párrafo que considera el origen del problema/oportunidad, el perfil del afectado/involucrado, el contexto de aparición y el mecanismo de resolución vigente",
            "(g) Contiene la(s) fuente(s) de información consultada(s)",
            "(h) Indica la metodología de recolección aplicada",
            "(i) Se presenta en formato digital/físico, con redacción clara, estructurada y sin errores ortográficos",
        ],
        "tonalli": "Sesión inicial en el taller de Lucía. Artesanías Tonalli: taller familiar, cerámica barro bruñido, 8 personas, venta a turistas y tiendas. Problema: cada pieza es única, describirla para catálogo digital toma 45 min por pieza (Lucía no sabe cómo redactar para e-commerce). Sentencia: \"Los artesanos del taller Tonalli invierten hasta 45 minutos por pieza para redactar descripciones de venta digital, sin un modelo de referencia ni apoyo tecnológico, lo que retrasa la apertura del canal en línea y reduce la capacidad de mostrar su catálogo completo.\"",
        "preguntas": [
            ("Resumen de la sesión inicial", "¿Cómo fue tu primera sesión con el emprendedor? ¿Qué planteó como su situación actual? ¿Qué recursos tecnológicos tiene disponibles hoy?"),
            ("Perfil empresarial", "Nombre legal, ubicación, giro, número de empleados, persona responsable y datos de contacto."),
            ("Problemas y oportunidades desde la perspectiva del cliente", "¿Qué te dijo el emprendedor que le duele más? ¿Qué oportunidad ve él/ella para su negocio?"),
            ("Procesos o áreas con oportunidades", "¿En qué parte del negocio identificaste el mayor potencial de mejora con IA? ¿Por qué?"),
            ("Alcance preliminar del proyecto", "¿Qué incluirá el proyecto y qué no? ¿Cuáles son las fronteras de tu intervención?"),
            ("Sentencia del problema/oportunidad", "Escribe en 1 párrafo: origen del problema, perfil del afectado, contexto en que aparece, mecanismo de resolución vigente (si lo hay)."),
            ("Fuentes de información consultadas", "¿Qué documentos, sistemas o personas consultaste para entender el contexto?"),
            ("Metodología de recolección", "¿Cómo levantaste la información? Entrevista abierta, cuestionario, observación directa, revisión documental…"),
        ],
    },
    {
        "num": "1.2", "slug": "analisis-mercado", "format": "word",
        "elemento": "1 · Identificar", "title": "Análisis de mercado de la MiPyME elaborado",
        "intro": "Documenta el macroentorno del sector, el comparativo de competidores y las oportunidades de diferenciación con IA. Alimenta las hipótesis que se validarán en las entrevistas de usuario.",
        "f21": [
            "(a) Contiene el análisis del macroentorno y tendencias del mercado del sector de la MiPyME: tendencias de consumo, cambios tecnológicos, comportamientos del cliente y dinámicas del mercado",
            "(b) Incluye un comparativo de competidores directos e indirectos: propuesta de valor, posicionamiento, uso de tecnología y capacidades digitales presentes en el mercado",
            "(c) Contiene la descripción de las oportunidades identificadas de diferenciación mediante IA, derivadas del análisis de tendencias, brechas competitivas y necesidades emergentes del usuario",
            "(d) Incluye información del entorno de la MiPyME para orientar las entrevistas con usuarios y partes interesadas, permitiendo precisar la hipótesis de problemas, necesidades y oportunidades a validar",
            "(e) Contiene el listado de herramientas y prompts de análisis con IA utilizados",
            "(f) Incluye las fuentes de información consultadas: reportes sectoriales, estudios de mercado, bases de datos, plataformas digitales y herramientas de análisis con IA",
            "(g) Se presenta en formato digital/físico, con redacción clara, estructurada y sin errores ortográficos",
        ],
        "tonalli": "Análisis del sector artesanías mexicanas + e-commerce de productos únicos/handmade. Tendencia: crecimiento de plataformas como Etsy MX, Amazon Handmade, Instagram Shopping. Brecha: la mayoría de artesanos en Tonalá carecen de presencia digital estructurada. Herramienta IA usada: Claude para análisis de tendencias, prompt: \"Analiza las tendencias de e-commerce para artesanías mexicanas únicas dirigidas a turismo doméstico e internacional en 2025.\"",
        "preguntas": [
            ("Análisis del macroentorno y tendencias", "¿Qué está pasando en el sector de tu MiPyME que sea relevante para el proyecto? Tendencias de consumo, cambios tecnológicos, regulatorios o sociales."),
            ("Comparativo de competidores", "¿Quiénes son los competidores directos e indirectos? ¿Cómo usan tecnología o IA? ¿Cuál es su propuesta de valor vs la de tu MiPyME?"),
            ("Oportunidades de diferenciación con IA", "A partir del análisis: ¿qué puede hacer tu MiPyME con IA que sus competidores no hacen? ¿Dónde hay brecha real?"),
            ("Información para orientar entrevistas", "¿Qué hipótesis de problema/oportunidad tienes ahora, que vas a confirmar o refutar con las entrevistas de usuario?"),
            ("Herramientas y prompts IA usados", "Lista las herramientas que usaste para el análisis de mercado + los prompts que resultaron más útiles."),
            ("Fuentes consultadas", "Reportes sectoriales, estudios de mercado, plataformas de datos, artículos de tendencias. Cita con detalle suficiente para que el evaluador pueda verificarlas."),
        ],
    },
    {
        "num": "1.3", "slug": "reporte-entrevistas", "format": "word",
        "elemento": "1 · Identificar", "title": "Reporte de entrevistas de necesidades del usuario, elaborado",
        "intro": "Documenta las entrevistas realizadas con usuarios y partes interesadas, el perfil de usuario construido, el análisis de causas raíz y las oportunidades de mejora identificadas.",
        "f21": [
            "(a) Contiene el registro de la(s) entrevista(s) realizada(s): objetivo de cada entrevista, perfil del entrevistado y medio utilizado",
            "(b) Especifica las herramientas/plataformas de IA utilizadas como apoyo en la investigación cualitativa, incluyendo propósito de uso y prompts aplicados",
            "(c) Incluye la descripción de los problemas/necesidades/experiencias y contexto de uso del usuario relacionados con el proceso analizado",
            "(d) Contiene la descripción del perfil del usuario integrado por sus necesidades, emociones, perspectiva, acciones y resultados esperados",
            "(e) Incluye el análisis del propósito de uso: cronología del proceso, cuatro fuerzas del progreso y narrativa de necesidad (situación, motivación, resultado esperado)",
            "(f) Contiene los hallazgos obtenidos durante las entrevistas: patrones de comportamiento y necesidades identificadas como prioritarias",
            "(g) Incluye la descripción de los problemas actuales del usuario y su impacto en el proceso o servicio analizado",
            "(h) Incluye el análisis de causa raíz mediante árbol de problema/causa-efecto",
            "(i) Incluye la descripción de las oportunidades de mejora y oportunidades de mercado mediante el uso de IA en la MiPyME",
            "(j) Contiene el listado de herramientas y prompts de análisis con IA utilizados",
            "(k) Se presenta en formato digital/físico, con redacción clara, estructurada y sin errores ortográficos",
        ],
        "tonalli": "4 entrevistas: Lucía (dueña), Diego (sobrino/apoyo), 2 clientes regulares que compran en el taller. Herramienta IA: Claude para síntesis de entrevistas y generación de user persona. Hallazgos principales: los clientes buscan \"la historia detrás de la pieza\" + \"saber que es única\" + \"poder regalarla con una descripción lista\". Cuatro fuerzas: Push = catálogo físico agotador; Pull = ver tiendas con fotos y descripciones atractivas en línea; Anxiety = miedo a que IA \"no capture la esencia artesanal\"; Habit = seguir vendiendo solo presencialmente.",
        "preguntas": [
            ("Registro de entrevistas", "Por cada entrevista: objetivo, perfil del entrevistado (quién es, qué hace, cómo se relaciona con el problema), medio utilizado (presencial, videollamada, etc.)."),
            ("Herramientas IA en investigación cualitativa", "¿Usaste IA para sintetizar entrevistas, generar user personas o explorar hipótesis? ¿Qué herramienta, con qué propósito y con qué prompt?"),
            ("Problemas, necesidades y contexto de uso", "¿Qué problemas concretos tiene el usuario en su vida diaria relacionados con el proceso que interviene tu solución?"),
            ("Perfil del usuario (necesidades, emociones, perspectiva, acciones, resultados esperados)", "Construye el perfil completo del usuario tipo. ¿Qué siente? ¿Qué hace hoy? ¿Qué quiere lograr?"),
            ("Análisis del propósito de uso (cuatro fuerzas + narrativa de necesidad)", "¿Qué empuja al usuario a buscar un cambio (Push)? ¿Qué le atrae de la solución propuesta (Pull)? ¿Qué le genera ansiedad (Anxiety)? ¿Qué hábito mantiene la situación actual (Habit)? Escribe la narrativa: \"Cuando [situación], quiero [motivación], para poder [resultado esperado].\""),
            ("Hallazgos (patrones y necesidades prioritarias)", "Resume los patrones que emergieron de las entrevistas. ¿Cuáles necesidades son las más frecuentes y las de mayor impacto?"),
            ("Problemas del usuario e impacto", "Por cada problema identificado: ¿cuánto le cuesta al usuario (tiempo, dinero, estrés)? ¿Qué consecuencias tiene si no se resuelve?"),
            ("Análisis de causa raíz (árbol de problema/causa-efecto)", "Dibuja o describe el árbol: problema central → causas raíz → efectos en el negocio y en el usuario."),
            ("Oportunidades de mejora y de mercado con IA", "A partir del análisis: ¿qué oportunidades concretas de mejora identificaste que podrían resolverse con IA?"),
            ("Herramientas y prompts IA usados", "Lista completa de herramientas + prompts aplicados en todo el proceso de investigación."),
        ],
    },
    {
        "num": "1.4", "slug": "matriz-priorizacion", "format": "excel",
        "elemento": "1 · Identificar", "title": "Matriz de priorización de oportunidades elaborada",
        "intro": "Hoja de cálculo para priorizar las oportunidades detectadas. Evalúa viabilidad comercial, impacto y recursos necesarios para decidir cuál desarrollar primero.",
        "f21": [
            "(a) Contiene los criterios de evaluación de viabilidad comercial, impacto y recursos definidos",
            "(b) Contiene las oportunidades clasificadas y ordenadas por prioridad",
            "(c) Contiene la recomendación de oportunidades seleccionadas para desarrollo",
            "(d) Se presenta en formato digital/físico, con redacción clara, estructura profesional y sin errores ortográficos",
        ],
        "tonalli": "3 oportunidades detectadas: (1) Asistente generador de descripciones y fichas a partir de foto (impacto alto, viabilidad alta, recursos bajos → SELECCIONADA); (2) Asistente de atención a turistas por WhatsApp (impacto medio, viabilidad media); (3) Análisis predictivo de inventario (impacto bajo en corto plazo, viabilidad baja → descartada). Se seleccionó la oportunidad 1.",
        "preguntas": [
            ("Criterios de evaluación definidos", "¿Qué criterios usaste para evaluar las oportunidades? Define qué significa \"alto/medio/bajo\" para viabilidad comercial, impacto y recursos en el contexto de tu MiPyME."),
            ("Oportunidades identificadas y su puntaje", "Por cada oportunidad: descripción breve + puntaje en cada criterio. Usa la tabla."),
            ("Clasificación y orden por prioridad", "Ordena las oportunidades de mayor a menor prioridad resultante del análisis."),
            ("Recomendación de oportunidades a desarrollar", "¿Cuál o cuáles seleccionaste? ¿Por qué? ¿Qué factores fueron determinantes en la decisión?"),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 2 · CONCEPTUALIZAR
    # -----------------------------------------------------------------------
    {
        "num": "2.1", "slug": "informe-ideacion", "format": "word",
        "elemento": "2 · Conceptualizar", "title": "Informe del proceso de ideación de soluciones documentado con el cliente/usuario",
        "intro": "Documenta la sesión de ideación: las preguntas generadoras, las técnicas aplicadas, las ideas obtenidas y cómo se refinaron para orientar el desarrollo.",
        "f21": [
            "(a) Contiene las preguntas generadoras de ideas formuladas a partir del problema priorizado",
            "(b) Contiene las preguntas sobre oportunidades de mejora o innovación en procesos, productos/servicios",
            "(c) Contiene la/s pregunta/s detonadora/s seleccionadas para la generación de ideas",
            "(d) Incluye las técnicas de ideación utilizadas",
            "(e) Contiene las ideas obtenidas a partir de las preguntas generadoras de ideas",
            "(f) Contiene la reformulación de las ideas que facilitan/impulsan la generación de soluciones",
            "(g) Contiene las herramientas y los prompts que se utilizaron en la sesión de ideación de soluciones de productos y servicios",
            "(h) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "Sesión de ideación con Lucía y Diego. Pregunta detonadora: \"¿Cómo podríamos ayudar a que cada pieza única de Tonalli cuente su propia historia para un comprador en línea que nunca ha estado en el taller?\" Técnica: brainwriting + expansión con Claude. Ideas generadas: (1) asistente que describe piezas a partir de foto; (2) QR en cada pieza con historia narrada en audio; (3) video-story generado automáticamente. Idea seleccionada: 1 + elementos de 3 (ficha visual + descripción textual).",
        "preguntas": [
            ("Preguntas generadoras de ideas a partir del problema priorizado", "Antes de la sesión: ¿qué preguntas preparaste para detonar ideas alrededor del problema central?"),
            ("Preguntas sobre oportunidades de mejora/innovación", "¿Qué preguntas exploraron oportunidades de innovar en procesos o en el producto/servicio mismo?"),
            ("Pregunta(s) detonadora(s) seleccionada(s)", "¿Cuál fue la pregunta \"¿Cómo podríamos…?\" que guio la sesión? ¿Cómo la construiste?"),
            ("Técnicas de ideación utilizadas", "¿Usaste brainwriting, SCAMPER, mapas mentales, Design Sprint, otra técnica? Describe cómo la aplicaste."),
            ("Ideas obtenidas", "Lista todas las ideas que surgieron en la sesión. Cantidad > calidad en esta etapa."),
            ("Reformulación de ideas", "¿Cómo refinaste o combinaste las ideas para acercarlas a una solución viable? ¿Cuáles se descartaron y por qué?"),
            ("Herramientas y prompts IA en la sesión", "¿Usaste IA para generar, expandir o filtrar ideas? ¿Qué herramienta y con qué prompt?"),
        ],
    },
    {
        "num": "2.2", "slug": "matriz-ideas-solucion", "format": "excel",
        "elemento": "2 · Conceptualizar", "title": "Matriz de ideas de solución validada por el cliente/usuario",
        "intro": "Tabla comparativa de todas las ideas generadas, evaluadas por novedad, utilidad y factibilidad, con la selección final documentada y validada por el cliente.",
        "f21": [
            "(a) Contiene el listado de ideas generadas durante el proceso de ideación",
            "(b) Contiene la descripción breve de cada idea de producto o servicio propuesto",
            "(c) Incluye una clasificación preliminar de las ideas según criterios de novedad, utilidad y factibilidad",
            "(d) Especifica las oportunidades de implementación de tecnologías digitales/IA identificadas y validadas por el cliente/usuario",
            "(e) Especifica la(s) idea(s) seleccionada(s) por el cliente",
            "(f) Se presenta en formato de matriz/tabla de análisis, en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "Matriz con 6 ideas evaluadas por Lucía y Diego. Criterios: novedad (1-5), utilidad para el negocio (1-5), factibilidad técnica (1-5). Ganadora: \"Asistente IA que genera descripción + ficha de producto desde foto\" → novedad 4, utilidad 5, factibilidad 4. Segunda: \"QR con historia narrada\" → descartada por costo de implementación por pieza.",
        "preguntas": [
            ("Listado de ideas con descripción breve", "Una fila por idea. Describe brevemente qué es y cómo funcionaría."),
            ("Clasificación por novedad, utilidad y factibilidad", "Puntúa cada idea en los tres criterios. Define qué significa cada nivel (1-5) en el contexto de tu MiPyME."),
            ("Oportunidades IA validadas por el cliente", "¿Qué tecnologías o herramientas de IA vio el cliente como aplicables y deseables para cada idea? ¿Hubo alguna que el cliente rechazó?"),
            ("Idea(s) seleccionada(s) por el cliente", "¿Cuál eligió el cliente? ¿Fue una sola idea o una combinación? Documenta el proceso de selección."),
        ],
    },
    {
        "num": "2.3", "slug": "modelo-negocio", "format": "word",
        "elemento": "2 · Conceptualizar", "title": "Modelo de negocio documentado",
        "intro": "Documento integrador que combina la propuesta de valor comercial (canvas) con el diseño del modelo de funcionamiento del prototipo: arquitectura, flujos, herramientas IA seleccionadas y consideraciones éticas.",
        "f21": [
            "(a) Incluye la descripción del valor diferencial de la idea respecto a soluciones convencionales",
            "(b) Contiene la descripción de la propuesta de valor comercial en el contexto de la MiPyME, en una frase",
            "(c) Contiene descritos los segmentos de clientes",
            "(d) Contiene definidas las formas de relación con el cliente y los canales de comunicación/distribución",
            "(e) Contiene los recursos y actividades clave necesarias para la operación",
            "(f) Contiene las fuentes de ingresos asociadas al producto o servicio",
            "(g) Contiene los costos de desarrollo, operación y mantenimiento",
            "(h) Contiene las alianzas clave para la operación y desarrollo del producto/servicio",
            "(i) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
            "(j) Especifica las funcionalidades clave del prototipo de la solución propuesta",
            "(k) Contiene la definición de los datos de entrada requeridos y los resultados esperados del componente de IA",
            "(l) Contiene las herramientas/plataformas de IA aplicables al desarrollo del prototipo",
            "(m) Contiene la justificación de la selección de las herramientas/plataformas de IA alineadas a las necesidades y recursos de la MiPyME",
            "(n) Describe los flujos de interacción de usuario con el prototipo",
            "(o) Describe la arquitectura del prototipo",
            "(p) Contiene la representación visual y la descripción de los requerimientos de diseño gráfico",
            "(q) Contiene los costos de desarrollo y operación del prototipo",
            "(r) Contiene la definición de los requerimientos técnicos mínimos del prototipo",
            "(s) Incluye las consideraciones de protección de datos personales y uso ético de IA aplicables al prototipo",
            "(t) Incluye las consideraciones de propiedad intelectual aplicables al producto",
            "(u) Incluye los términos de servicio de las herramientas/plataformas de IA utilizadas y la legislación mexicana de derecho de autor",
            "(v) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "Propuesta de valor: \"Cada pieza de Tonalli contará su historia en línea en menos de 2 minutos.\" Segmentos: turistas culturales que compran en línea + tiendas de decoración. Canal: Instagram Shopping + sitio web propio. Prototipo: workflow en Make.com que recibe foto de pieza → Claude Vision genera descripción poética + técnica → output formateado para Wix/tienda.",
        "preguntas": [
            ("Valor diferencial", "¿En qué es diferente tu solución respecto a lo que el emprendedor haría sin IA? ¿Cuál es la ventaja competitiva real?"),
            ("Propuesta de valor en una frase", "Escribe: \"Para [segmento], [nombre de la solución] es [categoría] que [beneficio clave], a diferencia de [alternativa convencional] que [limitación].\""),
            ("Segmentos de clientes", "¿A quién sirve esta solución? ¿Hay más de un segmento? Descríbelos."),
            ("Relación con el cliente y canales", "¿Cómo llegará la solución a los clientes? ¿Cómo se comunicarán y distribuirán? ¿Qué tipo de relación (autoservicio, asistida, comunidad)?"),
            ("Recursos y actividades clave", "¿Qué necesita tener y hacer el emprendedor para que la solución opere? Personas, herramientas, datos, habilidades."),
            ("Fuentes de ingresos", "¿Cómo generará dinero el emprendedor con esta solución? ¿Directa o indirectamente?"),
            ("Costos de desarrollo, operación y mantenimiento", "¿Qué costará desarrollar y mantener la solución? Desglosa suscripciones, tiempo, servicio del consultor."),
            ("Alianzas clave", "¿Hay proveedores, plataformas o personas externas que sean esenciales para que la solución funcione?"),
            ("Funcionalidades clave del prototipo", "¿Qué hace exactamente el prototipo? Lista las funciones mínimas que debe tener para ser viable."),
            ("Datos de entrada y resultados esperados del componente IA", "¿Qué le entra al componente de IA? ¿Qué debe salir? Define el contrato de datos de entrada y salida."),
            ("Herramientas/plataformas de IA seleccionadas y justificación", "¿Qué herramientas usarás? ¿Por qué estas y no otras? Considera el contexto y los recursos de la MiPyME."),
            ("Flujos de interacción del usuario con el prototipo", "¿Cómo interactúa el usuario con el prototipo paso a paso? Dibuja o describe el flujo."),
            ("Arquitectura del prototipo", "¿Cuáles son los componentes técnicos? ¿Cómo se conectan entre sí?"),
            ("Diseño gráfico y requerimientos visuales", "¿Qué aspecto visual tendrá el prototipo? ¿Hay requerimientos de interfaz?"),
            ("Costos de desarrollo y operación del prototipo", "¿Cuánto costará construirlo? ¿Cuánto costará mantenerlo por mes?"),
            ("Requerimientos técnicos mínimos", "¿Qué necesita tener la MiPyME para que el prototipo funcione? (Conexión, dispositivos, cuentas, etc.)"),
            ("Protección de datos y ética de IA", "¿Qué datos personales maneja el prototipo? ¿Cómo se protegen? ¿Hay riesgos de sesgo o uso indebido de IA?"),
            ("Propiedad intelectual y términos de servicio", "¿Quién es dueño de las descripciones generadas? ¿Los términos de la herramienta de IA permiten el uso comercial?"),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 3 · DESARROLLAR
    # -----------------------------------------------------------------------
    {
        "num": "3.1", "slug": "documentacion-prototipo", "format": "word",
        "elemento": "3 · Desarrollar", "title": "Documentación del prototipo funcional desarrollado",
        "intro": "Documenta el prototipo funcionando: alcances, restricciones, casos de uso probados, resultados de pruebas funcionales y manual de usuario para que el emprendedor opere de manera autónoma.",
        "f21": [
            "(a) Contiene los alcances y restricciones del prototipo funcional",
            "(b) Contiene la descripción de la operación del prototipo funcional, datos de entrada y parámetros de uso",
            "(c) Contiene los prompts y ajustes en las herramientas que se utilizan para la construcción del prototipo",
            "(d) Contiene la descripción de los casos de uso del prototipo funcional",
            "(e) Contiene el resultado de las pruebas funcionales y retroalimentación de los casos de uso",
            "(f) Incluye el manual de usuario que describe las instrucciones de operación del prototipo",
            "(g) Se presenta en formato digital/físico, con redacción clara, estructura profesional y sin errores ortográficos",
        ],
        "tonalli": "Prototipo funcionando: workflow en Make.com + Claude Vision. Alcance: genera descripción en español para piezas de cerámica. Restricción: no funciona bien con fotos con fondo muy desordenado. Caso de uso principal: Lucía toma foto con iPhone → la sube al workflow → en 90 segundos recibe descripción lista para copiar a la tienda en línea. Pruebas: 12 piezas piloto, 10 con resultado aceptable, 2 con problemas de iluminación.",
        "preguntas": [
            ("Alcances y restricciones del prototipo", "¿Qué SÍ hace el prototipo? ¿Qué NO hace? ¿Qué condiciones necesita para funcionar correctamente? (Tipo de foto, formato de datos, condiciones de red, etc.)"),
            ("Descripción de la operación (datos de entrada y parámetros)", "¿Cómo opera el prototipo paso a paso? ¿Qué le entra exactamente? ¿Qué parámetros puede configurar el usuario?"),
            ("Prompts y ajustes en las herramientas", "Lista los prompts que usaste para construir el prototipo. Incluye versiones previas y por qué los ajustaste."),
            ("Casos de uso documentados", "Por cada caso de uso: nombre, descripción, actor(es) involucrados, pasos, resultado esperado, resultado obtenido."),
            ("Resultados de pruebas funcionales y retroalimentación", "¿Cuántas pruebas hiciste? ¿Qué salió bien? ¿Qué falló? ¿Qué retroalimentación te dio el usuario?"),
            ("Manual de usuario", "Instrucciones paso a paso para que el emprendedor opere el prototipo de manera autónoma. Lenguaje simple, orientado a alguien sin experiencia técnica."),
        ],
    },
    {
        "num": "3.2", "slug": "plan-experimentacion", "format": "excel",
        "elemento": "3 · Desarrollar", "title": "Plan de experimentación documentado",
        "intro": "Hoja de cálculo con las hipótesis por categoría (adaptabilidad, deseabilidad, factibilidad, viabilidad), el diseño de las pruebas priorizadas y el cronograma de ejecución.",
        "f21": [
            "(a) Contiene al menos tres hipótesis seleccionadas por el cliente de cada una de las siguientes categorías: adaptabilidad, deseabilidad, factibilidad y viabilidad",
            "(b) Contiene el diseño de las pruebas priorizadas: hipótesis, métricas, criterios de éxito, nivel de criticidad, nivel de confianza, costo, tiempo, nombre de la prueba, nombre del responsable y tiempo de duración",
            "(c) Incluye la descripción del perfil de los usuarios participantes en las pruebas",
            "(d) Contiene el plan de ejecución de las pruebas considerando la actividad, responsable y temporalidad",
            "(e) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "12 hipótesis en total (3 por categoría). Ejemplos: Deseabilidad — \"Los clientes de Tonalli preferirán comprar en línea si la descripción de cada pieza transmite su unicidad artesanal\". Factibilidad — \"Lucía puede operar el asistente de manera autónoma con una sola sesión de capacitación\". Pruebas: 5 priorizadas, 10 usuarios participantes (4 clientes regulares, 3 clientes nuevos, 3 compradores potenciales vía Instagram).",
        "preguntas": [
            ("Hipótesis por categoría (mínimo 3 por cada una)", "Define al menos 3 hipótesis por categoría: adaptabilidad (¿la solución se adapta al contexto de la MiPyME?), deseabilidad (¿los usuarios la quieren?), factibilidad (¿es posible construirla y operarla?), viabilidad (¿genera valor económico?)."),
            ("Diseño de pruebas priorizadas", "Por cada prueba: hipótesis que valida, métricas de éxito, criterio de éxito (umbral), nivel de criticidad (alta/media/baja), nivel de confianza necesario, costo estimado, tiempo estimado, nombre de la prueba, responsable."),
            ("Perfil de usuarios participantes", "¿Quiénes participarán en las pruebas? Describe el perfil de cada tipo de usuario: características, nivel de experiencia digital, relación con la MiPyME."),
            ("Plan de ejecución", "Cronograma de las pruebas: qué se ejecuta cuándo, quién es el responsable, cuánto tiempo toma cada sesión."),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 4 · VALIDAR
    # -----------------------------------------------------------------------
    {
        "num": "4.1", "slug": "bitacora-pruebas", "format": "word",
        "elemento": "4 · Validar", "title": "Bitácora de ejecución de pruebas del plan de experimentación, elaborada",
        "intro": "Registro cronológico de cada sesión de prueba: quiénes participaron, qué hipótesis se evaluó, qué se observó, incidencias y evidencia documental.",
        "f21": [
            "(a) Contiene el registro cronológico de cada experimento ejecutado: fecha, duración, perfil del usuario participante y condiciones de prueba",
            "(b) Contiene la(s) hipótesis seleccionada(s) para ser evaluada(s) en cada sesión y los datos recopilados conforme a las métricas definidas",
            "(c) Incluye el registro de observaciones, incidencias técnicas y ajustes realizados durante la ejecución de cada prueba",
            "(d) Contiene la retroalimentación cualitativa del usuario documentada para cada caso de uso probado",
            "(e) Incluye la evidencia documental de las pruebas: capturas de pantalla/registros de interacción/grabaciones/transcripciones",
            "(f) Se presenta en formato digital/físico, con redacción clara, estructura cronológica y sin errores ortográficos",
        ],
        "tonalli": "Bitácora de 5 sesiones, 10 usuarios. Sesión 1 (12 mayo, 60 min, 2 clientes regulares): hipótesis de deseabilidad. Resultado: los dos usuarios quisieron comprar en línea cuando vieron la descripción generada. Incidencia: la foto de la sesión tenía luz fluorescente → descripción confundió textura. Ajuste: agregar instrucción de foto con luz natural al manual de usuario.",
        "preguntas": [
            ("Registro cronológico por sesión", "Por cada sesión de prueba: fecha y hora, duración, quiénes participaron (perfil), dónde se realizó, condiciones del entorno (dispositivo, conectividad, iluminación si aplica)."),
            ("Hipótesis evaluada y datos recopilados", "¿Qué hipótesis se validó en cada sesión? ¿Qué datos mediste? ¿Qué métricas obtuviste?"),
            ("Observaciones, incidencias y ajustes", "¿Qué observaste que no estaba previsto? ¿Qué fallo técnico ocurrió? ¿Qué ajuste hiciste en el momento o para la siguiente sesión?"),
            ("Retroalimentación cualitativa del usuario", "Citas textuales de lo que dijeron los usuarios. Expresiones faciales o corporales si los observaste presencialmente. Lo que NO dijeron pero comunicaron con su comportamiento."),
            ("Evidencia documental", "¿Tienes capturas de pantalla, grabaciones, transcripciones? Adjúntalas o describe dónde están. El evaluador necesita ver que el experimento ocurrió."),
        ],
    },
    {
        "num": "4.2", "slug": "reporte-resultados-validacion", "format": "word",
        "elemento": "4 · Validar", "title": "Reporte de resultados de validación de las pruebas, elaborado",
        "intro": "Sintetiza los hallazgos de todas las sesiones de prueba: perfil de participantes, resultados por hipótesis, comparativo contra criterios de éxito y patrones emergentes.",
        "f21": [
            "(a) Incluye el perfil de los participantes en las pruebas de validación de la(s) hipótesis",
            "(b) Contiene la descripción de los resultados obtenidos por cada hipótesis evaluada",
            "(c) Incluye el comparativo de resultados contra los criterios de éxito definidos en el plan de experimentación",
            "(d) Contiene los hallazgos de usabilidad, funcionalidad y aceptación del usuario derivados de la bitácora de experimentación",
            "(e) Contiene el análisis de patrones y tendencias identificados a partir de los datos recopilados",
            "(f) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "10 participantes (4 clientes regulares Tonalli, 3 clientes nuevos, 3 compradores potenciales Instagram). Resultado por hipótesis: deseabilidad → 9/10 usuarios querían comprar; factibilidad → Lucía logró operar sola tras 45 min de capacitación; viabilidad → estimación: 3 ventas adicionales/semana si canal en línea activo. Hallazgo de usabilidad: el paso de subir la foto al workflow resultó confuso para Lucía (requiere ajuste de UX).",
        "preguntas": [
            ("Perfil de participantes", "Resume quiénes participaron en todas las sesiones: cantidad, características relevantes, cómo se reclutaron."),
            ("Resultados por hipótesis", "Por cada hipótesis evaluada: ¿se validó o refutó? ¿Qué datos lo sustentan?"),
            ("Comparativo contra criterios de éxito", "Tabla: hipótesis → criterio de éxito definido → resultado obtenido → ¿se cumplió?"),
            ("Hallazgos de usabilidad, funcionalidad y aceptación", "¿Qué encontraste sobre la facilidad de uso, el funcionamiento técnico y la aceptación del usuario? Sé específico."),
            ("Patrones y tendencias", "¿Qué se repitió en múltiples sesiones? ¿Qué tendencia emerge de los datos?"),
        ],
    },
    {
        "num": "4.3", "slug": "resultados-por-hipotesis", "format": "excel",
        "elemento": "4 · Validar", "title": "Descripción de los resultados obtenidos por cada hipótesis, documentada",
        "intro": "Hoja de cálculo con una fila por hipótesis: metodología utilizada, contexto de la prueba y condiciones de aplicación conforme al plan de experimentación.",
        "f21": [
            "(a) Incluye la metodología utilizada en la realización de la prueba",
            "(b) Contiene la descripción del contexto de la realización de la prueba",
            "(c) Contiene las condiciones de aplicación de las pruebas conforme al plan de experimentación",
            "(d) Se presenta en formato digital/físico, con redacción clara, estructura profesional y sin errores ortográficos",
        ],
        "tonalli": "Hoja por hipótesis. Hipótesis 1 (deseabilidad · \"los clientes prefieren comprar si la descripción transmite unicidad\"): metodología → entrevista + observación con prototipo en vivo; contexto → sesión en el taller; condiciones → 2 clientes regulares, 30 min, prototipo con 5 piezas reales; resultado → validada (2/2 expresaron intención de compra).",
        "preguntas": [
            ("Metodología por hipótesis", "¿Qué método usaste para probar cada hipótesis? (Entrevista con prototipo, cuestionario, prueba A/B, observación directa, otro)"),
            ("Descripción del contexto de la prueba", "¿Dónde se realizó? ¿Cuándo? ¿Qué dispositivos o materiales se usaron? ¿Qué condiciones del entorno afectaron los resultados?"),
            ("Condiciones de aplicación conforme al plan", "¿Se ejecutó la prueba exactamente como estaba planeada? Si hubo desviaciones, ¿cuáles y por qué?"),
        ],
    },
    {
        "num": "4.4", "slug": "recomendaciones-prototipo", "format": "word",
        "elemento": "4 · Validar", "title": "Documento de recomendaciones al prototipo/pruebas, elaborado",
        "intro": "Sintetiza los ajustes recomendados al prototipo, la decisión de pivoteo/iteración/escalamiento y la hoja de ruta con próximos pasos, responsables y tiempos.",
        "f21": [
            "(a) Contiene las recomendaciones de ajuste al prototipo basadas en los hallazgos de validación",
            "(b) Incluye la decisión documentada y justificada de pivoteo/iteración/escalamiento del producto o servicio",
            "(c) Contiene la hoja de ruta con los siguientes pasos, responsables y tiempos estimados para la siguiente fase",
            "(d) Incluye los requerimientos técnicos y de recursos necesarios para la implementación/escalamiento",
            "(e) Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "tonalli": "Decisión: ITERAR (no pivotar, no escalar aún). Ajustes recomendados: (1) simplificar la interfaz para subir fotos → integrar botón directo en WhatsApp en lugar del workflow de Make; (2) añadir campos editables a la descripción generada antes de publicar. Hoja de ruta: 3 semanas para ajustes técnicos + 1 semana de re-validación con los mismos 10 usuarios.",
        "preguntas": [
            ("Recomendaciones de ajuste al prototipo", "Por cada hallazgo negativo de la validación: ¿qué cambio específico recomiendas? ¿Por qué ese cambio y no otro?"),
            ("Decisión de pivoteo/iteración/escalamiento (justificada)", "¿Cuál es tu recomendación? ¿Iterar (ajustar el prototipo actual), pivotar (cambiar la dirección), o escalar (implementar a mayor escala)? ¿En qué evidencia de la validación basas esa decisión?"),
            ("Hoja de ruta para la siguiente fase", "¿Qué se hace primero, qué después? Actividades, responsable de cada una y tiempo estimado."),
            ("Requerimientos técnicos y de recursos para la siguiente fase", "¿Qué necesitará la MiPyME en términos de herramientas, personas, presupuesto y tiempo para ejecutar la siguiente fase?"),
        ],
    },
]


# ===========================================================================
# PLANTILLAS POR FORMATO
# (mismo sistema visual que Estándar A; solo cambia la caja de caso pedagógico
#  y los textos de footer/subtitle)
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

.tonalli-box {
  background: #fdf6e3;
  border: 1pt dashed #d4a40e;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  font-style: italic;
  color: #6a5208;
}
.tonalli-box strong { color: #28467e; font-style: normal; }

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
<p class="subtitle">Manual de Desarrollar con IA · Producto del Elemento {elemento}</p>
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

<div class="tonalli-box"><strong>Caso pedagógico Artesanías Tonalli (ilustrativo, NO es tu solución):</strong> {tonalli}</div>

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
Template del Manual de Desarrollar con IA · Para ser llenado por el aspirante con datos de su proyecto real con una MiPyME
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
<p class="subtitle">Manual de Desarrollar con IA · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Excel es el formato natural para esta clase de producto: te permite añadir filas conforme detectes más elementos, ordenar por puntaje y generar gráficas. <strong>Llénalo con datos de TU MiPyME real.</strong></div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="tonalli-box"><strong>Caso pedagógico Artesanías Tonalli (ilustrativo):</strong> {tonalli}</div>

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
Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org · Template del Manual de Desarrollar con IA
</div>

</body>
</html>
"""


# ===========================================================================
# RENDERIZADORES
# ===========================================================================

def render_f21(criterios):
    html = ""
    for c in criterios:
        html += f'<li>{c}</li>\n'
    return html


def render_questions_word(preguntas):
    html = ""
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<div class="question-block">\n'
            f'<div><span class="question-num">{i}</span><span class="question-title">{title}</span></div>\n'
            f'<div class="question-help">{help_text}</div>\n'
            f'<div class="fill-area">[Escribe aquí tu respuesta con datos reales de tu MiPyME. Borra esta línea cuando empieces.]</div>\n'
            f'</div>\n'
        )
    return html


def render_questions_excel(preguntas):
    html = '<table class="matrix">\n<tr><th style="width: 4%;">#</th><th style="width: 28%;">Pregunta guía</th><th>Tu respuesta (llena con datos de TU MiPyME)</th></tr>\n'
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<tr>\n'
            f'<td style="text-align: center; font-weight: bold; color: #28467e;">{i}</td>\n'
            f'<td><strong>{title}</strong><br><span style="color: #666; font-size: 9pt; font-style: italic;">{help_text}</span></td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    html += '</table>\n'
    return html


def render_matrix_extra(num):
    """Matrices estructuradas adicionales según el producto."""

    # 1.4 · Matriz de priorización de oportunidades
    if num == "1.4":
        rows = ""
        for i in range(1, 7):
            rows += (
                f'<tr>\n'
                f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
                f'<td class="fill">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;color:#999;">VI×I/R</td>\n'
                f'<td class="fill">&nbsp;</td>\n'
                f'</tr>\n'
            )
        return f"""
<h2>Hoja de priorización · oportunidades detectadas</h2>
<p style="font-size: 10pt; color: #666;">Añade una fila por oportunidad. Puntúa viabilidad comercial (VI), impacto (I) y recursos necesarios (R, donde 5 = pocos recursos) con valores 1-5. El score orientativo es VI × I / R.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:26%;">Oportunidad</th><th style="width:10%;">Viabilidad comercial (1-5)</th><th style="width:10%;">Impacto (1-5)</th><th style="width:10%;">Recursos necesarios (1-5)</th><th style="width:8%;">Score</th><th>Recomendación</th></tr>
{rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:8pt;font-style:italic;">Convención: mayor viabilidad e impacto suman; mayor necesidad de recursos resta. Adapta la fórmula a tu criterio profesional.</p>
"""

    # 2.2 · Matriz de ideas de solución
    if num == "2.2":
        rows = ""
        for i in range(1, 8):
            rows += (
                f'<tr>\n'
                f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
                f'<td class="fill">&nbsp;</td>\n'
                f'<td class="fill">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;color:#999;">&nbsp;</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
                f'</tr>\n'
            )
        return f"""
<h2>Matriz de ideas · evaluación y selección</h2>
<p style="font-size: 10pt; color: #666;">Una fila por idea. Evalúa cada una con los tres criterios (1-5). La última columna marca si fue seleccionada por el cliente.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:22%;">Idea</th><th style="width:18%;">Descripción breve</th><th style="width:9%;">Novedad (1-5)</th><th style="width:9%;">Utilidad (1-5)</th><th style="width:9%;">Factibilidad (1-5)</th><th style="width:9%;">Score total</th><th>Seleccionada por el cliente</th></tr>
{rows}
</table>
"""

    # 3.2 · Plan de experimentación
    if num == "3.2":
        categories = [
            ("Adaptabilidad", "#e8f4e8", "#2d6a2d"),
            ("Deseabilidad", "#e8eef8", "#28467e"),
            ("Factibilidad", "#fff8e8", "#8a6000"),
            ("Viabilidad", "#f8e8e8", "#8a2000"),
        ]
        hipotesis_rows = ""
        for cat_name, bg, color in categories:
            hipotesis_rows += (
                f'<tr><td colspan="5" style="background:{bg};font-weight:bold;color:{color};padding:6pt 8pt;">'
                f'Categoría: {cat_name}</td></tr>\n'
            )
            for j in range(1, 4):
                hipotesis_rows += (
                    f'<tr>'
                    f'<td style="text-align:center;color:{color};font-weight:bold;">{cat_name[:2]}{j}</td>'
                    f'<td class="fill">&nbsp;</td>'
                    f'<td class="fill">&nbsp;</td>'
                    f'<td class="fill" style="text-align:center;">&nbsp;</td>'
                    f'<td class="fill">&nbsp;</td>'
                    f'</tr>\n'
                )

        prueba_rows = ""
        for i in range(1, 6):
            prueba_rows += (
                f'<tr>'
                f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>'
                f'</tr>\n'
            )

        return f"""
<h2>Hoja de hipótesis · mínimo 3 por categoría</h2>
<p style="font-size: 10pt; color: #666;">Escribe al menos 3 hipótesis por cada categoría. El cliente debe haber participado en su selección.</p>
<table class="matrix">
<tr><th style="width:6%;">ID</th><th style="width:30%;">Hipótesis</th><th style="width:24%;">Métrica de validación</th><th style="width:10%;">Criterio de éxito</th><th>Seleccionada por el cliente</th></tr>
{hipotesis_rows}
</table>

<h2 style="margin-top:24pt;">Diseño de pruebas priorizadas</h2>
<p style="font-size: 10pt; color: #666;">Por cada prueba que ejecutarás: detalla todos los campos que pide el F21.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:18%;">Nombre de la prueba</th><th style="width:14%;">Hipótesis que valida</th><th style="width:14%;">Métricas y criterio de éxito</th><th style="width:8%;">Criticidad</th><th style="width:8%;">Confianza</th><th style="width:8%;">Costo est.</th><th style="width:8%;">Duración</th><th>Responsable</th></tr>
{prueba_rows}
</table>
"""

    # 4.3 · Resultados por hipótesis
    if num == "4.3":
        rows = ""
        for i in range(1, 13):
            rows += (
                f'<tr>'
                f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill">&nbsp;</td>'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>'
                f'</tr>\n'
            )
        return f"""
<h2>Resultados por hipótesis</h2>
<p style="font-size: 10pt; color: #666;">Una fila por hipótesis. Documenta metodología, contexto, condiciones y resultado para cada una.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:18%;">Hipótesis (ID y enunciado)</th><th style="width:18%;">Metodología de la prueba</th><th style="width:20%;">Contexto de realización</th><th style="width:22%;">Condiciones de aplicación</th><th style="width:14%;">Resultado (validada / refutada / parcial)</th></tr>
{rows}
</table>
"""

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
            tonalli=p["tonalli"],
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
            tonalli=p["tonalli"],
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
        # Slug de archivo: num con guiones + slug, ej. "1-1-reporte-inicial.doc"
        slug_num = p["num"].replace(".", "-")
        filename = f"{slug_num}-{p['slug']}.{ext}"
        filepath = OUT / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")

    print(f"\nGenerados {len(PRODUCTS)} templates en {OUT}/")


if __name__ == "__main__":
    main()
