#!/usr/bin/env python3
"""
Genera las 12 plantillas de los productos del EC1830 · Adopción de soluciones
de inteligencia artificial en los procesos de la MiPyME (Ruta A, caso La Espiga):
- 8 Word (.doc) + 3 Excel (.xls) como HTML estilizado, que
  convert-legacy-office.py convierte después a .docx/.xlsx (OOXML real).
- 1 PowerPoint (.pptx) real generado con python-pptx — porque
  PowerPoint moderno NO abre HTML como .ppt, hay que generar OOXML.

Filosofía pedagógica: NO darle la solución al aspirante. Cada plantilla
muestra los criterios literales del EC1830 publicado en el DOF (28-oct-2026)
+ un ejemplo breve del caso La Espiga (solo para ilustrar el TIPO de
contenido) + preguntas guía que el aspirante responde con los datos de su
proyecto (en el lugar de trabajo o simulado).

Uso:
    python3 scripts/generate-templates.py

Salida: estandar-a/templates/<num>-<slug>.{doc|xls|pptx}; al final corre
convert-legacy-office.py.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-a" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

# Cada producto define su formato óptimo basado en la naturaleza del contenido:
#   "word"  → reportes narrativos, manuales técnicos, actas (HTML en .doc)
#   "excel" → matrices, cronogramas, tablas comparativas (HTML en .xls)
#   "pptx"  → presentación real generada con python-pptx (capacitación)
PRODUCTS = [
    # 'title' y 'f21' son el título y los criterios literales del EC1830 publicado en el DOF.
    # La clave 'f21' y la clase CSS f21-box conservan su nombre histórico: convert-legacy-office.py
    # busca la caja por esa clase. No renombrar sin cambiar el conversor.
    {
        'num': '1.1',
        'slug': 'reporte-evaluacion-inicial',
        'format': 'word',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'El reporte de evaluación inicial de la MiPyME, elaborado',
        'intro': 'Es el primer producto del proyecto: una foto del estado actual de la MiPyME, sus objetivos y los recursos disponibles.',
        'f21': [
            'Contiene el perfil empresarial de la MiPyME considerando nombre comercial/razón social, giro y número de empleados',
            'Incluye la ubicación, correo electrónico, teléfono y nombre de la persona de contacto por parte de la MiPyME',
            'Contiene los antecedentes/resultados de las acciones de mejora aplicadas previamente por el cliente en materia tecnológica',
            'Contiene las áreas de mejora/problemas a resolver desde la perspectiva del representante de la MiPyME y antigüedad de ello',
            'Incluye los objetivos, indicadores de impacto operativo y metas',
            'Indica los recursos, tiempos y entregas esperadas de acuerdo con el alcance planteado',
            'Se presenta de forma digital/físico sin errores ortográficos',
        ],
        'espiga': 'Tres sucursales en una ciudad de tamaño medio, doce empleados; pan tradicional y repostería, venta en mostrador y pedidos por WhatsApp. Doña Beatriz (dueña fundadora) y su hijo Carlos (recién egresado de administración, apoya la digitalización) quieren reducir el tiempo que las tres encargadas pasan respondiendo consultas repetitivas por WhatsApp.',
        'preguntas': [
            ('Perfil empresarial', 'Nombre comercial o razón social, giro y número de empleados. ¿Cómo describirías a la MiPyME en dos o tres líneas?'),
            ('Datos de contacto', 'Ubicación, correo electrónico, teléfono y nombre de la persona de contacto por parte de la MiPyME.'),
            ('Acciones previas del cliente', '¿Qué acciones de mejora en materia tecnológica ha aplicado antes la MiPyME? ¿Con qué resultados?'),
            ('Áreas de mejora desde la perspectiva del cliente', '¿Qué problemas o áreas de mejora identifica quien representa a la MiPyME? ¿Desde cuándo arrastran cada uno?'),
            ('Objetivos · indicadores · metas', '¿Qué quiere lograr la MiPyME con este proyecto? Para cada objetivo, ¿qué indicador de impacto operativo lo mide y cuál es la meta?'),
            ('Recursos · tiempos · entregas esperadas', 'De acuerdo con el alcance planteado: ¿con qué presupuesto, equipo humano y tiempos cuenta la MiPyME? ¿Qué entregas espera?'),
            ('Presentación y revisión final', '¿Lo entregarás en formato digital o físico? Antes de entregarlo, revisa que la redacción sea clara y que no tenga errores ortográficos; si puedes, pídele a otra persona que lo lea.'),
        ],
    },
    {
        'num': '1.2',
        'slug': 'informe-disponibilidad-datos',
        'format': 'word',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'El informe de disponibilidad y calidad de los datos de la MiPyME, elaborado',
        'intro': 'Documenta qué datos tiene la MiPyME para sostener soluciones de IA y cuál es su calidad.',
        'f21': [
            'Contiene las fuentes de información existentes en los procesos operativos',
            'Indica que la información requerida está completa y disponible en tiempo y forma',
            'Incluye las necesidades de optimización/estructuración de los datos existentes previo a la adopción',
            'Contiene los hallazgos detectados en la disponibilidad y calidad de los datos',
        ],
        'espiga': 'En La Espiga: pedidos por WhatsApp sin estructura, una libreta de pedidos por sucursal, contabilidad que lleva un despacho externo con archivos en papel y ningún CRM. Datos dispersos y sin estandarizar entre sucursales.',
        'preguntas': [
            ('Fuentes de información existentes', '¿Dónde viven los datos relevantes para el proceso a intervenir? CRM, ERP, hojas de cálculo, mensajes, correos, papel…'),
            ('Completitud y disponibilidad en tiempo', 'Por cada fuente: ¿los datos están completos? ¿se actualizan a tiempo? ¿qué frecuencia?'),
            ('Necesidades de optimización/estructuración', '¿Qué hay que limpiar, estandarizar, deduplicar o estructurar antes de poder usarlos con IA?'),
            ('Hallazgos relevantes', 'Lo más notable que descubriste sobre la calidad de los datos. ¿Qué obstáculos representa esto para las soluciones que quieres implementar?'),
        ],
    },
    {
        'num': '1.3',
        'slug': 'informe-diagnostico-procesos',
        'format': 'word',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'El informe de diagnóstico de procesos, actividades y áreas de trabajo, acordado',
        'intro': 'Mapea los procesos operativos y detecta los cuellos de botella + resistencias al cambio.',
        'f21': [
            'Contiene el mapa de los procesos analizados',
            'Incluye la clasificación de los procesos por área funcional',
            'Contiene los cuellos de botella y los principales puntos de dolor identificados',
            'Incluye las resistencias al cambio detectadas durante el diagnóstico',
        ],
        'espiga': 'Mapa de La Espiga: 6 procesos analizados (recepción de pedidos, producción, venta en mostrador, control de inventario, cobro y contabilidad). Cuello de botella principal: las tres encargadas suman unas 20 horas a la semana en tareas repetitivas, sobre todo responder las mismas consultas por WhatsApp. Resistencia: dos panaderos veteranos desconfían de «que la máquina les diga qué hornear».',
        'preguntas': [
            ('Mapa de procesos analizados', 'Dibuja o describe los procesos que analizaste. Indica qué hace cada uno y cómo se conectan. (Inserta una imagen del mapa si lo dibujaste en Miro/Lucidchart/papel).'),
            ('Clasificación por área funcional', 'Agrupa los procesos: ventas, operación, administración, soporte, atención a cliente… ¿Cuál concentra más procesos críticos?'),
            ('Cuellos de botella y puntos de dolor', 'Por cada proceso analizado: ¿dónde se atasca? ¿cuánto tiempo se pierde? ¿qué errores ocurren? ¿quién sufre el impacto?'),
            ('Resistencias al cambio detectadas', 'Durante el diagnóstico, ¿qué personas mostraron resistencia? ¿Qué temen perder o no entienden? Es información valiosa para la fase de capacitación.'),
        ],
    },
    {
        'num': '1.4',
        'slug': 'reporte-madurez-digital',
        'format': 'word',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'El reporte de madurez digital y disposición al cambio, elaborado',
        'intro': 'Evalúa qué tan preparada está la MiPyME (tecnología) y su personal (cultura) para incorporar IA.',
        'f21': [
            'Incluye la descripción de la metodología y la(s) herramienta(s) utilizada(s)',
            'Contiene los resultados del test de madurez digital y disposición al cambio aplicado',
            'Incluye la descripción del nivel de madurez digital por dimensión evaluada',
            'Contiene comentarios sobre la disposición al cambio por parte del personal',
            'Incluye las soluciones de IA recomendadas con base en los resultados obtenidos',
            'Incluye un tablero base de indicadores para el seguimiento de la transformación digital',
        ],
        'espiga': 'La Espiga obtuvo nivel 2 de 5 en madurez digital: usan WhatsApp, pero no tienen CRM ni datos integrados. Disposición al cambio: alta en Carlos, media en las tres encargadas y baja al inicio en Doña Beatriz, que pidió ver resultados antes de invertir.',
        'preguntas': [
            ('Metodología y herramienta usada', '¿Qué instrumento aplicaste para medir madurez digital? (Cuestionario, entrevistas, observación, test estandarizado). ¿Por qué lo elegiste?'),
            ('Resultados del test aplicado', 'Resultados del test de madurez digital y disposición al cambio que aplicaste, por dimensión: infraestructura, procesos, personas, datos, cultura. Apóyate en una tabla.'),
            ('Nivel de madurez digital por dimensión', 'Clasificación (inicial, en desarrollo, intermedio, avanzado) por cada dimensión. ¿Cuál es la dimensión más débil? ¿Cuál es la fortaleza?'),
            ('Disposición al cambio del personal', 'Por persona o grupo: ¿qué tan abierta está al cambio? ¿Qué evidencia observaste durante el diagnóstico?'),
            ('Soluciones de IA recomendadas según los resultados', 'Con base en los resultados, ¿qué soluciones de IA le recomiendas a la MiPyME? Explica por qué encajan con su nivel de madurez y con la disposición al cambio de su personal.'),
            ('Tablero base de indicadores', '¿Qué indicadores propones seguir mes a mes para dar seguimiento a la transformación digital? Por ejemplo, de tres a cinco, cada uno con su línea base actual y la meta esperada a 6 o 12 meses.'),
        ],
    },
    {
        'num': '1.5',
        'slug': 'matriz-impacto-viabilidad',
        'format': 'excel',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'La matriz de impacto, viabilidad y esfuerzo, propuesta',
        'intro': 'Hoja de cálculo para priorizar las oportunidades de IA detectadas. Asigna puntajes (1-5) por impacto, viabilidad y esfuerzo; la matriz revela cuáles atacar primero.',
        'f21': [
            'Contiene el listado de las soluciones de IA que mejor se interrelacionen respecto del impacto, la viabilidad y el esfuerzo en los procesos de la MiPyME',
            'Contiene la priorización de las oportunidades de soluciones de IA',
            'Incluye los beneficios esperados para la MiPyME y la viabilidad de la adopción',
        ],
        'espiga': 'En La Espiga se identificaron 5 oportunidades. Las dos de mayor impacto y viabilidad fueron las recomendadas para la primera fase: el sistema unificado de pedidos por WhatsApp con respuestas automáticas y el resumen automatizado de los pedidos del día para cocina.',
        'preguntas': [
            ('Oportunidades detectadas', 'Lista todas las oportunidades de IA que detectaste en el diagnóstico. Una por fila.'),
            ('Herramienta/plataforma sugerida', 'Por cada oportunidad: ¿qué herramienta de IA existente la resolvería? (ChatGPT, Claude, Zapier, Make, CRM con módulo de IA, etc.)'),
            ('Puntaje de IMPACTO (1-5)', '¿Cuánto valor genera? (Tiempo ahorrado, ingresos adicionales, errores reducidos, mejor experiencia). 5 = alto.'),
            ('Puntaje de VIABILIDAD (1-5)', '¿Qué tan fácil es de implementar dados los recursos actuales de la MiPyME? 5 = muy viable.'),
            ('Puntaje de ESFUERZO (1-5)', '¿Cuánto trabajo cuesta? (Tiempo + personas + costo). 5 = poco esfuerzo, 1 = mucho esfuerzo.'),
            ('Beneficios esperados', 'Breve frase por oportunidad: ¿qué mejora medible esperas?'),
            ('Priorización final', 'Las 2-3 oportunidades recomendadas para primera fase, y por qué.'),
        ],
    },
    {
        'num': '1.6',
        'slug': 'hoja-de-ruta',
        'format': 'excel',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'La hoja de ruta de adopción de soluciones de IA, elaborada',
        'intro': 'Cronograma tipo Gantt con las fases, actividades, responsables y recursos del proyecto.',
        'f21': [
            'Contiene el listado de la(s) solución(es) de IA seleccionada(s) para la MiPyME',
            'Contiene descritas las mejoras en la operación de los procesos con la solución de IA',
            'Incluye las fases/etapas de adopción del proyecto',
            'Incluye las actividades y responsables de cada etapa',
            'Contiene el cronograma con las actividades de adopción para cada etapa del proyecto',
            'Incluye los recursos tecnológicos, humanos y financieros requeridos',
            'Incluye indicadores de impacto operativo para evaluar el avance de la adopción y dar seguimiento al proyecto',
        ],
        'espiga': 'En La Espiga: cinco semanas, una etapa por semana. S1 configurar el asistente de WhatsApp y sus respuestas a preguntas frecuentes; S2 configurar el resumen automático de pedidos; S3 piloto en la sucursal principal; S4 extender a las tres sucursales y capacitar; S5 evaluar y ajustar.',
        'preguntas': [
            ('Soluciones seleccionadas (de la matriz 1.5)', 'Lista las soluciones de IA seleccionadas para la MiPyME: las que efectivamente vas a implementar.'),
            ('Mejoras en la operación con la solución', 'Por cada solución: ¿cómo quedará el proceso después de implementarla y qué mejora en su operación?'),
            ('Fases del proyecto', '¿Cuántas fases tendrá el proyecto? Para cada una: nombre + objetivo + tiempo estimado.'),
            ('Actividades y responsables por fase', 'Lista granular de actividades. Quién hace qué de tu lado + del lado de la MiPyME.'),
            ('Cronograma (Gantt)', 'Tabla con actividades en filas y semanas/quincenas en columnas. Marca con X cuándo se ejecuta cada actividad.'),
            ('Recursos tecnológicos / humanos / financieros', 'Equipo, suscripciones, plataformas, equipo humano, presupuesto desglosado por fase.'),
            ('Indicadores de impacto operativo', '¿Qué indicadores de impacto operativo usarás para evaluar el avance de la adopción y dar seguimiento al proyecto? Por cada uno: cómo se mide y cada cuándo.'),
        ],
    },
    {
        'num': '1.7',
        'slug': 'propuesta-final-adopcion',
        'format': 'word',
        'elemento': '1 · E5809 · Planear soluciones de Inteligencia Artificial alineadas a la MiPyME',
        'title': 'La propuesta final de adopción de soluciones de IA, integrada',
        'intro': 'Documento maestro de entrega al emprendedor que integra los productos previos en una narrativa coherente.',
        'f21': [
            'Contiene el informe de diagnóstico de procesos, actividades y áreas de trabajo',
            'Incluye el reporte de madurez digital y disposición al cambio',
            'Contiene la matriz de impacto, viabilidad y esfuerzo',
            'Incluye la hoja de ruta de adopción de soluciones de IA, considerando el cronograma, actividades y áreas de trabajo',
            'Contiene la propuesta económica de consultoría, considerando la aplicación del diagnóstico y del test de madurez digital y disposición al cambio',
            'Incluye la evidencia escrita/digital del visto bueno por parte de la persona responsable de la MiPyME',
            'Incluye el acuerdo de confidencialidad firmado por ambas partes',
            'Se presenta en formato digital / físico, con redacción clara y sin errores ortográficos',
        ],
        'espiga': 'Para La Espiga: documento de 18 a 25 páginas. Resumen ejecutivo de 1 página → diagnóstico → madurez → matriz → hoja de ruta → propuesta económica (honorarios profesionales y licencias mensuales, por separado) → anexos. Pensado para que Doña Beatriz lo lea en 20 minutos y entienda exactamente qué pasará. Andrea, la consultora, le envía la propuesta dos días antes y la presenta en la oficina trasera de la sucursal principal.',
        'preguntas': [
            ('Resumen ejecutivo (1 pág)', 'Página única que sintetiza: contexto + oportunidades priorizadas + propuesta + inversión + resultados esperados. Si el cliente solo lee esta página, debe entender qué va a pasar.'),
            ('Diagnóstico integrado (producto 1.3)', 'Incorpora el informe de diagnóstico de procesos, actividades y áreas de trabajo, o un resumen con el original como anexo.'),
            ('Madurez digital y disposición al cambio (producto 1.4)', 'Incluye el reporte de madurez digital y disposición al cambio, o un resumen con el tablero base.'),
            ('Matriz de oportunidades (producto 1.5)', 'Incluye la matriz de impacto, viabilidad y esfuerzo; destaca las oportunidades recomendadas para la primera fase.'),
            ('Hoja de ruta (producto 1.6)', 'Incluye la hoja de ruta de adopción con el cronograma, las actividades y las áreas de trabajo.'),
            ('Propuesta económica de consultoría', 'Honorarios profesionales + costos de licencias/herramientas + otros costos, considerando la aplicación del diagnóstico y del test de madurez digital. Total, forma de pago e hitos de cobro si aplica.'),
            ('Evidencia escrita o digital del visto bueno', '¿Cómo obtuviste el visto bueno de la persona responsable de la MiPyME? (Firma autógrafa, electrónica, correo de aprobación explícita, acuse). Adjunta o describe esa evidencia: sin ella el producto no cumple este criterio.'),
            ('Acuerdo de confidencialidad firmado', 'Convenio firmado por ambas partes. Adjunta o describe el acuerdo y sus firmas.'),
            ('Anexos', 'Documentos de soporte: instrumentos del diagnóstico, capturas, evidencias.'),
            ('Presentación y revisión final', '¿La entregarás en formato digital o físico? Antes de entregarla, revisa que la redacción sea clara y que no tenga errores ortográficos; si puedes, pídele a otra persona que la lea.'),
        ],
    },
    {
        'num': '2.1',
        'slug': 'soluciones-implementadas',
        'format': 'word',
        'elemento': '2 · E5810 · Adoptar soluciones de Inteligencia Artificial en el entorno de la MiPyME',
        'title': 'Las soluciones de IA en la operación, implementadas',
        'intro': 'El producto 2.1 NO es documental: es la solución MISMA funcionando. Esta plantilla sirve como inventario que documenta lo implementado para la evaluación.',
        'f21': [
            'Se encuentran configuradas en el entorno tecnológico de la MiPyME conforme al plan de adopción definido',
            'Operan en al menos un proceso administrativo/operativo/comercial del negocio de la MiPyME',
            'Incluyen la descripción del caso de uso para el cual fueron implementadas',
            'Muestran la evidencia de mejora en el funcionamiento y en condiciones reales de operación',
            'Especifican las herramientas/plataformas de IA utilizadas',
            'Indican el nombre del usuario responsable de la operación dentro de la MiPyME',
        ],
        'espiga': 'Inventario de La Espiga: dos soluciones operando. (1) El asistente de WhatsApp que responde las preguntas frecuentes, desde el 1 de abril. (2) El resumen de los pedidos del día para cocina, desde el 5 de abril; ahorra unos 30 minutos diarios. Responsables de la operación: las tres encargadas y Carlos.',
        'preguntas': [
            ('Solución implementada · nombre y proceso intervenido', 'Por cada solución: su nombre y el proceso administrativo, operativo o comercial de la MiPyME donde funciona ahora.'),
            ('Caso de uso documentado', '¿Para qué se implementó? ¿Qué problema concreto resuelve?'),
            ('Evidencia de mejora en condiciones reales', '¿Qué muestra que el proceso funciona mejor con la solución operando en condiciones reales? Capturas, registros de uso o métricas de las últimas 2-4 semanas, comparadas con cómo funcionaba antes. (Adjúntalas como anexos si son muchas).'),
            ('Herramienta/plataforma de IA utilizada', 'Nombre comercial exacto + módulo o versión.'),
            ('Usuario responsable de la operación', 'Quién en la MiPyME opera cada solución (nombre + cargo).'),
            ('Configuración conforme al plan de adopción (1.6)', '¿Dónde quedó configurada cada solución dentro del entorno tecnológico de la MiPyME? ¿Se configuró conforme a la hoja de ruta? Si hubo desviaciones, ¿por qué?'),
        ],
    },
    {
        'num': '2.2',
        'slug': 'informe-tecnico-configuracion',
        'format': 'word',
        'elemento': '2 · E5810 · Adoptar soluciones de Inteligencia Artificial en el entorno de la MiPyME',
        'title': 'El informe técnico de configuración de las soluciones de IA, elaborado',
        'intro': 'Manual técnico para que la MiPyME mantenga las soluciones después de tu consultoría. Es exhaustivo.',
        'f21': [
            'Contiene la descripción de las herramientas/plataformas de IA configuradas y su propósito dentro de los procesos de la MiPyME',
            'Incluye los parámetros de configuración aplicados en cada herramienta de IA',
            'Contiene especificadas las integraciones realizadas con los sistemas, plataformas o procesos existentes de la MiPyME',
            'Incluye los requisitos técnicos necesarios para el funcionamiento de las soluciones implementadas en la MiPyME',
            'Incluye los elementos de ciberseguridad considerados para la operación del sistema, así como las leyes y normas aplicables',
            'Contiene los accesos y permisos configurados para los usuarios de la MiPyME que operan las soluciones',
            'Contiene los resultados de las pruebas funcionales ejecutadas para verificar el funcionamiento de la solución en el entorno de la MiPyME, Pruebas de funcionamiento/Pruebas de integración/Pruebas de uso en condiciones reales',
            'Contiene especificados los indicadores de impacto operativo obtenidos durante la fase de pruebas',
            'Se presenta en formato digital, con redacción clara y sin errores ortográficos',
        ],
        'espiga': 'Informe técnico de La Espiga: unas 14 páginas que documentan los parámetros del asistente de WhatsApp, la integración con una hoja de cálculo en la nube para registrar los pedidos, los permisos de las tres encargadas y de Carlos, y los resultados de 15 pruebas funcionales antes de ponerlo en marcha.',
        'preguntas': [
            ('Resumen ejecutivo', 'Una página: qué se implementó, en qué entorno, con qué arquitectura general.'),
            ('Arquitectura general', 'Diagrama de cómo se conectan las herramientas entre sí y con los procesos de la MiPyME.'),
            ('Herramientas + propósito + parámetros', 'Por cada herramienta: nombre comercial, propósito en la MiPyME, todos los parámetros de configuración aplicados.'),
            ('Integraciones realizadas', '¿Con qué sistemas existentes se conectó cada herramienta? (CRM, hojas de cálculo, plataformas de mensajería, etc.)'),
            ('Requisitos técnicos', 'Conectividad, navegadores, sistemas operativos, suscripciones que la MiPyME necesita mantener.'),
            ('Ciberseguridad + normativa aplicable', 'Medidas de ciberseguridad consideradas para operar el sistema, y las leyes y normas aplicables. Por ejemplo, la LFPDPPP: principios (Arts. 5 a 12), consentimiento y aviso de privacidad (Arts. 7, 8 y 14), transferencias (Arts. 36 y 37), derechos ARCO (Arts. 22 a 34) y sanciones (Arts. 63 a 68).'),
            ('Accesos y permisos configurados', 'Tabla con cada usuario + rol + nivel de acceso por herramienta.'),
            ('Pruebas funcionales ejecutadas', 'Lista de pruebas (funcionamiento, integración, uso en condiciones reales) + resultados de cada una.'),
            ('Indicadores de impacto operativo en las pruebas', '¿Qué indicadores de impacto operativo obtuviste durante la fase de pruebas? Por ejemplo: tiempo de respuesta, consultas atendidas o errores, con el valor que mediste.'),
            ('Presentación y revisión final', 'Entrégalo en formato digital. Antes de entregarlo, revisa que la redacción sea clara y que no tenga errores ortográficos; si puedes, pídele a otra persona que lo lea.'),
        ],
    },
    {
        'num': '2.3',
        'slug': 'material-capacitacion',
        'format': 'pptx',
        'elemento': '2 · E5810 · Adoptar soluciones de Inteligencia Artificial en el entorno de la MiPyME',
        'title': 'El material de capacitación para la adopción de soluciones de IA, elaborado',
        'intro': 'Presentación visual para capacitar al personal de la MiPyME. Una lámina por paso, espacio para captura, prompts destacados y errores frecuentes. El formato PowerPoint te permite usarla en sesión presencial o compartirla para autoestudio.',
        'f21': [
            'Contiene las instrucciones paso a paso para operar cada herramienta de IA implementada',
            'Incluye ejemplos de uso aplicados al contexto específico de la MiPyME',
            'Especifica los prompts o instrucciones recomendadas para cada herramienta de IA',
            'Incluye las buenas prácticas de uso y las acciones a realizar ante errores frecuentes en la operación de la solución',
            'Está adaptado al nivel de alfabetización digital del personal capacitado',
            'Se presenta en formato digital, accesible y comprensible para el personal de la MiPyME',
        ],
        'espiga': 'Material de La Espiga: presentación de 12 láminas con 3 prompts recomendados, más una guía impresa de tres páginas para consulta rápida. Pensado para encargadas que usan el celular a diario pero nunca han usado un asistente de IA: lenguaje sencillo, capturas grandes y una lista de «qué hacer si algo no funciona».',
        'preguntas': [
            ('Lámina 1 · Bienvenida y objetivos del material', '¿Qué van a aprender? ¿Cuánto tiempo tomará? ¿Para qué les servirá en su día a día?'),
            ('Láminas 2-N · Instrucciones paso a paso por herramienta', 'Por cada herramienta: capturas numeradas con el flujo completo de uso. Si la herramienta tiene 5 botones importantes, dedica 1 lámina por botón. Visual antes que texto.'),
            ('Ejemplos aplicados al contexto de la MiPyME', "Por cada herramienta: 2-3 ejemplos REALES de la MiPyME (no ejemplos genéricos). El personal debe poder decir 'ah, eso lo hago yo el lunes en la mañana'."),
            ('Prompts recomendados', 'Por cada herramienta, los prompts o instrucciones que ya funcionan para los casos típicos. El personal los copia y pega; no se le pide redactar prompts desde cero.'),
            ('Buenas prácticas de uso', '¿Qué conviene hacer siempre al usar cada herramienta? Por ejemplo: revisar la respuesta antes de enviarla o cuidar los datos personales de los clientes.'),
            ('Errores frecuentes y qué hacer', 'Tabla con: error común → cómo identificarlo → cómo resolverlo → cuándo escalar a quien da soporte o a la persona responsable de la MiPyME.'),
            ('Adaptación al nivel digital y formato accesible', 'Si el personal no maneja tecnicismos, usa lenguaje cotidiano; si está acostumbrado a las apps, puedes ir más rápido. Entrega el material en formato digital que el personal pueda abrir y entender: letra grande, buen contraste y capturas claras.'),
            ('Lámina final · Recursos y soporte', '¿A quién acudir si algo falla? ¿Dónde encontrar este material después? ¿Cuándo se actualiza?'),
        ],
    },
    {
        'num': '3.1',
        'slug': 'reporte-evaluacion-resultados',
        'format': 'excel',
        'elemento': '3 · E5811 · Evaluar resultados e impacto de la adopción de soluciones de Inteligencia Artificial en la MiPyME',
        'title': 'El reporte de evaluación de resultados de la adopción de soluciones de IA, elaborado',
        'intro': 'Hoja de cálculo con la comparación antes/después de cada indicador + tablero visual + estimación de ROI.',
        'f21': [
            'Contiene la comparación de los indicadores de impacto operativo de los procesos antes y después de la adopción, mostrando la eficiencia lograda/retorno de inversión',
            'Incluye los resultados y hallazgos cualitativos en los procesos intervenidos',
            'Incluye el registro de incidencias presentadas durante la operación y las acciones correctivas aplicadas',
            'Contiene descrito el nivel de adopción de las soluciones de IA por parte del personal de la MiPyME',
            'Se presenta en formato digital / físico, con redacción clara y sin errores ortográficos',
        ],
        'espiga': 'Reporte de La Espiga: 8 semanas antes contra 8 semanas operando, con 3 indicadores. Tiempo de respuesta en WhatsApp: de 8 minutos a 30 segundos en promedio. Consultas atendidas al día (las tres sucursales): de 30 a 90. Horas semanales en tareas repetitivas (las tres encargadas): de 20 a 5. ROI estimado de 280 % a seis meses. Una incidencia mayor (el asistente dejó de responder 2 horas el 18 de abril) con su acción correctiva documentada.',
        'preguntas': [
            ('Indicadores · línea base · valor actual · variación', 'Tabla con cada indicador del proyecto, su valor antes de la adopción, su valor actual, y la variación porcentual.'),
            ('Tablero de indicadores integrado', 'Visualización gráfica (puedes generar gráficas con Excel mismo) con resultados cuantitativos + cualitativos.'),
            ('Impacto operativo', 'Tiempo ahorrado, ingresos adicionales, errores reducidos. Cuantifica todo lo cuantificable.'),
            ('Resultados y hallazgos cualitativos', '¿Qué cambió en los procesos intervenidos que no se ve en los números? Por ejemplo, lo que opinan el personal y los clientes, o cambios en la forma de trabajar.'),
            ('Cálculo del ROI', 'ROI = (beneficios obtenidos − costo total del proyecto) / costo total del proyecto × 100. Documenta los supuestos y de dónde sale cada cifra.'),
            ('Registro de incidencias + acciones correctivas', 'Tabla con cada incidencia: fecha, qué ocurrió, qué hiciste para corregirla, qué se aprendió.'),
            ('Nivel de adopción del personal', '¿Cuántas personas operan cada solución activamente? ¿Qué porcentaje del personal capacitado la usa? Evidencia: logs, encuesta a usuarios.'),
            ('Lecciones y recomendaciones', 'Resumen ejecutivo de lo que funcionó, lo que no, y recomendaciones de mejora continua.'),
            ('Presentación y revisión final', '¿Lo entregarás en formato digital o físico? Antes de entregarlo, revisa que la redacción sea clara y que no tenga errores ortográficos; si puedes, pídele a otra persona que lo lea.'),
        ],
    },
    {
        'num': '3.2',
        'slug': 'acta-de-cierre',
        'format': 'word',
        'elemento': '3 · E5811 · Evaluar resultados e impacto de la adopción de soluciones de Inteligencia Artificial en la MiPyME',
        'title': 'El acta de cierre del proyecto de adopción de soluciones de IA, documentada',
        'intro': 'Documento que formaliza el cierre del proyecto: resume lo logrado, deja por escrito los compromisos pendientes y los datos de contacto para soporte, y lo firman quien hizo la consultoría y el representante de la MiPyME.',
        'f21': [
            'Contiene el resumen ejecutivo del proyecto: alcance, objetivos y resultados obtenidos',
            'Incluye el listado de las soluciones de IA implementadas y su estado operativo al cierre',
            'Incluye las lecciones aprendidas durante el proyecto de adopción',
            'Contiene descritos los compromisos pendientes y próximos pasos acordados entre ambas partes',
            'Contiene los datos de contacto: nombre, correo y teléfono para el soporte técnico en incidencias futuras',
            'Incluye nombre completo y firmas del consultor y del representante de la MiPyME',
            'Se presenta en formato digital/físico, sin errores ortográficos',
        ],
        'espiga': 'Acta de La Espiga firmada el 30 de mayo por Doña Beatriz y por Andrea, la consultora. Compromiso pendiente: revisar el asistente en julio para agregar 10 preguntas frecuentes nuevas. Contacto de soporte: correo y WhatsApp de Andrea. Lección aprendida: capacitar primero a las personas más abiertas al cambio; después ellas convencen a las demás.',
        'preguntas': [
            ('Resumen ejecutivo del proyecto', 'Alcance original, objetivos planteados, resultados obtenidos. Una página.'),
            ('Soluciones implementadas + estado al cierre', 'Lista de cada solución + estado: operando / operando con incidencias / pausada / cancelada.'),
            ('Lecciones aprendidas', 'Lo que funcionó, lo que no, lo que harías diferente. 5-7 lecciones específicas.'),
            ('Compromisos pendientes y próximos pasos', 'Si quedó algo a futuro: qué, cuándo, responsable. Si no quedó nada pendiente, decláralo explícitamente.'),
            ('Contactos de soporte técnico', 'Nombre, correo y teléfono de quien dará soporte técnico ante incidencias futuras. Puedes agregar el horario de atención.'),
            ('Nombres completos y firmas', 'Nombre completo y firma de quien hizo la consultoría y del representante de la MiPyME, en papel o con firma electrónica.'),
            ('Presentación y revisión final', '¿La entregarás en formato digital o físico? Antes de entregarla, revisa que la redacción sea clara y que no tenga errores ortográficos; si puedes, pídele a otra persona que la lea.'),
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
  color: #4B5563;
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
.brand-header .subtitle { color: #4B5563; font-size: 10pt; margin: 0; }
.brand-header .meta { text-align: right; font-size: 9pt; color: #4B5563; width: 130pt; }
.brand-header .meta strong { color: #28467e; font-size: 11pt; }

.product-data {
  background: #EAF4FF;
  border: 1pt solid #D9E4F2;
  padding: 12pt 16pt;
  margin: 0 0 20pt 0;
  border-radius: 4pt;
}
.product-data table { width: 100%; border-collapse: collapse; }
.product-data td { padding: 4pt 8pt; font-size: 10pt; border: none; }
.product-data td:first-child { font-weight: bold; color: #28467e; width: 30%; }
.product-data .blank { border-bottom: 1pt solid #4B5563; display: inline-block; min-width: 220pt; }

.intro {
  background: #FFF3CC;
  border-left: 4pt solid #f7c031;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  color: #4B5563;
}

.f21-box {
  background: #EAF4FF;
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
.f21-box ul { margin: 0; padding-left: 18pt; color: #4B5563; }
.f21-box li { margin-bottom: 4pt; }
.f21-box .taxativo { background: #F7EDEF; color: #822d3f; font-weight: bold; padding: 1pt 6pt; border-radius: 3pt; font-size: 9pt; margin-left: 4pt; }

.espiga-box {
  background: #FFF3CC;
  border: 1pt dashed #f29100;
  padding: 12pt 16pt;
  margin: 14pt 0 20pt;
  font-size: 10pt;
  font-style: italic;
  color: #28467e;
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
  border-bottom: 1pt dotted #D9E4F2;
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
  color: #4B5563;
  font-size: 10pt;
  font-style: italic;
  margin: 6pt 0 8pt 30pt;
  line-height: 1.45;
}
.fill-area {
  border: 1pt dashed #D9E4F2;
  background: #FAFCFF;
  padding: 22pt 16pt;
  margin: 6pt 0 0 30pt;
  min-height: 60pt;
  color: #4B5563;
  font-style: italic;
  font-size: 10pt;
}

.footer {
  margin-top: 36pt;
  padding-top: 10pt;
  border-top: 1pt solid #D9E4F2;
  font-size: 8pt;
  color: #4B5563;
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
<p class="subtitle">Curso EC1830 · Producto del Elemento {elemento}</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Plantilla editable<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Quien te evalúa no busca que llenes la plantilla: busca que tu producto cumpla cada criterio del EC1830 con los datos de tu proyecto con una MiPyME, en tu lugar de trabajo o en una situación simulada. Las preguntas guía te orientan; las respuestas son tuyas.</div>

<div class="f21-box">
<h3>Qué pide el EC1830 (criterios literales)</h3>
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
Mi CompañIA · Una iniciativa de FUNDES México con el apoyo de Google.org<br>
Plantilla del curso EC1830 · Para que la llenes con los datos de tu proyecto con una MiPyME
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
table.matrix th, table.matrix td {{ border: 1pt solid #4B5563; padding: 6pt 8pt; vertical-align: top; }}
table.matrix th {{ background: #28467e; color: white; font-weight: bold; text-align: left; }}
table.matrix tr.score th {{ background: #f7c031; color: #28467e; }}
table.matrix td.fill {{ background: #fffbf0; min-height: 22pt; height: 22pt; color: #4B5563; font-style: italic; }}
table.matrix tr:nth-child(even) td.fill {{ background: #fffbf0; }}
</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;"><div class="brand-block">Mi<br>CompañIA</div></td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Curso EC1830 · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Excel es el formato natural para esta clase de producto: te permite añadir filas conforme detectes más oportunidades, ordenar por puntaje y generar gráficas. <strong>Llénala con los datos de tu proyecto.</strong></div>

<div class="f21-box">
<h3>Qué pide el EC1830 (criterios literales)</h3>
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
Mi CompañIA · FUNDES México con el apoyo de Google.org · Plantilla Excel del curso EC1830
</div>

</body>
</html>
"""

