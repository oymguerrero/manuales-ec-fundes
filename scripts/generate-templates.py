#!/usr/bin/env python3
"""
Genera los 13 templates de los productos del estándar Implementar IA en
el FORMATO MÁS ADECUADO para cada uno: Word (.doc), Excel (.xls) o
PowerPoint (.ppt) HTML — Office los abre nativamente.

Filosofía pedagógica: NO darle la solución al aspirante. Cada template
muestra el criterio F21 oficial + un ejemplo breve del caso La Espiga
(solo para ilustrar el TIPO de contenido) + preguntas guía que el
aspirante responde con datos de SU MiPyME real.

Uso:
    python3 scripts/generate-templates.py

Salida: estandar-a/templates/<num>-<slug>.{doc|xls|ppt}
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-a" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

# Cada producto define su formato óptimo basado en la naturaleza del contenido:
#   "word"  → reportes narrativos, manuales técnicos, actas
#   "excel" → matrices, cronogramas, tablas comparativas de indicadores
#   "ppt"   → presentaciones (capacitación al personal)
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
            ("Lámina 1 · Bienvenida y objetivos del material", "¿Qué van a aprender? ¿Cuánto tiempo tomará? ¿Para qué les servirá en su día a día?"),
            ("Láminas 2-N · Instrucciones paso a paso por herramienta", "Por cada herramienta: capturas numeradas con el flujo completo de uso. Si la herramienta tiene 5 botones importantes, dedica 1 lámina por botón. Visual antes que texto."),
            ("Ejemplos aplicados al contexto de la MiPyME", "Por cada herramienta: 2-3 ejemplos REALES de la MiPyME (no ejemplos genéricos). El personal debe poder decir 'ah, eso lo hago yo el lunes en la mañana'."),
            ("Prompts recomendados", "Lista de 5-10 prompts que ya funcionan para los casos típicos. El personal los copia/pega; no se les pide redactar prompts desde cero."),
            ("Errores frecuentes y qué hacer", "Tabla con: error común → cómo identificarlo → cómo resolverlo → cuándo escalar al consultor o a Carlos/Doña Beatriz."),
            ("Adaptación al nivel digital del personal", "Si el personal no maneja tecnicismos, usa lenguaje cotidiano. Si están acostumbrados a apps, puedes ir más rápido."),
            ("Lámina final · Recursos y soporte", "¿A quién acudir si algo falla? ¿Dónde encontrar este material después? ¿Cuándo se actualiza?"),
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


# ===========================================================================
# PLANTILLAS POR FORMATO
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
.f21-box .taxativo { background: #FFE0E0; color: #C0392B; font-weight: bold; padding: 1pt 6pt; border-radius: 3pt; font-size: 9pt; margin-left: 4pt; }

.espiga-box {
  background: #fdf6e3;
  border: 1pt dashed #d4a40e;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  font-style: italic;
  color: #6a5208;
}
.espiga-box strong { color: #28467e; font-style: normal; }

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
<p class="subtitle">Manual de Implementar IA · Producto del Elemento {elemento}</p>
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

<div class="espiga-box"><strong>Caso pedagógico La Espiga (ilustrativo, NO es tu solución):</strong> {espiga}</div>

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
Template del Manual de Implementar IA · Para ser llenado por el aspirante con datos de su proyecto real con una MiPyME
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
<p class="subtitle">Manual de Implementar IA · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Excel es el formato natural para esta clase de producto: te permite añadir filas conforme detectes más oportunidades, ordenar por puntaje y generar gráficas. <strong>Llénalo con datos de TU MiPyME real.</strong></div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="espiga-box"><strong>Caso pedagógico La Espiga (ilustrativo):</strong> {espiga}</div>

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
Mi CompañIA · FUNDES Latinoamérica con el apoyo de Google.org · Template Excel del Manual de Implementar IA
</div>

</body>
</html>
"""

