#!/usr/bin/env python3
"""
Genera los 13 templates Word (.doc HTML) para los productos del estándar
Implementar IA. Word y LibreOffice abren estos archivos directamente.

Uso:
    python3 scripts/generate-templates.py

Salida: estandar-a/templates/<num>-<slug>.doc (13 archivos)
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-a" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

# Datos de los 13 productos (clave, num, título, elemento, características F21)
PRODUCTS = [
    {
        "num": "1.4.1",
        "slug": "reporte-evaluacion-inicial",
        "elemento": "1 · Planear",
        "title": "Reporte de evaluación inicial de la MiPyME",
        "intro": "Producto del Elemento 1 (Planear) que recoge el perfil empresarial, contactos clave, áreas de mejora identificadas, objetivos del proyecto, indicadores, metas, recursos disponibles y tiempos.",
        "secciones": [
            ("a", "Perfil empresarial", "Razón social, sector, antigüedad, número de empleados, sucursales, productos/servicios principales, mercado objetivo."),
            ("b", "Datos de contacto", "Nombre del responsable principal, cargo, correo, teléfono, dirección de la matriz."),
            ("c", "Áreas de mejora identificadas", "Procesos, áreas operativas o problemas que la MiPyME desea mejorar con IA."),
            ("d", "Objetivos del proyecto", "Qué espera lograr la MiPyME con la implementación. Específicos, medibles, alineados al negocio."),
            ("e", "Indicadores y metas", "Métricas que se usarán para medir el éxito del proyecto. Línea base actual + meta esperada."),
            ("f", "Recursos disponibles", "Presupuesto estimado, equipo humano que participará, infraestructura tecnológica existente."),
            ("g", "Tiempos previstos", "Cronograma macro: fechas de inicio, hitos clave y cierre estimado."),
        ],
    },
    {
        "num": "1.4.2",
        "slug": "informe-disponibilidad-datos",
        "elemento": "1 · Planear",
        "title": "Informe de disponibilidad y calidad de los datos",
        "intro": "Diagnóstico de los datos con los que cuenta la MiPyME y su calidad para sustentar soluciones de IA.",
        "secciones": [
            ("a", "Inventario de fuentes de datos", "CRM, hojas de cálculo, sistemas contables, mensajes de WhatsApp, correos, etc. Anota qué datos tiene cada fuente."),
            ("b", "Volumen y antigüedad", "Cantidad de registros por fuente, periodo cubierto, frecuencia de actualización."),
            ("c", "Calidad de los datos", "Completitud, consistencia, precisión, formatos. ¿Hay duplicados? ¿Campos faltantes? ¿Errores de captura?"),
            ("d", "Privacidad y permisos", "¿Hay datos personales? ¿Aviso de privacidad vigente? ¿Consentimientos firmados?"),
            ("e", "Brechas identificadas", "Datos faltantes para los procesos a intervenir. Recomendaciones para llenarlas."),
        ],
    },
    {
        "num": "1.4.3",
        "slug": "informe-diagnostico-procesos",
        "elemento": "1 · Planear",
        "title": "Informe de diagnóstico de procesos, actividades y áreas",
        "intro": "Mapeo de procesos operativos, identificación de cuellos de botella y resistencias al cambio.",
        "secciones": [
            ("a", "Mapa de involucrados", "Personas internas y externas afectadas por cada proceso. Diagrama o lista con roles."),
            ("b", "Diagnóstico al personal operativo", "Hallazgos del diagnóstico aplicado a quienes ejecutan el proceso (no solo a la dirección)."),
            ("c", "Cuellos de botella y áreas de oportunidad", "Puntos donde el proceso se atasca, demora o presenta oportunidades. Localización y causas."),
            ("d", "Ineficiencias, duplicidad y tareas repetitivas", "Tareas susceptibles de automatización o asistencia inteligente."),
            ("e", "Disposición al cambio observada", "Indicadores cualitativos de apertura/resistencia al cambio en el equipo."),
        ],
    },
    {
        "num": "1.4.4",
        "slug": "reporte-madurez-digital",
        "elemento": "1 · Planear",
        "title": "Reporte de madurez digital y disposición al cambio",
        "intro": "Evaluación estructurada de la madurez digital de la MiPyME y la disposición del personal al cambio.",
        "secciones": [
            ("a", "Metodología aplicada", "Instrumento usado para medir madurez digital (cuestionario, entrevistas, observación). Justificación."),
            ("b", "Resultados cuantitativos", "Puntajes obtenidos por dimensión (infraestructura, procesos, personas, datos, cultura)."),
            ("c", "Niveles de madurez", "Clasificación de la MiPyME en niveles (inicial, en desarrollo, intermedio, avanzado) y por dimensión."),
            ("d", "Recomendaciones de avance", "Acciones específicas para mejorar la madurez en las dimensiones más bajas."),
            ("e", "Tablero base", "Visualización gráfica del estado actual + estado objetivo a 6/12 meses."),
        ],
    },
    {
        "num": "1.4.5",
        "slug": "matriz-impacto-viabilidad",
        "elemento": "1 · Planear",
        "title": "Matriz de impacto, viabilidad y esfuerzo",
        "intro": "Priorización de las oportunidades de IA identificadas, valorando impacto, viabilidad y esfuerzo de cada una.",
        "secciones": [
            ("a", "Inventario de oportunidades", "Lista completa de oportunidades de IA detectadas en el diagnóstico."),
            ("b", "Criterios de impacto", "Qué entendemos por impacto (ahorro de tiempo, ingresos adicionales, reducción de errores, satisfacción del cliente). Escala 1-5."),
            ("c", "Criterios de viabilidad", "Disponibilidad de datos, herramientas existentes, capacidad del equipo, presupuesto. Escala 1-5."),
            ("d", "Criterios de esfuerzo", "Complejidad técnica, tiempo requerido, número de personas involucradas. Escala 1-5."),
            ("e", "Matriz visual", "Tabla con cada oportunidad y sus tres puntajes. Cuadrante de prioridad (alto impacto / baja viabilidad, etc.)."),
            ("f", "Conclusión", "Las 2-3 oportunidades recomendadas para primera fase y por qué."),
        ],
    },
    {
        "num": "1.4.6",
        "slug": "hoja-de-ruta",
        "elemento": "1 · Planear",
        "title": "Hoja de ruta de implementación de soluciones de IA",
        "intro": "Plan operativo con fases, hitos y entregables del proyecto de implementación.",
        "secciones": [
            ("a", "Fases del proyecto", "Diagnóstico, diseño, configuración, prueba piloto, capacitación, despliegue, evaluación. Tiempos por fase."),
            ("b", "Hitos clave", "Eventos críticos del proyecto: kick-off, validación de propuesta, primera demo, go-live, cierre."),
            ("c", "Entregables por fase", "Qué documento o producto se entrega al cliente al cierre de cada fase."),
            ("d", "Dependencias y riesgos", "Tareas que dependen de otras. Riesgos identificados y planes de mitigación."),
            ("e", "Cronograma visual", "Diagrama Gantt o timeline simple con fechas tentativas."),
            ("f", "Roles y responsabilidades", "Quién hace qué de tu lado y del cliente. RACI simplificado."),
        ],
    },
    {
        "num": "1.4.7",
        "slug": "propuesta-final-implementacion",
        "elemento": "1 · Planear",
        "title": "Propuesta final de implementación integrada",
        "intro": "Documento integrador que reúne diagnóstico + matriz + hoja de ruta + estimaciones para presentación al emprendedor.",
        "secciones": [
            ("a", "Resumen ejecutivo", "Una página que sintetiza la situación actual, las oportunidades priorizadas, la propuesta de implementación y los resultados esperados."),
            ("b", "Soluciones propuestas", "Por cada oportunidad seleccionada: qué herramienta de IA, cómo se configurará, en qué proceso se integrará, qué impacto se espera."),
            ("c", "Cronograma maestro", "Línea de tiempo del proyecto completo: fases, semanas, hitos."),
            ("d", "Recursos requeridos", "Equipo humano, infraestructura tecnológica, suscripciones a herramientas."),
            ("e", "Resultados esperados", "Indicadores con metas cuantificadas y cómo se medirán."),
            ("f", "Inversión estimada", "Resumen económico (el detalle va en propuesta económica · 1.4.8)."),
            ("g", "Anexos", "Documentos de soporte: diagnóstico completo, matriz de priorización, etc."),
        ],
    },
    {
        "num": "1.4.8",
        "slug": "propuesta-economica-validada",
        "elemento": "1 · Planear",
        "title": "Propuesta económica de consultoría validada",
        "intro": "Documento contractual con honorarios, costos de implementación y, CRÍTICO, visto bueno POR ESCRITO + acuerdo de confidencialidad.",
        "secciones": [
            ("a", "Honorarios profesionales del consultor", "Monto, forma de pago, pagos parciales por hito si aplica."),
            ("b", "Costos de licencias y herramientas", "Suscripciones mensuales o únicas a herramientas de IA, plataformas, dominios, etc."),
            ("c", "Costos adicionales", "Equipo, capacitación externa, consultores especializados si los hay."),
            ("d", "Visto bueno POR ESCRITO del emprendedor", "REQUISITO TAXATIVO del estándar. Firma autógrafa, firma electrónica, correo de aprobación explícita o acuse digital. Nunca verbal."),
            ("e", "Acuerdo de confidencialidad firmado", "REQUISITO TAXATIVO del estándar. Convenio entre las partes sobre la confidencialidad de la información."),
            ("f", "Términos y condiciones", "Plazos, garantías, alcance de la consultoría, supuestos que pueden modificarla."),
        ],
    },
    {
        "num": "3.4.1",
        "slug": "soluciones-implementadas",
        "elemento": "2 · Ejecutar",
        "title": "Soluciones de IA implementadas en operación",
        "intro": "Producto NO documental: las soluciones reales configuradas y funcionando en el entorno tecnológico de la MiPyME en al menos un proceso. Este template documenta lo que implementaste.",
        "secciones": [
            ("a", "Inventario de soluciones implementadas", "Lista de cada solución de IA configurada (nombre comercial, módulo, proceso intervenido)."),
            ("b", "Estado operacional", "Confirmación de que cada solución está OPERANDO al momento de la evaluación. Capturas de pantalla de uso reciente."),
            ("c", "Procesos intervenidos", "Detalle de qué proceso operativo de la MiPyME usa ahora cada solución."),
            ("d", "Evidencia de funcionamiento", "Capturas, registros de uso, métricas de las últimas semanas."),
            ("e", "Personal autorizado", "Quiénes en la MiPyME tienen acceso a cada solución."),
        ],
    },
    {
        "num": "3.4.2",
        "slug": "informe-tecnico-configuracion",
        "elemento": "2 · Ejecutar",
        "title": "Informe técnico de configuración",
        "intro": "Documento técnico exhaustivo de cómo está configurada cada solución, para que la MiPyME pueda mantenerla más allá de la consultoría.",
        "secciones": [
            ("a", "Resumen ejecutivo", "Qué se implementó y para qué. Una página."),
            ("b", "Arquitectura general", "Diagrama de cómo se conectan las herramientas con los procesos."),
            ("c", "Configuración por solución", "Por cada solución: nombre, propósito, parámetros, integraciones, accesos y permisos."),
            ("d", "Requisitos técnicos", "Conectividad, suscripciones, equipos, navegadores soportados."),
            ("e", "Ciberseguridad y normativa aplicable", "Medidas de seguridad implementadas, cumplimiento LFPDPPP, controles de acceso."),
            ("f", "Pruebas ejecutadas", "Tipos de pruebas, resultados, indicadores de desempeño."),
            ("g", "Anexos técnicos", "Capturas de pantalla, configuraciones detalladas, scripts si aplica."),
        ],
    },
    {
        "num": "3.4.3",
        "slug": "material-capacitacion",
        "elemento": "2 · Ejecutar",
        "title": "Material de capacitación",
        "intro": "Material que entregas al personal para que opere autónomamente las soluciones implementadas.",
        "secciones": [
            ("a", "Instrucciones paso a paso", "Cómo operar cada herramienta. Capturas numeradas, lenguaje sencillo."),
            ("b", "Ejemplos contextualizados", "Ejemplos de uso aplicados a la realidad específica de la MiPyME."),
            ("c", "Prompts recomendados", "Lista de prompts efectivos para cada caso de uso típico (CRÍTICO según F21)."),
            ("d", "Buenas prácticas y manejo de errores", "Qué hacer si la herramienta falla, da una respuesta incorrecta, o el sistema no responde."),
            ("e", "Adaptación al nivel digital del personal", "Lenguaje, ritmo y profundidad acorde al nivel real de las personas que lo usarán."),
            ("f", "Formato accesible", "Documento digital, accesible (no PDF escaneado), con índice navegable."),
        ],
    },
    {
        "num": "4.4.1",
        "slug": "reporte-evaluacion-resultados",
        "elemento": "3 · Evaluar",
        "title": "Reporte de evaluación de resultados",
        "intro": "Documento que mide el impacto del proyecto comparando antes/después y estimando el retorno de inversión.",
        "secciones": [
            ("a", "Comparación de indicadores antes/después", "Tabla con cada indicador del proyecto: línea base + valor actual + variación porcentual."),
            ("b", "Tablero de indicadores", "Visualización gráfica de los resultados cuantitativos y cualitativos."),
            ("c", "Estimación de ROI", "Cálculo del retorno de inversión: beneficios obtenidos vs. costo total del proyecto."),
            ("d", "Incidencias documentadas", "Eventos no planificados que ocurrieron durante la operación. Acciones correctivas aplicadas."),
            ("e", "Lecciones aprendidas", "Qué funcionó bien, qué se haría diferente la próxima vez."),
            ("f", "Recomendaciones de optimización", "Próximos pasos recomendados para mejorar el rendimiento de las soluciones."),
        ],
    },
    {
        "num": "4.4.2",
        "slug": "acta-de-cierre",
        "elemento": "3 · Evaluar",
        "title": "Acta de cierre del proyecto",
        "intro": "Documento formal de cierre con conformidad explícita del emprendedor. CRÍTICO: requiere firmas de ambas partes y contactos de soporte futuro.",
        "secciones": [
            ("a", "Resumen del proyecto", "Qué se implementó, en qué tiempo, con qué resultados generales."),
            ("b", "Conformidad explícita del emprendedor", "Declaración formal de aceptación de los resultados. (REQUISITO TAXATIVO del F21)."),
            ("c", "Lecciones aprendidas", "Síntesis de las lecciones del proyecto para ambas partes."),
            ("d", "Compromisos pendientes", "Si quedó algún compromiso a futuro: qué, cuándo, responsable."),
            ("e", "Contactos de soporte", "Datos de contacto del consultor para incidencias futuras. (REQUISITO TAXATIVO)."),
            ("f", "Firmas", "Firma del consultor + firma del representante legal de la MiPyME. Físicas o digitales con valor legal. (REQUISITO TAXATIVO)."),
            ("g", "Formato", "Digital o físico, sin errores ortográficos, presentación profesional."),
        ],
    },
]


HTML_TEMPLATE = """<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:w="urn:schemas-microsoft-com:office:word"
      xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="ProgId" content="Word.Document">