# ===========================================================================
# GENERADOR PPTX REAL (2.3 material de capacitación)
# ===========================================================================
#
# python-pptx solo se importa si hay productos con format="pptx".
# La estética: 16:9, marca Mi CompañIA arriba, layout consistente con los
# otras 11 plantillas HTML (mismo azul, mismo amarillo, mismas cajas).

def generate_pptx_capacitacion(prod):
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.util import Inches, Pt

    AZUL = RGBColor(0x28, 0x46, 0x7E)
    AMARILLO = RGBColor(0xF7, 0xC0, 0x31)
    AZUL_CLARO = RGBColor(0xEA, 0xF4, 0xFF)      # --color-azul-suave
    AMARILLO_CLARO = RGBColor(0xFF, 0xF3, 0xCC)
    BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
    NEGRO = RGBColor(0x4B, 0x55, 0x63)           # --color-gris-texto
    GRIS = RGBColor(0x4B, 0x55, 0x63)            # --color-gris-texto
    GRIS_CLARO = RGBColor(0xFA, 0xFC, 0xFF)      # --color-blanco-calido
    GRIS_PUNTEADO = RGBColor(0xD9, 0xE4, 0xF2)   # --color-gris-linea
    CREMA = RGBColor(0xFF, 0xFB, 0xF0)           # --color-amarillo-mas-claro
    ROJO = RGBColor(0x82, 0x2D, 0x3F)            # granate brandbook

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    SW, SH = prs.slide_width, prs.slide_height
    blank = prs.slide_layouts[6]

    def solid(shape, color):
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.fill.background()

    def textbox(slide, x, y, w, h, text, *, size=18, bold=False, italic=False,
                color=AZUL, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font_name="Calibri"):
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        tf.margin_left = Inches(0.05)
        tf.margin_right = Inches(0.05)
        tf.margin_top = Inches(0.02)
        tf.margin_bottom = Inches(0.02)
        p = tf.paragraphs[0]
        p.alignment = align
        run = p.add_run()
        run.text = text
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        run.font.name = font_name
        return tb

    def filled_shape(slide, shape_type, x, y, w, h, fill, line_color=None):
        s = slide.shapes.add_shape(shape_type, x, y, w, h)
        solid(s, fill)
        if line_color is not None:
            s.line.color.rgb = line_color
            s.line.width = Pt(0.75)
        return s

    def header_bar(slide, prod):
        # franja azul superior
        band = filled_shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, SW, Inches(0.5), AZUL)
        # franja amarilla justo debajo
        filled_shape(slide, MSO_SHAPE.RECTANGLE, 0, Inches(0.5), SW, Inches(0.06), AMARILLO)
        # logo "Mi CompañIA"
        textbox(slide, Inches(0.35), Inches(0.05), Inches(3.5), Inches(0.4),
                "Mi CompañIA", size=14, bold=True, color=AMARILLO, anchor=MSO_ANCHOR.MIDDLE)
        # título de producto
        textbox(slide, Inches(3.9), Inches(0.05), Inches(7.5), Inches(0.4),
                f"· {prod['title']}", size=12, color=BLANCO, anchor=MSO_ANCHOR.MIDDLE)
        # número de producto a la derecha
        textbox(slide, Inches(11.4), Inches(0.05), Inches(1.8), Inches(0.4),
                f"Producto {prod['num']}", size=12, bold=True, color=AMARILLO,
                align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    def footer_band(slide, page_num=None, total=None):
        filled_shape(slide, MSO_SHAPE.RECTANGLE, 0, Inches(7.15), SW, Inches(0.35), AMARILLO)
        label = "Mi CompañIA  ·  FUNDES México  ·  AIxMiPyMEs"
        if page_num is not None and total is not None:
            label += f"   ·   {page_num} / {total}"
        textbox(slide, Inches(0), Inches(7.2), SW, Inches(0.3),
                label, size=10, bold=True, color=AZUL, align=PP_ALIGN.CENTER,
                anchor=MSO_ANCHOR.MIDDLE)

    # cuántas slides totales calcularemos: portada + datos + criterios del EC + Espiga + N preguntas + cierre
    total = 4 + len(prod["preguntas"]) + 1
    page = 1

    # ---- Slide 1: portada ----
    s = prs.slides.add_slide(blank)
    bg = filled_shape(s, MSO_SHAPE.RECTANGLE, 0, 0, SW, SH, AZUL)
    # bloque decorativo amarillo a la derecha
    filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(9.5), 0, Inches(3.833), SH, AMARILLO)
    filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(9.5), 0, Inches(0.12), SH, AMARILLO)
    # cuadro central
    textbox(s, Inches(0.7), Inches(2.0), Inches(8.5), Inches(0.6),
            f"EC1830  ·  PRODUCTO {prod['num']}  ·  ELEMENTO {prod['elemento']}",
            size=15, bold=True, color=AMARILLO)
    textbox(s, Inches(0.7), Inches(2.7), Inches(8.5), Inches(2.0),
            prod["title"], size=44, bold=True, color=BLANCO)
    # subtitle
    textbox(s, Inches(0.7), Inches(5.0), Inches(8.5), Inches(0.6),
            "Material de capacitación al personal", size=20, italic=True, color=AZUL_CLARO)
    # banda amarilla con autoría
    textbox(s, Inches(0.7), Inches(5.9), Inches(8.5), Inches(0.5),
            "Mi CompañIA  ·  FUNDES México con el apoyo de Google.org",
            size=12, bold=True, color=AMARILLO)
    # logo en banda derecha
    badge = filled_shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.1), Inches(3.0),
                        Inches(2.7), Inches(1.5), AZUL)
    tf = badge.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Mi\nCompañIA"
    r.font.size = Pt(28)
    r.font.bold = True
    r.font.color.rgb = AMARILLO

    # ---- Slide 2: datos de la capacitación ----
    page += 1
    s = prs.slides.add_slide(blank)
    header_bar(s, prod)
    textbox(s, Inches(0.5), Inches(1.0), Inches(12.3), Inches(0.8),
            "Datos de esta capacitación", size=32, bold=True, color=AZUL)
    textbox(s, Inches(0.5), Inches(1.8), Inches(12.3), Inches(0.6),
            "Completa antes de impartirla. Define alcance, audiencia y tiempo para que el evaluador vea contexto.",
            size=13, italic=True, color=GRIS)
    fields = [
        "Nombre de la MiPyME",
        "Personal capacitado (nombres + cargo)",
        "Fecha de la capacitación",
        "Duración estimada",
        "Soluciones cubiertas en esta sesión",
    ]
    for i, label in enumerate(fields):
        y = Inches(2.7 + i * 0.75)
        # franja azul claro
        filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.5), y, Inches(12.3), Inches(0.6), AZUL_CLARO)
        # label
        textbox(s, Inches(0.7), y, Inches(4.0), Inches(0.6),
                label + ":", size=13, bold=True, color=AZUL, anchor=MSO_ANCHOR.MIDDLE)
        # línea para llenar
        textbox(s, Inches(4.8), y, Inches(8.0), Inches(0.6),
                "________________________________________", size=13, color=GRIS, anchor=MSO_ANCHOR.MIDDLE)
    footer_band(s, page, total)

    # ---- Slide 3: criterios del EC1830 ----
    page += 1
    s = prs.slides.add_slide(blank)
    header_bar(s, prod)
    textbox(s, Inches(0.5), Inches(1.0), Inches(12.3), Inches(0.8),
            "Qué pide el EC1830 · criterios literales",
            size=28, bold=True, color=AZUL)
    textbox(s, Inches(0.5), Inches(1.8), Inches(12.3), Inches(0.5),
            "Texto literal del EC1830 publicado en el DOF. Tu material debe cubrir cada criterio.",
            size=12, italic=True, color=GRIS)
    box = filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(2.4),
                      Inches(12.3), Inches(4.5), AZUL_CLARO)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_top = Inches(0.3)
    tf.margin_right = Inches(0.4)
    # Criterios literales del EC1830; el EC no marca requisitos taxativos.
    for i, crit in enumerate(prod["f21"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        r = p.add_run()
        r.text = "•  " + crit
        r.font.size = Pt(14)
        r.font.color.rgb = AZUL
    footer_band(s, page, total)

    # ---- Slide 4: caso La Espiga ----
    page += 1
    s = prs.slides.add_slide(blank)
    header_bar(s, prod)
    textbox(s, Inches(0.5), Inches(1.0), Inches(12.3), Inches(0.8),
            "Ejemplo orientativo · caso La Espiga", size=28, bold=True, color=AZUL)
    textbox(s, Inches(0.5), Inches(1.8), Inches(12.3), Inches(0.5),
            "Solo para mostrar el TIPO de contenido. NO copies esto a tu MiPyME.",
            size=12, italic=True, color=GRIS)
    box = filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(2.4),
                      Inches(12.3), Inches(4.5), CREMA)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = prod["espiga"]
    r.font.size = Pt(16)
    r.font.italic = True
    r.font.color.rgb = RGBColor(0x28, 0x46, 0x7E)
    footer_band(s, page, total)

    # ---- Slide por cada pregunta guía ----
    for idx, (title, help_text) in enumerate(prod["preguntas"], start=1):
        page += 1
        title_lower = title.lower()
        is_prompt = "prompt" in title_lower
        is_errors = "error" in title_lower or "qué hacer" in title_lower

        s = prs.slides.add_slide(blank)
        header_bar(s, prod)
        # número grande en círculo
        circle = filled_shape(s, MSO_SHAPE.OVAL, Inches(0.55), Inches(0.95),
                             Inches(1.1), Inches(1.1), AZUL)
        tf = circle.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = str(idx)
        r.font.size = Pt(36)
        r.font.bold = True
        r.font.color.rgb = AMARILLO
        # eyebrow "LÁMINA N"
        textbox(s, Inches(1.85), Inches(0.95), Inches(11), Inches(0.4),
                f"LÁMINA {idx}", size=11, bold=True, color=AMARILLO)
        # título
        textbox(s, Inches(1.85), Inches(1.3), Inches(11.2), Inches(0.9),
                title, size=26, bold=True, color=AZUL)
        # subrayado amarillo
        filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(1.85), Inches(2.18),
                    Inches(2.5), Inches(0.06), AMARILLO)
        # help text
        textbox(s, Inches(0.5), Inches(2.4), Inches(12.3), Inches(0.8),
                help_text, size=13, italic=True, color=GRIS)

        # Contenido específico
        if is_prompt:
            # 2 cajas de prompt apiladas
            for i, (label_text, bg_color, accent) in enumerate([
                ("PROMPT SUGERIDO", AMARILLO_CLARO, AMARILLO),
                ("OTRO PROMPT", AZUL_CLARO, AZUL),
            ]):
                y = Inches(3.5 + i * 1.7)
                # franja izquierda como acento
                filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.5), y, Inches(0.12), Inches(1.5), accent)
                box = filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.62), y, Inches(12.2), Inches(1.5), bg_color)
                tf = box.text_frame
                tf.word_wrap = True
                tf.margin_left = Inches(0.3)
                tf.margin_top = Inches(0.15)
                tf.margin_right = Inches(0.3)
                p = tf.paragraphs[0]
                r = p.add_run()
                r.text = label_text
                r.font.size = Pt(10)
                r.font.bold = True
                r.font.color.rgb = AZUL
                p2 = tf.add_paragraph()
                p2.space_before = Pt(4)
                r = p2.add_run()
                r.text = "[ Pega aquí un prompt completo: rol del asistente + contexto de la MiPyME + formato de salida esperado + ejemplo. ]"
                r.font.size = Pt(13)
                r.font.italic = True
                r.font.color.rgb = RGBColor(0x28, 0x46, 0x7E)
                r.font.name = "Courier New"
        elif is_errors:
            # tabla de 4 columnas x 5 filas (1 header + 4 data)
            tbl_shape = s.shapes.add_table(rows=5, cols=4,
                                            left=Inches(0.5), top=Inches(3.5),
                                            width=Inches(12.3), height=Inches(3.5))
            tbl = tbl_shape.table
            tbl.columns[0].width = Inches(2.6)
            tbl.columns[1].width = Inches(2.5)
            tbl.columns[2].width = Inches(3.7)
            tbl.columns[3].width = Inches(3.5)
            headers = ["Error frecuente", "Cómo identificarlo", "Cómo resolverlo", "Cuándo escalar"]
            for c, h in enumerate(headers):
                cell = tbl.cell(0, c)
                cell.fill.solid()
                cell.fill.fore_color.rgb = AZUL
                cell.text = h
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(12)
                        run.font.bold = True
                        run.font.color.rgb = BLANCO
            for row in range(1, 5):
                for col in range(4):
                    cell = tbl.cell(row, col)
                    cell.fill.solid()
                    cell.fill.fore_color.rgb = GRIS_CLARO if row % 2 == 1 else BLANCO
                    cell.text = ""
        else:
            # caja de captura + caja de notas
            cap = filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(3.5),
                              Inches(7.0), Inches(3.5), AZUL_CLARO, line_color=GRIS_PUNTEADO)
            tf = cap.text_frame
            tf.word_wrap = True
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = tf.margin_right = Inches(0.3)
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = "📷  Inserta aquí la captura\n\n[Sugerencia: marca con círculo rojo cada zona importante]"
            r.font.size = Pt(13)
            r.font.italic = True
            r.font.color.rgb = RGBColor(0x52, 0x9E, 0xD7)
            # caja de notas a la derecha
            notes = filled_shape(s, MSO_SHAPE.RECTANGLE, Inches(7.7), Inches(3.5),
                                Inches(5.1), Inches(3.5), GRIS_CLARO)
            tf = notes.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_right = Inches(0.3)
            tf.margin_top = Inches(0.2)
            p = tf.paragraphs[0]
            r = p.add_run()
            r.text = "NOTAS PARA EL CAPACITADOR"
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = AZUL
            p2 = tf.add_paragraph()
            p2.space_before = Pt(8)
            r = p2.add_run()
            r.text = "[ Escribe aquí qué decir mientras muestras la captura. Ejemplos reales de la MiPyME van mejor que descripciones genéricas. ]"
            r.font.size = Pt(12)
            r.font.italic = True
            r.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
        footer_band(s, page, total)

    # ---- Slide final: cierre ----
    page += 1
    s = prs.slides.add_slide(blank)
    filled_shape(s, MSO_SHAPE.RECTANGLE, 0, 0, SW, SH, AZUL)
    textbox(s, Inches(0.5), Inches(2.4), Inches(12.3), Inches(1.5),
            "¿Dudas durante la operación?", size=42, bold=True, color=AMARILLO,
            align=PP_ALIGN.CENTER)
    textbox(s, Inches(0.5), Inches(4.0), Inches(12.3), Inches(0.8),
            "El soporte sigue disponible: los datos de contacto están en el acta de cierre del proyecto.",
            size=18, color=BLANCO, align=PP_ALIGN.CENTER)
    textbox(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.6),
            "Este material puede actualizarse cuando se añadan nuevas FAQ o flujos.",
            size=14, italic=True, color=AZUL_CLARO, align=PP_ALIGN.CENTER)
    filled_shape(s, MSO_SHAPE.RECTANGLE, 0, Inches(6.85), SW, Inches(0.65), AMARILLO)
    textbox(s, Inches(0), Inches(6.95), SW, Inches(0.5),
            "Mi CompañIA  ·  FUNDES México con el apoyo de Google.org",
            size=13, bold=True, color=AZUL, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    return prs


# ===========================================================================
# RENDERIZADORES
# ===========================================================================

def render_f21(criterios):
    # Criterios literales del EC1830; el EC no marca requisitos taxativos.
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
            f'<div class="fill-area">[Escribe aquí tu respuesta con los datos de tu proyecto. Borra esta línea cuando empieces.]</div>\n'
            f'</div>\n'
        )
    return html


