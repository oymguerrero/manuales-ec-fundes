# Sistema de Diseño Web — Mi CompañIA

## 1. Identidad visual

### Nombre

Mi CompañIA

### Concepto central

"La IA que acompaña a las MiPyMEs mexicanas paso a paso."

### Personalidad

* Cercana
* Práctica
* Esperanzadora
* Honesta
* Empoderadora

### Voz

Hablamos como un amigo que sabe: claro, humano, útil y sin tecnicismos innecesarios.

---

## 2. Paleta de color

### Colores principales

| Nombre         | Uso                               | HEX       |
| -------------- | --------------------------------- | --------- |
| Azul principal | Confianza, tecnología, estructura | `#1F4E8C` |
| Azul claro     | Cercanía, accesibilidad           | `#4DA3DF` |
| Amarillo Mi    | Energía, optimismo, acción        | `#FFC233` |
| Azul profundo  | Títulos, contraste, autoridad     | `#0B2E63` |
| Blanco cálido  | Fondo principal                   | `#FAFCFF` |

### Colores secundarios

| Nombre         | Uso                | HEX       |
| -------------- | ------------------ | --------- |
| Verde impacto  | Resultados, avance | `#3FA35B` |
| Azul suave     | Fondos de tarjetas | `#EAF4FF` |
| Amarillo suave | Fondos de énfasis  | `#FFF3CC` |
| Gris texto     | Texto secundario   | `#4B5563` |
| Gris línea     | Bordes suaves      | `#D9E4F2` |

### Contraste mínimo (WCAG AA)

| Combinación                              | Ratio mínimo | Uso                  |
| ---------------------------------------- | ------------ | -------------------- |
| `#0B2E63` sobre `#FFC233`                | ≥ 4.5:1      | Botón primario       |
| `#1F4E8C` sobre `#FAFCFF`                | ≥ 4.5:1      | Texto sobre fondo    |
| `#4B5563` sobre `#FAFCFF`                | ≥ 4.5:1      | Texto secundario     |
| `#FAFCFF` sobre `#1F4E8C`                | ≥ 4.5:1      | Texto sobre azul     |

Verificar todos los pares de color en producción con herramienta WCAG antes de publicar.

---

## 3. Tipografía

### Fuente principal

Inter

```css
font-family: 'Inter', sans-serif;
```

### Fuente alternativa

DM Sans

```css
font-family: 'DM Sans', sans-serif;
```

### Jerarquía tipográfica — Desktop

| Elemento        | Tamaño   | Peso |
| --------------- | -------- | ---- |
| Hero / H1       | 56–64 px | 800  |
| H2              | 36–44 px | 700  |
| H3              | 24–28 px | 700  |
| Texto destacado | 20–22 px | 600  |
| Cuerpo          | 16–18 px | 400  |
| Texto pequeño   | 13–14 px | 500  |
| Botones         | 16 px    | 700  |

### Jerarquía tipográfica — Móvil (≤ 768px)

| Elemento        | Tamaño   | Peso |
| --------------- | -------- | ---- |
| Hero / H1       | 32–36 px | 800  |
| H2              | 24–28 px | 700  |
| H3              | 20–22 px | 700  |
| Texto destacado | 17–18 px | 600  |
| Cuerpo          | 15–16 px | 400  |
| Texto pequeño   | 13 px    | 500  |
| Botones         | 15 px    | 700  |

---

## 4. Estilo visual

### Principios

* Claridad antes que decoración
* Mucho espacio en blanco
* Tarjetas redondeadas
* Íconos simples
* Ilustraciones humanas
* Datos grandes y fáciles de leer
* Lenguaje visual amable

### Bordes

```css
border-radius: 20px;
```

### Sombras

```css
box-shadow: 0 12px 32px rgba(31, 78, 140, 0.10);
```

### Líneas divisorias

```css
border: 1px solid #D9E4F2;
```

---

## 5. Componentes principales

### Header

#### Navegación sugerida

* Qué es
* Para MiPyMEs
* Para aliados
* Impacto
* Contacto

#### Botón principal

```css
background: #FFC233;
color: #0B2E63;
border-radius: 999px;
font-weight: 700;
```

Texto:

```
Quiero sumarme
```

---

### Hero section

#### Copy sugerido

```
La IA que acompaña a las MiPyMEs mexicanas

Mi CompañIA ayuda a los negocios de México a dar sus primeros
pasos con Inteligencia Artificial de forma sencilla, práctica
y acompañada.

[Quiero conocer el programa]   [Soy aliado]
```

---

### Cards de datos

#### Ejemplo

```
99.8%
de los negocios en México son MiPyMEs.
```

#### Colores

* Número: `#1F4E8C`
* Énfasis: `#FFC233`

---

### Cards de ejes

#### Ejes principales

1. Sensibilización
2. Formación y certificación de talento
3. Adopción con acompañamiento real

#### Estilo

* Número circular
* Ícono
* Título azul profundo
* Descripción corta
* Fondo blanco
* Borde suave

---

### Sección para aliados

#### Título

```
¿Por qué aliarse con Mi CompañIA?
```

#### Mensaje clave

```
Tú conoces a las empresas.
Nosotros tenemos el camino.
```

#### Bloques de contenido

**Qué hace un aliado** — tres ítems con ícono:
* Convoca y difunde su red
* Abre espacios para talleres y eventos
* Co-construye rutas de aprendizaje para su comunidad

**Qué recibe el aliado** — tres ítems con ícono:
* Visibilidad como actor clave en transformación digital
* Contenido y herramientas listas para sus empresas
* Reporte de impacto de las MiPyMEs de su red

#### CTA diferenciado

```css
/* Botón aliado — distinto al CTA de MiPyME */
background: #0B2E63;
color: #FAFCFF;
border-radius: 999px;
font-weight: 700;
```

Texto:

```
Quiero ser aliado
```

---

### Botones

#### Botón primario (MiPyME)

```css
background: #FFC233;
color: #0B2E63;
border-radius: 999px;
padding: 14px 28px;
font-weight: 700;
min-height: 44px; /* Área táctil mínima móvil */
```

#### Botón secundario