<meta name="Generator" content="Microsoft Word">
<meta name="Originator" content="Microsoft Word">
<title>{num} · {title}</title>
<!--[if gte mso 9]>
<xml>
<w:WordDocument>
<w:View>Print</w:View>
<w:Zoom>100</w:Zoom>
<w:DoNotOptimizeForBrowser/>
</w:WordDocument>
</xml>
<![endif]-->
<style>
@page {{
  size: 21.59cm 27.94cm;
  margin: 2.5cm 2cm;
}}
body {{
  font-family: 'Calibri', 'Arial', sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #333;
}}
.brand-header {{
  border-bottom: 3pt solid #f7c031;
  padding-bottom: 12pt;
  margin-bottom: 24pt;
}}
.brand-header table {{
  width: 100%;
  border: none;
  border-collapse: collapse;
}}
.brand-header td {{
  border: none;
  vertical-align: middle;
  padding: 0;
}}
.brand-header h1 {{
  color: #28467e;
  font-size: 18pt;
  margin: 0 0 4pt 0;
  font-weight: bold;
}}
.brand-header .subtitle {{
  color: #666;
  font-size: 10pt;
  margin: 0;
}}
.brand-header .meta {{
  text-align: right;
  font-size: 9pt;
  color: #666;
}}
.product-num {{
  display: inline-block;
  background: #f7c031;
  color: #28467e;
  padding: 4pt 10pt;
  border-radius: 4pt;
  font-weight: bold;
  font-size: 10pt;
  margin-bottom: 10pt;
}}
h2 {{
  color: #28467e;
  font-size: 14pt;
  border-bottom: 1pt solid #f7c031;
  padding-bottom: 4pt;
  margin-top: 22pt;
  margin-bottom: 12pt;
}}
h3 {{
  color: #1F4E8C;
  font-size: 12pt;
  margin-top: 16pt;
  margin-bottom: 8pt;
}}
.intro {{
  background: #FFF3CC;
  border-left: 4pt solid #f7c031;
  padding: 12pt 16pt;
  margin: 16pt 0;
  font-size: 10pt;
  color: #555;
}}
.section {{
  margin-bottom: 18pt;
}}
.section-letter {{
  display: inline-block;
  background: #28467e;
  color: white;
  width: 24pt;
  height: 24pt;
  text-align: center;
  border-radius: 50%;
  font-weight: bold;
  font-size: 11pt;
  line-height: 24pt;
  vertical-align: middle;
  margin-right: 6pt;
}}
.section-title {{
  font-weight: bold;
  color: #28467e;
  font-size: 12pt;
}}
.section-help {{
  color: #666;
  font-size: 10pt;
  font-style: italic;
  margin: 4pt 0 8pt 32pt;
}}
.fill-area {{
  border: 1pt dashed #ccc;
  background: #fafafa;
  padding: 18pt;
  margin: 6pt 0 0 32pt;
  min-height: 60pt;
  color: #aaa;
  font-style: italic;
  font-size: 10pt;
}}
.product-data {{
  background: #f5f9ff;
  border: 1pt solid #cce0f5;
  padding: 12pt 16pt;
  margin: 0 0 24pt 0;
  border-radius: 4pt;
}}
.product-data table {{
  width: 100%;
  border-collapse: collapse;
}}
.product-data td {{
  padding: 4pt 8pt;
  font-size: 10pt;
  border: none;
}}
.product-data td:first-child {{
  font-weight: bold;
  color: #28467e;
  width: 30%;
}}
.product-data .blank {{
  border-bottom: 1pt solid #999;
  display: inline-block;
  min-width: 200pt;
}}
.footer {{
  margin-top: 40pt;
  padding-top: 12pt;
  border-top: 1pt solid #ddd;
  font-size: 8pt;
  color: #999;
  text-align: center;
  font-style: italic;
}}
.required-badge {{
  background: #FFE0E0;
  color: #C0392B;
  font-size: 9pt;
  font-weight: bold;
  padding: 2pt 8pt;
  border-radius: 3pt;
  margin-left: 8pt;
}}
</style>
</head>
<body>

