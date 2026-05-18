#!/usr/bin/env python3
"""
Genera los 13 templates de los productos del estándar Implementar IA en
archivos OFIMÁTICOS REALES: .docx (Word), .xlsx (Excel), .pptx (PowerPoint).

Antes se usaba HTML con extensión .doc/.xls/.ppt, lo que provocaba el
warning "el formato no coincide con la extensión" en Office y, en el
caso de PowerPoint, que el archivo simplemente no abriera (PowerPoint
2010+ ya no importa HTML). Ahora se usan python-docx, openpyxl y
python-pptx para producir los formatos OOXML modernos.

Filosofía pedagógica: NO darle la solución al aspirante. Cada template
muestra el criterio F21 oficial + un ejemplo breve del caso La Espiga
(solo para ilustrar el TIPO de contenido) + preguntas guía que el
aspirante responde con datos de SU MiPyME real.

Uso:
    python scripts/generate-templates.py

Requiere:
    pip install python-docx openpyxl python-pptx

Salida: estandar-a/templates/<num>-<slug>.{docx|xlsx|pptx}
"""

from pathlib import Path

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt, RGBColor

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from pptx import Presentation
from pptx.dml.color import RGBColor as PPTColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt as PPTPt

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-a" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Colores y constantes de marca Mi CompañIA
# -----------------------------------------------------------------------------
COLOR_AZUL = "28467E"
COLOR_AMARILLO = "F7C031"
COLOR_AZUL_CLARO = "F0F7FF"
COLOR_AMARILLO_CLARO = "FFF3CC"
COLOR_TAX_BG = "FFE0E0"
COLOR_TAX_FG = "C0392B"
COLOR_GRIS_BG = "FAFAFA"
COLOR_GRIS_BORDE = "DDDDDD"

# Para python-docx y python-pptx (necesitan tupla RGB o RGBColor)
RGB_AZUL = RGBColor(0x28, 0x46, 0x7E)
RGB_AMARILLO = RGBColor(0xF7, 0xC0, 0x31)
RGB_GRIS_TXT = RGBColor(0x66, 0x66, 0x66)
RGB_TAX = RGBColor(0xC0, 0x39, 0x2B)
RGB_BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
RGB_NEGRO_TXT = RGBColor(0x33, 0x33, 0x33)

PPT_AZUL = PPTColor(0x28, 0x46, 0x7E)
PPT_AMARILLO = PPTColor(0xF7, 0xC0, 0x31)
PPT_AMARILLO_CLARO = PPTColor(0xFF, 0xF3, 0xCC)
PPT_AZUL_CLARO = PPTColor(0xF0, 0xF7, 0xFF)
PPT_BLANCO = PPTColor(0xFF, 0xFF, 0xFF)
PPT_GRIS = PPTColor(0x66, 0x66, 0x66)
PPT_TAX = PPTColor(0xC0, 0x39, 0x2B)


# =============================================================================
# DATOS DE LOS 13 PRODUCTOS (criterio F21 + caso Espiga + preguntas guía)
# =============================================================================