def render_questions_excel(preguntas):
    html = '<table class="matrix">\n<tr><th style="width: 4%;">#</th><th style="width: 28%;">Pregunta guía</th><th>Tu respuesta (con los datos de tu proyecto)</th></tr>\n'
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<tr>\n'
            f'<td style="text-align: center; font-weight: bold; color: #28467e;">{i}</td>\n'
            f'<td><strong>{title}</strong><br><span style="color: #4B5563; font-size: 9pt; font-style: italic;">{help_text}</span></td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    html += '</table>\n'
    return html


def render_matrix_example(num):
    """Para la 1.5 (matriz impacto/viabilidad), añade una hoja de cálculo pre-armada."""
    if num != "1.5":
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
            # Fórmula real, no el texto "=I*V/E": {f} lo sustituye el conversor
            # por el número de fila de la hoja.
            f'<td class="fill" style="text-align:center;color:#4B5563;">'
            f'=IFERROR(ROUND(D{{f}}*E{{f}}/F{{f}},2),"")</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    return f"""
<h2>Hoja de matriz · oportunidades de IA priorizadas</h2>
<p style="font-size: 10pt; color: #4B5563;">Añade tantas filas como oportunidades hayas detectado. Llena impacto (I), viabilidad (V) y esfuerzo (E) con valores 1-5. El score relativo (I × V / E) te orienta sobre cuál priorizar.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:22%;">Oportunidad</th><th style="width:16%;">Herramienta sugerida</th><th style="width:9%;">Impacto (1-5)</th><th style="width:9%;">Viabilidad (1-5)</th><th style="width:9%;">Esfuerzo (1-5)</th><th style="width:9%;">Score</th><th>Beneficio esperado</th></tr>
{rows}
</table>
<p style="font-size:9pt;color:#4B5563;margin-top:8pt;font-style:italic;">Convención: I y V altos suman, esfuerzo alto resta (por eso aparece en el denominador). No hay fórmula universal — adapta el cálculo a tu criterio profesional.</p>
"""


def render_gantt_example(num):
    """Para la 1.6 (hoja de ruta), añade un cronograma Gantt vacío."""
    if num != "1.6":
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
<p style="font-size: 10pt; color: #4B5563;">Marca con X (o con un color en Excel) las semanas en las que se ejecuta cada actividad. Adapta el número de semanas a tu proyecto.</p>
<table class="matrix">
<tr><th style="width:4%;">#</th><th style="width:24%;">Actividad</th><th style="width:14%;">Responsable</th>{weeks_header}</tr>
{rows}
</table>
"""