```css
background: #EAF4FF;
color: #1F4E8C;
border: 1px solid #D9E4F2;
border-radius: 999px;
min-height: 44px;
```

#### Botón aliado (primario oscuro)

```css
background: #0B2E63;
color: #FAFCFF;
border-radius: 999px;
padding: 14px 28px;
font-weight: 700;
min-height: 44px;
```

---

## 6. Íconos

### Estilo

* Lineales
* Redondeados
* Amables
* Simples

### Temas

* Tienda
* Personas
* IA
* Gráficas
* Educación
* Apretón de manos
* Mensajes
* Crecimiento
* Comunidad

---

## 7. Ilustraciones

### Deben sentirse

* Humanas
* Cercanas
* Cotidianas
* Mexicanas
* Positivas

### Evitar

* Robots fríos
* Estética sci-fi
* Exceso de hologramas
* Visuales corporativos rígidos
* Sparkles genéricos de IA

---

## 8. Lenguaje de marca

### Sí usamos

* Tu negocio
* Paso a paso
* A tu ritmo
* Herramientas
* Acompañamiento
* Ahorrar tiempo
* Mejorar
* Crecer
* Clientes

### Evitamos

* Transformación digital
* Framework
* Pipeline
* Stakeholders
* Disruptivo
* Optimizar
* Algoritmo sin explicación

> **Nota para secciones de aliados**: En el copy dirigido a aliados institucionales
> (cámaras, gobierno, academia) se permite "transformación digital" como término
> reconocido en ese contexto. Para secciones dirigidas a MiPyMEs, aplica la
> restricción sin excepción.

---

## 9. Frases ancla

```
La IA no te reemplaza. Te acompaña.
```

```
Tu negocio ya tiene experiencia. Solo necesita un empujón digital.
```

```
Paso a paso, a tu ritmo, con compañIA.
```

> Las letras **IA** siempre en mayúscula y con color diferenciado (`#FFC233`)
> cuando aparezcan en titulares o frases ancla destacadas.

---

## 10. Layout recomendado

1. Header
2. Hero
3. El reto
4. Qué es Mi CompañIA
5. Tres ejes
6. Para MiPyMEs
7. Para aliados
8. Impacto esperado
9. CTA final
10. Footer

---

## 11. Diseño responsivo

### Breakpoints

| Breakpoint | Ancho      | Contexto                         |
| ---------- | ---------- | -------------------------------- |
| Móvil      | ≤ 767px    | Smartphones (audiencia principal)|
| Tablet     | 768–1023px | Tablets y pantallas medianas     |
| Desktop    | ≥ 1024px   | Escritorio                       |

### Principios responsivos

* **Mobile-first**: Diseñar primero para 375px y escalar hacia arriba.
* Las cards de ejes se apilan verticalmente en móvil (una por fila).
* La navegación colapsa en hamburger menu en móvil.
* Imágenes con `width: 100%; max-width: 100%` por defecto.
* Peso de página objetivo: **< 2 MB** en primera carga (crítico para usuarios con conectividad limitada).
* Lazy loading obligatorio para imágenes e ilustraciones.

---

## 12. Accesibilidad

* Contraste mínimo 4.5:1 para todo texto sobre fondo (ver tabla sección 2).
* Área táctil mínima: **44 × 44 px** para todos los botones e íconos interactivos.
* Texto alternativo (`alt`) obligatorio en todas las ilustraciones e íconos con significado.
* Íconos decorativos: `aria-hidden="true"`.
* Jerarquía de encabezados respetada: un solo `H1` por página, `H2` para secciones, `H3` para subsecciones.
* Formularios con `<label>` explícito en cada campo.
* Navegación por teclado funcional en todos los componentes interactivos.
* Sin contenido que dependa exclusivamente de color para transmitir significado.

---

## 13. Footer

### Contenido

* Logo Mi CompañIA
* FUNDES Latinoamérica
* Google.org
* Contacto
* Redes sociales

### Copy final

```
Mi CompañIA es una iniciativa de FUNDES Latinoamérica con el apoyo de Google.org.
```

---

## 14. Sensación general

### La web debe sentirse como

* Una guía clara
* Un aliado confiable
* Una invitación amable
* Tecnología explicada para personas reales

### No debe sentirse como

* Una consultora fría
* Una startup exagerada
* Una web gubernamental rígida
* Una campaña de miedo
* Un sitio técnico complejo

---

## 15. Diagramas y figuras

Esta sección establece cómo hacer **diagramas SVG inline** y **figuras con imágenes** para que mantengan consistencia visual con la marca Mi CompañIA. Cualquier diagrama nuevo debe seguir estos lineamientos antes de incorporarse al sitio.

### 15.1 Principios

1. **Función pedagógica antes que decoración.** Si un diagrama no acelera la comprensión, no va. Si una tabla cumple el mismo propósito, mejor tabla.
2. **SVG inline preferido sobre imagen.** Sin créditos consumidos, peso despreciable, accesibilidad nativa, escala perfecta en cualquier viewport.
3. **Accesibilidad obligatoria.** Todo diagrama lleva `role="img"`, `<title>` y `<desc>` accesibles para lectores de pantalla.
4. **Caption explicativo siempre.** Cada diagrama va seguido de una frase que extrae la conclusión clave. El diagrama muestra, el caption interpreta.
5. **Paleta de marca, no colores libres.** Solo se usan los tokens de la sección 2; nada de paletas decorativas.

### 15.2 Cuándo usar diagrama, tabla o imagen

| Tipo | Cuándo usarlo | Cuándo NO |
|---|---|---|
| **SVG diagrama** | Hay relaciones espaciales o jerarquías (qué alimenta a qué, qué pesa más, qué viene antes) | Solo hay datos planos sin relación visual |
| **Tabla `.prose-table`** | Datos comparables fila por fila, sin jerarquía visual | El lector necesita ver patrón o flujo de un vistazo |
| **`<figure>` con foto** | Refuerzo emocional o de contexto humano (consultora con MiPyME real) | Para concepto abstracto, regla o jerarquía |
| **Texto narrativo solo** | El concepto se explica mejor con palabras | Hay más de 4 elementos relacionados |