PRODUCTS = [
    {
        "num": "1.4.1", "slug": "reporte-evaluacion-inicial", "format": "word",
        "elemento": "1 · Planear", "title": "Reporte de evaluación inicial de la MiPyME",
        "intro": "Es el primer producto del proyecto: una foto del estado actual de la MiPyME, sus objetivos y los recursos disponibles.",
        "f21": [
            "Contiene el perfil empresarial de la MiPyME, giro y número de empleados",
            "Incluye el nombre de la MiPyME, ubicación, email y teléfono de contacto",
            "Contiene el resultado de las acciones aplicadas previamente por el cliente",
            "Contiene las áreas de mejora de oportunidades/problemas a resolver desde la perspectiva del cliente y antigüedad de ello",
            "Incluye los objetivos, indicadores y metas",
            "Indica los recursos, tiempos y entregas esperadas",
            "Se presenta de forma digital/físico sin errores ortográficos",
        ],
        "espiga": "Panadería La Espiga (caso pedagógico del manual): 3 sucursales en una ciudad media, 12 empleados, vende pan tradicional. Doña Beatriz (dueña) y Carlos (hijo, apoyo administrativo) quieren reducir el tiempo que las encargadas pasan respondiendo consultas repetitivas por WhatsApp.",
        "preguntas": [
            ("Perfil empresarial", "¿Cómo describirías a la MiPyME en 2-3 líneas? Giro, número de empleados, antigüedad."),
            ("Datos de contacto", "Nombre legal, ubicación, persona responsable, correo y teléfono."),
            ("Acciones previas del cliente", "¿Qué ha intentado hacer la MiPyME antes para resolver estos problemas? ¿Con qué resultados?"),
            ("Áreas de mejora desde la perspectiva del cliente", "¿Qué problemas u oportunidades identifica la MiPyME? ¿Desde cuándo arrastran cada uno?"),
            ("Objetivos · indicadores · metas", "¿Qué quiere lograr la MiPyME con este proyecto? Para cada objetivo, ¿qué indicador lo mide y cuál es la meta?"),
            ("Recursos · tiempos · entregas esperadas", "¿Con qué presupuesto, equipo humano y tiempos cuenta? ¿Qué entregables espera al cierre?"),
        ],
    },
    {
        "num": "1.4.2", "slug": "informe-disponibilidad-datos", "format": "word",
        "elemento": "1 · Planear", "title": "Informe de disponibilidad y calidad de los datos",
        "intro": "Documenta qué datos tiene la MiPyME para sostener soluciones de IA y cuál es su calidad.",
        "f21": [
            "Contiene las fuentes de información existentes en los procesos operativos",
            "Indica que la información requerida está completa y disponible en tiempo",
            "Incluye las necesidades de optimización/estructuración de los datos previos a la implementación",
            "Contiene los hallazgos detectados en la disponibilidad y calidad de los datos",
        ],
        "espiga": "En La Espiga: pedidos por WhatsApp (sin estructura), libretas de papel por sucursal, contabilidad externa en Excel, ningún CRM. Datos dispersos, sin estandarización entre sucursales.",
        "preguntas": [
            ("Fuentes de información existentes", "¿Dónde viven los datos relevantes para el proceso a intervenir? CRM, ERP, hojas de cálculo, mensajes, correos, papel…"),
            ("Completitud y disponibilidad en tiempo", "Por cada fuente: ¿los datos están completos? ¿se actualizan a tiempo? ¿qué frecuencia?"),
            ("Necesidades de optimización/estructuración", "¿Qué hay que limpiar, estandarizar, deduplicar o estructurar antes de poder usarlos con IA?"),
            ("Hallazgos relevantes", "Lo más notable que descubriste sobre la calidad de los datos. ¿Qué obstáculos representa esto para las soluciones que quieres implementar?"),
        ],
    },
    {
        "num": "1.4.3", "slug": "informe-diagnostico-procesos", "format": "word",
        "elemento": "1 · Planear", "title": "Informe de diagnóstico de procesos, actividades y áreas",
        "intro": "Mapea los procesos operativos y detecta los cuellos de botella + resistencias al cambio.",
        "f21": [
            "Contiene el mapa de los procesos analizados",
            "Incluye la clasificación de los procesos por área funcional",
            "Contiene los cuellos de botella y los principales puntos de dolor identificados",
            "Menciona las resistencias al cambio detectadas durante el diagnóstico",
        ],
        "espiga": "Mapa de La Espiga: 6 procesos analizados (recepción de pedidos, producción, venta en mostrador, control de inventario, cobro, contabilidad). Cuello clave: las encargadas pierden 4-5 horas/semana atendiendo consultas repetitivas en WhatsApp. Resistencia: dos panaderos veteranos desconfían de 'que la máquina les diga qué hornear'.",
        "preguntas": [
            ("Mapa de procesos analizados", "Dibuja o describe los procesos que analizaste. Indica qué hace cada uno y cómo se conectan. (Inserta una imagen del mapa si lo dibujaste en Miro/Lucidchart/papel)."),
            ("Clasificación por área funcional", "Agrupa los procesos: ventas, operación, administración, soporte, atención a cliente… ¿Cuál concentra más procesos críticos?"),
            ("Cuellos de botella y puntos de dolor", "Por cada proceso analizado: ¿dónde se atasca? ¿cuánto tiempo se pierde? ¿qué errores ocurren? ¿quién sufre el impacto?"),
            ("Resistencias al cambio detectadas", "Durante el diagnóstico, ¿qué personas mostraron resistencia? ¿Qué temen perder o no entienden? Es información valiosa para la fase de capacitación."),
        ],
    },
    {
        "num": "1.4.4", "slug": "reporte-madurez-digital", "format": "word",
        "elemento": "1 · Planear", "title": "Reporte de madurez digital y disposición al cambio",
        "intro": "Evalúa qué tan preparada está la MiPyME (tecnología) y su personal (cultura) para incorporar IA.",
        "f21": [
            "Incluye la descripción de la metodología y la herramienta utilizadas",
            "Contiene los resultados del test aplicado",
            "Incluye el nivel de madurez digital por dimensión evaluada",
            "Contiene descrito el nivel de disposición al cambio por parte del personal",
            "Incluye recomendaciones basadas en los resultados obtenidos",
            "Incluye un tablero base de indicadores para el seguimiento de la transformación digital",
        ],
        "espiga": "La Espiga obtuvo nivel 2 de 5 en madurez digital (uso de WhatsApp sí, CRM no, datos integrados no). Disposición al cambio: alta en Carlos (28 años), media en las 3 encargadas (40-55), baja en Doña Beatriz al inicio del proyecto (se 'destrabó' tras ver el primer piloto del chatbot).",
        "preguntas": [
            ("Metodología y herramienta usada", "¿Qué instrumento aplicaste para medir madurez digital? (Cuestionario, entrevistas, observación, test estandarizado). ¿Por qué lo elegiste?"),
            ("Resultados del test aplicado", "Resultados crudos por dimensión: infraestructura, procesos, personas, datos, cultura. Apóyate de una tabla."),
            ("Nivel de madurez digital por dimensión", "Clasificación (inicial, en desarrollo, intermedio, avanzado) por cada dimensión. ¿Cuál es la dimensión más débil? ¿Cuál es la fortaleza?"),
            ("Disposición al cambio del personal", "Por persona o grupo: ¿qué tan abierta está al cambio? ¿Qué evidencia observaste durante el diagnóstico?"),
            ("Recomendaciones basadas en resultados", "Acciones específicas para mejorar la madurez en las dimensiones bajas + estrategia para destrabar las resistencias detectadas."),
            ("Tablero base de indicadores", "¿Qué indicadores propondrás seguir mes a mes? Define mínimo 3-5 indicadores con su línea base actual + meta esperada a 6/12 meses."),
        ],
    },
    {
        "num": "1.4.5", "slug": "matriz-impacto-viabilidad", "format": "excel",
        "elemento": "1 · Planear", "title": "Matriz de impacto, viabilidad y esfuerzo",
        "intro": "Hoja de cálculo para priorizar las oportunidades de IA detectadas. Asigna puntajes (1-5) por impacto, viabilidad y esfuerzo; la matriz revela cuáles atacar primero.",
        "f21": [
            "Contiene descritas las soluciones de IA para su aplicación en los procesos priorizados",
            "Incluye las tecnologías/herramientas/plataformas sugeridas de IA adecuadas al contexto de la empresa",
            "Contiene la priorización de las oportunidades de soluciones de IA",
            "Incluye los beneficios esperados para la MiPyME y la viabilidad de la implementación",
        ],
        "espiga": "En La Espiga se identificaron 5 oportunidades. Las dos con mayor impacto + viabilidad (chatbot WhatsApp para FAQ + reporte automatizado de pedidos a cocina) fueron las recomendadas para primera fase.",
        "preguntas": [
            ("Oportunidades detectadas", "Lista todas las oportunidades de IA que detectaste en el diagnóstico. Una por fila."),
            ("Herramienta/plataforma sugerida", "Por cada oportunidad: ¿qué herramienta de IA existente la resolvería? (ChatGPT, Claude, Zapier, Make, CRM con módulo de IA, etc.)"),
            ("Puntaje de IMPACTO (1-5)", "¿Cuánto valor genera? (Tiempo ahorrado, ingresos adicionales, errores reducidos, mejor experiencia). 5 = alto."),
            ("Puntaje de VIABILIDAD (1-5)", "¿Qué tan fácil es de implementar dados los recursos actuales de la MiPyME? 5 = muy viable."),
            ("Puntaje de ESFUERZO (1-5)", "¿Cuánto trabajo cuesta? (Tiempo + personas + costo). 5 = poco esfuerzo, 1 = mucho esfuerzo."),
            ("Beneficios esperados", "Breve frase por oportunidad: ¿qué mejora medible esperas?"),
            ("Priorización final", "Las 2-3 oportunidades recomendadas para primera fase, y por qué."),
        ],
    },
    {
        "num": "1.4.6", "slug": "hoja-de-ruta", "format": "excel",
        "elemento": "1 · Planear", "title": "Hoja de ruta de implementación de soluciones de IA",
        "intro": "Cronograma tipo Gantt con las fases, actividades, responsables y recursos del proyecto.",
        "f21": [
            "Contiene descritas las soluciones de IA seleccionadas para la MiPyME",
            "Contiene descritas la operación de los procesos con la solución de IA",
            "Incluye las fases/etapas de implementación del proyecto",
            "Incluye las actividades y responsables de cada etapa",
            "Contiene el cronograma con las actividades de implementación para cada etapa del proyecto",
            "Incluye los recursos tecnológicos, humanos y financieros requeridos",
            "Incluye indicadores para evaluar el avance de la implementación y darle seguimiento al proyecto",
        ],
        "espiga": "En La Espiga: 4 fases en 5 semanas. S1 configuración del chatbot + plantillas de respuestas FAQ; S2 configuración del reporte automatizado de pedidos; S3 piloto con sucursal principal; S4 expansión a las 3 sucursales + capacitación; S5 evaluación y ajustes.",
        "preguntas": [
            ("Soluciones seleccionadas (de la matriz 1.4.5)", "Lista las soluciones que efectivamente vas a implementar."),
            ("Operación del proceso CON la solución", "Por cada solución: descripción de cómo quedará el proceso después de implementada."),
            ("Fases del proyecto", "¿Cuántas fases tendrá el proyecto? Para cada una: nombre + objetivo + tiempo estimado."),
            ("Actividades y responsables por fase", "Lista granular de actividades. Quién hace qué de tu lado + del lado de la MiPyME."),
            ("Cronograma (Gantt)", "Tabla con actividades en filas y semanas/quincenas en columnas. Marca con X cuándo se ejecuta cada actividad."),
            ("Recursos tecnológicos / humanos / financieros", "Equipo, suscripciones, plataformas, equipo humano, presupuesto desglosado por fase."),
            ("Indicadores de seguimiento", "¿Cómo sabrás semana a semana si vas en tiempo y con calidad? Define indicadores de proceso."),
        ],
    },
    {
        "num": "1.4.7", "slug": "propuesta-final-implementacion", "format": "word",
        "elemento": "1 · Planear", "title": "Propuesta final de implementación integrada",
        "intro": "Documento maestro de entrega al emprendedor que integra los productos previos en una narrativa coherente.",
        "f21": [
            "Contiene el informe de diagnóstico de procesos, actividades y áreas de trabajo (1.4.3)",
            "Incluye el reporte de madurez digital y disposición al cambio (1.4.4)",
            "Contiene la matriz de impacto, viabilidad y esfuerzo (1.4.5)",
            "Incluye la hoja de ruta de implementación de soluciones de IA (1.4.6)",
            "Contiene la propuesta económica de consultoría (1.4.8)",
            "Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "espiga": "Para La Espiga: documento maestro de 18-25 páginas. Resumen ejecutivo de 1 pág → diagnóstico → madurez → matriz → hoja de ruta → propuesta económica → anexos. Pensado para que Doña Beatriz lo lea en 20 minutos y entienda exactamente qué pasará.",
        "preguntas": [
            ("Resumen ejecutivo (1 pág)", "Página única que sintetiza: contexto + oportunidades priorizadas + propuesta + inversión + resultados esperados. Si el cliente solo lee esta página, debe entender qué va a pasar."),
            ("Diagnóstico integrado (referencia a 1.4.3)", "Incorpora el informe de diagnóstico o haz un resumen + adjunta el original como anexo."),
            ("Madurez digital y disposición al cambio (referencia a 1.4.4)", "Incluye el reporte o resumen + tablero base."),
            ("Matriz de oportunidades (referencia a 1.4.5)", "Incluye la matriz priorizada — destaca las oportunidades recomendadas para primera fase."),
            ("Hoja de ruta (referencia a 1.4.6)", "Cronograma maestro visible + recursos requeridos."),
            ("Propuesta económica (referencia a 1.4.8)", "Esquema de inversión + propuesta económica detallada — termina llevando al visto bueno por escrito."),
            ("Anexos", "Documentos de soporte: instrumentos del diagnóstico, capturas, evidencias."),
        ],
    },
    {
        "num": "1.4.8", "slug": "propuesta-economica-validada", "format": "word",
        "elemento": "1 · Planear", "title": "Propuesta económica de consultoría validada",
        "intro": "Documento contractual con la inversión + dos REQUISITOS TAXATIVOS del F21: visto bueno por escrito + acuerdo de confidencialidad.",
        "f21": [
            "Contiene la metodología para la implementación de soluciones de IA",
            "Incluye el cronograma, actividades y áreas de trabajo",
            "Contiene descrita la propuesta del monto de inversión por la aplicación del diagnóstico y el test de madurez digital y disposición al cambio",
            "Incluye la evidencia POR ESCRITO del visto bueno por parte de la persona responsable de la MiPyME (REQUISITO TAXATIVO)",
            "Incluye el acuerdo de confidencialidad (REQUISITO TAXATIVO)",
        ],
        "espiga": "Para La Espiga: honorarios profesionales + suscripción mensual de herramientas. Doña Beatriz firmó visto bueno el 15 de marzo + NDA simple de 1 página. Sin esos documentos firmados el evaluador NO da el producto por cumplido.",
        "preguntas": [
            ("Metodología para la implementación", "¿Con qué enfoque vas a ejecutar el proyecto? Pasos generales, principios que guiarán las decisiones."),
            ("Cronograma + áreas de trabajo + actividades", "Síntesis del cronograma + en qué área de la MiPyME ocurre cada actividad."),
            ("Propuesta económica detallada", "Honorarios profesionales (consultor) + costos de licencias/herramientas + otros costos. Total + forma de pago + hitos de cobro si aplica."),
            ("Visto bueno POR ESCRITO del emprendedor", "¿Cómo obtuviste el visto bueno? (Firma autógrafa, electrónica, correo de aprobación explícita, acuse). Adjunta o describe el documento."),
            ("Acuerdo de confidencialidad firmado", "Convenio entre las partes. Adjunta o describe el acuerdo y sus firmas."),
        ],
    },
    {
        "num": "3.4.1", "slug": "soluciones-implementadas", "format": "word",
        "elemento": "2 · Ejecutar", "title": "Inventario de soluciones de IA implementadas",
        "intro": "El producto 3.4.1 NO es documental: es la solución MISMA funcionando. Este template sirve como inventario que documenta lo implementado para la evaluación.",
        "f21": [
            "Se encuentran configuradas en el entorno tecnológico de la MiPyME conforme al plan de implementación definido",
            "Operan en al menos un proceso administrativo/operativo/comercial del negocio de la MiPyME",
            "Incluyen la descripción del caso de uso para el cual fueron implementadas",
            "Contiene evidencia de funcionamiento en condiciones reales de operación",
            "Especifican las herramientas/plataformas de IA utilizadas",
            "Indican el nombre del usuario responsable de la operación dentro de la MiPyME",
        ],
        "espiga": "Inventario para La Espiga: 2 soluciones operando. (1) Chatbot WhatsApp para FAQ desde el 1 de abril, atiende ~80 consultas/día. (2) Reporte automatizado de pedidos del día desde el 5 de abril, ahorra 30 min/día.",
        "preguntas": [
            ("Solución implementada · nombre y proceso intervenido", "Por cada solución: nombre comercial + proceso operativo donde funciona ahora."),
            ("Caso de uso documentado", "¿Para qué se implementó? ¿Qué problema concreto resuelve?"),
            ("Evidencia de funcionamiento", "Capturas, registros de uso, métricas de las últimas 2-4 semanas. (Adjunta como anexos si son muchas)."),
            ("Herramienta/plataforma de IA utilizada", "Nombre comercial exacto + módulo o versión."),
            ("Usuario responsable de la operación", "Quién en la MiPyME opera cada solución (nombre + cargo)."),
            ("Cumplimiento del plan de implementación (1.4.6)", "Cada solución, ¿se desplegó conforme al cronograma? Si hubo desviaciones, ¿por qué?"),
        ],
    },
    {
        "num": "3.4.2", "slug": "informe-tecnico-configuracion", "format": "word",
        "elemento": "2 · Ejecutar", "title": "Informe técnico de configuración",
        "intro": "Manual técnico para que la MiPyME mantenga las soluciones después de tu consultoría. Es exhaustivo.",
        "f21": [
            "Contiene la descripción de las herramientas/plataformas de IA configuradas y su propósito",
            "Incluye los parámetros de configuración aplicados en cada herramienta",
            "Contiene especificadas las integraciones realizadas con sistemas/plataformas/procesos existentes",
            "Incluye los requisitos técnicos necesarios para el funcionamiento",
            "Incluye los elementos de ciberseguridad considerados + leyes y normas aplicables",
            "Contiene los accesos y permisos configurados para los usuarios de la MiPyME",
            "Contiene los resultados de las pruebas funcionales (funcionamiento/integración/uso en condiciones reales)",
            "Contiene especificados los indicadores de desempeño obtenidos durante la fase de pruebas",
            "Se presenta en formato digital, con redacción clara y sin errores ortográficos",
        ],
        "espiga": "Informe técnico de La Espiga: 14 páginas que documentan cada parámetro del chatbot WhatsApp, la integración con Google Sheets para registrar pedidos, los permisos de las 3 encargadas + Carlos, y los resultados de 15 pruebas funcionales ejecutadas antes del go-live.",
        "preguntas": [
            ("Resumen ejecutivo", "Una página: qué se implementó, en qué entorno, con qué arquitectura general."),
            ("Arquitectura general", "Diagrama de cómo se conectan las herramientas entre sí y con los procesos de la MiPyME."),
            ("Herramientas + propósito + parámetros", "Por cada herramienta: nombre comercial, propósito en la MiPyME, todos los parámetros de configuración aplicados."),
            ("Integraciones realizadas", "¿Con qué sistemas existentes se conectó cada herramienta? (CRM, hojas de cálculo, plataformas de mensajería, etc.)"),
            ("Requisitos técnicos", "Conectividad, navegadores, sistemas operativos, suscripciones que la MiPyME necesita mantener."),
            ("Ciberseguridad + normativa aplicable", "Medidas de seguridad implementadas + cumplimiento LFPDPPP (mínimo Arts. 5-12 principios + 7,8,14 aviso de privacidad + 36-37 transferencias + 22-34 ARCO + 63-68 sanciones)."),
            ("Accesos y permisos configurados", "Tabla con cada usuario + rol + nivel de acceso por herramienta."),
            ("Pruebas funcionales ejecutadas", "Lista de pruebas (funcionamiento, integración, uso en condiciones reales) + resultados de cada una."),
            ("Indicadores de desempeño en pruebas", "Métricas obtenidas durante las pruebas: tiempo de respuesta, precisión, errores, etc."),
        ],
    },
    {
        "num": "3.4.3", "slug": "material-capacitacion", "format": "ppt",
        "elemento": "2 · Ejecutar", "title": "Material de capacitación al personal",
        "intro": "Presentación visual que el personal de la MiPyME usará para operar las soluciones de forma autónoma. Por eso es PowerPoint, no Word: el personal aprende mejor con visuales paso a paso.",
        "f21": [
            "Contiene las instrucciones paso a paso para operar cada herramienta de IA implementada",
            "Incluye ejemplos de uso aplicados al contexto específico de la MiPyME",
            "Especifica los prompts o instrucciones recomendadas para cada herramienta de IA",
            "Incluye las buenas prácticas de uso y las acciones a realizar ante errores frecuentes",
            "Considera el nivel de alfabetización digital del personal capacitado",
            "Se presenta en formato digital, accesible y comprensible para el personal de la MiPyME",
        ],
        "espiga": "Material de La Espiga: presentación de 12 láminas + 3 prompts pre-cargados. Pensada para encargadas con uso intermedio de smartphone pero sin experiencia previa con asistentes de IA. Lenguaje sencillo, capturas grandes, lista de 'qué hacer si algo no funciona'.",
        "preguntas": [
            ("Bienvenida y objetivos del material", "¿Qué van a aprender? ¿Cuánto tiempo tomará? ¿Para qué les servirá en su día a día?"),
            ("Instrucciones paso a paso por herramienta", "Por cada herramienta: capturas numeradas con el flujo completo de uso. Si la herramienta tiene 5 botones importantes, dedica 1 lámina por botón. Visual antes que texto."),
            ("Ejemplos aplicados al contexto de la MiPyME", "Por cada herramienta: 2-3 ejemplos REALES de la MiPyME (no ejemplos genéricos). El personal debe poder decir 'ah, eso lo hago yo el lunes en la mañana'."),
            ("Prompts recomendados", "Lista de 5-10 prompts que ya funcionan para los casos típicos. El personal los copia/pega; no se les pide redactar prompts desde cero."),
            ("Errores frecuentes y qué hacer", "Tabla con: error común → cómo identificarlo → cómo resolverlo → cuándo escalar al consultor o a Carlos/Doña Beatriz."),
            ("Adaptación al nivel digital del personal", "Si el personal no maneja tecnicismos, usa lenguaje cotidiano. Si están acostumbrados a apps, puedes ir más rápido."),
            ("Recursos y soporte", "¿A quién acudir si algo falla? ¿Dónde encontrar este material después? ¿Cuándo se actualiza?"),
        ],
    },
    {
        "num": "4.4.1", "slug": "reporte-evaluacion-resultados", "format": "excel",
        "elemento": "3 · Evaluar", "title": "Reporte de evaluación de resultados",
        "intro": "Hoja de cálculo con la comparación antes/después de cada indicador + tablero visual + estimación de ROI.",
        "f21": [
            "Contiene la comparación de los indicadores de desempeño de los procesos antes y después de la implementación",
            "Incluye el tablero de indicadores integrando resultados cuantitativos y cualitativos en los procesos intervenidos",
            "Contiene el impacto operativo de las soluciones (tiempos, Retorno de inversión, errores reducidos)",
            "Incluye el registro de incidencias presentadas durante la operación y las acciones correctivas aplicadas",
            "Contiene especificadas el nivel de adopción de las soluciones por parte del personal de la MiPyME",
            "Se presenta en formato digital/físico, con redacción clara y sin errores ortográficos",
        ],
        "espiga": "Reporte de La Espiga: tabla comparativa de 5 indicadores (tiempo de respuesta WhatsApp, consultas atendidas/día, horas semanales en tareas repetitivas, errores en pedidos, ventas online). Resultado: ROI estimado 280% a 6 meses. 1 incidencia mayor (caída del chatbot 2 horas el 18 de abril) con su acción correctiva documentada.",
        "preguntas": [
            ("Indicadores · línea base · valor actual · variación", "Tabla con cada indicador del proyecto, su valor antes de la implementación, su valor actual, y la variación porcentual."),
            ("Tablero de indicadores integrado", "Visualización gráfica (puedes generar gráficas con Excel mismo) con resultados cuantitativos + cualitativos."),
            ("Impacto operativo", "Tiempo ahorrado, ingresos adicionales, errores reducidos. Cuantifica todo lo cuantificable."),
            ("Cálculo del ROI", "Beneficios obtenidos / costo total del proyecto × 100. Documenta los supuestos."),
            ("Registro de incidencias + acciones correctivas", "Tabla con cada incidencia: fecha, qué ocurrió, qué hiciste para corregirla, qué se aprendió."),
            ("Nivel de adopción del personal", "¿Cuántas personas operan cada solución activamente? ¿Qué porcentaje del personal capacitado la usa? Evidencia: logs, encuesta a usuarios."),
            ("Lecciones y recomendaciones", "Resumen ejecutivo de lo que funcionó, lo que no, y recomendaciones de mejora continua."),
        ],
    },
    {
        "num": "4.4.2", "slug": "acta-de-cierre", "format": "word",
        "elemento": "3 · Evaluar", "title": "Acta de cierre del proyecto",
        "intro": "Documento legal de cierre. CRÍTICO: requiere firmas de ambas partes + contactos de soporte. Sin estos elementos el evaluador NO da por cumplido el producto.",
        "f21": [
            "Contiene el resumen ejecutivo del proyecto: alcance, objetivos y resultados obtenidos",
            "Incluye el listado de las soluciones de IA implementadas y su estado operativo al cierre",
            "Incluye las lecciones aprendidas durante el proyecto de implementación",
            "Contiene descritos los compromisos pendientes y próximos pasos acordados entre ambas partes",
            "Contiene los contactos de soporte técnico para incidencias futuras (REQUISITO TAXATIVO)",
            "Incluye las firmas del consultor y del representante de la MiPyME (REQUISITO TAXATIVO)",
            "Se presenta en formato digital/físico, sin errores ortográficos",
        ],
        "espiga": "Acta de La Espiga firmada el 30 de mayo por Doña Beatriz y por el consultor. Compromisos pendientes: revisar el chatbot en julio para añadir 10 nuevas FAQ. Contacto de soporte: correo + WhatsApp del consultor. Lección clave registrada: 'capacitar PRIMERO a las personas más abiertas al cambio, luego ellas convencen a las escépticas'.",
        "preguntas": [
            ("Resumen ejecutivo del proyecto", "Alcance original, objetivos planteados, resultados obtenidos. Una página."),
            ("Soluciones implementadas + estado al cierre", "Lista de cada solución + estado: operando / operando con incidencias / pausada / cancelada."),
            ("Lecciones aprendidas", "Lo que funcionó, lo que no, lo que harías diferente. 5-7 lecciones específicas."),
            ("Compromisos pendientes y próximos pasos", "Si quedó algo a futuro: qué, cuándo, responsable. Si no quedó nada pendiente, decláralo explícitamente."),
            ("Contactos de soporte técnico (REQUISITO TAXATIVO)", "Datos completos del consultor para incidencias futuras: nombre, correo, teléfono, horario de respuesta esperado."),
            ("Firmas (REQUISITO TAXATIVO)", "Firma del consultor + firma del representante legal o emprendedor de la MiPyME. Físicas o digitales con valor legal."),
        ],
    },
]


# =============================================================================
# UTILIDADES python-docx
# =============================================================================

def _shade_cell(cell, hex_color):
    """Aplica color de fondo a una celda de tabla Word."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tc_pr.append(shd)


def _set_cell_border(cell, color="DDDDDD", sz=4):
    """Bordes delgados a las celdas."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        b = OxmlElement(f'w:{edge}')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), str(sz))
        b.set(qn('w:color'), color)
        tc_borders.append(b)
    tc_pr.append(tc_borders)


def _add_brand_header(doc, prod):
    """Encabezado de marca: bloque azul/amarillo + título + meta."""
    table = doc.add_table(rows=1, cols=3)
    table.autofit = False
    widths = (Cm(2.6), Cm(11.5), Cm(3.5))
    for col, w in zip(table.columns, widths):
        col.width = w
    for cell, w in zip(table.rows[0].cells, widths):
        cell.width = w
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    brand_cell, title_cell, meta_cell = table.rows[0].cells
    _shade_cell(brand_cell, COLOR_AZUL)
    p = brand_cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Mi\nCompañIA")
    run.font.color.rgb = RGB_AMARILLO
    run.font.bold = True
    run.font.size = Pt(11)

    p_t = title_cell.paragraphs[0]
    run = p_t.add_run(prod["title"])
    run.font.color.rgb = RGB_AZUL
    run.font.bold = True
    run.font.size = Pt(15)
    p_sub = title_cell.add_paragraph()
    run = p_sub.add_run(f"Producto {prod['num']} · Elemento {prod['elemento']}")
    run.font.color.rgb = RGB_GRIS_TXT
    run.font.size = Pt(9.5)

    p_m = meta_cell.paragraphs[0]
    p_m.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p_m.add_run(f"{prod['num']}\n")
    run.font.color.rgb = RGB_AZUL
    run.font.bold = True
    run.font.size = Pt(11)
    run = p_m.add_run("Estándar A · Implementar IA\nFUNDES · MiPyMEs")
    run.font.color.rgb = RGB_GRIS_TXT
    run.font.size = Pt(8.5)

    # línea amarilla divisora
    sep = doc.add_paragraph()
    p_pr = sep._p.get_or_add_pPr()
    p_bdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '18')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), COLOR_AMARILLO)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def _add_project_data_block(doc):
    """Bloque azul claro con datos del proyecto para llenar."""
    table = doc.add_table(rows=4, cols=2)
    table.autofit = False
    widths = (Cm(4.5), Cm(13.0))
    for col, w in zip(table.columns, widths):
        col.width = w
    rows_data = [
        ("Nombre de la MiPyME:", ""),
        ("Responsable del proyecto:", ""),
        ("Fecha de elaboración:", ""),
        ("Versión:", ""),
    ]
    for i, (label, value) in enumerate(rows_data):
        cells = table.rows[i].cells
        for c in cells:
            _shade_cell(c, COLOR_AZUL_CLARO)
            _set_cell_border(c, color="CCE0F5", sz=4)
        cells[0].width = widths[0]
        cells[1].width = widths[1]
        p = cells[0].paragraphs[0]
        r = p.add_run(label)
        r.font.bold = True
        r.font.color.rgb = RGB_AZUL
        r.font.size = Pt(10)
        cells[1].paragraphs[0].add_run("__________________________________________________").font.color.rgb = RGBColor(0x99, 0x99, 0x99)
    doc.add_paragraph()


