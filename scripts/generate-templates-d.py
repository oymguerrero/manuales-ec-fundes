#!/usr/bin/env python3
"""
Genera las 16 plantillas de los productos del EC1836 · Creación de soluciones
tecnológicas con Inteligencia Artificial en la modernización digital de la MiPyME (Ruta D).

- 15 Word (.doc) como HTML estilizado con MIME Office
-  1 Excel (.xls) como HTML estilizado con MIME Office

Caso pedagógico: Distribuidora El Surtido, mayorista de abarrotes.
22 empleados, 3 camionetas de reparto, ~200 clientes (tiendas de barrio).
Gerente general: Raúl García (ingeniero). Hoy: pedidos por teléfono y WhatsApp, rutas
definidas a mano e inventario en hojas de cálculo desconectadas. Quiere una
solución que ordene los pedidos, mejore las rutas y prediga la demanda, sin
área de sistemas propia. El caso ilustra el TIPO de contenido; quien se prepara
responde con los datos de su proyecto con una MiPyME, en su lugar de trabajo
o en una situación simulada.

Filosofía pedagógica: NO darle la solución a quien se prepara. Cada plantilla muestra:
  (1) los criterios literales del EC1836 publicado en el DOF (28-oct-2026)
  (2) un ejemplo breve del caso El Surtido (solo ilustrativo)
  (3) preguntas guía que se responden con los datos del proyecto propio

Uso:
    python3 scripts/generate-templates-d.py

Salida: estandar-d/templates/<num_con_guiones>-<slug>.{docx|xlsx}
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "estandar-d" / "templates"
OUT.mkdir(parents=True, exist_ok=True)

PRODUCTS = [
    {
        'num': '1.1',
        'slug': '1-1-diagnostico-oportunidades',
        'format': 'word',
        'elemento': '1 · E5829',
        'title': 'El diagnóstico de oportunidades de modernización digital de la MiPyME documentado',
        'intro': 'Es el punto de partida técnico del proyecto: documenta el perfil de la MiPyME, el resumen de la sesión con la persona responsable, las necesidades de modernización digital que expresó, la infraestructura tecnológica con la que cuenta y lo que ya intentó antes.',
        'f21': [
            'Contiene el perfil de la MiPyME, especificando su tamaño, giro, colaboradores, ubicación, nombre y correo electrónico de la persona de contacto',
            'Incluye el resumen de la sesión sostenida con el responsable de la MiPyME, especificando día, hora, lugar, asistentes y acuerdos tomados en la reunión',
            'Tiene las necesidades de modernización digital detectadas correspondientes con lo expresado por los representantes de la MiPyME',
            'Proporciona el análisis de infraestructura tecnológica existente especificando el hardware, software y conectividad con la que cuenta la MiPyME',
            'Refiere las experiencias en implementación de soluciones de modernización digital con las que cuenta la MiPyME',
        ],
        'caso': 'Distribuidora El Surtido: mayorista de abarrotes, 22 empleados, 3 camionetas y unas 200 tiendas de barrio como clientes, en la región. Empresa pequeña (22 personas). Contacto: Raúl García, gerente general, raul@elsurtido.example. Sesión de levantamiento: martes 4 de marzo, 10:00 h, en la oficina de El Surtido. Asistentes: Raúl García, Luisa Morales (capturista), Carlos Ibarra (chofer líder y coordinador de rutas) y Ana Liz, consultora de Consultoría Digital MX. Acuerdo: entregar la propuesta en unas 2 semanas. Necesidades que expresó Raúl: ordenar los pedidos que llegan por teléfono y WhatsApp, definir mejor las rutas de reparto (hoy las decide cada chofer y hay un mapa dibujado a mano) y saber con tiempo qué producto va a hacer falta. Infraestructura: 3 computadoras con Windows 10, 1 servidor local básico, internet de 50 Mbps, 3 smartphones Android con datos, sin ERP y sin área de sistemas. Experiencias previas: un Excel compartido en 2023, abandonado por conflictos de versiones; ninguna experiencia con IA.',
        'preguntas': [
            ('Perfil de la MiPyME', 'Escribe el nombre de la empresa, su tamaño (micro, pequeña o mediana, y en qué criterio te basas), el giro, el número de colaboradores, la ubicación y los datos de la persona de contacto: nombre, cargo y correo electrónico.'),
            ('Resumen de la sesión con el responsable', '¿Qué día, a qué hora y dónde fue la sesión? ¿Quiénes asistieron y con qué cargo? ¿Qué acuerdos se tomaron?'),
            ('Necesidades de modernización digital detectadas', '¿Qué procesos quiere mejorar o digitalizar la MiPyME? Anótalos con las palabras de quienes los expresaron y deja aparte tu interpretación.'),
            ('Infraestructura tecnológica existente', '¿Con qué hardware cuenta (computadoras, servidores, celulares)? ¿Qué software usa hoy? ¿Qué conectividad tiene y de qué velocidad?'),
            ('Experiencias previas con soluciones de modernización digital', '¿Ha intentado antes implementar alguna solución digital? ¿Qué pasó y qué dejó esa experiencia, tanto en resultados como en resistencias o aprendizajes?'),
        ],
    },
    {
        'num': '1.2',
        'slug': '1-2-diagnostico-madurez-digital',
        'format': 'word',
        'elemento': '1 · E5829',
        'title': 'El diagnóstico de madurez digital y disposición al cambio de la MiPyME elaborado',
        'intro': 'Dice en qué punto está la MiPyME en su camino de digitalización: cómo opera hoy, qué tan ordenados están sus datos, cómo recibe el cambio su equipo, qué distancia hay entre lo que tiene y lo que quiere lograr, y qué información sobre modernización digital existe ya en la empresa. El EC1836 no fija una escala de madurez: usa la que elijas y explícala en el documento.',
        'f21': [
            'Contiene el estado digital/tecnológico actual de la MiPyME',
            'Establece el estado de los activos de información y su grado de estructuración',
            'Tiene el estatus de disposición al cambio de la MiPyME',
            'Indica las brechas digitales/tecnológicas existentes entre el estado actual de la MiPyME y la expectativa de modernización digital',
            'Incluye la información disponible de la MiPyME con relación al tema de modernización digital',
            'Menciona la fecha del diagnóstico, el nombre de la MiPyME, a quién va dirigido y el nombre de la empresa consultora/consultor que lo realizó',
        ],
        'caso': 'Estado digital de El Surtido: madurez baja. Usan herramientas digitales básicas (WhatsApp, hojas de cálculo) sin integración entre ellas. Activos de información: lista de unos 200 clientes en Excel sin depurar desde 2022; 3 años de pedidos en una hoja de cálculo; inventario en tres hojas que nadie sincroniza. Datos personales de los clientes: nombre, teléfono y dirección de entrega. Disposición al cambio: alta en Raúl, que impulsa el proyecto; media en capturistas, por el temor a perder su trabajo; con resistencias entre los choferes, que cambiarían una rutina de años. Brechas: captura digital de pedidos, rutas de reparto con apoyo de datos y predicción de demanda. Información disponible: Raúl no tiene documentos ni política interna sobre digitalización. Fecha del diagnóstico: 10 de marzo. Dirigido a: Raúl García, Distribuidora El Surtido. Elaborado por: Ana Liz, de Consultoría Digital MX.',
        'preguntas': [
            ('Estado digital/tecnológico actual', '¿Cómo opera hoy la MiPyME? Indica qué procesos son manuales, cuáles tienen apoyo digital parcial y cuáles ya están digitalizados, y explica con qué criterio calificas su nivel de madurez.'),
            ('Activos de información y su grado de estructuración', '¿Qué datos tiene (clientes, pedidos, inventario, ventas)? ¿En qué formato están: papel, hojas de cálculo, sistema, mensajes? ¿Qué tan fácil es consultarlos y qué tanto puede confiar la empresa en ellos?'),
            ('Disposición al cambio', '¿Cómo reacciona el equipo ante la digitalización? ¿Quiénes la impulsan y quiénes tienen dudas o resistencias? ¿Qué razones dan?'),
            ('Brechas digitales/tecnológicas', '¿Qué distancia hay entre el estado actual y lo que la MiPyME espera lograr? Enlista las brechas y ordénalas por su efecto en el negocio.'),
            ('Información disponible sobre modernización digital', '¿Existe algún documento, plan, política, capacitación o asesoría previa de la MiPyME sobre este tema? Si no hay nada, dilo.'),
            ('Identificación del diagnóstico', 'Fecha del diagnóstico, nombre de la MiPyME, persona a quien va dirigido (nombre y cargo) y nombre de la empresa consultora o del consultor que lo elaboró.'),
        ],
    },
    {
        'num': '1.3',
        'slug': '1-3-propuesta-modernizacion-digital',
        'format': 'word',
        'elemento': '1 · E5829',
        'title': 'El documento de propuesta de modernización digital para la MiPyME elaborado',
        'intro': 'Es la propuesta técnica del proyecto: convierte los diagnósticos en una solución concreta. Reúne las propuestas priorizadas, los requerimientos funcionales y no funcionales, las tecnologías y los servicios de IA con su justificación, el diagrama de arquitectura, el modelo de datos, la ciberseguridad y el presupuesto con su calendario. En esta plantilla el diagrama es un espacio reservado: inserta el tuyo.',
        'f21': [
            'Contiene las propuestas de modernización digital correspondientes con las necesidades detectadas en la MiPyME, por orden de prioridad de atención',
            'Tiene los requerimientos funcionales y no funcionales para la implementación de la modernización digital de acuerdo con los diagnósticos realizados',
            'Muestra información sobre las tecnologías, APIs y servicios de IA seleccionados con su justificación técnica',
            'Incluye el diagrama de arquitectura del sistema propuesto con sus componentes',
            'Refiere el modelo de datos y flujo de información entre componentes de la propuesta de solución tecnológica',
            'Cumple con los aspectos de ciberseguridad, manejo de información confidencial y normativas aplicables',
            'Establece el presupuesto y calendarización para la implementación de la propuesta',
        ],
        'caso': 'Propuestas priorizadas de El Surtido: 1) captura de pedidos con un bot de WhatsApp y un formulario web, 2) rutas de reparto con apoyo de Google Routes API, 3) predicción de demanda con Prophet. Requerimientos funcionales: captar pedidos desde el celular, ver las rutas del día en un tablero y obtener un pronóstico semanal de inventario. Requerimientos no funcionales: disponibilidad de 99.5 % en horario de pedidos, respuesta en menos de 3 segundos y funcionamiento parcial sin conexión. Tecnologías: Python con FastAPI (backend), React (interfaz), PostgreSQL (base de datos), un servicio de IA generativa por API para interpretar pedidos escritos en lenguaje natural, Google Routes API para las rutas y Prophet para el pronóstico, todo en un VPS en la nube. Se justificó cada una frente a otras opciones por costo, conocimiento del equipo y mantenimiento. [Aquí va el diagrama de arquitectura: bot de WhatsApp y formulario web, API en FastAPI, PostgreSQL, servicio de IA, Google Routes API, Prophet y tablero en React.] Ciberseguridad: HTTPS, inicio de sesión con roles, cifrado de datos sensibles y cumplimiento de la LFPDPPP (el sistema trata nombre, teléfono y dirección de entrega). Presupuesto total: $85,000 MXN. Calendario: 12 semanas.',
        'preguntas': [
            ('Propuestas de modernización digital por orden de prioridad', '¿Qué soluciones propones, en qué orden y por qué? Liga cada propuesta con una necesidad detectada en tus diagnósticos.'),
            ('Requerimientos funcionales', '¿Qué tiene que hacer el sistema? Enlista las funciones concretas que responden a los diagnósticos.'),
            ('Requerimientos no funcionales', '¿Qué cualidades debe tener? Piensa en disponibilidad, tiempo de respuesta, uso desde el celular, funcionamiento sin conexión, rendimiento con carga y facilidad de uso. Fija un umbral medible para cada una: lo usarás en el reporte de rendimiento del Elemento 4.'),
            ('Tecnologías, APIs y servicios de IA con su justificación técnica', '¿Qué lenguajes, bibliotecas, bases de datos, APIs y servicios de IA elegiste? De cada uno, explica por qué y frente a qué alternativas lo elegiste.'),
            ('Diagrama de arquitectura con sus componentes', 'Inserta el diagrama. Debe mostrar cada componente (interfaz, backend, base de datos, servicios de IA y servicios externos) y cómo se conectan.'),
            ('Modelo de datos y flujo de información', '¿Qué entidades maneja el sistema (clientes, pedidos, productos, rutas, usuarios)? ¿Cómo se relacionan? ¿Por dónde circula la información entre componentes y dónde se guarda cada dato?'),
            ('Ciberseguridad, información confidencial y normativas aplicables', '¿Qué datos personales o confidenciales tratará el sistema? ¿Cómo los protegerás (autenticación, cifrado, accesos)? ¿Qué normas aplican, como la LFPDPPP, y cómo las cumples?'),
            ('Presupuesto y calendarización', '¿Cuánto cuesta la implementación? Desglósalo por componente o etapa. ¿En cuánto tiempo se hará y cuáles son los hitos del calendario?'),
        ],
    },
    {
        'num': '1.4',
        'slug': '1-4-propuesta-autorizada',
        'format': 'word',
        'elemento': '1 · E5829',
        'title': 'La propuesta de modernización digital para la MiPyME autorizada',
        'intro': 'Es la versión de la propuesta que queda después de revisarla con la persona responsable de la MiPyME. Documenta los cambios respecto al documento original que presentaste y lleva el visto bueno (VoBo) de esa persona.',
        'f21': [
            'Contiene las modificaciones al documento original presentado',
            'Incluye el VoBo de la persona responsable por parte de la MiPyME',
        ],
        'caso': 'El Surtido: cambios acordados con Raúl en la reunión del 18 de marzo. 1) La predicción de demanda se mantiene, pero pasa a ser la tercera prioridad, después de la captura de pedidos y de las rutas, porque Raúl necesita primero ordenar la captura. 2) El presupuesto se desglosa por prioridad para que Raúl pueda seguir cada avance. 3) El calendario se confirma en 12 semanas, con la predicción en las últimas. VoBo: [firma] Raúl García, gerente general de Distribuidora El Surtido. Fecha: 20 de marzo.',
        'preguntas': [
            ('Modificaciones al documento original', '¿Qué cambios se hicieron a la propuesta después de presentarla a la persona responsable de la MiPyME? Anota qué se ajustó, qué se quitó y qué se agregó, con la razón de cada cambio.'),
            ('VoBo de la persona responsable de la MiPyME', 'Deja el espacio para el visto bueno: nombre completo, cargo, fecha y firma de la persona responsable de la MiPyME. Consíguelo con el documento ya revisado, para que el VoBo avale la versión que quedó.'),
        ],
    },
    {
        'num': '2.1',
        'slug': '2-1-entorno-desarrollo-configurado',
        'format': 'word',
        'elemento': '2 · E5830',
        'title': 'El entorno de desarrollo de la solución tecnológica de modernización digital configurado',
        'intro': 'Documenta el repositorio y el entorno donde se construye la solución: la estructura de carpetas, el archivo de dependencias con versiones, las instrucciones del README, la evidencia de que las variables de entorno y las credenciales están separadas del código, el stack elegido y el historial de cambios.',
        'f21': [
            'Contiene el repositorio de la solución tecnológica de modernización digital con la estructura de carpetas organizada según el stack tecnológico seleccionado',
            'Incluye el archivo de dependencias con las versiones especificadas de cada librería y framework utilizado',
            'Tiene las instrucciones de instalación, configuración y ejecución del proyecto en el archivo README',
            'Contiene la evidencia de la configuración de variables de entorno y credenciales de APIs de IA de forma segura, separadas de la solución tecnológica de modernización digital, manteniendo la confidencialidad y seguridad de la información',
            'Refiere el stack tecnológico seleccionado correspondiente con la arquitectura definida en la propuesta autorizada',
            'Describe el historial de cambios documentado',
        ],
        'caso': 'El Surtido: repositorio privado de la consultora. Estructura: /backend (FastAPI), /frontend (React), /ml (pronóstico con Prophet), /docs, /tests y /scripts. Dependencias con versión fija, por ejemplo fastapi==0.110.0 en el backend y react 18.2.0 en el frontend. README: clonar el repositorio, copiar .env.example a .env, instalar con pip install -r requirements.txt y arrancar con uvicorn main:app --reload. Credenciales: en el archivo .env, que está en .gitignore; sus nombres son DATABASE_URL, JWT_SECRET_KEY, GOOGLE_ROUTES_API_KEY y la clave del servicio de IA; en el repositorio solo viaja .env.example, sin valores. El stack coincide con la propuesta autorizada: Python con FastAPI, PostgreSQL y React. Historial: v0.1 (entorno base), v0.2 (modelos de la base de datos), v0.3 (endpoints de pedidos), con mensajes de commit descriptivos.',
        'preguntas': [
            ('Repositorio y estructura de carpetas', '¿Dónde está el repositorio? ¿Cómo se organizan las carpetas según el stack que elegiste y para qué sirve cada una?'),
            ('Archivo de dependencias con versiones', '¿Qué bibliotecas y frameworks usa la solución? Enlístalos con su versión exacta (requirements.txt, package.json u otro). ¿Qué problema evitas al fijar las versiones?'),
            ('Instrucciones en el README', '¿Qué pasos debe seguir otra persona para instalar, configurar y ejecutar el proyecto? Pruébalas en una máquina limpia o pídele a alguien que las siga sin tu ayuda.'),
            ('Variables de entorno y credenciales de APIs de IA', '¿Qué credenciales y configuraciones sensibles tiene el proyecto? ¿Dónde viven y cómo quedan separadas del código? ¿Qué evidencia tienes de ello (por ejemplo, el .gitignore y el archivo de ejemplo sin valores)?'),
            ('Stack tecnológico frente a la propuesta autorizada', '¿El stack configurado corresponde con la arquitectura de la propuesta autorizada? Si hubo cambios, ¿cuáles y por qué?'),
            ('Historial de cambios documentado', '¿Cómo documentas los cambios (commits descriptivos, CHANGELOG, etiquetas de versión)? Resume los hitos del historial.'),
        ],
    },
    {
        'num': '2.2',
        'slug': '2-2-checklist-verificacion-solucion',
        'format': 'word',
        'elemento': '2 · E5830',
        'title': 'La solución tecnológica de modernización digital con IA desarrollada',
        'intro': 'Este producto es la solución misma: el backend, la integración con IA, la interfaz y la base de datos funcionando. No es un documento que se llena, así que aquí tienes una lista de verificación. Úsala para comprobar, criterio por criterio, qué parte de tu solución lo cumple, qué evidencia tienes y dónde la puedes mostrar.',
        'f21': [
            'Contiene el backend operativo con la lógica de negocio implementada según los requerimientos funcionales de la propuesta autorizada',
            'Incluye la integración con los modelos/servicios de IA seleccionados, funcionando con manejo de errores y respuestas de respaldo',
            'Tiene la interfaz de usuario de manera funcional, responsiva, accesible y conectada al backend',
            'Indica el esquema de base de datos implementado con procedimientos de respaldo automatizado configurados',
            'Establece las medidas de seguridad aplicadas sobre validación y sanitización de datos de entrada, autenticación de usuarios, cifrado de datos sensibles y control de acceso basado en roles',
            'Refiere la manera en que se protegen los datos personales en el desarrollo de la solución tecnológica',
            'Incluye su documentación, nomenclatura consistente y la separación de responsabilidades específicas de las funciones de cada componente del sistema',
        ],
        'caso': 'El Surtido: backend en FastAPI con endpoints /pedidos, /rutas e /inventario; el servicio de IA generativa interpreta pedidos escritos en lenguaje natural y, si no responde, el sistema pasa a captura manual. Interfaz en React, pensada para el celular de los repartidores y con contraste suficiente para leerse al sol. Base de datos PostgreSQL con tablas de pedidos, clientes, productos y rutas, y respaldo diario automatizado. Seguridad: validación de entradas, inicio de sesión con vencimiento a las 8 horas, contraseñas cifradas y roles de administrador, operador y repartidor. Datos personales: nombre, teléfono y dirección de entrega, porque el ruteo la necesita; el aviso de privacidad aparece en el primer uso. Código documentado, con nombres consistentes y separación entre rutas, servicios y modelos.',
        'preguntas': [
            ('Backend: lógica de negocio según los requerimientos funcionales', 'Enlista los endpoints o funciones principales. ¿Cada requerimiento funcional de la propuesta autorizada está implementado? Marca cada uno: implementado, parcial o pendiente, y dónde puedes mostrarlo.'),
            ('Integración con modelos o servicios de IA', '¿Qué servicio de IA integraste y para qué función? ¿Qué pasa cuando falla o no responde? ¿Qué respuesta de respaldo entrega?'),
            ('Interfaz de usuario funcional, responsiva y accesible', '¿Se ve y funciona bien en celular y en computadora? ¿Está conectada al backend? ¿Qué revisión de accesibilidad hiciste?'),
            ('Esquema de base de datos y respaldo automatizado', 'Describe las tablas principales y sus relaciones. ¿El respaldo automatizado está configurado? ¿Cada cuánto corre y dónde se guarda?'),
            ('Medidas de seguridad', 'Marca las que aplicaste y describe cómo: [ ] validación y sanitización de datos de entrada, [ ] autenticación de usuarios, [ ] cifrado de datos sensibles, [ ] control de acceso basado en roles.'),
            ('Protección de los datos personales en el desarrollo', '¿Qué datos personales trata la solución y cómo los proteges mientras la desarrollas? ¿Existe aviso de privacidad? ¿La MiPyME sabe qué datos se guardan?'),
            ('Documentación, nomenclatura y separación de responsabilidades', '¿El código está documentado? ¿Los nombres son consistentes? ¿Cada componente tiene responsabilidades separadas o todo vive en un solo archivo?'),
        ],
    },
    {
        'num': '2.3',
        'slug': '2-3-reporte-pruebas-tecnicas',
        'format': 'word',
        'elemento': '2 · E5830',
        'title': 'El reporte de pruebas técnicas de la solución tecnológica de modernización digital elaborado',
        'intro': 'Documenta cómo comprobaste que la solución funciona: los casos de prueba, los resultados de las pruebas unitarias, de integración y funcionales, las vulnerabilidades encontradas, la verificación de la IA, el plan de contingencia y los datos del reporte.',
        'f21': [
            'Contiene los casos de prueba definidos para cada componente de la solución tecnológica con datos de entrada y resultados esperados',
            'Incluye los resultados de las pruebas unitarias, las de integración y las funcionales ejecutadas',
            'Apunta las vulnerabilidades de seguridad identificadas, así como el estatus de corrección de las que son solucionables',
            'Tiene la información sobre la verificación realizada del correcto funcionamiento de las integraciones con los modelos/servicios de IA',
            'Describe el plan de contingencia ante la interrupción/saturación del servicio de la solución tecnológica',
            'Refiere la validación realizada sobre la calidad y relevancia de las respuestas generadas por los componentes de IA',
            'Señala la fecha de las pruebas realizadas, el nombre del responsable de aplicarlas y la versión de la solución tecnológica de modernización digital evaluada',
        ],
        'caso': 'El Surtido: versión v0.8.2, pruebas del 12 de mayo, responsable: Ana Liz, de Consultoría Digital MX. Caso TC-01, captura de un pedido por el bot de WhatsApp: entrada «quiero 5 cajas de atún»; resultado esperado: pedido registrado con producto, cantidad, cliente y hora. Pruebas unitarias: 47, con 45 aprobadas y 2 fallos ya corregidos. Integración: el servicio de IA respondió bien en 98 % de 50 llamadas. Vulnerabilidades: una posible inyección SQL en /buscar-cliente (corregida validando la entrada) y un token de sesión sin vencimiento (corregido a 8 horas). Contingencia: si el servicio de IA no responde, el sistema pasa a captura manual; si la base de datos falla, los pedidos se guardan localmente y se sincronizan al restaurarla. Calidad de la IA: 94 % de 100 pedidos escritos de formas distintas se interpretaron correctamente.',
        'preguntas': [
            ('Casos de prueba por componente', 'Por cada componente de tu solución, documenta al menos un caso con su nombre, los datos de entrada y el resultado esperado.'),
            ('Resultados de pruebas unitarias, de integración y funcionales', '¿Cuántas pruebas de cada tipo ejecutaste? ¿Cuántas pasaron y cuántas fallaron? ¿Qué hiciste con las que fallaron?'),
            ('Vulnerabilidades de seguridad y su estatus', '¿Qué revisión de seguridad hiciste? De cada vulnerabilidad: descripción, nivel de riesgo y estatus (corregida, en proceso, o sin corrección posible con su justificación).'),
            ('Verificación de las integraciones con modelos o servicios de IA', '¿Cómo comprobaste que cada integración funciona? ¿Cuántas pruebas hiciste y qué resultado tuvieron?'),
            ('Plan de contingencia', '¿Qué pasa si el servicio se interrumpe o se satura? Describe qué hace el sistema y qué hace el equipo en cada escenario de falla.'),
            ('Validación de la calidad y relevancia de las respuestas de IA', '¿Con qué casos y con qué criterio decidiste que una respuesta es buena? ¿Qué porcentaje lo fue y qué errores encontraste?'),
            ('Fecha, responsable y versión evaluada', 'Fecha de las pruebas, nombre de quien las aplicó y versión exacta de la solución que se evaluó.'),
        ],
    },
    {
        'num': '2.4',
        'slug': '2-4-documentacion-tecnica',
        'format': 'word',
        'elemento': '2 · E5830',
        'title': 'La documentación técnica de la solución tecnológica de modernización digital elaborada',
        'intro': 'Es el manual técnico de la solución: la arquitectura tal como quedó, los endpoints de la API, el mantenimiento, las decisiones técnicas, la configuración de la IA y las dependencias externas. Con él, otra persona puede entender, mantener y hacer crecer la solución.',
        'f21': [
            'Contiene la descripción de la arquitectura implementada con diagrama actualizado de componentes y flujos de datos',
            'Incluye la referencia de los endpoints de la API con sus parámetros, respuestas esperadas y códigos de error',
            'Tiene las instrucciones para mantenimiento, actualización y modificación futura',
            'Incluye las decisiones técnicas tomadas durante el desarrollo con su justificación',
            'Refiere la configuración de los componentes de IA, los modelos utilizados, los prompts implementados con sus parámetros y criterios de selección',
            'Considera las dependencias externas con sus versiones, licencias y procedimiento de actualización',
        ],
        'caso': 'El Surtido: arquitectura implementada [aquí va el diagrama actualizado]. Cambio frente a la propuesta: se agregó una caché para las respuestas repetidas del servicio de IA. Endpoint ejemplo: POST /api/pedidos; entrada {cliente_id, productos[], notas}; respuesta {pedido_id, status, eta_entrega}; errores: 400 por validación y 503 si el servicio de IA no está disponible. Mantenimiento: actualizar dependencias con pip install -U -r requirements.txt en un entorno de pruebas y correr las pruebas antes de pasar a producción. Decisión técnica: un modelo de lenguaje por API, en lugar de uno propio, por costo y desempeño para unos 150 pedidos al día. Configuración de IA: prompt de clasificación de pedidos versión 2.3, temperatura 0.2 y máximo de 500 tokens. Dependencias: cada una con su versión y su licencia, y revisión mensual de sus cambios.',
        'preguntas': [
            ('Arquitectura implementada con diagrama actualizado', 'Describe la arquitectura como quedó y adjunta el diagrama de componentes y flujos de datos. ¿Qué cambió frente a la propuesta y por qué?'),
            ('Referencia de los endpoints de la API', 'Por cada endpoint: método, ruta, descripción, parámetros, respuesta esperada y códigos de error con su significado.'),
            ('Mantenimiento, actualización y modificación futura', '¿Cómo se actualiza el sistema, cómo se reinicia si falla y cómo se cambia el esquema de la base de datos? ¿Quién puede hacer cada cambio y con qué herramientas?'),
            ('Decisiones técnicas y su justificación', '¿Qué decisiones importantes tomaste (lenguaje, bibliotecas, proveedor de IA, base de datos, arquitectura)? Por cada una: qué alternativas viste y por qué elegiste esa.'),
            ('Configuración de los componentes de IA', '¿Qué modelos usas, con qué parámetros y con qué prompts? ¿Con qué criterios los seleccionaste?'),
            ('Dependencias externas con versiones, licencias y actualización', 'Enlista bibliotecas, servicios y APIs externas. De cada una: versión, licencia y cómo se actualiza sin romper el sistema.'),
        ],
    },
    {
        'num': '3.1',
        'slug': '3-1-checklist-despliegue-produccion',
        'format': 'word',
        'elemento': '3 · E5831',
        'title': 'La solución tecnológica de modernización digital desplegada en el entorno productivo de la MiPyME',
        'intro': 'Este producto es la solución instalada y funcionando en el entorno productivo de la MiPyME, no un documento. Por eso aquí tienes una lista de verificación: úsala para comprobar, criterio por criterio, qué parte del despliegue está lista y qué evidencia tienes para mostrarla.',
        'f21': [
            'Contiene la solución tecnológica instalada y operativa en la infraestructura de la MiPyME conforme a la arquitectura autorizada',
            'Incluye los modelos/servicios de IA conectados y respondiendo en el entorno productivo de la MiPyME',
            'Tiene la base de datos final de producción con los respaldos automatizados configurados',
            'Refiere el procedimiento para monitorear el consumo de tokens/créditos de las APIS de IA',
            'Describe las medidas de seguridad implementadas en el entorno productivo conforme a la propuesta de modernización digital autorizada',
        ],
        'caso': 'El Surtido: un VPS en la nube de 2 vCPU y 4 GB de RAM con Linux, en https://app.elsurtido.example con certificado de seguridad activo. Servicio de IA conectado en producción: se confirmó con una llamada de prueba el 2 de junio. Base de datos PostgreSQL 16 de producción, con respaldo diario a las 02:00 h guardado fuera del servidor, con retención de 30 días. Monitoreo: el panel del proveedor de IA muestra el consumo de tokens y envía un aviso por correo al llegar a 80 % del límite mensual. Seguridad: firewall que deja abiertos solo los puertos 80, 443 y 22, bloqueo automático tras intentos fallidos de acceso y actualizaciones de seguridad automáticas. La arquitectura desplegada es la que Raúl autorizó.',
        'preguntas': [
            ('Solución instalada y operativa en la infraestructura de la MiPyME', '¿Dónde está instalada (servidor propio, VPS, nube)? ¿La dirección de producción responde? ¿La arquitectura desplegada coincide con la autorizada?'),
            ('Modelos o servicios de IA conectados y respondiendo en producción', '¿Los servicios de IA están configurados en el entorno productivo y no solo en el de desarrollo? ¿Qué llamada de prueba hiciste y qué respondió?'),
            ('Base de datos de producción y respaldos automatizados', '¿La base de datos de producción está lista y con los datos que corresponden? ¿Cada cuánto corre el respaldo, dónde se guarda y lo has probado restaurando?'),
            ('Procedimiento para monitorear el consumo de tokens o créditos de las APIs de IA', '¿Cómo vigilas el consumo? ¿Hay alertas o límites configurados? ¿Qué haces cuando el consumo se acerca al límite?'),
            ('Medidas de seguridad del entorno productivo', '¿Qué medidas están activas (HTTPS, firewall, autenticación, cifrado, actualizaciones)? ¿Coinciden con las de la propuesta autorizada?'),
        ],
    },
    {
        'num': '3.2',
        'slug': '3-2-documentacion-tecnica-implementacion',
        'format': 'word',
        'elemento': '3 · E5831',
        'title': 'La documentación técnica de implementación elaborada',
        'intro': 'Es el registro técnico del despliegue: el diagrama de la infraestructura de producción, los roles con sus permisos y el registro de accesos, la configuración del dominio y del certificado, los pasos ejecutados con sus resultados y el procedimiento de respaldo y restauración.',
        'f21': [
            'Contiene el diagrama de infraestructura del entorno de producción con sus componentes y conexiones',
            'Incluye la asignación de roles con permisos y registro de credenciales y accesos a la solución tecnológica, manteniendo la confidencialidad y seguridad de la información',
            'Tiene la configuración del dominio, certificado de seguridad y redirecciones aplicadas, manteniendo la confidencialidad y seguridad de la información',
            'Enlista los pasos ejecutados durante el despliegue con los resultados obtenidos y sus evidencias',
            'Señala el procedimiento de respaldo y restauración de la base de datos a realizar en caso necesario',
        ],
        'caso': 'El Surtido: infraestructura de producción [aquí va el diagrama]: un VPS con la aplicación, la base de datos PostgreSQL, almacenamiento externo para los respaldos y un punto de entrada con certificado. Roles: Raúl García, administrador con acceso total; Luisa Morales, operador de pedidos e inventario, sin acceso a configuración; Carlos Ibarra, coordinador de rutas, que asigna pedidos; y los repartidores (Mario, Miguel Ángel Cruz y Sandra Reyes), que solo ven sus rutas en el celular. Las contraseñas no se anotan aquí: viven en el gestor de contraseñas de la empresa. Dominio: app.elsurtido.example apunta al VPS; el certificado se renueva solo y HTTP redirige a HTTPS. Pasos: 1) actualizar el sistema (OK), 2) instalar Python 3.11 (OK), 3) clonar el repositorio (OK), 4) configurar .env (OK), 5) migrar la base de datos (OK), 6) prueba de humo en app.elsurtido.example/health (OK). Respaldo con pg_dump comprimido y restauración con psql sobre la base de producción.',
        'preguntas': [
            ('Diagrama de infraestructura del entorno de producción', 'Adjunta el diagrama con servidores, base de datos, servicios externos y sus conexiones. Debe mostrar lo que quedó instalado.'),
            ('Roles con permisos y registro de credenciales y accesos', '¿Qué roles existen y qué puede y no puede hacer cada uno? ¿Quién tiene acceso a qué? No escribas contraseñas ni claves: indica dónde se guardan de forma segura.'),
            ('Dominio, certificado de seguridad y redirecciones', '¿Qué dominio configuraste y cómo apunta al servidor? ¿Qué certificado instalaste y cómo se renueva? ¿Qué redirecciones aplicaste? No pongas llaves privadas.'),
            ('Pasos del despliegue con resultados y evidencias', 'Enlista los pasos en orden. De cada uno: qué hiciste, qué resultado obtuviste, qué error apareció y cómo lo resolviste. Adjunta capturas.'),
            ('Respaldo y restauración de la base de datos', '¿Cómo se hace el respaldo y cómo se restaura? Escribe los pasos o comandos. ¿Probaste la restauración y cuánto tardó?'),
        ],
    },
    {
        'num': '3.3',
        'slug': '3-3-reporte-capacitacion',
        'format': 'word',
        'elemento': '3 · E5831',
        'title': 'El reporte de capacitación/transferencia de conocimiento al personal de la MiPyME elaborado',
        'intro': 'Documenta la sesión con la que capacitas al equipo de la MiPyME: los temas, los manuales de usuario y de mantenimiento, los problemas frecuentes que el personal puede resolver solo y los datos de la sesión. El EC1836 incluye un desempeño en el que capacitas al equipo; este reporte es el producto que lo acompaña.',
        'f21': [
            'Contiene los temas cubiertos correspondientes con las funcionalidades de la solución tecnológica de modernización digital implementada',
            'Incluye los manuales de usuario y de mantenimiento de la solución tecnológica de modernización digital con capturas de pantalla y procedimientos paso a paso',
            'Tiene los procedimientos de resolución de problemas frecuentes que el personal de la MiPyME puede ejecutar de manera autónoma',
            'Detalla la información sobre los asistentes, fecha, duración y materiales entregados en la sesión de capacitación',
        ],
        'caso': 'El Surtido: capacitación el 5 de junio, de 10:00 a 13:00 h (3 horas), en la oficina. Asistentes: Raúl García (gerente general), Luisa Morales (capturista) y los repartidores Mario, Miguel Ángel Cruz y Sandra Reyes. Temas: 1) captura de pedidos por WhatsApp (30 min), 2) tablero de rutas (45 min), 3) consulta de inventario y alertas (20 min), 4) cómo reportar un error o pedir soporte (15 min). Materiales: manual de usuario impreso, manual de mantenimiento básico, tarjeta de referencia rápida plastificada y el WhatsApp de soporte de Consultoría Digital MX. Problema frecuente: «el bot no entendió mi pedido». Solución: escribir «PEDIDO: [producto] [cantidad]» y el sistema lo captura directo.',
        'preguntas': [
            ('Temas cubiertos y funcionalidades de la solución', '¿Qué temas trataste y cuánto tiempo dedicaste a cada uno? ¿Cada funcionalidad principal de la solución quedó cubierta?'),
            ('Manual de usuario con capturas de pantalla y pasos', 'Adjunta el manual o describe su contenido: cómo entrar, cómo usar cada funcionalidad, con una captura por paso, y cómo salir.'),
            ('Manual de mantenimiento con capturas de pantalla y pasos', '¿Qué puede hacer el personal para mantener la solución (reiniciar, dar de alta un usuario, exportar un reporte)? Documenta cada procedimiento paso a paso.'),
            ('Resolución de problemas frecuentes', '¿Qué problemas es más probable que encuentre el personal? De cada uno: qué ocurre, causa probable y pasos para resolverlo sin ayuda del consultor.'),
            ('Asistentes, fecha, duración y materiales', '¿Quiénes asistieron (nombre y cargo)? ¿Qué día y a qué hora fue? ¿Cuánto duró? ¿Qué materiales entregaste?'),
        ],
    },
    {
        'num': '3.4',
        'slug': '3-4-acta-final',
        'format': 'word',
        'elemento': '3 · E5831',
        'title': 'El acta final de la solución tecnológica de modernización digital elaborada',
        'intro': 'Formaliza la entrega de la solución a la MiPyME: qué entregaste y en qué estado funciona, el acuse de que la persona responsable recibió las credenciales y la documentación, los compromisos de mantenimiento y las firmas de conformidad. El cierre del proyecto se documenta después, en el reporte final del Elemento 4.',
        'f21': [
            'Contiene la descripción de los entregables transferidos a la MiPyME con su estatus de funcionamiento',
            'Incluye el acuse de entrega de credenciales de acceso y la documentación de la solución tecnológica al responsable de la MiPyME',
            'Tiene los compromisos de mantenimiento y niveles de servicio acordados con la MiPyME incluyendo vigencia, alcance y límites de responsabilidad del desarrollador',
            'Cuenta con la firma de conformidad del responsable de la MiPyME y del consultor',
        ],
        'caso': 'El Surtido: entregables transferidos: 1) solución web en producción en app.elsurtido.example: funcionando; 2) código fuente en el repositorio privado, ya a nombre de la empresa: entregado; 3) manuales de usuario y de mantenimiento: entregados; 4) base de datos de producción con sus datos migrados: funcionando. Acuse de entrega: Raúl García firmó de recibido el acceso de administrador y los accesos al servidor, que se entregaron en sobre sellado y quedaron en el gestor de contraseñas de la empresa; el acuse no lleva las contraseñas. También acusó de recibo la documentación técnica y de usuario. Compromisos: soporte correctivo por 30 días sin costo, con respuesta en 4 horas hábiles, hasta el 5 de julio; cubre errores del sistema entregado y no incluye funciones nuevas. Firmas: Raúl García (Distribuidora El Surtido) y Ana Liz (Consultoría Digital MX), 5 de junio.',
        'preguntas': [
            ('Entregables transferidos y su estatus de funcionamiento', 'Enlista cada componente que entregaste. De cada uno: descripción y estatus al entregarlo (funcionando, con limitaciones conocidas o pendiente de ajuste).'),
            ('Acuse de entrega de credenciales de acceso y documentación', '¿Cómo dejaste constancia de que la persona responsable recibió las credenciales y la documentación? ¿Quién firmó, cuándo y cómo? El acuse prueba la entrega: no escribas contraseñas en él.'),
            ('Compromisos de mantenimiento y niveles de servicio', '¿Qué soporte acordaste? Escribe la vigencia, el alcance (qué cubre y qué no), el tiempo de respuesta y los límites de responsabilidad de quien desarrolló la solución.'),
            ('Firma de conformidad', 'Deja espacio para nombre, cargo y firma de la persona responsable de la MiPyME y del consultor, con la fecha del acta.'),
        ],
    },
    {
        'num': '4.1',
        'slug': '4-1-reporte-rendimiento-tecnico',
        'format': 'excel',
        'elemento': '4 · E5832',
        'title': 'El reporte de rendimiento técnico de la solución tecnológica de modernización digital elaborado',
        'intro': 'Mide cómo se comporta la solución ya en operación: disponibilidad, latencia, tasa de error y consumo de recursos; compara esas cifras con los umbrales de tu propuesta, analiza los componentes de IA e identifica el periodo, las herramientas y a la persona responsable.',
        'f21': [
            'Contiene las métricas de rendimiento de la solución tecnológica de modernización recolectadas: disponibilidad, latencia, tasa de error y consumo de recursos',
            'Incluye la comparación de los indicadores técnicos contra los umbrales definidos en los requerimientos de la propuesta',
            'Tiene el análisis de rendimiento de los componentes de IA: calidad de respuestas, ejemplos representativos, tiempos de procesamiento y costos por consulta',
            'Proporciona información sobre el periodo de medición, las herramientas utilizadas y el nombre del responsable del reporte',
        ],
        'caso': 'El Surtido: periodo del 1 al 30 de junio; responsable: Ana Liz, de Consultoría Digital MX. Herramientas: un servicio de monitoreo de disponibilidad, el registro de la API para latencia y errores, y el panel del proveedor de IA para el consumo. Disponibilidad: 99.7 % (umbral de la propuesta: 99.5 %, cumplido). Latencia promedio: 1.8 s (umbral: menos de 3 s, cumplido). Tasa de error: 0.8 % (umbral: menos de 2 %, cumplido). IA: 96.2 % de los pedidos interpretados correctamente (meta: 90 %), con 1.2 s de procesamiento y $0.003 USD por consulta. Consumo de junio: $12.40 USD, dentro del presupuesto de $20 USD.',
        'preguntas': [
            ('Métricas de rendimiento recolectadas', 'Para el periodo, registra disponibilidad (% de tiempo operativo), latencia promedio, tasa de error y consumo de recursos del servidor (CPU y memoria). ¿Con qué herramienta mediste cada una?'),
            ('Comparación contra los umbrales de la propuesta', 'Por cada indicador: ¿cuál era el umbral de los requerimientos de tu propuesta, cuál fue el resultado y se cumplió?'),
            ('Análisis de rendimiento de los componentes de IA', '¿Qué calidad tuvieron sus respuestas? Incluye un ejemplo representativo bueno y uno con error, el tiempo de procesamiento y el costo por consulta.'),
            ('Periodo, herramientas y responsable', 'Fecha de inicio y de fin de la medición, herramientas que usaste para cada métrica y nombre de quien elabora el reporte.'),
        ],
    },
    {
        'num': '4.2',
        'slug': '4-2-reporte-retroalimentacion',
        'format': 'word',
        'elemento': '4 · E5832',
        'title': 'El reporte de retroalimentación de usuarios de la MiPyME elaborado',
        'intro': 'Recoge lo que opinan los usuarios sobre la solución en operación: los resultados de los instrumentos de satisfacción, las áreas de mejora, las recomendaciones de ajuste y los datos de la consulta. Aplica los instrumentos a los usuarios de la MiPyME, o a quienes desempeñen ese rol si la evaluación es simulada.',
        'f21': [
            'Contiene los resultados de los instrumentos de medición de satisfacción aplicados a los usuarios de la MiPyME',
            'Detalla la información sobre las áreas de mejora identificadas a partir de los resultados del monitoreo, priorizadas según su impacto en la operación de la MiPyME',
            'Indica las recomendaciones de ajuste priorizadas por impacto en la experiencia del usuario y en los objetivos de negocio de la MiPyME',
            'Tiene la cantidad de usuarios participantes en el proceso de retroalimentación, la fecha de aplicación y los instrumentos utilizados',
        ],
        'caso': 'El Surtido: 4 usuarios encuestados: Luisa Morales, Miguel Ángel Cruz, Sandra Reyes y Raúl García. Instrumento: encuesta de satisfacción de 1 a 5 con preguntas abiertas. Satisfacción general: 4.2 de 5; lo mejor valorado fue la captura de pedidos por WhatsApp (4.8). Área de mejora 1, prioridad alta: la confirmación del pedido tarda más de 5 minutos y los clientes pierden confianza. Área de mejora 2, prioridad media: el tablero se ve mal en la pantalla pequeña de los celulares de los repartidores. Recomendaciones: 1) acelerar el envío de confirmaciones (alta: afecta al cliente), 2) ajustar la interfaz a pantallas de menos de 5 pulgadas (media). Fecha de aplicación: 28 de junio.',
        'preguntas': [
            ('Resultados de los instrumentos de satisfacción', '¿Qué instrumentos aplicaste (encuesta, entrevista, observación) y qué resultados obtuviste? Preséntalos ordenados, con puntuaciones, porcentajes o citas.'),
            ('Áreas de mejora priorizadas', '¿Qué aspectos de la solución hay que mejorar según el monitoreo y la consulta? Ordénalos por su efecto en la operación de la MiPyME.'),
            ('Recomendaciones de ajuste priorizadas', 'Por cada área de mejora, ¿qué ajuste recomiendas? Ordénalos por su efecto en la experiencia del usuario y en los objetivos de negocio.'),
            ('Participantes, fecha e instrumentos', '¿Cuántos usuarios participaron y qué rol tiene cada uno? ¿Qué día se aplicó? ¿Qué instrumentos usaste?'),
        ],
    },
    {
        'num': '4.3',
        'slug': '4-3-plan-optimizacion',
        'format': 'word',
        'elemento': '4 · E5832',
        'title': 'El plan de optimización de la solución tecnológica de modernización digital elaborado',
        'intro': 'Cierra el ciclo de mejora: propone acciones con su esfuerzo y beneficio, los ajustes a los componentes de IA, las lecciones aprendidas, las mejoras que van más allá de lo que se pidió y la estrategia para mantener la solución al día.',
        'f21': [
            'Incluye las acciones de optimización propuestas para cada área de mejora con su estimación de esfuerzo y beneficio esperado',
            'Especifica los ajustes a los componentes de IA recomendados, incluyendo calibración de modelos, ajustes de prompts/cambio de proveedores de servicio',
            'Tiene las lecciones aprendidas y recomendaciones para escalamiento futuro de la solución tecnológica de modernización digital',
            'Propone mejoras y optimizaciones pertinentes y adicionales a las solicitadas en el plan de mantenimiento con base en el análisis de los datos de rendimiento realizado y en las tendencias de IA del mercado',
            'Define la estrategia de actualización ante cambios en los modelos de IA, tecnologías utilizadas/normatividad aplicable',
        ],
        'caso': 'El Surtido: plan de optimización v1.0, julio. Acción 1: acelerar el envío de confirmaciones (esfuerzo: 8 h; beneficio: bajar de 5 minutos a menos de 30 s la confirmación, con efecto directo en la confianza de las tiendas). Acción 2: ajustar la interfaz a pantallas de menos de 5 pulgadas (esfuerzo: 4 h; beneficio: mejor experiencia para los repartidores). Ajustes de IA: bajar la temperatura del prompt de clasificación de 0.2 a 0.1 para más consistencia, agregar ejemplos de pedidos con errores de ortografía y, en Prophet, incluir temporadas y días festivos porque el error de pronóstico a 6 semanas fue de 18 % frente al objetivo de 10 %. Lecciones aprendidas: los clientes usan muchas abreviaturas locales que el prompt inicial no contemplaba, y 3 horas de capacitación fueron pocas para los repartidores: conviene hacer 2 sesiones. Mejora adicional: alertas de inventario bajo a partir de los datos de pedidos, para que no salga una camioneta sin lo que van a pedir. Actualización: revisar cada trimestre los cambios del servicio de IA y de Google Routes API, seguir los avisos de versiones de FastAPI y revisar la LFPDPPP si se reforma.',
        'preguntas': [
            ('Acciones de optimización con esfuerzo y beneficio', 'Por cada área de mejora de tu reporte de retroalimentación: ¿qué acción propones, cuánto esfuerzo requiere y qué beneficio esperas?'),
            ('Ajustes a los componentes de IA', '¿Qué ajustes recomiendas: calibrar modelos, cambiar prompts o cambiar de proveedor? Respáldalos con los datos de rendimiento.'),
            ('Lecciones aprendidas y escalamiento futuro', '¿Qué harías distinto en otro proyecto? ¿Qué recomiendas si la MiPyME quisiera escalar la solución a más usuarios, más funciones o más operación?'),
            ('Mejoras adicionales a las solicitadas', 'Además de corregir lo detectado, ¿qué mejoras o optimizaciones propones a partir de los datos de rendimiento y de las tendencias de IA del mercado?'),
            ('Estrategia de actualización', '¿Cómo mantendrás la solución al día cuando cambien los modelos de IA, las tecnologías que usa o la normatividad aplicable?'),
        ],
    },
    {
        'num': '4.4',
        'slug': '4-4-reporte-cierre-proyecto',
        'format': 'word',
        'elemento': '4 · E5832',
        'title': 'El reporte final de cierre del proyecto de modernización digital elaborado',
        'intro': 'Es el reporte con el que el proyecto se cierra: resume lo que se logró, lista lo que quedó en manos de la MiPyME, deja constancia de que recibió las credenciales y la documentación actualizadas, dice qué mantenimiento sigue comprometido y hasta cuándo, y termina con la firma de conformidad de la persona responsable sobre el cierre.',
        'f21': [
            'Contiene el resumen ejecutivo del proyecto, incluyendo objetivos, alcance logrado y resultados obtenidos',
            'Establece la descripción de los entregables transferidos a la MiPyME con su estatus de funcionamiento',
            'Adjunta el acuse de entrega de la actualización de las credenciales de acceso y de la documentación al responsable de la MiPyME',
            'Tiene los compromisos de mantenimiento y niveles de servicio acordados y actualizados con la MiPyME incluyendo vigencia y alcance',
            'Enlista las recomendaciones para la continuidad y evolución de la solución tecnológica implementada en la MiPyME',
            'Incluye la firma de conformidad del responsable de la MiPyME sobre el cierre del proyecto',
        ],
        'caso': 'Distribuidora El Surtido, reporte final de cierre, agosto. Resumen ejecutivo: el objetivo era bajar de 5 minutos a menos de 1 la confirmación de pedidos por WhatsApp y dejar de perder pedidos en hora pico; se logró: 94 % de las confirmaciones salen en menos de 30 segundos y no se perdió ningún pedido en las últimas cuatro semanas medidas. Entregables: bot y formulario de captura de pedidos (operando), tablero de rutas (operando), manual de usuario v1.2 (entregado), manual de mantenimiento v1.0 (entregado) y repositorio con documentación técnica (transferido a la cuenta de la empresa). Acuse: el 12 de agosto Raúl García recibió los accesos de administrador de la plataforma, del proveedor de IA y del VPS, ya actualizados, con acuse firmado. Mantenimiento: el soporte correctivo se amplió de 30 días a 6 meses, hasta febrero; respuesta en 24 h hábiles si una falla detiene la operación y en 72 h para el resto; no incluye funciones nuevas. Recomendaciones: revisar cada trimestre el costo por consulta del servicio de IA, capacitar a una segunda persona como respaldo de Raúl y afinar la predicción de demanda cuando haya seis meses de operación. Firma de conformidad: Raúl García, gerente general de Distribuidora El Surtido, 15 de agosto.',
        'preguntas': [
            ('Resumen ejecutivo del proyecto', '¿Con qué objetivo arrancó el proyecto y qué alcance lograste? Compara lo prometido con lo entregado y respáldalo con las cifras de tu reporte de rendimiento técnico.'),
            ('Entregables transferidos y su estatus', 'Enlista todo lo que queda en manos de la MiPyME (solución, manuales, código, accesos) y anota si cada entregable está operando, operando con observaciones o pendiente.'),
            ('Acuse de entrega de la actualización de credenciales y documentación', '¿Cómo dejaste constancia de que la persona responsable recibió las credenciales actualizadas y la documentación? ¿Quién firmó, cuándo y por qué medio? Adjunta el acuse.'),
            ('Compromisos de mantenimiento y niveles de servicio actualizados', '¿Qué mantenimiento queda comprometido, con qué vigencia y alcance? Si cambió respecto al acta de entrega, di qué cambió. Anota también lo que no cubre.'),
            ('Recomendaciones para la continuidad y evolución', '¿Qué debería hacer la MiPyME para que la solución siga sirviéndole? Piensa en costos que pueden cambiar, personas que conviene capacitar y mejoras que pedirán más datos.'),
            ('Firma de conformidad sobre el cierre', '¿Quién firma el cierre por parte de la MiPyME y con qué cargo? Deja el espacio para nombre, cargo, fecha y firma.'),
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
<p class="subtitle">Curso EC1836 · Producto del Elemento {elemento}</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Plantilla editable<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Quien te evalúa no busca que llenes la plantilla: busca que tu producto cumpla cada criterio del EC1836 con los datos de tu proyecto con una MiPyME, en tu lugar de trabajo o en una situación simulada. Las preguntas guía te orientan; las respuestas son tuyas.</div>

<div class="f21-box">
<h3>Qué pide el EC1836 (criterios literales)</h3>
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
Mi CompañIA · Una iniciativa de FUNDES México con el apoyo de Google.org<br>
Plantilla del curso EC1836 · Para que la llenes con los datos de tu proyecto con una MiPyME
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
<p class="subtitle">Curso EC1836 · Producto del Elemento {elemento} · Excel</p>
</td>
<td class="meta"><strong>Producto {num}</strong><br>Hoja editable · Excel<br><em>Mi CompañIA · FUNDES</em></td>
</tr>
</table>
</div>

<div class="intro"><strong>Sobre esta plantilla.</strong> {intro} Excel es el formato natural para este producto: permite añadir filas de medición, calcular promedios y comparativos automáticamente. <strong>Llénala con los datos de tu proyecto.</strong></div>

<div class="f21-box">
<h3>Qué pide el EC1836 (criterios literales)</h3>
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
Mi CompañIA · Una iniciativa de FUNDES México con el apoyo de Google.org · Plantilla del curso EC1836
</div>

</body>
</html>
"""