### 15.3 Tipos canónicos de diagrama

Estos son los **10 patrones probados** en el proyecto Mi CompañIA. Antes de inventar uno nuevo, revisa si tu caso encaja en alguno:

| # | Patrón | Cuándo usarlo | Ejemplo en el sitio |
|---|---|---|---|
| 1 | **Jerárquico vertical** (rectángulos apilados con flechas) | Hay niveles institucionales o de autoridad | Arquitectura SNC en `maestro/que-es.html` |
| 2 | **Pirámide** (3-5 niveles trapezoidales) | Hay estratificación por complejidad/cantidad | Niveles SNC en `maestro/que-es.html` |
| 3 | **Radial / ciclo** (centro + outer nodes con líneas radiales) | Un actor central recibe servicios de varios | 4 estándares en torno a la MiPyME |
| 4 | **Timeline horizontal** (línea base + nodos numerados) | Hay una secuencia temporal | 6 pasos del proceso · 4 semanas de preparación |
| 5 | **Flujo en árbol** (productos con flechas que se ramifican) | Un producto alimenta a varios siguientes | 8 productos del Elemento 1 |
| 6 | **Mapa de involucrados** (centro humano + actores en círculos) | Hay personas conectadas por flujo de información | La Espiga: Doña Beatriz al centro |
| 7 | **Cuadrante 2×2** (4 zonas + puntos ubicados) | Decisiones según dos ejes (impacto/esfuerzo) | Matriz de oportunidades de IA |
| 8 | **Donut / dual donut** (anillos con segmentos coloreados) | Distribución porcentual de un total | 126 reactivos del IEC vs 100.17 puntos |
| 9 | **Barras comparativas** (antes/después de lado a lado) | Indicador único cambia entre dos estados | Antes/después de La Espiga (3 indicadores) |
| 10 | **Grupos temáticos** (3-4 contenedores con items dentro) | Larga lista que se agrupa para memorizar mejor | 9 características del informe técnico |

### 15.4 Paleta específica para diagramas

Subset de los tokens de marca con **roles semánticos** asignados:

| Token | Hex | Rol en diagrama |
|---|---|---|
| Azul profundo | `#0B2E63` | Contenedor primario · jerarquía superior · autoridad |
| Azul principal | `#1F4E8C` | Contenedor secundario · flechas · etiquetas estructurales |
| Azul claro | `#4DA3DF` | Contenedor terciario · nivel operativo · variantes "ligeras" |
| Amarillo Mi | `#FFC233` | Acento crítico · highlights · borde de elementos importantes |
| Amarillo suave | `#FFF3CC` | Fondo de cuadrante "atención" · zona neutra-positiva |
| Verde impacto | `#3FA35B` | Resultados positivos · "después" mejorado · Quick Wins · DONE |
| Verde suave | `#ECF7EF` | Fondo de cuadrante "bueno" |
| Azul suave | `#EAF4FF` | Fondo de cuadrante "positivo" / fondo SVG |
| Blanco cálido | `#FAFCFF` | Texto sobre fondos oscuros · fondo del SVG |
| Gris texto | `#4B5563` | Texto secundario · etiquetas explicativas en cursiva |
| Gris línea | `#D9E4F2` | Líneas auxiliares · bordes suaves · fondos neutros |

**Solo para casos específicos** (uso limitado a diagramas con semántica negativa o terceros externos):

| Token | Hex | Uso restringido |
|---|---|---|
| Rojo | `#9F2929` | Indicadores negativos · "antes" malo · AHV que restan · descartar |
| Naranja | `#B85800` | Advertencias · zona "alto esfuerzo bajo impacto" |
| Morado | `#7C3AED` | Actores externos · terceros · plantillas guía |

> **Regla:** un diagrama típico usa 3-5 colores como máximo. Si necesitas más, probablemente la información debe segmentarse en dos diagramas.

### 15.5 Tipografía dentro del SVG

```svg
font-family="Inter, sans-serif"
```

Escalas recomendadas (en píxeles SVG, no `rem`):

| Uso | Tamaño | Peso |
|---|---|---|
| Título principal del diagrama | 14-16 | 700 |
| Etiqueta de contenedor grande | 13-14 | 700 |
| Texto de cuerpo en nodo | 11-13 | 600 |
| Número grande (KPI, badge) | 18-32 | 800 |
| Etiqueta de eje / leyenda | 10-11 | 600 |
| Anotación italic / aclaración | 9-10 | 400 (italic) |

**Color de texto:** sobre fondo oscuro → `#FAFCFF`; sobre fondo claro → `#0B2E63` o `#4B5563`. **Nunca** usar `black` o `#000`.

### 15.6 Plantilla SVG base obligatoria

Todo diagrama empieza con esta estructura:

```html
<svg class="diagram" viewBox="0 0 [W] [H]"
     role="img"
     aria-labelledby="svg-[id]-title svg-[id]-desc">
  <title id="svg-[id]-title">[Título corto, 1 línea]</title>
  <desc id="svg-[id]-desc">[Narración alternativa completa para lector de pantalla — describe el diagrama como si la persona no lo viera, incluyendo los datos relevantes]</desc>

  <defs>
    <!-- Marker para flechas, solo si hay flechas -->
    <marker id="arrow-[id]" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1F4E8C"/>
    </marker>
  </defs>

  <!-- Contenido del diagrama -->
</svg>
<p class="diagram-caption">[Caption breve · una conclusión clave que el lector no debe perderse]</p>
```

**Reglas del `viewBox`:**

- Ancho típico: `800-1000` para diagramas full-width; `700` para `.diagram--compact`.
- Alto: lo que la composición requiera; evita ratios extremos (no más de 3:1 ni menos de 2:3).
- **Nunca** especifiques `width` ni `height` fijos en el `<svg>` — solo `viewBox` y la clase `.diagram` se encarga del layout.

### 15.7 Convenciones de markers (flechas)

Cada diagrama con flechas declara su propio marker en `<defs>` con `id` único (ej. `arrow-mapa`, `arrow-flow`). Color del marker debe coincidir con el `stroke` de la línea.