def _add_intro_box(doc, text):
    """Caja amarilla suave con la introducción."""
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(17.5)
    cell = t.rows[0].cells[0]
    cell.width = Cm(17.5)
    _shade_cell(cell, COLOR_AMARILLO_CLARO)
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '18')
    left.set(qn('w:color'), COLOR_AMARILLO)
    tc_borders.append(left)
    tc_pr.append(tc_borders)
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    doc.add_paragraph()


def _add_f21_box(doc, criterios):
    """Caja con el criterio F21 literal del estándar."""
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(17.5)
    cell = t.rows[0].cells[0]
    _shade_cell(cell, COLOR_AZUL_CLARO)
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '18')
    left.set(qn('w:color'), '1F4E8C')
    tc_borders.append(left)
    tc_pr.append(tc_borders)

    p = cell.paragraphs[0]
    r = p.add_run("CRITERIO F21 · LO QUE EL EVALUADOR VERIFICA")
    r.font.bold = True
    r.font.color.rgb = RGB_AZUL
    r.font.size = Pt(10)
    for c in criterios:
        para = cell.add_paragraph()
        para.paragraph_format.left_indent = Cm(0.4)
        is_tax = "REQUISITO TAXATIVO" in c
        clean = c.replace("(REQUISITO TAXATIVO)", "").strip()
        bullet = para.add_run("•  ")
        bullet.font.color.rgb = RGB_AZUL
        bullet.font.bold = True
        bullet.font.size = Pt(10)
        run = para.add_run(clean)
        run.font.size = Pt(10)
        run.font.color.rgb = RGB_NEGRO_TXT
        if is_tax:
            para.add_run("  ")
            tax_run = para.add_run(" REQUISITO TAXATIVO ")
            tax_run.font.bold = True
            tax_run.font.color.rgb = RGB_BLANCO
            tax_run.font.size = Pt(8)
            # fondo rojo al run mediante shading no es trivial — usamos
            # caracteres y un color de fuente fuerte para llamar la atención
            # adicional con un fondo amarillo del run:
            rPr = tax_run._r.get_or_add_rPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), COLOR_TAX_FG)
            rPr.append(shd)
    doc.add_paragraph()