# ===========================================================================
# RENDERIZADORES
# ===========================================================================

def render_f21(criterios):
    """Genera la lista HTML de criterios literales del EC1836."""
    html = ""
    for c in criterios:
        html += f'<li>{c}</li>\n'
    return html


def render_questions_word(preguntas):
    """Genera los bloques de preguntas guía para las plantillas Word."""
    html = ""
    for i, (title, help_text) in enumerate(preguntas, 1):
        html += (
            f'<div class="question-block">\n'
            f'<div><span class="question-num">{i}</span>'
            f'<span class="question-title">{title}</span></div>\n'
            f'<div class="question-help">{help_text}</div>\n'
            f'<div class="fill-area">[Escribe aquí tu respuesta con los datos de tu proyecto. '
            f'Borra esta línea cuando empieces.]</div>\n'
            f'</div>\n'
        )
    return html


def render_questions_excel(preguntas):
    """Genera la tabla de preguntas guía para la plantilla Excel."""
    html = (
        '<table class="matrix">\n'
        '<tr>'
        '<th style="width: 4%;">#</th>'
        '<th style="width: 28%;">Pregunta guía</th>'
        '<th>Tu respuesta (con los datos de tu proyecto)</th>'
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
                # Variación calculada: (resultado real - umbral) / umbral
                f'<td class="fill" style="text-align:center;color:#4B5563;">'
                f'=IFERROR(ROUND((C{{f}}-B{{f}})/B{{f}}*100,2),"")</td>\n'
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
  Herramientas posibles: un servicio de monitoreo de disponibilidad, las métricas del servidor o los registros (logs) de la aplicación.
</p>

<h2>Hoja 2 · Comparativo indicadores técnicos vs umbrales de la propuesta</h2>
<p style="font-size: 10pt; color: #666;">
  Compara el resultado real del periodo contra el umbral que definiste en la propuesta de modernización digital autorizada.
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
  revisando una muestra de respuestas de la operación (el caso de El Surtido usó 50 llamadas; el tamaño de la muestra lo decides tú y lo explicas).
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
  El EC1836 pide ejemplos representativos de la calidad de las respuestas. Elige un caso correcto y uno con error, tomados de la operación de tu solución.
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
    print(f"\nGeneradas {n} plantillas en {OUT}/")
    import subprocess
    import sys
    subprocess.run([sys.executable, str(ROOT / "scripts" / "convert-legacy-office.py")], check=True)
