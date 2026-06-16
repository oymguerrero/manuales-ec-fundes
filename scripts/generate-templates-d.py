#!/usr/bin/env python3
"""
Genera los 14 templates de los productos del Estándar D · Desarrollo de soluciones
de transformación digital con IA en MiPyMEs.

- 13 Word (.doc) como HTML estilizado con MIME Office
-  1 Excel (.xls) como HTML estilizado con MIME Office

Caso pedagógico: Distribuidora El Surtido — distribuidora mayorista de abarrotes.
22 empleados, 3 camionetas de reparto, ~200 clientes (tiendas de barrio).
Gerente: Raúl (ingeniero). Sistema actual: pedidos por teléfono/WhatsApp,
rutas definidas a mano, inventario en hojas de cálculo desconectadas.
Quiere una solución que ordene los pedidos, optimice las rutas y prediga
la demanda, sin contar con un área de sistemas propia.

Filosofía pedagógica: NO darle la solución al aspirante. Cada template muestra:
  (1) el criterio F21 literal
  (2) ejemplo breve del caso El Surtido (solo ilustrativo)
  (3) preguntas guía que el aspirante responde con datos de SU MiPyME real

Uso:
    python3 scripts/generate-templates-d.py

Salida: estandar-d/templates/<num_con_guiones>-<slug>.{doc|xls}
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-d" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

PRODUCTS = [
    # -----------------------------------------------------------------------
    # ELEMENTO 1 · DIAGNOSTICAR
    # -----------------------------------------------------------------------
    {
        "num": "1.1",
        "slug": "1-1-diagnostico-oportunidades",
        "format": "word",
        "elemento": "1 · Diagnosticar",
        "title": "Diagnóstico de oportunidades de transformación digital de la MiPyME, documentado",
        "intro": (
            "Es el punto de partida técnico del proyecto: un diagnóstico completo que documenta "
            "el perfil de la MiPyME, el resumen de la sesión de levantamiento con el responsable, "
            "las necesidades de transformación digital detectadas, el análisis de la infraestructura "
            "tecnológica existente y las experiencias previas de la empresa con soluciones digitales."
        ),
        "f21": [
            "(a) Contiene el perfil de la MiPyME, especificando su tamaño, giro, colaboradores, "
            "ubicación, nombre y correo electrónico de la persona de contacto",
            "(b) Incluye el resumen de la sesión sostenida con el responsable de la MiPyME, "
            "especificando día, hora, lugar, asistentes y acuerdos tomados en la reunión",
            "(c) Tiene las necesidades de transformación digital detectadas correspondientes con "
            "lo expresado por los representantes de la MiPyME",
            "(d) Proporciona el análisis de infraestructura tecnológica existente especificando el "
            "hardware, software y conectividad con la que cuenta la MiPyME",
            "(e) Refiere las experiencias en implementación de soluciones de transformación digital "
            "con las que cuenta la MiPyME",
        ],
        "caso": (
            "Distribuidora El Surtido · mayorista de abarrotes · 22 empleados · 3 camionetas. "
            "Contacto: Raúl García (gerente general) / raul@elsurtido.mx. "
            "Sesión de levantamiento: martes 4 de marzo 2025, 10:00 h, oficina El Surtido, "
            "asistentes: Raúl García (gerente), Luisa Morales (capturista), Carlos Ibarra (chofer líder). "
            "Acuerdo: entregar propuesta técnica en 2 semanas. "
            "Necesidades detectadas: captura de pedidos caótica (WhatsApp + llamadas mezcladas), "
            "rutas de reparto ineficientes (sin optimización), inventario reactivo (sin predicción). "
            "Infraestructura: 3 PCs Windows 10, 1 servidor local básico, internet 50 Mbps, "
            "3 smartphones Android con datos, sin sistema ERP. "
            "Experiencias previas: intentaron Excel compartido en 2023 — abandonado por conflictos "
            "de versiones; ninguna experiencia con IA."
        ),
        "preguntas": [
            (
                "Perfil de la MiPyME",
                "Nombre de la empresa, tamaño (micro/pequeña/mediana), giro económico, "
                "número de colaboradores, ubicación y datos de contacto del responsable "
                "(nombre, cargo, correo electrónico).",
            ),
            (
                "Resumen de la sesión de levantamiento",
                "¿Cuándo y dónde realizaste la sesión? ¿Quiénes asistieron? "
                "¿Cuáles fueron los acuerdos y compromisos establecidos?",
            ),
            (
                "Necesidades de transformación digital detectadas",
                "¿Cuáles son los procesos que la MiPyME quiere mejorar o digitalizar? "
                "Lista las necesidades tal como las expresó el responsable, no tu interpretación.",
            ),
            (
                "Análisis de infraestructura tecnológica",
                "¿Con qué hardware cuenta la MiPyME (computadoras, servidores, dispositivos móviles)? "
                "¿Qué software usa actualmente? ¿Qué tipo de conectividad y velocidad de internet tiene?",
            ),
            (
                "Experiencias previas con transformación digital",
                "¿La MiPyME ha intentado antes implementar soluciones digitales? "
                "¿Qué resultados tuvo? ¿Qué aprendizajes o resistencias dejaron esas experiencias?",
            ),
        ],
    },
    {
        "num": "1.2",
        "slug": "1-2-diagnostico-madurez-digital",
        "format": "word",
        "elemento": "1 · Diagnosticar",
        "title": "Diagnóstico de madurez digital y disposición al cambio de la MiPyME, elaborado",
        "intro": (
            "Evalúa en qué punto está la MiPyME en su camino de digitalización: el estado "
            "tecnológico actual, la calidad y estructuración de sus activos de información, "
            "la disposición del equipo al cambio, las brechas entre dónde está y dónde necesita "
            "estar, y la información disponible sobre transformación digital en la organización. "
            "Incluye la identificación formal del documento."
        ),
        "f21": [
            "(a) Contiene el estado digital/tecnológico actual de la MiPyME",
            "(b) Establece el estado de los activos de información y su grado de estructuración",
            "(c) Tiene el estatus de disposición al cambio de la MiPyME",
            "(d) Indica las brechas digitales/tecnológicas existentes entre el estado actual de "
            "la MiPyME y la expectativa de transformación digital",
            "(e) Incluye la información disponible de la MiPyME con relación al tema de transformación digital",
            "(f) Menciona la fecha del diagnóstico, el nombre de la MiPyME, a quién va dirigido "
            "y el nombre de la empresa consultora/consultor que lo realizó",
        ],
        "caso": (
            "Estado digital actual El Surtido: nivel 1/5 — procesos manuales con apoyo puntual de "
            "herramientas digitales básicas (WhatsApp, hojas de cálculo). "
            "Activos de información: lista de 200 clientes en Excel sin depurar desde 2022; "
            "historial de pedidos solo en mensajes de WhatsApp (no estructurado); "
            "inventario en hoja de cálculo local sin respaldo. "
            "Disposición al cambio: alta en Raúl (impulsor), media en capturistas "
            "(temor a perder empleo), baja en choferes (resistencia a cambio de rutina). "
            "Brechas principales: captura digital de pedidos, trazabilidad de entregas, "
            "predicción de demanda. "
            "Fecha: 10 marzo 2025. Dirigido a: Raúl García, El Surtido. "
            "Elaborado por: Consultoría Digital MX."
        ),
        "preguntas": [
            (
                "Estado digital/tecnológico actual",
                "¿En qué nivel de madurez digital clasificas a la MiPyME y por qué? "
                "Describe cómo opera digitalmente hoy: ¿qué procesos son manuales, cuáles están "
                "parcialmente digitalizados, cuáles completamente?",
            ),
            (
                "Activos de información y su grado de estructuración",
                "¿Qué datos tiene la MiPyME (clientes, pedidos, inventario, ventas)? "
                "¿En qué formato están? ¿Están en papel, Excel, sistema, WhatsApp? "
                "¿Son fácilmente accesibles y confiables?",
            ),
            (
                "Disposición al cambio del equipo",
                "¿Cómo describe la actitud del equipo ante la digitalización? "
                "¿Quiénes son los impulsores del cambio? ¿Quiénes tienen resistencias y por qué?",
            ),
            (
                "Brechas digitales/tecnológicas",
                "¿Cuál es la diferencia entre el estado tecnológico actual y lo que necesita "
                "la MiPyME para lograr sus objetivos de transformación? "
                "Lista las brechas por orden de impacto.",
            ),
            (
                "Información disponible sobre transformación digital",
                "¿La MiPyME tiene algún documento, plan o política interna sobre digitalización? "
                "¿Han recibido capacitaciones o asesorías previas en el tema?",
            ),
            (
                "Identificación del documento",
                "Fecha del diagnóstico, nombre de la MiPyME, persona a quien va dirigido "
                "(nombre y cargo), y nombre del consultor o empresa consultora que lo elaboró.",
            ),
        ],
    },
    {
        "num": "1.3",
        "slug": "1-3-propuesta-transformacion-digital",
        "format": "word",
        "elemento": "1 · Diagnosticar",
        "title": "Documento de propuesta de transformación digital para la MiPyME, elaborado",
        "intro": (
            "La propuesta técnica central del proyecto: traduce los diagnósticos en una solución "
            "concreta con arquitectura definida. Incluye las propuestas priorizadas de transformación, "
            "los requerimientos funcionales y no funcionales, las tecnologías y APIs seleccionadas "
            "con justificación técnica, el diagrama de arquitectura (en este template representado "
            "como un placeholder — el aspirante inserta el diagrama real), el modelo de datos y "
            "flujo de información, los aspectos de ciberseguridad y el presupuesto con calendarización."
        ),
        "f21": [
            "(a) Contiene las propuestas de transformación digital correspondientes con las necesidades "
            "detectadas en la MiPyME, por orden de prioridad de atención",
            "(b) Tiene los requerimientos funcionales y no funcionales para la implementación de la "
            "transformación digital de acuerdo con los diagnósticos realizados",
            "(c) Muestra información sobre las tecnologías, APIs y servicios de inteligencia artificial "
            "seleccionados con su justificación técnica",
            "(d) Incluye el diagrama de arquitectura del sistema propuesto con sus componentes",
            "(e) Refiere el modelo de datos y flujo de información entre componentes de la propuesta de solución",
            "(f) Cumple con los aspectos de ciberseguridad, manejo de información confidencial y normativas aplicables",
            "(g) Establece el presupuesto y calendarización para la implementación de la propuesta",
        ],
        "caso": (
            "El Surtido — Propuestas priorizadas: 1) App de captura de pedidos (WhatsApp Bot + webapp), "
            "2) Optimizador de rutas con IA (Google Routes API + ML), 3) Predictor de demanda (Prophet/LLM). "
            "Requerimientos funcionales: captura de pedidos desde móvil, dashboard de rutas en tiempo real, "
            "predicción semanal de inventario. Requerimientos no funcionales: disponibilidad 99.5%, "
            "latencia < 3s, soporte offline parcial. "
            "Tecnologías seleccionadas: Python/FastAPI (backend), React (frontend), PostgreSQL (BD), "
            "OpenAI API (procesamiento de lenguaje natural), Google Routes API (optimización de rutas). "
            "[DIAGRAMA DE ARQUITECTURA: ver archivo adjunto arquitectura-el-surtido-v1.png] "
            "Ciberseguridad: HTTPS, JWT auth, cifrado de datos sensibles, cumplimiento LFPDPPP. "
            "Presupuesto total: $85,000 MXN. Plazo: 12 semanas."
        ),
        "preguntas": [
            (
                "Propuestas de transformación digital priorizadas",
                "¿Cuáles son las soluciones que propones implementar, en qué orden de prioridad "
                "y por qué ese orden? Vincula cada propuesta con una necesidad detectada en el diagnóstico.",
            ),
            (
                "Requerimientos funcionales",
                "¿Qué debe hacer exactamente el sistema? Lista las funciones específicas que el "
                "sistema tendrá que ejecutar para satisfacer las necesidades de la MiPyME.",
            ),
            (
                "Requerimientos no funcionales",
                "¿Qué características de calidad debe tener el sistema? "
                "(Disponibilidad mínima, latencia máxima, escalabilidad, usabilidad, "
                "soporte offline, rendimiento bajo carga, entre otros.)",
            ),
            (
                "Tecnologías, APIs y servicios de IA seleccionados",
                "¿Qué lenguajes, frameworks, bases de datos, APIs de IA y servicios en la nube "
                "usarás? Por cada uno: justifica técnicamente por qué lo elegiste sobre las alternativas.",
            ),
            (
                "Diagrama de arquitectura del sistema",
                "Adjunta el diagrama de arquitectura que muestra los componentes del sistema "
                "y cómo se conectan entre sí. El diagrama debe incluir: frontend, backend, "
                "base de datos, integraciones de IA y servicios externos.",
            ),
            (
                "Modelo de datos y flujo de información",
                "¿Qué entidades principales tiene el sistema (usuarios, pedidos, productos, rutas)? "
                "¿Cómo fluye la información entre los componentes? "
                "¿Dónde se almacena, procesa y consume cada tipo de dato?",
            ),
            (
                "Aspectos de ciberseguridad y cumplimiento normativo",
                "¿Cómo protegerás los datos de los clientes y de la MiPyME? "
                "¿Qué controles de autenticación y cifrado implementarás? "
                "¿Cómo cumples con la LFPDPPP? ¿Qué datos personales tratará el sistema?",
            ),
            (
                "Presupuesto y calendarización",
                "¿Cuánto cuesta el proyecto? Desglosa por componente o fase. "
                "¿En cuántas semanas o meses se desarrolla? "
                "¿Cuáles son los hitos principales del calendario de implementación?",
            ),
        ],
    },
    {
        "num": "1.4",
        "slug": "1-4-propuesta-autorizada",
        "format": "word",
        "elemento": "1 · Diagnosticar",
        "title": "Propuesta de transformación digital para la MiPyME, autorizada",
        "intro": (
            "Es la versión final de la propuesta, después de revisión y negociación con el "
            "responsable de la MiPyME. Documenta las modificaciones que se acordaron respecto "
            "al documento original e incluye el visto bueno formal del responsable de la MiPyME. "
            "Sin esta firma, el producto no está completo. Asegura tenerla antes del día "
            "de tu evaluación."
        ),
        "f21": [
            "(a) Contiene las modificaciones al documento original presentado",
            "(b) Incluye el VoBo de la persona responsable por parte de la MiPyME",
        ],
        "caso": (
            "El Surtido — Modificaciones acordadas en reunión del 18 marzo 2025: "
            "1) Se elimina el módulo de predicción de demanda del alcance inicial (costo y plazo). "
            "Se implementará en fase 2. 2) El presupuesto ajustado es $65,000 MXN (sin predicción). "
            "3) Se amplía el plazo de 10 a 12 semanas por agenda del equipo El Surtido. "
            "VoBo: [Firma] Raúl García, Gerente General, El Surtido · Fecha: 20 marzo 2025."
        ),
        "preguntas": [
            (
                "Modificaciones al documento original",
                "¿Qué cambios se hicieron a la propuesta original después de presentarla "
                "al responsable de la MiPyME? Describe qué se ajustó, qué se eliminó "
                "y qué se agregó, con la razón de cada cambio.",
            ),
            (
                "VoBo del responsable de la MiPyME",
                "Incluye aquí el espacio para la firma y datos del responsable de la MiPyME "
                "que autoriza la propuesta: nombre completo, cargo, fecha y firma. "
                "NOTA: sin el VoBo firmado este producto no está completo. "
                "Asegúrate de obtenerlo antes de tu evaluación.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 2 · CONSTRUIR
    # -----------------------------------------------------------------------
    {
        "num": "2.1",
        "slug": "2-1-entorno-desarrollo-configurado",
        "format": "word",
        "elemento": "2 · Construir",
        "title": "Entorno de desarrollo de la solución de transformación digital, configurado",
        "intro": (
            "Documenta el repositorio de código y el entorno de desarrollo configurado: "
            "la estructura de carpetas, el archivo de dependencias con versiones fijadas, "
            "el README con instrucciones de instalación, la gestión segura de variables de "
            "entorno y credenciales de APIs, el stack tecnológico alineado a la propuesta "
            "autorizada y el historial de cambios. Es la base desde la que parte todo el desarrollo."
        ),
        "f21": [
            "(a) Contiene el repositorio de la solución de transformación digital con la estructura "
            "de carpetas organizada según el stack tecnológico seleccionado",
            "(b) Incluye el archivo de dependencias con las versiones especificadas de cada "
            "librería y framework utilizado",
            "(c) Tiene las instrucciones de instalación, configuración y ejecución del proyecto "
            "en el archivo README",
            "(d) Indica la configuración de variables de entorno y credenciales de APIs de IA "
            "de forma segura, separadas de la solución de transformación digital",
            "(e) Refiere el stack tecnológico seleccionado correspondiente con la arquitectura "
            "definida en la propuesta autorizada",
            "(f) Describe el historial de cambios documentado",
        ],
        "caso": (
            "El Surtido — Repositorio: github.com/consultoria-mx/el-surtido-td (privado). "
            "Estructura: /backend (FastAPI), /frontend (React), /ml (modelos), "
            "/docs, /tests, /scripts. "
            "Dependencias backend: fastapi==0.110.0, sqlalchemy==2.0.28, openai==1.14.0, "
            "python-jose==3.3.0. Dependencias frontend: react@18.2.0, axios@1.6.7. "
            "README: clonar repo → crear .env desde .env.example → pip install -r requirements.txt "
            "→ uvicorn main:app --reload. "
            "Variables de entorno en .env (en .gitignore): OPENAI_API_KEY, DATABASE_URL, "
            "JWT_SECRET_KEY, GOOGLE_ROUTES_API_KEY. "
            "Historial: v0.1 (entorno base), v0.2 (modelos BD), v0.3 (endpoints pedidos)."
        ),
        "preguntas": [
            (
                "Repositorio y estructura de carpetas",
                "¿Dónde está alojado el repositorio (GitHub, GitLab, otro)? "
                "¿Cuál es la estructura de carpetas del proyecto? "
                "Explica para qué sirve cada carpeta principal.",
            ),
            (
                "Archivo de dependencias con versiones fijadas",
                "¿Qué librerías y frameworks usas? Lista todas con su versión exacta. "
                "(requirements.txt para Python, package.json para Node, etc.) "
                "¿Por qué es importante fijar las versiones?",
            ),
            (
                "README: instrucciones de instalación y ejecución",
                "¿Qué pasos sigue alguien nuevo para levantar el proyecto en su máquina? "
                "Las instrucciones deben ser suficientemente claras para seguirlas sin conocerte.",
            ),
            (
                "Variables de entorno y credenciales de APIs",
                "¿Qué credenciales y configuraciones sensibles tiene el proyecto? "
                "¿Cómo las gestionas de forma segura (archivo .env, vault, secretos del CI)? "
                "¿Confirmaste que el .env NO está en el repositorio?",
            ),
            (
                "Stack tecnológico alineado a la propuesta",
                "¿El stack configurado coincide exactamente con lo que se aprobó en la propuesta "
                "de transformación digital? Si hubo cambios, ¿cuáles y por qué?",
            ),
            (
                "Historial de cambios documentado",
                "¿Cómo documentas los cambios del proyecto? (commits con mensajes descriptivos, "
                "CHANGELOG.md, tags de versión). Describe los hitos principales del historial.",
            ),
        ],
    },
    {
        "num": "2.2",
        "slug": "2-2-checklist-verificacion-solucion",
        "format": "word",
        "elemento": "2 · Construir",
        "title": "Checklist de verificación de la solución de transformación digital con IA, desarrollada",
        "intro": (
            "NOTA PEDAGÓGICA: El Producto 2.2 es la solución de software en sí misma "
            "(código, repositorio, sistema funcionando), no un documento tradicional. "
            "No puede ser un template de Word porque ES el sistema que construiste. "
            "Este template es un checklist de verificación que te ayuda a asegurarte de que "
            "tu solución cumple con todos los criterios del F21 antes de la evaluación. "
            "Úsalo para autoevaluar tu solución y documentar las evidencias que presentarás."
        ),
        "f21": [
            "(a) Contiene el backend operativo con la lógica de negocio implementada según los "
            "requerimientos funcionales de la propuesta autorizada",
            "(b) Incluye la integración con los modelos/servicios de IA seleccionados, funcionando "
            "con manejo de errores y respuestas de respaldo",
            "(c) Tiene la interfaz de usuario de manera funcional, responsiva, accesible y "
            "conectada al backend",
            "(d) Indica el esquema de base de datos implementado con procedimientos de respaldo "
            "automatizado configurados",
            "(e) Establece las medidas de seguridad aplicadas sobre validación y sanitización de "
            "datos de entrada, autenticación de usuarios, cifrado de datos sensibles y control "
            "de acceso basado en roles",
            "(f) Refiere la manera en que se protegen los datos personales en el desarrollo de la solución",
            "(g) Incluye su documentación, nomenclatura consistente y la separación de "
            "responsabilidades específicas de las funciones de cada componente del sistema",
        ],
        "caso": (
            "El Surtido — Backend: FastAPI con endpoints /pedidos, /rutas, /inventario; "
            "integración OpenAI para procesamiento de pedidos en lenguaje natural; "
            "manejo de errores con fallback a captura manual si OpenAI no responde. "
            "Frontend: React, responsivo en móvil (choferes usan smartphone), "
            "accesible con contraste WCAG AA. "
            "BD: PostgreSQL con tablas pedidos, clientes, productos, rutas; "
            "respaldo automatizado diario con pg_dump + cron. "
            "Seguridad: validación de inputs con Pydantic, JWT con expiración 8h, "
            "cifrado de contraseñas con bcrypt, roles: admin/operador/chofer. "
            "Protección de datos: solo se almacena nombre y teléfono del cliente; "
            "aviso de privacidad integrado en el onboarding. "
            "Documentación de código: docstrings en todas las funciones, nombres en español, "
            "separación clara de routers/services/models."
        ),
        "preguntas": [
            (
                "Backend — ¿La lógica de negocio está implementada conforme a los requerimientos?",
                "Lista los endpoints o funciones principales de tu backend. "
                "¿Cada requerimiento funcional de la propuesta está implementado? "
                "Marca: implementado / parcial / pendiente.",
            ),
            (
                "Integración con IA — ¿Los modelos/servicios de IA funcionan con manejo de errores?",
                "¿Qué servicio de IA integraste y en qué funcionalidad? "
                "¿Qué pasa cuando el servicio de IA no responde o devuelve error? "
                "¿Tienes respuesta de respaldo (fallback) implementada?",
            ),
            (
                "Interfaz de usuario — ¿Es funcional, responsiva y accesible?",
                "¿La UI se ve correctamente en móvil y escritorio? "
                "¿Está conectada al backend y muestra datos reales? "
                "¿Pasó alguna verificación de accesibilidad básica?",
            ),
            (
                "Base de datos — ¿El esquema está implementado y el respaldo automatizado?",
                "Describe las tablas principales y sus relaciones. "
                "¿El respaldo automatizado está configurado y probado? "
                "¿Con qué frecuencia se ejecuta y dónde se almacena?",
            ),
            (
                "Seguridad — ¿Están aplicadas todas las medidas del F21?",
                "Marca cada medida implementada: "
                "[ ] Validación y sanitización de datos de entrada "
                "[ ] Autenticación de usuarios "
                "[ ] Cifrado de datos sensibles "
                "[ ] Control de acceso basado en roles. "
                "Describe cómo implementaste cada una.",
            ),
            (
                "Protección de datos personales",
                "¿Qué datos personales trata el sistema? "
                "¿Cómo los proteges? ¿Tienes aviso de privacidad? "
                "¿La MiPyME tiene conocimiento de qué datos se almacenan y cómo?",
            ),
            (
                "Documentación y calidad del código",
                "¿El código tiene comentarios o docstrings que explican cada función? "
                "¿La nomenclatura es consistente? "
                "¿Las responsabilidades están separadas (no todo en un solo archivo)?",
            ),
        ],
    },
    {
        "num": "2.3",
        "slug": "2-3-reporte-pruebas-tecnicas",
        "format": "word",
        "elemento": "2 · Construir",
        "title": "Reporte de pruebas técnicas de la solución de transformación digital, elaborado",
        "intro": (
            "Documenta el proceso completo de pruebas de la solución: los casos de prueba "
            "definidos con datos de entrada y resultados esperados, los resultados de pruebas "
            "unitarias, de integración y funcionales, las vulnerabilidades de seguridad identificadas "
            "y su estatus de corrección, la verificación de los servicios de IA, el plan de "
            "contingencia, la validación de calidad de respuestas de IA y la identificación "
            "del documento."
        ),
        "f21": [
            "(a) Contiene los casos de prueba definidos para cada componente de la solución "
            "con datos de entrada y resultados esperados",
            "(b) Incluye los resultados de las pruebas unitarias, las de integración y las "
            "funcionales ejecutadas",
            "(c) Apunta las vulnerabilidades de seguridad identificadas, así como el estatus "
            "de corrección de las que son solucionables",
            "(d) Tiene la información sobre la verificación realizada del correcto funcionamiento "
            "de las integraciones con los modelos/servicios de IA",
            "(e) Describe el plan de contingencia ante la interrupción/saturación del servicio de la solución",
            "(f) Refiere la validación realizada sobre la calidad y relevancia de las respuestas "
            "generadas por los componentes de IA",
            "(g) Señala la fecha de las pruebas realizadas, el nombre del responsable de aplicarlas "
            "y la versión de la solución de transformación digital evaluada",
        ],
        "caso": (
            "El Surtido — versión v0.8.2 · 12 mayo 2025 · Responsable: Consultoría Digital MX. "
            "Casos de prueba: TC-01 Captura de pedido vía WhatsApp Bot (entrada: 'quiero 5 cajas "
            "de atún', resultado esperado: pedido registrado con producto, cantidad, cliente y hora). "
            "Pruebas unitarias: 47 tests, 45 OK, 2 fallos (corregidos). "
            "Pruebas de integración: OpenAI API respondió correctamente en 98% de 50 llamadas de prueba. "
            "Vulnerabilidades: 1 SQL injection potencial en endpoint /buscar-cliente — CORREGIDA "
            "con Pydantic validation. 1 token JWT sin expiración — CORREGIDA con exp=8h. "
            "Plan de contingencia: si OpenAI no responde, el sistema activa modo de captura manual; "
            "si la base de datos falla, los pedidos se almacenan localmente y se sincronizan al restaurar. "
            "Calidad de respuestas IA: el 94% de los pedidos en lenguaje natural fueron interpretados "
            "correctamente en 100 pruebas con lenguaje variado."
        ),
        "preguntas": [
            (
                "Casos de prueba definidos",
                "Por cada componente principal de tu solución: ¿qué caso de prueba definiste? "
                "Documenta al menos un caso por componente con: nombre del caso, datos de entrada "
                "utilizados y resultado esperado.",
            ),
            (
                "Resultados de pruebas unitarias, de integración y funcionales",
                "¿Cuántas pruebas unitarias ejecutaste? ¿Cuántas pasaron y cuántas fallaron? "
                "¿Qué pruebas de integración hiciste? ¿Qué pruebas funcionales ejecutaste "
                "(simular el uso real del sistema)?",
            ),
            (
                "Vulnerabilidades de seguridad identificadas",
                "¿Hiciste alguna revisión de seguridad (manual o con herramientas)? "
                "¿Qué vulnerabilidades encontraste? Por cada una: descripción, nivel de riesgo "
                "y estatus de corrección (corregida / en proceso / aceptada con justificación).",
            ),
            (
                "Verificación de integraciones con servicios de IA",
                "¿Cómo verificaste que la integración con el servicio de IA funciona correctamente? "
                "¿Cuántas pruebas hiciste? ¿Qué porcentaje de respuestas fue correcto? "
                "¿Cómo funciona el sistema cuando el servicio de IA no está disponible?",
            ),
            (
                "Plan de contingencia",
                "¿Qué pasa si el sistema principal falla? ¿Si la base de datos no responde? "
                "¿Si el servicio de IA está saturado? "
                "Describe el plan de contingencia para cada escenario de falla crítico.",
            ),
            (
                "Validación de calidad de respuestas de IA",
                "¿Cómo evaluaste que las respuestas del componente de IA son correctas y relevantes? "
                "¿Cuántos casos de prueba usaste? ¿Qué porcentaje fue satisfactorio? "
                "¿Qué criterios usaste para definir si una respuesta es aceptable?",
            ),
            (
                "Identificación del reporte",
                "Fecha en que se ejecutaron las pruebas, nombre del responsable de realizarlas "
                "y versión exacta de la solución que se evaluó.",
            ),
        ],
    },
    {
        "num": "2.4",
        "slug": "2-4-documentacion-tecnica",
        "format": "word",
        "elemento": "2 · Construir",
        "title": "Documentación técnica de la solución de transformación digital, elaborada",
        "intro": (
            "El manual técnico completo de la solución: la arquitectura implementada con diagrama "
            "actualizado, la referencia de endpoints de la API, las instrucciones de mantenimiento "
            "y actualización, las decisiones técnicas tomadas con su justificación, la configuración "
            "de los componentes de IA y las dependencias externas. Este documento es lo que permite "
            "a otro desarrollador entender, mantener y evolucionar la solución."
        ),
        "f21": [
            "(a) Contiene la descripción de la arquitectura implementada con diagrama actualizado "
            "de componentes y flujos de datos",
            "(b) Incluye la referencia de los endpoints de la API con sus parámetros, respuestas "
            "esperadas y códigos de error",
            "(c) Tiene las instrucciones para mantenimiento, actualización y modificación futura",
            "(d) Incluye las decisiones técnicas tomadas durante el desarrollo con su justificación",
            "(e) Refiere la configuración de los componentes de IA, los modelos utilizados, los "
            "prompts implementados con sus parámetros y criterios de selección",
            "(f) Considera las dependencias externas con sus versiones, licencias y procedimiento "
            "de actualización",
        ],
        "caso": (
            "El Surtido — Arquitectura implementada: [ver diagrama-arquitectura-final-v1.png] "
            "Cambios respecto a propuesta: se añadió Redis como caché para respuestas de IA. "
            "API endpoints: POST /api/pedidos (body: {cliente_id, productos[], notas}, "
            "response: {pedido_id, status, eta_entrega}, errores: 400 validación, 503 IA no disponible). "
            "Mantenimiento: actualizar dependencias con 'pip install -U -r requirements.txt' "
            "en ambiente de staging; ejecutar tests antes de desplegar en producción. "
            "Decisión técnica: se eligió OpenAI GPT-4o-mini sobre alternativas locales por "
            "costo/desempeño para el volumen de El Surtido (~150 pedidos/día). "
            "Prompt de clasificación de pedidos: versión 2.3, temperatura 0.2, max_tokens 500. "
            "Dependencias: openai==1.14.0 (MIT), fastapi==0.110.0 (MIT), "
            "sqlalchemy==2.0.28 (MIT). Actualización: revisar changelog mensualmente."
        ),
        "preguntas": [
            (
                "Arquitectura implementada (con diagrama actualizado)",
                "Describe la arquitectura tal como quedó después del desarrollo. "
                "Adjunta el diagrama final actualizado. "
                "¿Hubo cambios respecto al diagrama de la propuesta original? ¿Cuáles y por qué?",
            ),
            (
                "Referencia de endpoints de la API",
                "Por cada endpoint de tu API: método HTTP, ruta, descripción, "
                "parámetros de entrada (body/query/path), respuesta esperada (estructura y tipos), "
                "códigos de error posibles con su significado.",
            ),
            (
                "Instrucciones de mantenimiento y actualización",
                "¿Cómo se actualiza el sistema cuando hay una nueva versión? "
                "¿Cómo se reinicia si falla? ¿Cómo se migra la base de datos cuando cambia el esquema? "
                "¿Quién puede hacer qué tipo de cambio y con qué herramientas?",
            ),
            (
                "Decisiones técnicas tomadas con justificación",
                "¿Qué decisiones técnicas importantes tomaste durante el desarrollo? "
                "(lenguaje, framework, proveedor de IA, arquitectura, base de datos). "
                "Por cada decisión: qué alternativas evaluaste y por qué elegiste la que elegiste.",
            ),
            (
                "Configuración de componentes de IA",
                "¿Qué modelo de IA usas? ¿Con qué parámetros (temperatura, max_tokens, top_p)? "
                "¿Cuáles son los prompts que implementaste? "
                "¿Por qué elegiste ese modelo sobre otros disponibles?",
            ),
            (
                "Dependencias externas con versiones y licencias",
                "Lista todas las librerías, servicios y APIs externas que usa el sistema. "
                "Por cada una: versión exacta, licencia de uso y procedimiento para actualizarla "
                "sin romper el sistema.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 3 · IMPLEMENTAR
    # -----------------------------------------------------------------------
    {
        "num": "3.1",
        "slug": "3-1-checklist-despliegue-produccion",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Checklist de despliegue de la solución de transformación digital en entorno productivo",
        "intro": (
            "NOTA PEDAGÓGICA: El Producto 3.1 es la solución instalada y operativa en la "
            "infraestructura real de la MiPyME, no un documento. No puede encapsularse en "
            "un template de Word porque ES el sistema desplegado en producción. "
            "Este checklist te ayuda a verificar que todos los criterios del F21 están cumplidos "
            "antes de tu evaluación y a documentar las evidencias de que el despliegue se realizó "
            "correctamente. El evaluador podrá solicitar que le muestres el sistema en producción "
            "funcionando."
        ),
        "f21": [
            "(a) Contiene la solución instalada y operativa en la infraestructura de la MiPyME "
            "conforme a la arquitectura autorizada",
            "(b) Incluye los modelos/servicios de inteligencia artificial conectados y respondiendo "
            "en el entorno productivo de la MiPyME",
            "(c) Tiene la base de datos final de producción con los respaldos automatizados configurados",
            "(d) Refiere el procedimiento para monitorear el consumo de tokens/créditos de las APIs de IA",
            "(e) Describe las medidas de seguridad implementadas en el entorno productivo conforme "
            "a la propuesta de transformación digital autorizada",
        ],
        "caso": (
            "El Surtido — Servidor de producción: DigitalOcean Droplet 2vCPU/4GB RAM, Ubuntu 22.04. "
            "URL producción: https://app.elsurtido.mx (SSL Let's Encrypt activo). "
            "Servicio de IA en producción: OpenAI API — confirmado respondiendo con ping de prueba "
            "el 2 junio 2025. "
            "BD de producción: PostgreSQL 16, respaldo diario con pg_dump a las 02:00h, "
            "almacenado en DigitalOcean Spaces con retención de 30 días. "
            "Monitoreo de tokens: dashboard en OpenAI Platform con alerta por email al llegar "
            "al 80% del límite mensual configurado. "
            "Seguridad en producción: firewall ufw (solo puertos 80, 443, 22), "
            "fail2ban activo, actualizaciones automáticas de seguridad habilitadas."
        ),
        "preguntas": [
            (
                "Solución instalada y operativa en la infraestructura de la MiPyME",
                "¿En qué infraestructura está desplegada la solución (servidor propio, "
                "nube — AWS/GCP/Azure/DigitalOcean, hosting compartido)? "
                "¿La URL de producción está activa y funcionando? "
                "¿La arquitectura desplegada coincide con la autorizada?",
            ),
            (
                "Servicios de IA conectados en producción",
                "¿Los modelos/servicios de IA están configurados en el entorno de producción "
                "(no en el de desarrollo)? ¿Hiciste una prueba de ping o llamada real en "
                "producción y fue exitosa? Documenta el resultado.",
            ),
            (
                "Base de datos de producción y respaldos automatizados",
                "¿La base de datos de producción tiene los datos migrados correctamente? "
                "¿El respaldo automatizado está configurado y probado? "
                "¿Con qué frecuencia se ejecuta? ¿Dónde se almacenan los respaldos? "
                "¿Puedes restaurar a partir de un respaldo?",
            ),
            (
                "Procedimiento de monitoreo de consumo de tokens/créditos de IA",
                "¿Cómo monitoreas el consumo de tokens o créditos del servicio de IA en producción? "
                "¿Hay alertas configuradas? ¿Qué pasa cuando se acerca al límite?",
            ),
            (
                "Medidas de seguridad en el entorno productivo",
                "¿Qué medidas de seguridad están activas en producción? "
                "(HTTPS, firewall, autenticación, cifrado en tránsito y en reposo). "
                "¿Coinciden con las medidas definidas en la propuesta autorizada?",
            ),
        ],
    },
    {
        "num": "3.2",
        "slug": "3-2-documentacion-tecnica-implementacion",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Documentación técnica de implementación, elaborada",
        "intro": (
            "El registro técnico completo del proceso de despliegue: el diagrama de infraestructura "
            "del entorno de producción, el registro de credenciales y accesos con permisos por rol, "
            "la configuración del dominio y certificado de seguridad, el log paso a paso del "
            "despliegue con sus resultados y el procedimiento de respaldo y restauración. "
            "Este documento es la bitácora técnica del despliegue."
        ),
        "f21": [
            "(a) Contiene el diagrama de infraestructura del entorno de producción con sus "
            "componentes y conexiones",
            "(b) Incluye el registro de credenciales y accesos a la solución, documentados "
            "con permisos asignados por rol",
            "(c) Tiene la configuración del dominio, certificado de seguridad y redirecciones aplicadas",
            "(d) Enlista los pasos ejecutados durante el despliegue con los resultados obtenidos "
            "y sus evidencias",
            "(e) Señala el procedimiento de respaldo y restauración de la base de datos a realizar "
            "en caso necesario",
        ],
        "caso": (
            "El Surtido — Infraestructura de producción: [ver diagrama-infra-prod.png] "
            "Componentes: DigitalOcean Droplet (servidor app), Managed PostgreSQL, "
            "Spaces (almacenamiento de respaldos), Load Balancer. "
            "Credenciales: Raúl (admin — acceso total), Luisa (operador — pedidos/inventario, "
            "sin acceso a configuración), choferes (solo app móvil — vista de rutas asignadas). "
            "Dominio: app.elsurtido.mx → IP del servidor. SSL: Let's Encrypt (certbot), "
            "renovación automática. Redireccionamiento HTTP → HTTPS activo. "
            "Pasos de despliegue ejecutados: 1) apt update && apt upgrade (OK), "
            "2) instalar Python 3.11 (OK), 3) clonar repo (OK), 4) configurar .env "
            "(OK), 5) migraciones BD (OK), 6) prueba de humo: curl app.elsurtido.mx/health (OK). "
            "Respaldo: pg_dump elsurtido_prod | gzip > backup_$(date +%F).sql.gz; "
            "restauración: gunzip backup.sql.gz | psql elsurtido_prod."
        ),
        "preguntas": [
            (
                "Diagrama de infraestructura de producción",
                "Adjunta el diagrama que muestra los componentes del entorno de producción "
                "(servidores, bases de datos, CDN, servicios externos) y cómo se conectan entre sí. "
                "El diagrama debe reflejar la infraestructura real, no la propuesta.",
            ),
            (
                "Registro de credenciales y accesos por rol",
                "¿Qué roles de acceso existen en el sistema? Por cada rol: qué puede hacer "
                "y qué no puede hacer. "
                "NOTA: No documentes contraseñas aquí — describe los roles y permisos, "
                "e indica dónde se almacenan las credenciales de forma segura.",
            ),
            (
                "Configuración del dominio, SSL y redirecciones",
                "¿Qué dominio se configuró? ¿Cómo está vinculado al servidor? "
                "¿Qué certificado SSL se instaló y cómo se renueva? "
                "¿Hay redirecciones configuradas (HTTP → HTTPS, www → sin www)?",
            ),
            (
                "Log de pasos del despliegue con resultados",
                "Lista los pasos que ejecutaste durante el despliegue en orden. "
                "Para cada paso: qué hiciste, qué resultado obtuviste y si hubo algún error "
                "y cómo lo resolviste. Adjunta capturas de pantalla como evidencia.",
            ),
            (
                "Procedimiento de respaldo y restauración",
                "¿Cómo se hace el respaldo de la base de datos? (comando exacto o proceso). "
                "¿Cómo se restaura a partir de un respaldo? (pasos exactos). "
                "¿Probaste la restauración? ¿Cuánto tiempo tardó?",
            ),
        ],
    },
    {
        "num": "3.3",
        "slug": "3-3-reporte-capacitacion",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Reporte de capacitación/transferencia de conocimiento al personal de la MiPyME, elaborado",
        "intro": (
            "Documenta la sesión de capacitación al equipo de la MiPyME: los temas cubiertos "
            "alineados a las funcionalidades de la solución, los manuales de usuario y de "
            "mantenimiento con capturas de pantalla y procedimientos paso a paso, los procedimientos "
            "de resolución de problemas frecuentes que el personal puede ejecutar de forma autónoma, "
            "y los datos de la sesión (asistentes, fecha, duración, materiales entregados). "
            "RECUERDA: la capacitación es el único desempeño observable del Estándar D — "
            "el evaluador te observará impartirla."
        ),
        "f21": [
            "(a) Contiene los temas cubiertos correspondientes con las funcionalidades de la "
            "solución de transformación digital implementada",
            "(b) Incluye los manuales de usuario y de mantenimiento de la solución de "
            "transformación digital con capturas de pantalla y procedimientos paso a paso",
            "(c) Tiene los procedimientos de resolución de problemas frecuentes que el personal "
            "de la MiPyME puede ejecutar de manera autónoma",
            "(d) Detalla la información sobre los asistentes, fecha, duración y materiales "
            "entregados en la sesión de capacitación",
        ],
        "caso": (
            "El Surtido — Sesión de capacitación: 5 junio 2025, 10:00-13:00h, oficina El Surtido. "
            "Asistentes: Luisa Morales (capturista), Miguel Ángel Cruz (chofer), "
            "Sandra Reyes (chofer), Raúl García (gerente). "
            "Temas cubiertos: 1) Captura de pedidos desde WhatsApp Bot (30 min), "
            "2) Uso del dashboard de rutas (45 min), 3) Consulta de inventario y alertas (20 min), "
            "4) Reporte de errores al soporte (15 min). "
            "Materiales entregados: Manual de usuario (PDF impreso), tarjeta de referencia rápida "
            "(plastificada), contacto de soporte (WhatsApp de Consultoría Digital MX). "
            "Problema frecuente #1: 'El Bot no entendió mi pedido' → Solución: escribir "
            "'PEDIDO: [producto] [cantidad]' y el sistema lo captura directamente."
        ),
        "preguntas": [
            (
                "Temas cubiertos en la capacitación",
                "¿Qué temas abordaste en la capacitación? "
                "Lista cada tema con el tiempo aproximado que le dedicaste. "
                "¿Cada funcionalidad principal de la solución fue cubierta?",
            ),
            (
                "Manual de usuario con capturas de pantalla",
                "El manual de usuario debe incluir: cómo iniciar sesión, cómo usar cada "
                "funcionalidad principal (con capturas de pantalla de cada paso) y cómo cerrar "
                "sesión. ¿Tu manual está completo? Adjúntalo o describe su contenido aquí.",
            ),
            (
                "Manual de mantenimiento básico",
                "¿Qué puede hacer el personal de la MiPyME para mantener el sistema por su cuenta? "
                "(Ejemplos: cómo reiniciar si hay error, cómo agregar un usuario nuevo, cómo "
                "exportar un reporte). Documenta cada procedimiento paso a paso.",
            ),
            (
                "Procedimientos de resolución de problemas frecuentes",
                "¿Cuáles son los 3-5 problemas más comunes que el usuario puede encontrar? "
                "Por cada uno: descripción del problema, causa probable y pasos para resolverlo "
                "sin necesidad de llamar al consultor.",
            ),
            (
                "Datos de la sesión: asistentes, fecha, duración y materiales",
                "¿Quiénes asistieron (nombre y cargo)? ¿En qué fecha y horario fue la sesión? "
                "¿Cuántas horas duró? ¿Qué materiales entregaste al equipo de la MiPyME?",
            ),
        ],
    },
    {
        "num": "3.4",
        "slug": "3-4-acta-final",
        "format": "word",
        "elemento": "3 · Implementar",
        "title": "Acta final de la solución de transformación digital, elaborada",
        "intro": (
            "El cierre formal del proyecto de implementación: el documento que registra qué "
            "entregaste, en qué estado está funcionando, qué credenciales y documentación "
            "transferiste al responsable de la MiPyME, los compromisos de mantenimiento y "
            "niveles de servicio acordados, y la firma de conformidad de ambas partes. "
            "Sin la firma del responsable de la MiPyME, este producto no está completo."
        ),
        "f21": [
            "(a) Contiene la descripción de los entregables transferidos a la MiPyME con su "
            "estatus de funcionamiento",
            "(b) Incluye las credenciales de acceso y la documentación entregados al responsable de la MiPyME",
            "(c) Tiene los compromisos de mantenimiento y niveles de servicio acordados con la "
            "MiPyME incluyendo vigencia, alcance y límites de responsabilidad del desarrollador",
            "(d) Cuenta con la firma de conformidad del responsable de la MiPyME y del consultor",
        ],
        "caso": (
            "El Surtido — Entregables transferidos: 1) Solución web en producción (app.elsurtido.mx) — "
            "FUNCIONANDO; 2) Código fuente en repositorio privado GitHub — ENTREGADO; "
            "3) Manual de usuario y mantenimiento — ENTREGADO; 4) BD de producción con datos migrados — "
            "FUNCIONANDO. "
            "Credenciales entregadas: acceso de administrador a Raúl García (sobre sellado), "
            "acceso al servidor DigitalOcean (sobre sellado), claves API documentadas en gestor "
            "de contraseñas de El Surtido. "
            "Compromisos: soporte correctivo 30 días post-entrega sin costo adicional; "
            "tiempo de respuesta: 4h en días hábiles; alcance: corrección de errores del sistema "
            "entregado; NO incluye nuevas funcionalidades. "
            "Vigencia del soporte: hasta el 5 julio 2025. "
            "Firma: Raúl García (El Surtido) · Consultor (Consultoría Digital MX) · 5 junio 2025."
        ),
        "preguntas": [
            (
                "Entregables transferidos con estatus de funcionamiento",
                "Lista cada componente que entregaste a la MiPyME. "
                "Por cada uno: descripción, estatus al momento de la entrega "
                "(funcionando / con limitaciones conocidas / pendiente de ajuste).",
            ),
            (
                "Credenciales y documentación entregados",
                "¿Qué credenciales entregaste al responsable de la MiPyME y de qué forma? "
                "(sobre sellado, gestor de contraseñas, en persona). "
                "¿Qué documentación técnica y de usuario entregaste?",
            ),
            (
                "Compromisos de mantenimiento y niveles de servicio",
                "¿Qué soporte post-entrega acordaste? Define: vigencia del soporte (fechas), "
                "alcance (qué cubre y qué no cubre), tiempo de respuesta comprometido "
                "y límites de responsabilidad del consultor.",
            ),
            (
                "Firma de conformidad",
                "Espacio para la firma de ambas partes: nombre completo, cargo y firma del "
                "responsable de la MiPyME, y nombre y firma del consultor. Fecha del acta. "
                "NOTA: sin ambas firmas este producto no está completo.",
            ),
        ],
    },

    # -----------------------------------------------------------------------
    # ELEMENTO 4 · OPTIMIZAR
    # -----------------------------------------------------------------------
    {
        "num": "4.1",
        "slug": "4-1-reporte-rendimiento-tecnico",
        "format": "excel",
        "elemento": "4 · Optimizar",
        "title": "Reporte de rendimiento técnico de la solución de transformación digital, elaborado",
        "intro": (
            "Producto de medición técnica de la solución en operación real. Registra las métricas "
            "de rendimiento (disponibilidad, latencia, tasa de error, consumo de recursos), "
            "las compara contra los umbrales definidos en la propuesta, analiza el rendimiento "
            "de los componentes de IA (calidad de respuestas, tiempos, costos por consulta) "
            "e identifica el responsable, las herramientas de medición y el periodo de análisis. "
            "Excel es el formato natural para este producto: permite añadir filas de medición "
            "y calcular promedios automáticamente."
        ),
        "f21": [
            "(a) Contiene las métricas de rendimiento de la solución de transformación recolectadas: "
            "disponibilidad, latencia, tasa de error y consumo de recursos",
            "(b) Incluye la comparación de los indicadores técnicos contra los umbrales definidos "
            "en los requerimientos de la propuesta",
            "(c) Tiene el análisis de rendimiento de los componentes de IA: calidad de respuestas, "
            "ejemplos representativos, tiempos de procesamiento y costos por consulta",
            "(d) Proporciona información sobre el periodo de medición, las herramientas utilizadas "
            "y el nombre del responsable del reporte",
        ],
        "caso": (
            "El Surtido — Periodo: 1-30 junio 2025 · Responsable: Consultoría Digital MX. "
            "Herramientas: UptimeRobot (disponibilidad), Datadog APM (latencia/errores), "
            "OpenAI Dashboard (tokens). "
            "Disponibilidad: 99.7% (umbral propuesta: 99.5% — CUMPLIDO). "
            "Latencia promedio: 1.8s (umbral: < 3s — CUMPLIDO). "
            "Tasa de error: 0.8% (umbral: < 2% — CUMPLIDO). "
            "IA: 96.2% de pedidos interpretados correctamente (meta: 90% — SUPERADO). "
            "Tiempo de procesamiento IA: 1.2s promedio. Costo por consulta: $0.003 USD. "
            "Consumo total junio: $12.40 USD (presupuesto mensual: $20 USD — DENTRO DEL LÍMITE)."
        ),
        "preguntas": [
            (
                "Métricas de rendimiento del periodo",
                "Para el periodo de medición: "
                "Disponibilidad (% de uptime), Latencia promedio (ms o segundos), "
                "Tasa de error (%), Consumo de recursos del servidor (CPU%, RAM%). "
                "¿Con qué herramienta mediste cada métrica?",
            ),
            (
                "Comparativo contra umbrales de la propuesta",
                "Por cada métrica: ¿cuál era el umbral definido en la propuesta? "
                "¿Cuál fue el resultado real? ¿Se cumplió (S/N)?",
            ),
            (
                "Rendimiento de los componentes de IA",
                "¿Cuál es el porcentaje de respuestas correctas del componente de IA? "
                "Incluye ejemplos representativos (un caso bueno, un caso con error). "
                "¿Cuál es el tiempo promedio de respuesta de la IA? "
                "¿Cuál es el costo promedio por consulta y el costo total del periodo?",
            ),
            (
                "Identificación del reporte",
                "Periodo exacto de medición (fecha inicio y fecha fin), "
                "herramientas utilizadas para cada métrica y "
                "nombre del responsable de elaborar el reporte.",
            ),
        ],
    },
    {
        "num": "4.2",
        "slug": "4-2-reporte-retroalimentacion",
        "format": "word",
        "elemento": "4 · Optimizar",
        "title": "Reporte de retroalimentación de usuarios de la MiPyME, elaborado",
        "intro": (
            "Documenta la retroalimentación recogida de los usuarios reales de la MiPyME "
            "sobre la solución en operación: los resultados de los instrumentos de medición "
            "de satisfacción aplicados, las áreas de mejora identificadas priorizadas por impacto, "
            "las recomendaciones de ajuste y los datos de la consulta (número de usuarios, "
            "fecha, instrumentos). Recuerda: necesitas usuarios reales — no puedes simular "
            "esta retroalimentación."
        ),
        "f21": [
            "(a) Contiene los resultados de los instrumentos de medición de satisfacción "
            "aplicados a los usuarios de la MiPyME",
            "(b) Detalla la información sobre las áreas de mejora identificadas a partir de "
            "los resultados del monitoreo, priorizadas según su impacto en la operación de la MiPyME",
            "(c) Indica las recomendaciones de ajuste priorizadas por impacto en la experiencia "
            "del usuario y en los objetivos de negocio de la MiPyME",
            "(d) Tiene la cantidad de usuarios participantes en el proceso de retroalimentación, "
            "la fecha de aplicación y los instrumentos utilizados",
        ],
        "caso": (
            "El Surtido — 4 usuarios encuestados (Luisa, Miguel, Sandra, Raúl). "
            "Instrumento: encuesta de satisfacción 1-5 + preguntas abiertas. "
            "Resultados: satisfacción general 4.2/5. "
            "Mayor satisfacción: captura de pedidos desde WhatsApp (4.8/5), "
            "reducción de llamadas perdidas. "
            "Área de mejora #1 (alta prioridad): las notificaciones de confirmación de pedido "
            "tardan más de 5 minutos — afecta la confianza del cliente. "
            "Área de mejora #2 (media prioridad): el dashboard no funciona bien en la "
            "pantalla pequeña del teléfono de los choferes (Nokia 3.4). "
            "Recomendaciones: 1) Optimizar pipeline de notificaciones (prioridad alta, "
            "impacto directo en satisfacción del cliente externo). "
            "2) Ajustar CSS para pantallas menores a 5 pulgadas (prioridad media). "
            "Fecha de aplicación: 28 junio 2025."
        ),
        "preguntas": [
            (
                "Resultados de los instrumentos de satisfacción",
                "¿Qué instrumento usaste para medir la satisfacción? (encuesta, entrevista, "
                "observación directa, NPS). ¿Cuáles fueron los resultados principales? "
                "Presenta los datos de forma organizada (puntuaciones, porcentajes, citas representativas).",
            ),
            (
                "Áreas de mejora identificadas y priorizadas",
                "¿Qué aspectos del sistema necesitan mejorar según los usuarios? "
                "Lista cada área de mejora e indica su nivel de prioridad "
                "(alta / media / baja) según el impacto que tiene en la operación diaria de la MiPyME.",
            ),
            (
                "Recomendaciones de ajuste priorizadas",
                "Para cada área de mejora identificada: ¿qué ajuste concreto recomiendas? "
                "Ordénalas por impacto combinado en la experiencia del usuario y en los "
                "objetivos de negocio de la MiPyME.",
            ),
            (
                "Datos de la consulta de retroalimentación",
                "¿Cuántos usuarios participaron? ¿Cuáles son sus roles en la MiPyME? "
                "¿En qué fecha se aplicó el instrumento? "
                "¿Qué instrumento(s) utilizaste exactamente?",
            ),
        ],
    },
    {
        "num": "4.3",
        "slug": "4-3-plan-optimizacion",
        "format": "word",
        "elemento": "4 · Optimizar",
        "title": "Plan de optimización de la solución de transformación digital, elaborado",
        "intro": (
            "El documento que cierra el ciclo: propone las acciones de optimización con estimación "
            "de esfuerzo y beneficio, define los ajustes a los componentes de IA (calibración, "
            "prompts, proveedores), documenta las lecciones aprendidas, propone mejoras adicionales "
            "más allá de lo solicitado (este es el AHV de Iniciativa del Elemento 4) y establece "
            "la estrategia de actualización ante cambios en tecnologías y normatividad. "
            "Es el documento que demuestra que el proyecto no termina con la entrega — evoluciona."
        ),
        "f21": [
            "(a) Incluye las acciones de optimización propuestas para cada área de mejora con "
            "su estimación de esfuerzo y beneficio esperado",
            "(b) Especifica los ajustes a los componentes de IA recomendados, incluyendo "
            "calibración de modelos, ajustes de prompts/cambio de proveedores de servicio",
            "(c) Tiene las lecciones aprendidas y recomendaciones para escalamiento futuro "
            "de la solución de transformación digital",
            "(d) Propone mejoras y optimizaciones pertinentes y adicionales a las solicitadas "
            "en el plan de mantenimiento con base en el análisis de los datos de rendimiento "
            "realizado y en las tendencias de IA del mercado",
            "(e) Define la estrategia de actualización ante cambios en los modelos de IA, "
            "tecnologías utilizadas/normatividad aplicable",
        ],
        "caso": (
            "El Surtido — Plan de optimización v1.0 · julio 2025. "
            "Acción #1: optimizar pipeline de notificaciones (esfuerzo: 8h, beneficio: "
            "reducir tiempo de confirmación de 5 min a <30s — alto impacto en confianza). "
            "Acción #2: ajustar responsive para pantallas <5 pulgadas (esfuerzo: 4h, "
            "beneficio: mejorar experiencia de choferes — impacto medio). "
            "Ajustes de IA: reducir temperatura del prompt de clasificación de 0.2 a 0.1 "
            "para mejorar consistencia; añadir ejemplos de pedidos con errores ortográficos "
            "al system prompt. "
            "Lecciones aprendidas: 1) El lenguaje real de los clientes de El Surtido tiene "
            "muchas abreviaciones locales — el prompt inicial no las contemplaba. "
            "2) La capacitación en 3h fue insuficiente para los choferes — recomendar 2 sesiones. "
            "Mejora adicional propuesta (iniciativa): integrar predicción de demanda con datos "
            "históricos de los primeros 3 meses, usando Prophet — estimado de implementación: "
            "3 semanas, potencial de reducción de desperdicio de inventario del 15%. "
            "Estrategia de actualización: revisar cambios de API de OpenAI cada trimestre; "
            "suscribirse a changelog de FastAPI; revisar LFPDPPP en caso de modificaciones legislativas."
        ),
        "preguntas": [
            (
                "Acciones de optimización con esfuerzo y beneficio estimados",
                "Para cada área de mejora identificada en el reporte de retroalimentación: "
                "¿qué acción de optimización propones? "
                "Estima el esfuerzo (horas de trabajo) y el beneficio esperado (qué mejora y en cuánto).",
            ),
            (
                "Ajustes a los componentes de IA",
                "¿Qué ajustes propones a los componentes de IA de la solución? "
                "(Cambios en los prompts, ajuste de parámetros como temperatura, "
                "cambio de modelo o proveedor de servicio). Justifica cada ajuste con datos.",
            ),
            (
                "Lecciones aprendidas y recomendaciones de escalamiento",
                "¿Qué aprendiste de este proyecto que harías diferente la próxima vez? "
                "¿Qué recomendarías si la MiPyME quisiera escalar la solución a más usuarios, "
                "más locaciones o más funcionalidades?",
            ),
            (
                "Mejoras adicionales propuestas (iniciativa propia)",
                "Más allá de corregir los problemas detectados, ¿qué mejoras adicionales propones "
                "basándote en el rendimiento observado y en las tendencias de IA del mercado? "
                "Esta sección demuestra la actitud de Iniciativa que evalúa el F21 en este elemento.",
            ),
            (
                "Estrategia de actualización tecnológica y normativa",
                "¿Cómo planeas mantener la solución actualizada cuando cambien: "
                "los modelos de IA que usa (nuevas versiones, APIs descontinuadas), "
                "las tecnologías del stack (actualizaciones de seguridad, fin de soporte), "
                "o la normatividad aplicable (cambios en LFPDPPP u otras regulaciones)?",
            ),
        ],
    },
]


# ===========================================================================
# PLANTILLAS POR FORMATO
# (mismo sistema visual que los Estándares A, B y C)
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
<p class="subtitle">Manual de Transformación Digital con IA · Producto del Elemento {elemento}</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Template editable<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Tu evaluador no busca que llenes el template — busca que respondas con datos de TU proyecto real con una MiPyME. Las preguntas guía te orientan; las respuestas son tuyas.</div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Distribuidora El Surtido (ilustrativo, NO es tu solución):</strong> {caso}</div>

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
Template del Manual de Desarrollo de Soluciones de Transformación Digital con IA · Para ser llenado por el aspirante con datos de su proyecto real con una MiPyME
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
<p class="subtitle">Manual de Transformación Digital con IA · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre este template.</strong> {intro} Excel es el formato natural para este producto: permite añadir filas de medición, calcular promedios y comparativos automáticamente. <strong>Llénalo con datos reales de TU proyecto.</strong></div>

<div class="f21-box">
<h3>Qué evalúa el F21 oficial</h3>
<ul>{f21_html}</ul>
</div>

<div class="caso-box"><strong>Caso pedagógico Distribuidora El Surtido (ilustrativo):</strong> {caso}</div>

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
Mi CompañIA · Una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org · Template del Manual de Desarrollo de Soluciones de Transformación Digital con IA
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
            f'<div class="fill-area">[Escribe aquí tu respuesta con datos reales de tu proyecto. '
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
        '<th>Tu respuesta (llena con datos de TU proyecto real)</th>'
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
      - Hoja 1: métricas de rendimiento por periodo (10 filas)
      - Hoja 2: comparativo indicadores vs umbrales (5 filas)
      - Hoja 3: análisis de rendimiento de componentes de IA (5 filas)
    """

    if num == "4.1":
        # --- Hoja 1: métricas de rendimiento por periodo ---
        metricas_rows = ""
        for i in range(1, 11):
            metricas_rows += (
                f'<tr>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Fecha/periodo
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Disponibilidad %
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Latencia prom (ms)
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Tasa de error %
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # CPU %
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # RAM %
                f'<td class="fill">&nbsp;</td>\n'                              # Herramienta medición
                f'<td class="fill">&nbsp;</td>\n'                              # Notas/incidencias
                f'</tr>\n'
            )

        # --- Hoja 2: comparativo indicadores vs umbrales ---
        comparativo_rows = ""
        indicadores = [
            "Disponibilidad (%)",
            "Latencia promedio (ms)",
            "Tasa de error (%)",
            "CPU promedio (%)",
            "RAM promedio (%)",
        ]
        for ind in indicadores:
            comparativo_rows += (
                f'<tr>\n'
                f'<td style="font-weight:bold;">{ind}</td>\n'
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Umbral propuesta
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Resultado real
                f'<td class="fill" style="text-align:center;color:#999;">=%</td>\n'  # Variación %
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Cumplido S/N
                f'</tr>\n'
            )

        # --- Hoja 3: rendimiento de componentes de IA ---
        ia_rows = ""
        for i in range(1, 6):
            ia_rows += (
                f'<tr>\n'
                f'<td class="fill">&nbsp;</td>\n'                              # Componente de IA
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # % respuestas correctas
                f'<td class="fill">&nbsp;</td>\n'                              # Ejemplo bueno
                f'<td class="fill">&nbsp;</td>\n'                              # Ejemplo con error
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Tiempo prom (ms)
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Costo por consulta (USD)
                f'<td class="fill" style="text-align:center;">&nbsp;</td>\n'  # Costo total periodo
                f'</tr>\n'
            )

        return f"""
<h2>Hoja 1 · Métricas de rendimiento por periodo</h2>
<p style="font-size: 10pt; color: #666;">
  Registra una fila por periodo de medición (día, semana o mes, según la frecuencia acordada).
  Disponibilidad % = tiempo operativo / tiempo total x 100. Tasa de error % = solicitudes fallidas / solicitudes totales x 100.
</p>
<table class="matrix">
<tr>
  <th style="width: 10%;">Fecha/Periodo</th>
  <th style="width: 12%;">Disponibilidad (%)</th>
  <th style="width: 12%;">Latencia prom. (ms)</th>
  <th style="width: 10%;">Tasa error (%)</th>
  <th style="width: 8%;">CPU (%)</th>
  <th style="width: 8%;">RAM (%)</th>
  <th style="width: 16%;">Herramienta de medición</th>
  <th>Notas / Incidencias</th>
</tr>
{metricas_rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:6pt;font-style:italic;">
  Herramientas recomendadas: UptimeRobot, Datadog, Grafana, New Relic, o los logs nativos del servidor.
</p>

<h2>Hoja 2 · Comparativo indicadores técnicos vs umbrales de la propuesta</h2>
<p style="font-size: 10pt; color: #666;">
  Compara el resultado real del periodo contra el umbral que definiste en la propuesta de transformación digital autorizada.
  Variación % = (Resultado real - Umbral) / Umbral × 100. Positivo = mejor que el umbral; negativo = por debajo.
</p>
<table class="matrix">
<tr>
  <th style="width: 28%;">Indicador técnico</th>
  <th style="width: 18%;">Umbral de la propuesta</th>
  <th style="width: 18%;">Resultado real del periodo</th>
  <th style="width: 12%;">Variación %</th>
  <th style="width: 12%;">Cumplido (S/N)</th>
</tr>
{comparativo_rows}
</table>

<h2>Hoja 3 · Rendimiento de componentes de IA</h2>
<p style="font-size: 10pt; color: #666;">
  Por cada componente de IA que integra la solución. El % de respuestas correctas se calcula
  revisando una muestra de respuestas reales (mínimo 50 casos para ser estadísticamente representativo).
  El costo por consulta se obtiene del dashboard del proveedor de IA.
</p>
<table class="matrix">
<tr>
  <th style="width: 18%;">Componente de IA</th>
  <th style="width: 13%;">% respuestas correctas</th>
  <th style="width: 18%;">Ejemplo de respuesta correcta</th>
  <th style="width: 18%;">Ejemplo de respuesta incorrecta</th>
  <th style="width: 10%;">Tiempo prom. (ms)</th>
  <th style="width: 10%;">Costo/consulta (USD)</th>
  <th style="width: 10%;">Costo total periodo</th>
</tr>
{ia_rows}
</table>
<p style="font-size:9pt;color:#999;margin-top:6pt;font-style:italic;">
  Los ejemplos representativos (correcto e incorrecto) son obligatorios según el F21. Selecciona casos reales de producción.
</p>
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


def generate_all():
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

    count = 0
    for p in PRODUCTS:
        content, ext = render_product(p)
        filename = f"{p['slug']}.{ext}"
        filepath = OUT / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"  [ok] {filename}  ({p['format'].upper()})")
        count += 1

    return count


if __name__ == "__main__":
    n = generate_all()
    print(f"\nGenerados {n} templates en {OUT}/")