```html
<defs>
  <marker id="arrow-XX" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1F4E8C"/>
  </marker>
</defs>

<line x1="..." y1="..." x2="..." y2="..."
      stroke="#1F4E8C" stroke-width="2"
      marker-end="url(#arrow-XX)"/>
```

Stroke-widths estándar:

- Conexión principal: `stroke-width="3"` (azul profundo o principal)
- Conexión secundaria: `stroke-width="2"`
- Línea auxiliar / leyenda: `stroke-width="1.5"`
- Línea media / divisor: `stroke-width="1"` con `stroke-dasharray="4 3"`

### 15.8 Bordes redondeados

Coherente con el resto del sistema visual:

| Elemento | `rx` (radio) |
|---|---|
| Contenedor grande (rectángulo principal) | `14-16` |
| Contenedor mediano (sección dentro de diagrama) | `8-10` |
| Botón / píldora pequeña | `6-8` |
| Círculo / badge | usar `<circle>`, no rectángulo |

### 15.9 Sombras y profundidad

**No** usar `filter="drop-shadow(...)"` dentro del SVG. La profundidad se logra con la clase `.diagram` del CSS:

```css
.diagram {
  border: 1px solid var(--color-gris-linea);
  border-radius: var(--radius-sm);
  padding: 20px;
  box-shadow: var(--shadow-sm);
}
```

### 15.10 Accesibilidad: cómo escribir un buen `<desc>`

El `<desc>` es el **equivalente del `alt` para imágenes**, pero más extenso. Debe permitir que una persona con lector de pantalla entienda el diagrama sin verlo.

**Bien:**

> "Cinco oportunidades ubicadas en cuadrante. Asistente WhatsApp y Resumen diario a cocina están en la zona de alto impacto (prioridad 1). Registro unificado de pedidos está en impacto medio y esfuerzo medio (prioridad 2). Conciliación contable digital tiene alto esfuerzo (prioridad 3). Tablero de inventario está en bajo impacto y alto esfuerzo (aplazar)."

**Mal:**

> "Cuadrante con cinco oportunidades."

### 15.11 Caption: cómo extraer la conclusión

El caption (`.diagram-caption`) **no describe** el diagrama; **interpreta** la conclusión clave que el lector debe llevarse. Una sola frase, máximo dos.

**Bien:**

> "Asimetría clave: los 15 reactivos de peso mayor (12% de los reactivos) aportan el 50% del puntaje. Identificarlos y prepararlos con prioridad es la mejor inversión de tu tiempo."

**Mal:**

> "Distribución de los 126 reactivos del IEC."

### 15.12 Figuras con imágenes (`<figure>`)

Para fotos reales (higgsfield u otros), usar siempre el componente semántico:

```html
<figure class="figure">
  <img src="../img/[nombre].jpg"
       alt="[Descripción significativa, no decorativa]"
       loading="lazy"
       width="1920" height="1080" />
  <figcaption>[Frase que conecta la imagen con el contenido pedagógico]</figcaption>
</figure>
```

**Reglas obligatorias:**

- `loading="lazy"` salvo para imágenes en el hero (above-the-fold).
- `width` y `height` declarados para evitar layout shift.
- `alt` significativo, no genérico. Ejemplo: "Profesional mexicana sosteniendo su Certificado en su oficina" (sí); "imagen.jpg" (no).
- Imagen ≤ 400 KB. Comprimir a JPG calidad 80-85 y resize a 1920px de ancho máximo.

### 15.13 Cuándo NO hacer un diagrama

Frenos honestos. No agregues un diagrama si:

- Hay menos de 3 elementos relacionados (mejor lista o texto).
- La relación es lineal sin ramificaciones (mejor `<ol>`).
- Los datos cambian con frecuencia (un diagrama estático envejece mal).
- Estás "rellenando" porque la página se ve muy textual (el diseño se resuelve con espaciado y tipografía, no con decoración).
- No tienes un caption interpretativo claro que escribir.

### 15.14 Pipeline para crear un diagrama nuevo

1. **Identifica el tipo** según la tabla §15.3. Si no encaja, considera primero adaptar uno existente antes de inventar.
2. **Escribe primero el caption** (la conclusión). Si no puedes redactarlo, el diagrama no debería existir todavía.
3. **Dibuja el wireframe** a lápiz o en herramienta libre — viewBox, posiciones aproximadas.
4. **Implementa el SVG** siguiendo §15.6 (plantilla base obligatoria).
5. **Aplica la paleta** según §15.4 (solo tokens de marca, máximo 5 colores).
6. **Escribe `<title>` y `<desc>`** accesibles según §15.10.
7. **Revisa con el agente `mi-compania-brand-reviewer`** antes de commit.
8. **Verifica responsive**: el `viewBox` debe permitir que el diagrama se vea bien desde 320px hasta 1920px.

### 15.15 Diagramas existentes como referencia

Antes de crear uno nuevo, revisa estos 13 ejemplos canónicos:

| Archivo | Diagrama | Patrón |
|---|---|---|
| `maestro/que-es.html` | Arquitectura SNC (3 niveles + Tú) | Jerárquico vertical |
| `maestro/que-es.html` | Pirámide niveles SNC | Pirámide |
| `maestro/como-se-evalua.html` | 5 evidencias → portafolio | Flujo convergente |
| `maestro/proceso.html` | Timeline 6 pasos | Timeline horizontal |
| `maestro/cuatro-estandares.html` | Ciclo 4 estándares + MiPyME | Radial |
| `estandar-a/index.html` | Mapa funcional Estándar A | Jerárquico horizontal |
| `estandar-a/elemento-1.html` | Flujo 8 productos | Flujo en árbol |
| `estandar-a/elemento-1.html` | Mapa La Espiga | Mapa de involucrados |
| `estandar-a/elemento-1.html` | Cuadrante impacto/esfuerzo | Cuadrante 2×2 |
| `estandar-a/elemento-2.html` | 9 componentes informe técnico | Grupos temáticos |
| `estandar-a/elemento-3.html` | Antes vs Después La Espiga | Barras comparativas |
| `estandar-a/instrumento.html` | Doble donut IEC | Donut/pie |
| `estandar-a/ruta-preparacion.html` | Timeline 4 semanas | Timeline horizontal |