PPT_TEMPLATE = """<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:p="urn:schemas-microsoft-com:office:powerpoint"
      xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="ProgId" content="PowerPoint.Slide">
<meta name="Generator" content="Microsoft PowerPoint">
<title>{num} · {title}</title>
<style>{base_styles}
.slide {{ background: white; border: 1pt solid #ccc; padding: 30pt; margin: 16pt 0; min-height: 380pt; page-break-after: always; position: relative; box-shadow: 0 2pt 8pt rgba(0,0,0,0.08); }}
.slide-num {{ position: absolute; bottom: 16pt; right: 20pt; font-size: 9pt; color: #999; }}
.slide h2 {{ border-bottom: 2pt solid #f7c031; padding-bottom: 8pt; margin-top: 0; font-size: 20pt; color: #28467e; }}
.slide-body {{ font-size: 12pt; line-height: 1.6; color: #333; min-height: 200pt; }}
.fill-slide {{ border: 1pt dashed #ccc; background: #fafafa; padding: 22pt 18pt; min-height: 180pt; color: #aaa; font-style: italic; }}
</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;"><div class="brand-block">Mi<br>CompañIA</div></td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Manual de Implementar IA · Producto del Elemento {elemento} · PowerPoint</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Presentación editable · PowerPoint<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Por qué PowerPoint y no Word.</strong> {intro}</div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="espiga-box"><strong>Caso pedagógico La Espiga (ilustrativo):</strong> {espiga}</div>

<h2>Estructura sugerida de tu presentación</h2>
<p style="font-size: 10pt; color: #666; margin-bottom: 18pt;">Cada bloque a continuación es una lámina sugerida. Adapta cantidad y orden a tu MiPyME y al número de soluciones que vas a capacitar.</p>

{questions_html}

<div class="footer">
Mi CompañIA · FUNDES Latinoamérica con el apoyo de Google.org · Template PowerPoint del Manual de Implementar IA
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
        is_tax = "REQUISITO TAXATIVO" in c
        text = c.replace(" (REQUISITO TAXATIVO)", "")
        if is_tax:
            html += f'<li>{text} <span class="taxativo">REQUISITO TAXATIVO</span></li>\n'
        else:
            html += f'<li>{text}</li>\n'
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


def render_matrix_example(num):
    """Para 1.4.5 (matriz impacto/viabilidad), añade una hoja de cálculo pre-armada."""
    if num != "1.4.5":
        return ""
    rows = ""
    for i in range(1, 9):
        rows += (
            f'<tr>\n'
            f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
            f'<td class="fill">&nbsp;</td><td class="fill">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;color:#999;">=I*V/E</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    return f"""