<div class="brand-header">
<table>
<tr>
<td style="width: 80pt;">
<!-- Logo placeholder. En la versión web, el logo se inserta como imagen. -->
<div style="background: #28467e; color: #f7c031; font-weight: bold; font-size: 14pt; padding: 14pt 8pt; text-align: center; border-radius: 6pt;">Mi<br>CompañIA</div>
</td>
<td style="padding-left: 14pt;">
<h1>{title}</h1>
<p class="subtitle">Manual de Implementar IA · Producto del Elemento {elemento}</p>
</td>
<td class="meta" style="width: 140pt;">
<strong>Producto {num}</strong><br>
Template editable<br>
<em>Mi CompañIA · FUNDES</em>
</td>
</tr>
</table>
</div>

<div class="intro">
<strong>Sobre este template.</strong> {intro} Llena cada sección con los datos reales de tu MiPyME. El evaluador revisará que cada característica del F21 esté cubierta — usa este template como guía, pero adapta el contenido a tu proyecto real. <strong>Documentos fabricados ad hoc se detectan con facilidad.</strong>
</div>

<div class="product-data">
<table>
<tr><td>Nombre del proyecto</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>MiPyME (razón social)</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Persona responsable</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Consultor responsable</td><td><span class="blank">&nbsp;</span></td></tr>
<tr><td>Fecha del documento</td><td><span class="blank">&nbsp;</span></td></tr>
</table>
</div>