> **Cuando agregues un diagrama nuevo, actualiza esta tabla.**

---

## 16. Aprendizaje activo · patrones interactivos

Esta sección establece los principios pedagógicos y los patrones técnicos para componentes interactivos. Para cualquier sección con riesgo de "muro de texto", consulta primero §16.1 (cuándo intervenir) y §16.4 (catálogo de patrones).

### 16.1 Principios pedagógicos (los 8 marcos que aplicamos)

Mi CompañIA combina ocho marcos pedagógicos. Cada decisión de diseño puede justificarse contra al menos uno:

1. **Andragogía (Knowles)** — Adultos: necesidad de saber, auto-concepto, experiencia, disposición, problema-orientación, motivación intrínseca.
2. **Bloom revisado (Anderson)** — Niveles cognitivos: Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear.
3. **Carga cognitiva (Sweller)** — Memoria de trabajo limitada: chunking (5-7), eliminar carga extraña, scaffolding, worked examples.
4. **Dual Coding (Paivio)** — Verbal + visual juntos sube retención ~50%.
5. **Microlearning** — Unidades de 3-7 min, una idea por unidad, evaluación inmediata.
6. **UDL** — Múltiples medios de representación, acción/expresión y compromiso.
7. **Backward Design (Wiggins)** — Empieza por el resultado: objetivo → evidencia → actividad.
8. **CONOCER** — Los 4 tipos de evidencia mapean a Bloom: Conocimientos (1-2), Productos (3, 6), Desempeños (3-4), AHV (5).

> **Regla de oro:** antes de cada actividad, escribe el objetivo de Backward Design en una línea ("al terminar esta actividad, el aspirante podrá…"). Si no puedes escribirlo, la actividad no debe existir todavía.

### 16.2 Cuándo intervenir un muro de texto

Aplica cualquiera de estas heurísticas y considera convertir:

- Sección con **>500 palabras** seguidas sin componente interactivo.
- Lista de **>7 items** sin agrupación visual.
- **>5 términos** definidos en párrafos seguidos.
- Procedimiento de **>5 pasos** sin numeración visual.
- Comparación que se hace en prosa cuando debería ser tabla/diagrama.
- Tiempo estimado de lectura **>8 minutos** sin pausa interactiva.

**No intervengas si:**

- La sección es deliberadamente narrativa (ej. bienvenida emocional).
- El texto es documentación técnica de referencia (FAQ, glosario formal).
- El contenido cambia con frecuencia (un componente complejo envejece mal).

### 16.3 Tabla de decisión: qué patrón usar

| Si la información es… | Patrón recomendado | Bloom |
|---|---|---|
| Glosario de 5-15 términos | **Flip cards** | 1-2 |
| Verificación de comprensión | **Quiz multiple choice con feedback** | 2-3 |
| Decisión profesional ("qué harías") | **Decision scenario** branching | 3-5 |
| Clasificación de items en grupos | **Sort drag-drop** | 3-4 |
| Secuencia / orden de pasos | **Sequence drag-drop** | 3 |
| Pares relacionados (causa-efecto, término-def) | **Match pairs** | 2-3 |
| Comparación de dos estados | **Comparison slider** | 4 |
| Diagrama con detalles ocultos | **Hotspot diagram** | 2-3 |
| Caso complejo con bifurcaciones | **Case study branching** | 3-5 |
| Reflexión abierta | **Reflection prompt** | 5-6 |
| Cálculo / simulación | **Calculator / simulator** | 3 |
| Concepto que requiere movimiento | **Microvideo** | 1-3 |
| Accesibilidad / commute | **Audio narration** | 1-2 |

### 16.4 Catálogo de patrones (markup canónico)

Los contratos HTML completos viven en el agente `mi-compania-frontend.md` § "Componentes interactivos pedagógicos". Aquí los principios:

**Reglas universales para todo componente interactivo:**

1. **Elemento semántico correcto.** Usa `<button>` para acciones, `<input type="radio">` para selección excluyente, `<details>/<summary>` para revelación progresiva. Nunca `<div onclick>`.
2. **Navegación por teclado.** Todo lo clickeable debe ser focusable (Tab) y accionable (Enter / Space).
3. **Estado anunciado.** Zonas de feedback dinámico llevan `aria-live="polite"`.
4. **Fallback sin JS.** Si el JavaScript falla, la información factual debe quedar legible. Ej: un quiz sin JS debe seguir mostrando la pregunta y dejar que el lector razone por su cuenta.
5. **Sin trampas de foco.** El foco no debe quedar atrapado en una actividad; siempre debe poder salir con Tab.

### 16.5 Audio y video

#### Microvideo

**Cuándo:** concepto que se entiende mejor con movimiento (proceso de 6 pasos, secuencia temporal, comparación dinámica).

**Especificaciones:**
- Duración: 1-3 minutos (idealmente 90 seg)
- Aspect ratio: 16:9 (1920×1080)
- Formato: MP4 H.264, ~10 MB por minuto
- Subtítulos: archivo `.vtt` en español obligatorio (accesibilidad)
- Poster: frame representativo (`img/poster-X.jpg`)
- Ubicación: `media/`

**Markup:**
```html
<figure class="figure figure--video">
  <video controls preload="metadata" poster="../img/poster-X.jpg"
         width="1920" height="1080">
    <source src="../media/video-X.mp4" type="video/mp4" />
    <track default kind="captions" srclang="es" src="../media/video-X.vtt" />
  </video>
  <figcaption>Microvideo · [duración] · [tema]</figcaption>
</figure>
```

#### Audio narrado

**Cuándo:** accesibilidad UDL, aspirantes que quieren consumir en commute, alternativa al texto largo.

**Especificaciones:**
- Duración: 3-10 minutos por sección
- Formato: MP3 128 kbps, ~1-2 MB por minuto
- Voz: TTS Neural premium (Google Cloud `es-US-Neural2-A/B`) o grabación humana
- `speakingRate: 0.95` para contenido pedagógico
- Transcripción accesible **obligatoria** (aria + UDL)
- Ubicación: `media/`