def render_indicators_example(num):
    """Para la 3.1 (reporte de evaluación de resultados), añade tabla antes/después."""
    if num != "3.1":
        return ""
    rows = ""
    for i in range(1, 7):
        rows += (
            f'<tr>\n'
            f'<td style="text-align:center;color:#28467e;font-weight:bold;">{i}</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'
            # Variación calculada: (valor actual - línea base) / línea base
            f'<td class="fill" style="text-align:center;color:#4B5563;">'
            f'=IFERROR(ROUND((D{{f}}-C{{f}})/C{{f}}*100,2),"")</td>\n'
            f'<td class="fill">&nbsp;</td>\n'
            f'</tr>\n'
        )
    return f"""
<h2>Tabla antes/después de indicadores</h2>
<p style="font-size: 10pt; color: #4B5563;">Por cada indicador del proyecto, registra la línea base, el valor actual y la variación. Así cubres de forma explícita el primer criterio del EC1830.</p>
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




def render_product(p):
    """Devuelve (contenido, extensión). Para pptx, contenido es un objeto
    Presentation que main() guarda con .save(path)."""
    f21_html = render_f21(p["f21"])

    if p["format"] == "word":
        questions_html = render_questions_word(p["preguntas"])
        html = WORD_TEMPLATE.format(
            num=p["num"], title=p["title"], elemento=p["elemento"], intro=p["intro"],
            espiga=p["espiga"], f21_html=f21_html, questions_html=questions_html,
            base_styles=BASE_STYLES,
        )
        return html, "doc"
    elif p["format"] == "excel":
        questions_html = render_questions_excel(p["preguntas"])
        matrix_html = render_matrix_example(p["num"]) + render_gantt_example(p["num"]) + render_indicators_example(p["num"])
        html = EXCEL_TEMPLATE.format(
            num=p["num"], title=p["title"], elemento=p["elemento"], intro=p["intro"],
            espiga=p["espiga"], f21_html=f21_html, questions_html=questions_html,
            matrix_html=matrix_html, base_styles=BASE_STYLES,
        )
        return html, "xls"
    elif p["format"] == "pptx":
        return generate_pptx_capacitacion(p), "pptx"
    raise ValueError(f"Formato desconocido: {p['format']}")


def main():
    # Borrar archivos legacy: OOXML generados antes (.docx/.xlsx) que
    # ya no usamos, y carpetas auxiliares que Office crea al previsualizar
    # HTML-en-extensión-Office.
    for ext in (".docx", ".xlsx"):
        for f in OUT.glob(f"*{ext}"):
            f.unlink()
            print(f"  [del legacy] {f.name}")
    for d in OUT.glob("*.files"):
        if d.is_dir():
            import shutil
            shutil.rmtree(d)
            print(f"  [del legacy dir] {d.name}")
    # Nombres de la numeración anterior (1-4-x, 3-4-x, 4-4-x) y el .doc que
    # precedió al .pptx del material de capacitación.
    for huerfano in list(OUT.glob("1-4-*")) + list(OUT.glob("3-4-*")) + \
            list(OUT.glob("4-4-*")):
        huerfano.unlink()
        print(f"  [del legacy] {huerfano.name}")

    for p in PRODUCTS:
        content, ext = render_product(p)
        filename = f"{p['num'].replace('.', '-')}-{p['slug']}.{ext}"
        filepath = OUT / filename
        if p["format"] == "pptx":
            content.save(filepath)
        else:
            filepath.write_text(content, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")
    print(f"\nGeneradas {len(PRODUCTS)} plantillas en {OUT}/")
    import subprocess
    import sys
    subprocess.run([sys.executable, str(ROOT / "scripts" / "convert-legacy-office.py")], check=True)


if __name__ == "__main__":
    main()