<h2>Características del producto (F21)</h2>

{secciones_html}

<div class="footer">
Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org<br>
Template descargable del Manual de Implementar IA · Para ser llenado por el aspirante con datos de su proyecto real con una MiPyME
</div>

</body>
</html>
"""

SECTION_TEMPLATE = """<div class="section">
<div>
<span class="section-letter">{letter}</span>
<span class="section-title">{title}</span>{required}
</div>
<div class="section-help">{help_text}</div>
<div class="fill-area">[Llena aquí el contenido de la característica {letter}. Borra esta línea cuando empieces a escribir.]</div>
</div>
"""


def render_section(letter, title, help_text):
    required_badge = ""
    # Marca características críticas/taxativas
    if "REQUISITO TAXATIVO" in help_text or "CRÍTICO" in help_text:
        required_badge = '<span class="required-badge">REQUISITO TAXATIVO</span>'
    return SECTION_TEMPLATE.format(
        letter=letter,
        title=title,
        help_text=help_text,
        required=required_badge,
    )


def render_product(p):
    secciones_html = "\n".join(render_section(*s) for s in p["secciones"])
    return HTML_TEMPLATE.format(
        num=p["num"],
        title=p["title"],
        elemento=p["elemento"],
        intro=p["intro"],
        secciones_html=secciones_html,
    )


def main():
    for p in PRODUCTS:
        filename = f"{p['num'].replace('.', '-')}-{p['slug']}.doc"
        filepath = OUT / filename
        html = render_product(p)
        filepath.write_text(html, encoding="utf-8")
        print(f"  [ok] {filename}")
    print(f"\nGenerados {len(PRODUCTS)} templates en {OUT}/")


if __name__ == "__main__":
    main()