**Markup:**
```html
<div class="audio-narration">
  <button class="audio-narration__toggle" type="button"
          aria-expanded="false" aria-controls="audio-X">
    🎧 Escuchar esta sección · [duración]
  </button>
  <audio id="audio-X" controls preload="none" hidden>
    <source src="../media/audio-X.mp3" type="audio/mpeg" />
  </audio>
  <details class="audio-narration__transcript">
    <summary>Ver transcripción</summary>
    <p>[transcripción completa]</p>
  </details>
</div>
```

**Reglas de redacción para narración** (script del audio):

- Oraciones cortas (máximo 18 palabras) — el oído no puede pausar como el ojo.
- Evita anidación de subordinadas.
- Marca pausas entre ideas (`<break time="500ms"/>` en SSML).
- Repite el sujeto cuando hayan pasado 2+ oraciones — el oyente pierde referencia.
- Lee en voz alta antes de mandar a TTS.
- 130-150 palabras por minuto a `speakingRate 0.95`.

### 16.6 Microlearning · arquitectura de la unidad

Una unidad de aprendizaje **bien diseñada** sigue este esquema (≤8 min total):

1. **Activador (30 seg)** — Pregunta inicial, reflexión breve, mini-diagnóstico. Conecta con lo que el aspirante ya sabe.
2. **Concepto (2-3 min)** — Explicación principal, idealmente texto + diagrama o microvideo.
3. **Ejemplo aplicado (1-2 min)** — La Espiga u otro caso concreto.
4. **Práctica activa (2-3 min)** — Quiz, flip cards, decisión o reflexión que ejercita Bloom 3+.
5. **Cierre (30 seg)** — Puntos clave (`.key-points`) y enlace a siguiente unidad.

### 16.7 Anti-patrones (no hagas)

- ❌ **Quiz puramente memorístico** ("¿qué dijo la sección anterior?") — Bloom 1 sin aplicación → poco valor.
- ❌ **Actividad sin feedback** — el aspirante necesita saber si acertó y por qué.
- ❌ **Distractores ridículos** — opciones obviamente malas degradan la actividad.
- ❌ **Más de 7 items en una actividad** — chunking violado, frustración.
- ❌ **Decoración sin función** — animaciones, GIFs sin valor pedagógico.
- ❌ **Texto sobre video sin opción de pausar/transcripción** — viola UDL.
- ❌ **Componente complejo sin fallback** — si JS falla, la información debe seguir accesible.

### 16.8 Pipeline para convertir un muro de texto

Usa el skill `/convertir-muro-de-texto` o sigue manualmente:

1. **Detecta** muros con las heurísticas de §16.2.
2. **Diagnostica** con el `mi-compania-pedagogo` (objetivo + Bloom + patrón).
3. **Diseña** el contenido de la actividad (preguntas, opciones, feedback, secuencia).
4. **Implementa** vía `mi-compania-frontend` (markup) y, si es audio/video, vía `mi-compania-asset-generator`.
5. **Revisa** con `mi-compania-brand-reviewer` (valida §15, §16, accesibilidad, peso).

### 16.9 Catálogo de componentes interactivos ya implementados

Estado de la biblioteca compartida en `assets/styles.css` + `assets/interactive.js`:

| Componente | Patrón Bloom | Estado |
|---|---|---|
| **Lesson Tabs LMS** (sidebar + panel + progress + check) | Estructura de lección | ✅ (ver §17) |
| **Accordion modules** (`<details>` con badge + meta) | Recordar | ✅ (base del Lesson Tabs) |
| Tabs ARIA accesibles | Recordar/Comprender | ✅ |
| Accordion FAQ (`<details>`) | Recordar | ✅ nativo |
| Checklist con localStorage | Aplicar (autoevaluación) | ✅ |
| Mini-diagnóstico | Evaluar | ✅ |
| Finder cuestionario | Aplicar (decisión) | ✅ |
| Glosario filtrable | Recordar | ✅ |
| Reflection prompt (callout--reflection) | Crear/Evaluar | ✅ |
| Key points (recapitulación) | Comprender | ✅ |
| Flip cards | Recordar | ✅ |
| Quiz multiple choice | Comprender/Aplicar | ✅ |
| **Audio narration con mini-bar flotante** | UDL (vía auditiva) | ✅ (ElevenLabs · voz Alice · ver §17.7) |
| Decision scenario | Aplicar/Analizar | ⏳ pendiente |
| Sort drag-drop | Aplicar/Analizar | ⏳ pendiente |
| Sequence drag-drop | Aplicar | ⏳ pendiente |
| Comparison slider | Analizar | ⏳ pendiente |
| Hotspot diagram | Recordar/Aplicar | ⏳ pendiente |
| Microvideo embed | variable | ⏳ pendiente |

> **Cuando se implemente un componente nuevo, mueve su fila de pendiente a implementado y actualiza esta tabla.**

---

## 17. Navegación de capítulos: Lesson Tabs (LMS-style)

Patrón principal para presentar **capítulos del manual** que tienen 3 o más
secciones. Inspirado en Coursera / LinkedIn Learning / Moodle: sidebar
vertical con la lista de módulos + panel principal con el contenido +
tracking de avance visible. El HTML semántico sigue siendo `<details>/<summary>`
para que Ctrl+F, screen readers y print sigan funcionando.

### 17.1 Cuándo usar este patrón

Aplica `.lesson-tabs` cuando:

- La página representa un **capítulo de lectura secuencial** con 3+ secciones
  conceptuales independientes (no son pasos en cadena, son temas paralelos
  o agrupados temáticamente).
- El aspirante se beneficia de **ver dónde está parado** y cuánto le falta.
- Hace sentido permitir **marcar como leído** y persistir el avance entre
  visitas (un manual de estudio largo, no una página de referencia).

**NO uses lesson-tabs cuando:**

- La página es referencial (FAQ, glosario, recursos) → usa accordion FAQ.
- La página tiene una sola sección larga → estructura normal con headings.
- La página tiene contenido secuencial obligatorio paso-a-paso → considera
  un stepper dedicado en lugar de tabs.