def _add_espiga_box(doc, text):
    """Caja crema con el caso La Espiga (solo ilustrativo)."""
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(17.5)
    cell = t.rows[0].cells[0]
    _shade_cell(cell, "FDF6E3")
    _set_cell_border(cell, color="D4A40E", sz=4)
    p = cell.paragraphs[0]
    r = p.add_run("Ejemplo orientativo (caso La Espiga) — NO copies esto a tu MiPyME")
    r.font.bold = True
    r.font.color.rgb = RGB_AZUL
    r.font.size = Pt(9.5)
    para = cell.add_paragraph()
    r = para.add_run(text)
    r.font.italic = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x6A, 0x52, 0x08)
    doc.add_paragraph()


def _add_question_block(doc, idx, title, help_text):
    """Bloque pregunta con número, título, ayuda y zona para llenar."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    n = p.add_run(f"  {idx}  ")
    n.font.bold = True
    n.font.color.rgb = RGB_BLANCO
    n.font.size = Pt(11)
    rPr = n._r.get_or_add_rPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), COLOR_AZUL)
    rPr.append(shd)
    sp = p.add_run("  ")
    sp.font.size = Pt(11)
    t = p.add_run(title)
    t.font.bold = True
    t.font.color.rgb = RGB_AZUL
    t.font.size = Pt(12)

    h = doc.add_paragraph()
    h.paragraph_format.left_indent = Cm(1.0)
    h_r = h.add_run(help_text)
    h_r.font.italic = True
    h_r.font.size = Pt(10)
    h_r.font.color.rgb = RGB_GRIS_TXT

    # zona para llenar (tabla 1x1 con fondo gris suave)
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(16.5)
    cell = t.rows[0].cells[0]
    cell.width = Cm(16.5)
    _shade_cell(cell, COLOR_GRIS_BG)
    _set_cell_border(cell, color=COLOR_GRIS_BORDE, sz=4)
    p_in = cell.paragraphs[0]
    p_in.paragraph_format.left_indent = Cm(0.3)
    r = p_in.add_run("[ Escribe aquí la respuesta para TU MiPyME. Borra este marcador antes de presentar. ]")
    r.font.italic = True
    r.font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)
    r.font.size = Pt(10)
    # añadir altura mínima al bloque vía 3 párrafos vacíos
    for _ in range(3):
        cell.add_paragraph()
    doc.add_paragraph()


def _add_footer(doc, prod):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(20)
    r = p.add_run(f"Producto {prod['num']} · Mi CompañIA · FUNDES · Iniciativa AIxMiPyMEs")
    r.font.size = Pt(8)
    r.font.italic = True
    r.font.color.rgb = RGBColor(0x99, 0x99, 0x99)


# =============================================================================
# GENERADOR WORD (.docx)
# =============================================================================

def generate_word(prod):
    doc = Document()
    # margenes
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(1.8)
        section.right_margin = Cm(1.8)

    _add_brand_header(doc, prod)
    _add_project_data_block(doc)
    _add_intro_box(doc, prod["intro"])
    _add_f21_box(doc, prod["f21"])
    _add_espiga_box(doc, prod["espiga"])

    h = doc.add_paragraph()
    r = h.add_run("Preguntas guía para construir el producto")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGB_AZUL
    p_pr = h._p.get_or_add_pPr()
    p_bdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '8')
    bottom.set(qn('w:color'), COLOR_AMARILLO)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)

    for i, (title, help_text) in enumerate(prod["preguntas"], start=1):
        _add_question_block(doc, i, title, help_text)

    _add_footer(doc, prod)
    return doc


# =============================================================================
# UTILIDADES openpyxl
# =============================================================================

THIN = Side(style="thin", color="DDDDDD")
BORDER_ALL = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
BORDER_NONE = Border()
FILL_AZUL = PatternFill("solid", fgColor=COLOR_AZUL)
FILL_AZUL_CLARO = PatternFill("solid", fgColor=COLOR_AZUL_CLARO)
FILL_AMARILLO = PatternFill("solid", fgColor=COLOR_AMARILLO)
FILL_AMARILLO_CLARO = PatternFill("solid", fgColor=COLOR_AMARILLO_CLARO)
FILL_GRIS = PatternFill("solid", fgColor=COLOR_GRIS_BG)
FILL_ESPIGA = PatternFill("solid", fgColor="FDF6E3")
FILL_TAX = PatternFill("solid", fgColor=COLOR_TAX_FG)
FILL_F21 = PatternFill("solid", fgColor=COLOR_AZUL_CLARO)
ALIGN_WRAP = Alignment(wrap_text=True, vertical="top")
ALIGN_WRAP_CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

FONT_TITULO = Font(name="Calibri", size=16, bold=True, color=COLOR_AZUL)
FONT_SUB = Font(name="Calibri", size=10, color="666666")
FONT_HEADER = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
FONT_BOLD_AZUL = Font(name="Calibri", size=11, bold=True, color=COLOR_AZUL)
FONT_NORMAL = Font(name="Calibri", size=10, color="333333")
FONT_HELP = Font(name="Calibri", size=9, italic=True, color="666666")
FONT_BRAND = Font(name="Calibri", size=11, bold=True, color=COLOR_AMARILLO)


def _ws_brand_header(ws, prod, total_cols=8):
    """Bloque de encabezado de marca en hoja de Excel."""
    ws.merge_cells(start_row=1, start_column=1, end_row=2, end_column=1)
    cell = ws.cell(row=1, column=1, value="Mi\nCompañIA")
    cell.fill = FILL_AZUL
    cell.font = FONT_BRAND
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.column_dimensions["A"].width = 11

    ws.merge_cells(start_row=1, start_column=2, end_row=1, end_column=total_cols)
    cell = ws.cell(row=1, column=2, value=prod["title"])
    cell.font = FONT_TITULO
    cell.alignment = Alignment(horizontal="left", vertical="center")

    ws.merge_cells(start_row=2, start_column=2, end_row=2, end_column=total_cols)
    cell = ws.cell(row=2, column=2, value=f"Producto {prod['num']} · Elemento {prod['elemento']} · Estándar A · Implementar IA")
    cell.font = FONT_SUB
    cell.alignment = Alignment(horizontal="left", vertical="center")

    ws.row_dimensions[1].height = 28
    ws.row_dimensions[2].height = 18

    # franja amarilla
    ws.row_dimensions[3].height = 6
    for c in range(1, total_cols + 1):
        ws.cell(row=3, column=c).fill = FILL_AMARILLO


def _ws_meta_block(ws, start_row, total_cols=8):
    """Bloque de datos del proyecto."""
    row = start_row
    labels = ["Nombre de la MiPyME:", "Responsable del proyecto:", "Fecha de elaboración:", "Versión:"]
    for i, label in enumerate(labels):
        ws.cell(row=row + i, column=1, value=label).font = FONT_BOLD_AZUL
        ws.cell(row=row + i, column=1).fill = FILL_AZUL_CLARO
        ws.merge_cells(start_row=row + i, start_column=2, end_row=row + i, end_column=total_cols)
        c = ws.cell(row=row + i, column=2, value="")
        c.fill = FILL_AZUL_CLARO
        c.border = Border(bottom=Side(style="thin", color="999999"))
        ws.row_dimensions[row + i].height = 22
    return row + len(labels)


def _ws_intro(ws, start_row, text, total_cols=8):
    ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=total_cols)
    c = ws.cell(row=start_row, column=1, value=text)
    c.fill = FILL_AMARILLO_CLARO
    c.font = Font(name="Calibri", size=10, italic=True, color="555555")
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="left", indent=1)
    ws.row_dimensions[start_row].height = 50
    return start_row + 1


def _ws_f21(ws, start_row, criterios, total_cols=8):
    ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=total_cols)
    c = ws.cell(row=start_row, column=1, value="CRITERIO F21 · LO QUE EL EVALUADOR VERIFICA")
    c.font = Font(name="Calibri", size=10, bold=True, color=COLOR_AZUL)
    c.fill = FILL_F21
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[start_row].height = 20
    start_row += 1
    for crit in criterios:
        ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=total_cols)
        is_tax = "REQUISITO TAXATIVO" in crit
        clean = "•  " + crit.replace("(REQUISITO TAXATIVO)", "").strip()
        if is_tax:
            clean += "   ⚠ REQUISITO TAXATIVO"
        c = ws.cell(row=start_row, column=1, value=clean)
        c.fill = FILL_F21
        c.font = Font(name="Calibri", size=10, bold=is_tax, color=COLOR_TAX_FG if is_tax else "333333")
        c.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.row_dimensions[start_row].height = 30 if is_tax else 22
        start_row += 1
    return start_row + 1


def _ws_espiga(ws, start_row, text, total_cols=8):
    ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=total_cols)
    c = ws.cell(row=start_row, column=1, value="Ejemplo orientativo (caso La Espiga) — NO copies esto a tu MiPyME")
    c.font = Font(name="Calibri", size=9, bold=True, color=COLOR_AZUL)
    c.fill = FILL_ESPIGA
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[start_row].height = 18
    start_row += 1
    ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=total_cols)
    c = ws.cell(row=start_row, column=1, value=text)
    c.font = Font(name="Calibri", size=10, italic=True, color="6A5208")
    c.fill = FILL_ESPIGA
    c.alignment = Alignment(wrap_text=True, vertical="top", indent=1)
    ws.row_dimensions[start_row].height = 60
    return start_row + 1


# =============================================================================
# GENERADOR EXCEL (.xlsx) — 3 productos con hojas a la medida
# =============================================================================

def generate_excel_1_4_5(prod):
    """Matriz impacto/viabilidad — con fórmula de prioridad."""
    wb = Workbook()
    # Hoja 1: Instructivo
    ws = wb.active
    ws.title = "Instructivo"
    _ws_brand_header(ws, prod, total_cols=8)
    r = _ws_meta_block(ws, 4, total_cols=8) + 1
    r = _ws_intro(ws, r, prod["intro"], total_cols=8) + 1
    r = _ws_f21(ws, r, prod["f21"], total_cols=8)
    r = _ws_espiga(ws, r, prod["espiga"], total_cols=8) + 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    c = ws.cell(row=r, column=1, value="Preguntas guía → llena la pestaña 'Matriz' con tus oportunidades reales")
    c.font = FONT_BOLD_AZUL
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    r += 1
    for i, (q, help_text) in enumerate(prod["preguntas"], start=1):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
        c = ws.cell(row=r, column=1, value=f"{i}. {q}")
        c.font = Font(name="Calibri", size=11, bold=True, color=COLOR_AZUL)
        c.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.row_dimensions[r].height = 20
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
        c = ws.cell(row=r, column=1, value=help_text)
        c.font = FONT_HELP
        c.alignment = Alignment(wrap_text=True, vertical="top", indent=2)
        ws.row_dimensions[r].height = 32
        r += 1

    # Hoja 2: Matriz (la útil)
    ws2 = wb.create_sheet("Matriz")
    _ws_brand_header(ws2, prod, total_cols=8)
    headers = ["#", "Oportunidad detectada", "Herramienta sugerida", "Impacto (1-5)", "Viabilidad (1-5)", "Esfuerzo (1-5)", "Score = I+V+E", "Beneficio esperado"]
    widths = [5, 30, 25, 12, 12, 12, 13, 35]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws2.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws2.column_dimensions[get_column_letter(i)].width = w
    ws2.row_dimensions[4].height = 30

    # 8 filas de oportunidades vacías + fórmula
    for i in range(5, 13):
        ws2.cell(row=i, column=1, value=i - 4).alignment = ALIGN_WRAP_CENTER
        ws2.cell(row=i, column=7, value=f"=SUM(D{i}:F{i})")
        for col in range(1, 9):
            cell = ws2.cell(row=i, column=col)
            cell.border = BORDER_ALL
            cell.alignment = ALIGN_WRAP if col not in (1, 4, 5, 6, 7) else ALIGN_WRAP_CENTER
            cell.font = FONT_NORMAL
        ws2.row_dimensions[i].height = 36

    # Sección de priorización debajo
    pr_row = 15
    ws2.merge_cells(start_row=pr_row, start_column=1, end_row=pr_row, end_column=8)
    c = ws2.cell(row=pr_row, column=1, value="Priorización final — escribe aquí qué oportunidades llevas a primera fase y por qué")
    c.font = FONT_BOLD_AZUL
    c.fill = FILL_AMARILLO_CLARO
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.row_dimensions[pr_row].height = 22
    for r in range(pr_row + 1, pr_row + 6):
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
        c = ws2.cell(row=r, column=1, value="")
        c.fill = FILL_GRIS
        c.border = Border(bottom=THIN)

    return wb


def generate_excel_1_4_6(prod):
    """Hoja de ruta con Gantt por semanas."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Instructivo"
    _ws_brand_header(ws, prod, total_cols=10)
    r = _ws_meta_block(ws, 4, total_cols=10) + 1
    r = _ws_intro(ws, r, prod["intro"], total_cols=10) + 1
    r = _ws_f21(ws, r, prod["f21"], total_cols=10)
    r = _ws_espiga(ws, r, prod["espiga"], total_cols=10) + 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
    c = ws.cell(row=r, column=1, value="Preguntas guía → llena la pestaña 'Gantt' con las fases reales de tu proyecto")
    c.font = FONT_BOLD_AZUL
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    r += 1
    for i, (q, h) in enumerate(prod["preguntas"], start=1):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
        ws.cell(row=r, column=1, value=f"{i}. {q}").font = Font(name="Calibri", size=11, bold=True, color=COLOR_AZUL)
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.row_dimensions[r].height = 20
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
        ws.cell(row=r, column=1, value=h).font = FONT_HELP
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top", indent=2)
        ws.row_dimensions[r].height = 32
        r += 1

    # Hoja 2: Gantt
    ws2 = wb.create_sheet("Gantt")
    _ws_brand_header(ws2, prod, total_cols=12)
    headers = ["Fase", "Actividad", "Responsable"] + [f"S{i}" for i in range(1, 9)] + ["Notas"]
    widths = [12, 30, 18] + [5] * 8 + [25]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws2.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws2.column_dimensions[get_column_letter(i)].width = w
    ws2.row_dimensions[4].height = 30
    # 15 filas vacías
    for i in range(5, 20):
        for col in range(1, 13):
            cell = ws2.cell(row=i, column=col)
            cell.border = BORDER_ALL
            cell.alignment = ALIGN_WRAP if col in (1, 2, 3, 12) else ALIGN_WRAP_CENTER
            cell.font = FONT_NORMAL
        ws2.row_dimensions[i].height = 24

    # Hoja 3: Recursos
    ws3 = wb.create_sheet("Recursos")
    _ws_brand_header(ws3, prod, total_cols=5)
    headers = ["Tipo", "Recurso", "Cantidad", "Costo estimado (MXN)", "Notas"]
    widths = [18, 30, 12, 22, 35]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws3.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws3.column_dimensions[get_column_letter(i)].width = w
    ws3.row_dimensions[4].height = 30
    tipos = ["Tecnológico", "Tecnológico", "Tecnológico", "Humano", "Humano", "Financiero", "Financiero"]
    for i, t in enumerate(tipos, start=5):
        ws3.cell(row=i, column=1, value=t).font = FONT_BOLD_AZUL
        for col in range(1, 6):
            ws3.cell(row=i, column=col).border = BORDER_ALL
            ws3.cell(row=i, column=col).alignment = ALIGN_WRAP if col != 4 else ALIGN_WRAP_CENTER
        ws3.row_dimensions[i].height = 24

    return wb


