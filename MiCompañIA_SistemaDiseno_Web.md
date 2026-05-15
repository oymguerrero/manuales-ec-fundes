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