### 17.2 Anatomía del componente

```
┌─────────────────────────────────────────────────────────────────┐
│  ▰▰▰░░░░  3 de 6 módulos completados              [Reiniciar]   │  ← header
├──────────────────┬──────────────────────────────────────────────┤
│  ✓ 1.1 ¿Por qué  │  ┌─ 1.3 Cómo funciona el sistema en México ┐│
│  ✓ 1.2 ¿Qué es   │  │  [contenido completo del módulo]         ││  ← panel
│  ▶ 1.3 Cómo fun  │  │                                          ││
│    1.4 ¿Qué es   │  │  ← Anterior  · ✓ Marcar y continuar →    ││
│    1.5 Mitos y   │  └──────────────────────────────────────────┘│
│    1.6 Quién pue │                                              │
└──────────────────┴──────────────────────────────────────────────┘
   ↑ sidebar             ↑ panel-card
```

Tres estados visuales en cada item del sidebar:
- **○ pendiente** (gris) — aún no abierto
- **▶ activo** (azul con borde lateral) — módulo abierto actualmente
- **✓ completado** (verde) — marcado como leído

### 17.3 Estructura HTML mínima

El wrapper `<div class="lesson-tabs">` envuelve un `<div class="accordion accordion--modules">`
que a su vez contiene una serie de `<details class="accordion__item">`. El JS
construye dinámicamente el header, sidebar, panel y footer.

```html
<div class="lesson-tabs" data-progress-key="manual-X-cap-Y">
  <div class="accordion accordion--modules" aria-label="Módulos del Capítulo Y">

    <details class="accordion__item" id="anchor-1" open>
      <summary>
        <span class="accordion__num">1.1</span>
        <span class="accordion__title-main">Título del módulo</span>
        <span class="accordion__meta">Quizzes · audio · 5 min</span>
      </summary>
      <div class="accordion__body">
        <!-- Contenido normal: párrafos, imágenes, callouts, quizzes, SVG... -->
      </div>
    </details>

    <details class="accordion__item" id="anchor-2">
      <summary>
        <span class="accordion__num">1.2</span>
        <span class="accordion__title-main">Otro módulo</span>
        <span class="accordion__meta">3 min</span>
      </summary>
      <div class="accordion__body">…</div>
    </details>

    <!-- N módulos más -->
  </div>
</div>
```

**Reglas para el markup:**

| Regla | Por qué |
|---|---|
| `data-progress-key` debe ser único por capítulo (ej. `maestro-cap2-que-es`) | Es la key de `localStorage`. Si dos capítulos comparten key, comparten avance |
| Solo UN `<details>` con `open` al inicio | Define qué módulo se muestra al cargar la página |
| `id` único por módulo | Permite deep-linking (`/que-es.html#sistema` abre directamente ese módulo) |
| El `<summary>` debe tener `.accordion__num`, `.accordion__title-main`, `.accordion__meta` | El JS los replica al sidebar y al panel header |
| Numerar `N.M` por convención (capítulo.módulo) | Da contexto inmediato al lector |
| No incluir botones "Expandir/Colapsar todos" | El layout es tab, no acordeón. El JS los remueve si los encuentra |

### 17.4 Comportamiento JS automático

`assets/interactive.js` expone `initLessonTabs()` que se ejecuta sobre cada
`.lesson-tabs` automáticamente al cargar la página:

1. **Lee `localStorage`** con la key `mi-compania-lessons::<data-progress-key>` →
   array de IDs de módulos completados.
2. **Construye el header** con progreso (`N de M módulos · X%`) + botón "Reiniciar".
3. **Construye el sidebar** clonando los datos de cada `<summary>` como botones
   clickeables.
4. **Mueve los `<details>` originales** dentro del panel principal. La visibilidad
   de cada uno la controla el atributo `open` (mutual exclusion: solo uno
   abierto a la vez).
5. **Conecta eventos**: click en sidebar item, botones `← Anterior` y
   `✓ Marcar y continuar`, hover sobre check para desmarcar.
6. **Si la URL incluye un hash** que coincide con el `id` de un módulo, abre
   ese módulo en lugar del primer `[open]`.

### 17.5 Estados visuales y semántica

- **Activo**: el módulo `[open]` actual. CSS aplica borde lateral azul y badge
  azul con icono `▶`. Solo uno a la vez.
- **Completado**: añadido al set `completed`. CSS aplica badge verde con `✓`.
  Persistente entre visitas.
- **Pendiente**: estado por defecto. Badge gris con el número.
- **Hover sobre badge completado**: cambia a rojo con `×` → click desmarca.

Transiciones:
```
Pendiente → click sidebar → Activo
Activo → click "✓ Marcar y continuar" → Completado + abre siguiente como Activo
Completado → click sidebar → Activo (sigue completado al fondo)
Completado → click sobre badge ✓ → Pendiente
```

### 17.6 Tracking de avance (localStorage)

- **Storage key**: `mi-compania-lessons::<data-progress-key>`
- **Formato**: array JSON de IDs de módulos completados.
- **Scope**: por navegador y por usuario; no se sincroniza con servidor.
- **Privacidad**: el botón "Reiniciar" exige `confirm()` antes de borrar.
- **Degradación**: si `localStorage` está bloqueado, el componente sigue
  funcionando pero sin persistir avance entre sesiones.

Convención de naming para `data-progress-key`:

| Manual | Patrón | Ejemplos |
|---|---|---|
| Manual Maestro | `maestro-capN-<slug>` | `maestro-cap2-que-es`, `maestro-cap4-proceso` |
| Estándar A | `estandar-a-<seccion>` | `estandar-a-elemento-1`, `estandar-a-elemento-2` |

### 17.7 Audio narration con mini-bar flotante

Patrón complementario para **UDL (Universal Design for Learning)**: cualquier
módulo extenso puede tener una narración alternativa al texto. El componente
es independiente del lesson-tabs pero se integra dentro del `.accordion__body`.

**Markup:**