def generate_excel_4_4_1(prod):
    """Reporte de resultados con tabla comparativa antes/después."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Instructivo"
    _ws_brand_header(ws, prod, total_cols=8)
    r = _ws_meta_block(ws, 4, total_cols=8) + 1
    r = _ws_intro(ws, r, prod["intro"], total_cols=8) + 1
    r = _ws_f21(ws, r, prod["f21"], total_cols=8)
    r = _ws_espiga(ws, r, prod["espiga"], total_cols=8) + 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    c = ws.cell(row=r, column=1, value="Llena la pestaña 'Indicadores' con tus métricas reales. Usa 'Incidencias' para el registro de fallos, 'Adopción' para el uso del personal.")
    c.font = FONT_BOLD_AZUL
    c.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
    ws.row_dimensions[r].height = 30
    r += 1
    for i, (q, h) in enumerate(prod["preguntas"], start=1):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
        ws.cell(row=r, column=1, value=f"{i}. {q}").font = Font(name="Calibri", size=11, bold=True, color=COLOR_AZUL)
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.row_dimensions[r].height = 20
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
        ws.cell(row=r, column=1, value=h).font = FONT_HELP
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top", indent=2)
        ws.row_dimensions[r].height = 32
        r += 1

    # Hoja 2: Indicadores
    ws2 = wb.create_sheet("Indicadores")
    _ws_brand_header(ws2, prod, total_cols=6)
    headers = ["#", "Indicador", "Unidad", "Línea base (antes)", "Valor actual (después)", "Variación %"]
    widths = [5, 32, 12, 20, 20, 14]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws2.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws2.column_dimensions[get_column_letter(i)].width = w
    ws2.row_dimensions[4].height = 30
    for i in range(5, 13):
        ws2.cell(row=i, column=1, value=i - 4).alignment = ALIGN_WRAP_CENTER
        ws2.cell(row=i, column=6, value=f'=IFERROR((E{i}-D{i})/D{i}, "")')
        ws2.cell(row=i, column=6).number_format = "0.0%"
        for col in range(1, 7):
            ws2.cell(row=i, column=col).border = BORDER_ALL
            ws2.cell(row=i, column=col).alignment = ALIGN_WRAP if col == 2 else ALIGN_WRAP_CENTER
            ws2.cell(row=i, column=col).font = FONT_NORMAL
        ws2.row_dimensions[i].height = 30

    # bloque ROI
    roi_row = 15
    ws2.merge_cells(start_row=roi_row, start_column=1, end_row=roi_row, end_column=6)
    c = ws2.cell(row=roi_row, column=1, value="Cálculo de ROI")
    c.font = FONT_BOLD_AZUL
    c.fill = FILL_AMARILLO_CLARO
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    pairs = [("Beneficio total estimado (MXN)", "B17"), ("Costo total del proyecto (MXN)", "B18"), ("ROI estimado (%)", "B19")]
    for i, (label, ref) in enumerate(pairs, start=16):
        ws2.cell(row=i + 1, column=1, value=label).font = FONT_BOLD_AZUL
        ws2.cell(row=i + 1, column=2, value=0).fill = FILL_GRIS
        ws2.cell(row=i + 1, column=2).border = BORDER_ALL
    ws2.cell(row=19, column=2, value="=IFERROR((B17-B18)/B18, \"\")")
    ws2.cell(row=19, column=2).number_format = "0.0%"

    # Hoja 3: Incidencias
    ws3 = wb.create_sheet("Incidencias")
    _ws_brand_header(ws3, prod, total_cols=5)
    headers = ["Fecha", "¿Qué ocurrió?", "Impacto", "Acción correctiva", "Aprendizaje"]
    widths = [14, 35, 18, 35, 30]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws3.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws3.column_dimensions[get_column_letter(i)].width = w
    ws3.row_dimensions[4].height = 30
    for i in range(5, 13):
        for col in range(1, 6):
            ws3.cell(row=i, column=col).border = BORDER_ALL
            ws3.cell(row=i, column=col).alignment = ALIGN_WRAP
            ws3.cell(row=i, column=col).font = FONT_NORMAL
        ws3.row_dimensions[i].height = 30

    # Hoja 4: Adopción
    ws4 = wb.create_sheet("Adopción")
    _ws_brand_header(ws4, prod, total_cols=5)
    headers = ["Solución", "Personal capacitado", "Personal que la usa activamente", "% adopción", "Evidencia (log, encuesta, etc.)"]
    widths = [25, 18, 24, 12, 35]
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws4.cell(row=4, column=i, value=h)
        c.fill = FILL_AZUL
        c.font = FONT_HEADER
        c.alignment = ALIGN_WRAP_CENTER
        c.border = BORDER_ALL
        ws4.column_dimensions[get_column_letter(i)].width = w
    ws4.row_dimensions[4].height = 30
    for i in range(5, 10):
        ws4.cell(row=i, column=4, value=f'=IFERROR(C{i}/B{i}, "")')
        ws4.cell(row=i, column=4).number_format = "0.0%"
        for col in range(1, 6):
            ws4.cell(row=i, column=col).border = BORDER_ALL
            ws4.cell(row=i, column=col).alignment = ALIGN_WRAP if col in (1, 5) else ALIGN_WRAP_CENTER
            ws4.cell(row=i, column=col).font = FONT_NORMAL
        ws4.row_dimensions[i].height = 30

    return wb


EXCEL_GENERATORS = {
    "1.4.5": generate_excel_1_4_5,
    "1.4.6": generate_excel_1_4_6,
    "4.4.1": generate_excel_4_4_1,
}


# =============================================================================
# GENERADOR POWERPOINT (.pptx)
# =============================================================================

def _ppt_fill_solid(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def _ppt_textbox(slide, left, top, width, height, text, *, size=18, bold=False, color=PPT_AZUL, align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = PPTPt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return tb


def generate_pptx(prod):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    SLIDE_W = prs.slide_width
    SLIDE_H = prs.slide_height
    blank = prs.slide_layouts[6]

    # ---- Slide 1: portada ----
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    _ppt_fill_solid(bg, PPT_AZUL)
    # bloque amarillo abajo
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(6.7), SLIDE_W, Inches(0.8))
    _ppt_fill_solid(band, PPT_AMARILLO)
    # bloque Mi CompañIA
    badge = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.5), Inches(1.6), Inches(1.0))
    _ppt_fill_solid(badge, PPT_AMARILLO)
    tf = badge.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "Mi CompañIA"
    run.font.size = PPTPt(14)
    run.font.bold = True
    run.font.color.rgb = PPT_AZUL

    _ppt_textbox(s, Inches(0.6), Inches(2.5), Inches(12), Inches(1.0),
                 f"PRODUCTO {prod['num']}", size=18, bold=True, color=PPT_AMARILLO)
    _ppt_textbox(s, Inches(0.6), Inches(3.0), Inches(12), Inches(2.0),
                 prod["title"], size=40, bold=True, color=PPT_BLANCO)
    _ppt_textbox(s, Inches(0.6), Inches(5.2), Inches(12), Inches(0.8),
                 f"Elemento {prod['elemento']}  ·  Estándar A · Implementar IA", size=16, color=PPT_BLANCO)
    _ppt_textbox(s, Inches(0.6), Inches(6.9), Inches(12), Inches(0.4),
                 "FUNDES Latinoamérica  ·  Iniciativa AIxMiPyMEs", size=11, bold=True, color=PPT_AZUL)

    # ---- Slide 2: datos del proyecto ----
    s = prs.slides.add_slide(blank)
    _ppt_header_bar(s, prod, SLIDE_W)
    _ppt_textbox(s, Inches(0.5), Inches(1.2), Inches(12), Inches(0.6),
                 "Datos del proyecto — completa antes de capacitar", size=24, bold=True, color=PPT_AZUL)
    fields = [
        "Nombre de la MiPyME:",
        "Personal asistente (nombres + cargos):",
        "Fecha de la capacitación:",
        "Duración estimada:",
        "Soluciones cubiertas en esta capacitación:",
    ]
    for i, label in enumerate(fields):
        top = Inches(2.2 + i * 0.75)
        box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), top, Inches(12.3), Inches(0.55))
        _ppt_fill_solid(box, PPT_AZUL_CLARO)
        tf = box.text_frame
        tf.margin_left = Inches(0.2)
        tf.vertical_anchor = 3
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = label
        run.font.size = PPTPt(14)
        run.font.bold = True
        run.font.color.rgb = PPT_AZUL

    # ---- Slide 3: Criterio F21 ----
    s = prs.slides.add_slide(blank)
    _ppt_header_bar(s, prod, SLIDE_W)
    _ppt_textbox(s, Inches(0.5), Inches(1.2), Inches(12.3), Inches(0.6),
                 "Criterio F21 — lo que el evaluador verifica", size=24, bold=True, color=PPT_AZUL)
    box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(2.0), Inches(12.3), Inches(5.0))
    _ppt_fill_solid(box, PPT_AZUL_CLARO)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.2)
    for i, crit in enumerate(prod["f21"]):
        is_tax = "REQUISITO TAXATIVO" in crit
        clean = crit.replace("(REQUISITO TAXATIVO)", "").strip()
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = PPTPt(8)
        r = p.add_run()
        r.text = "• " + clean
        r.font.size = PPTPt(13)
        r.font.color.rgb = PPT_AZUL if not is_tax else PPT_TAX
        r.font.bold = is_tax
        if is_tax:
            r2 = p.add_run()
            r2.text = "   ⚠ REQUISITO TAXATIVO"
            r2.font.size = PPTPt(11)
            r2.font.bold = True
            r2.font.color.rgb = PPT_TAX

    # ---- Slide 4: Caso La Espiga ----
    s = prs.slides.add_slide(blank)
    _ppt_header_bar(s, prod, SLIDE_W)
    _ppt_textbox(s, Inches(0.5), Inches(1.2), Inches(12.3), Inches(0.6),
                 "Ejemplo del caso La Espiga (orientativo, NO copies)", size=22, bold=True, color=PPT_AZUL)
    box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(2.0), Inches(12.3), Inches(4.5))
    _ppt_fill_solid(box, PPTColor(0xFD, 0xF6, 0xE3))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = prod["espiga"]
    r.font.size = PPTPt(16)
    r.font.italic = True
    r.font.color.rgb = PPTColor(0x6A, 0x52, 0x08)

    # ---- Slides por cada pregunta guía ----
    for i, (title, help_text) in enumerate(prod["preguntas"], start=1):
        s = prs.slides.add_slide(blank)
        _ppt_header_bar(s, prod, SLIDE_W)
        # número grande
        circle = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.5), Inches(1.2), Inches(0.9), Inches(0.9))
        _ppt_fill_solid(circle, PPT_AZUL)
        tf = circle.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = str(i)
        r.font.size = PPTPt(28)
        r.font.bold = True
        r.font.color.rgb = PPT_BLANCO
        # título
        _ppt_textbox(s, Inches(1.6), Inches(1.2), Inches(11.2), Inches(1.0),
                     title, size=26, bold=True, color=PPT_AZUL)
        # ayuda
        _ppt_textbox(s, Inches(1.6), Inches(2.2), Inches(11.2), Inches(1.0),
                     help_text, size=14, italic=True, color=PPT_GRIS)
        # caja para llenar
        box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(3.6), Inches(12.3), Inches(3.4))
        _ppt_fill_solid(box, PPTColor(0xFA, 0xFA, 0xFA))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.3)
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = "[ Escribe aquí el contenido para TU MiPyME. Borra este marcador antes de presentar. ]"
        r.font.size = PPTPt(13)
        r.font.italic = True
        r.font.color.rgb = PPTColor(0xAA, 0xAA, 0xAA)

    # ---- Slide de cierre ----
    s = prs.slides.add_slide(blank)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    _ppt_fill_solid(bg, PPT_AZUL)
    _ppt_textbox(s, Inches(0.5), Inches(2.8), Inches(12.3), Inches(1.5),
                 "¿Dudas durante la operación?", size=36, bold=True, color=PPT_AMARILLO, align=PP_ALIGN.CENTER)
    _ppt_textbox(s, Inches(0.5), Inches(4.2), Inches(12.3), Inches(1.0),
                 "Contacta a tu consultor — los datos están en el Acta de cierre (producto 4.4.2)", size=18, color=PPT_BLANCO, align=PP_ALIGN.CENTER)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(6.7), SLIDE_W, Inches(0.8))
    _ppt_fill_solid(band, PPT_AMARILLO)
    _ppt_textbox(s, Inches(0.5), Inches(6.85), Inches(12.3), Inches(0.5),
                 "Mi CompañIA  ·  FUNDES Latinoamérica  ·  AIxMiPyMEs", size=13, bold=True, color=PPT_AZUL, align=PP_ALIGN.CENTER)

    return prs


def _ppt_header_bar(slide, prod, slide_w):
    """Barra superior tipo header en cada slide."""
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, slide_w, Inches(0.55))
    _ppt_fill_solid(band, PPT_AZUL)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(0.55), slide_w, Inches(0.08))
    _ppt_fill_solid(line, PPT_AMARILLO)
    _ppt_textbox(slide, Inches(0.4), Inches(0.08), Inches(8), Inches(0.5),
                 f"Mi CompañIA  ·  {prod['title']}", size=12, bold=True, color=PPT_AMARILLO)
    _ppt_textbox(slide, Inches(9), Inches(0.08), Inches(4), Inches(0.5),
                 f"Producto {prod['num']}", size=12, bold=True, color=PPT_AMARILLO, align=PP_ALIGN.RIGHT)


# =============================================================================
# CLEANUP: borra archivos legacy (.doc/.xls/.ppt) que ya migramos a OOXML
# =============================================================================

def cleanup_legacy():
    for ext in (".doc", ".xls", ".ppt"):
        for f in OUT.glob(f"*{ext}"):
            print(f"  [del legacy] {f.name}")
            f.unlink()


# =============================================================================
# MAIN
# =============================================================================

def main():
    cleanup_legacy()
    for prod in PRODUCTS:
        fmt = prod["format"]
        if fmt == "word":
            doc = generate_word(prod)
            path = OUT / f"{prod['num'].replace('.', '-')}-{prod['slug']}.docx"
            doc.save(path)
            print(f"  [ok] {path.name}  (WORD)")
        elif fmt == "excel":
            wb = EXCEL_GENERATORS[prod["num"]](prod)
            path = OUT / f"{prod['num'].replace('.', '-')}-{prod['slug']}.xlsx"
            wb.save(path)
            print(f"  [ok] {path.name}  (EXCEL)")
        elif fmt == "ppt":
            prs = generate_pptx(prod)
            path = OUT / f"{prod['num'].replace('.', '-')}-{prod['slug']}.pptx"
            prs.save(path)
            print(f"  [ok] {path.name}  (PPTX)")
        else:
            raise ValueError(f"Formato desconocido: {fmt}")
    print(f"\nGenerados {len(PRODUCTS)} templates en {OUT}/")


if __name__ == "__main__":
    main()