<h2>Hoja de matriz · oportunidades de IA priorizadas</h2>
<p style="font-size: 10pt; color: #666;">Añade tantas filas como oportunidades hayas detectado. Llena impacto (I), viabilidad (V) y esfuerzo (E) con valores 1-5. El score relativo (I × V / E) te orienta sobre cuál priorizar.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:22%;">Oportunidad</th><th style="width:16%;">Herramienta sugerida</th><th style="width:9%;">Impacto (1-5)</th><th style="width:9%;">Viabilidad (1-5)</th><th style="width:9%;">Esfuerzo (1-5)</th><th style="width:9%;">Score</th><th>Beneficio esperado</th></tr>
{rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:8pt;font-style:italic;">Convención: I y V altos suman, esfuerzo alto resta (por eso aparece en el denominador). No hay fórmula universal — adapta el cálculo a tu criterio profesional.</p>
"""


def render_gantt_example(num):
    """Para 1.4.6 (hoja de ruta), añade un cronograma Gantt vacío."""
    if num != "1.4.6":
        return ""
    weeks_header = ''.join(f'<th style="width:5%;text-align:center;">S{i}</th>' for i in range(1, 13))
    rows = ""
    for i in range(1, 9):
        empty_cells = ''.join('<td class="fill" style="text-align:center;">&nbsp;</td>' for _ in range(12))
        rows += (
            f'<tr>\n'
            f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'{empty_cells}\n'
            f'</tr>\n'
        )
    return f"""
<h2>Cronograma Gantt · semanas del proyecto</h2>
<p style="font-size: 10pt; color: #666;">Marca con X (o con un color en Excel) las semanas en las que se ejecuta cada actividad. Adapta el número de semanas a tu proyecto.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:24%;">Actividad</th><th style="width:14%;">Responsable</th>{weeks_header}</tr>
{rows}
</table>
"""


def render_indicators_example(num):
    """Para 4.4.1 (reporte de evaluación de resultados), añade tabla antes/después."""
    if num != "4.4.1":
        return ""
    rows = ""
    for i in range(1, 7):
        rows += (
            f'<tr>\n'
            f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;color:#999;">=(actual-base)/base</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    return f"""
<h2>Tabla antes/después de indicadores</h2>
<p style="font-size: 10pt; color: #666;">Por cada indicador del proyecto, registra la línea base, el valor actual y la variación. Cumple con el primer criterio del F21 explícitamente.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:30%;">Indicador</th><th style="width:14%;">Línea base</th><th style="width:14%;">Valor actual</th><th style="width:14%;">Variación %</th><th>Observación</th></tr>
{rows}
</table>
<h2 style="margin-top:24pt;">Registro de incidencias</h2>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:14%;">Fecha</th><th style="width:30%;">Incidencia</th><th style="width:24%;">Acción correctiva</th><th>Lección aprendida</th></tr>
{''.join(f'<tr><td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td><td class="fill">&nbsp;</td><td class="fill">&nbsp;</td><td class="fill">&nbsp;</td><td class="fill">&nbsp;</td></tr>' for i in range(1, 5))}
</table>
"""


def render_slides_ppt(preguntas):
    html = ""
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<div class="slide">\n'
            f'<h2>{title}</h2>\n'
            f'<div class="slide-body">\n'
            f'<p style="font-style:italic;color:#666;font-size:11pt;margin-bottom:14pt;">{help_text}</p>\n'
            f'<div class="fill-slide">[Diseña aquí esta lámina. Si es PowerPoint, conviértela en visual: capturas, iconos grandes, poco texto. El personal de la MiPyME aprende mirando, no leyendo.]</div>\n'
            f'</div>\n'
            f'<div class="slide-num">Lámina {i}</div>\n'
            f'</div>\n'
        )
    return html


def render_product(p):
    f21_html = render_f21(p["f21"])
    extension_by_format = {"word": "doc", "excel": "xls", "ppt": "ppt"}
    ext = extension_by_format[p["format"]]

    if p["format"] == "word":
        questions_html = render_questions_word(p["preguntas"])
        html = WORD_TEMPLATE.format(
            num=p["num"], title=p["title"], elemento=p["elemento"], intro=p["intro"],
            espiga=p["espiga"], f21_html=f21_html, questions_html=questions_html,
            base_styles=BASE_STYLES,
        )
    elif p["format"] == "excel":
        questions_html = render_questions_excel(p["preguntas"])
        matrix_html = render_matrix_example(p["num"]) + render_gantt_example(p["num"]) + render_indicators_example(p["num"])
        html = EXCEL_TEMPLATE.format(
            num=p["num"], title=p["title"], elemento=p["elemento"], intro=p["intro"],
            espiga=p["espiga"], f21_html=f21_html, questions_html=questions_html,
            matrix_html=matrix_html, base_styles=BASE_STYLES,
        )
    elif p["format"] == "ppt":
        questions_html = render_slides_ppt(p["preguntas"])
        html = PPT_TEMPLATE.format(
            num=p["num"], title=p["title"], elemento=p["elemento"], intro=p["intro"],
            espiga=p["espiga"], f21_html=f21_html, questions_html=questions_html,
            base_styles=BASE_STYLES,
        )
    return html, ext


def main():
    # Borrar templates viejos (.doc) que cambian de extensión
    legacy = ["1-4-5-matriz-impacto-viabilidad.doc", "1-4-6-hoja-de-ruta.doc",
              "3-4-3-material-capacitacion.doc", "4-4-1-reporte-evaluacion-resultados.doc"]
    for fn in legacy:
        p = OUT / fn
        if p.exists():
            p.unlink()
            print(f"  [del] {fn}")

    for p in PRODUCTS:
        html, ext = render_product(p)
        filename = f"{p['num'].replace('.', '-')}-{p['slug']}.{ext}"
        filepath = OUT / filename
        filepath.write_text(html, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")
    print(f"\nGenerados {len(PRODUCTS)} templates en {OUT}/")


if __name__ == "__main__":
    main()