```html
<div class="audio-narration">
  <div class="audio-narration__header">
    <button class="audio-narration__toggle" type="button"
            aria-expanded="false" aria-controls="audio-X">
      Escuchar esta sección
    </button>
    <span class="audio-narration__meta">2 min 30 seg · voz Alice · narración alternativa al texto</span>
  </div>
  <div class="audio-narration__player" id="audio-X" hidden>
    <audio controls preload="none">
      <source src="../media/audio-X.mp3" type="audio/mpeg" />
      Tu navegador no soporta audio HTML5. <a href="../media/audio-X.mp3">Descarga el archivo MP3</a>.
    </audio>
  </div>
  <details class="audio-narration__transcript">
    <summary>Ver transcripción</summary>
    <div class="audio-narration__transcript-body">
      <!-- Transcripción limpia del audio, sin tags SSML -->
    </div>
  </details>
</div>
```

**Comportamiento:**

- El botón `Toggle` **solo muestra/oculta** el reproductor visual. Nunca pausa
  el audio (decisión deliberada: muchos usuarios lo confundían con pause).
- Click → cambia texto a "Ocultar reproductor".
- `audio.ended` restablece el estado inicial.
- **Mini-bar flotante**: aparece automáticamente al hacer scroll fuera del
  contenedor mientras el audio se reproduce. Permite pausar y volver al
  reproductor original con scroll suave. `IntersectionObserver` detecta
  visibilidad.
- El botón `×` del mini-bar pausa el audio y oculta el bar.
- Mobile (<560px): bar full-width abajo. Desktop: pill centrado abajo.

**Voz y guion:**

- Generación: **ElevenLabs Multilingual v2** (`scripts/tts-elevenlabs.ps1`).
- Voz por defecto: **Alice** (`Xb7hH8MSUJpSbSDYk0k2`), "Clear, Engaging Educator".
- Idioma: español de México.
- SSML soportado: `<break time>`, `<emphasis>`, prosody básico.
- **Pronunciación "mipyme"**: escribir en SSML en minúscula (`mipyme`,
  `mipymes`) para forzar lectura como palabra, no acrónimo deletreado.
- Capacidad ElevenLabs free: ~10,000 chars/mes; planificar.
- Scripts viven en `media/scripts/*.txt` (SSML), audios en `media/audio-*.mp3`.

### 17.8 Accesibilidad, print y mobile

| Aspecto | Comportamiento |
|---|---|
| **Ctrl+F** | Funciona en TODOS los módulos (texto en DOM, no oculto por JS) |
| **Screen reader** | Cada item del sidebar es `<button>` con `aria-controls` al `<details>` correspondiente. El header tiene `role="progressbar"` con `aria-valuenow` actualizado |
| **Keyboard** | Tab navega los items del sidebar; Enter/Space activa; Tab continúa en el panel |
| **`@media print`** | Esconde header + sidebar + footer; expande TODOS los módulos como flujo lineal con `<summary>` visible |
| **Mobile <900px** | Sidebar pasa a stack vertical arriba del panel. Padding reducido |
| **`prefers-reduced-motion`** | Animaciones de transición desactivadas, pero la funcionalidad intacta |

### 17.9 Decisiones de UX consolidadas

1. **TOC clásico arriba se elimina** cuando se usa `.lesson-tabs`. El sidebar
   cumple esa función con valor añadido (estados de avance).
2. **El click en un módulo del sidebar marca como activo, NO como completado**.
   El completado requiere acción explícita (botón "Marcar y continuar") para
   no inflar falsamente el avance.
3. **Solo un módulo abierto a la vez** (mutual exclusion). Reduce carga
   cognitiva. Para imprimir o leer todo de corrido, `@media print` expone todo.
4. **`open` inicial en el primer módulo** del primer capítulo de cada manual.
   Los capítulos posteriores también abren su primer módulo, pero el usuario
   puede preferir saltar a uno específico vía hash.
5. **Sin barra global de navegación entre capítulos dentro del lesson-tabs**.
   La navegación entre capítulos se maneja vía:
   - sub-nav del manual (top, persistente)
   - `<section id="siguiente">` al final de cada página (link al cap siguiente)
6. **Reiniciar requiere confirm**. Borrar el avance es destructivo desde la
   perspectiva del usuario.

### 17.10 Antipatrones (qué NO hacer)

| ❌ Antipatrón | ✅ En lugar de eso |
|---|---|
| Anidar `lesson-tabs` dentro de `lesson-tabs` | Un capítulo = un `.lesson-tabs`. Si necesitas sub-temas, usa Tabs ARIA o accordion FAQ dentro del módulo |
| Reusar el mismo `data-progress-key` en dos páginas | Cada capítulo único debe tener key única, si no, el avance se mezcla |
| Poner contenido importante FUERA del `lesson-tabs` (entre el header y el wrapper) | El usuario tab-navegando puede perderlo. Si es contexto general, ponlo en el hero o en el primer módulo |
| Usar `lesson-tabs` para una página con solo 2 módulos | Sobrecarga visual. Para 2 módulos, prosa lineal o tabs horizontales bastan |
| Marcar todos los módulos como completados automáticamente al cargar | Falsea el progreso del usuario. La marca solo se aplica con su acción explícita |
| Eliminar el `<summary>` de los `<details>` originales pensando que el sidebar reemplaza | El `<summary>` sigue siendo necesario para Ctrl+F, print y screen readers. El JS lo oculta visualmente vía CSS, no del DOM |

### 17.11 Páginas que actualmente implementan este patrón

- `maestro/que-es.html` — 6 módulos (Cap 2)
- `maestro/como-se-evalua.html` — 4 módulos (Cap 3)
- `maestro/proceso.html` — 7 módulos (mapa + 6 pasos, Cap 4)
- `maestro/cuatro-estandares.html` — 4 módulos (Cap 5)
- `estandar-a/elemento-1.html` — 7 módulos
- `estandar-a/elemento-2.html` — 7 módulos
- `estandar-a/elemento-3.html` — 7 módulos

> **Cuando agregues un nuevo capítulo extenso al manual, considera si debe
> heredar este patrón. Si lo aplicas, recuerda asignar un `data-progress-key`
> único y actualizar esta lista.**
