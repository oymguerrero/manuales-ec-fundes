"""Convierte las plantillas HTML con extensión .doc/.xls a OOXML real.

Uso:
    python scripts/convert-legacy-office.py

Genera .docx/.xlsx, actualiza los enlaces HTML del sitio y elimina únicamente
los archivos fuente legacy que se convirtieron correctamente.
"""

from pathlib import Path
import re

from bs4 import BeautifulSoup, NavigableString, Tag
from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIRS = [ROOT / f"estandar-{letter}" / "templates" for letter in "abcd"]

# Sistema de diseño Mi CompañIA (design.md §2.1 paleta oficial, §3.1 tipografía).
# python-docx arranca con el tema por omisión de Office (Calibri + azules
# #4F81BD), así que hay que fijar tipografía, color y espaciado a mano o los
# archivos descargables no se parecen al sitio.
#
# Tipografía: el sitio usa Afacad, pero un .docx no lleva la fuente consigo y
# casi nadie la tiene instalada. Word sustituiría por lo que encontrara y la
# composición se rompería en la máquina de quien descarga. Calibri viene con
# Office en Windows y en Mac desde 2007, y donde no está —LibreOffice, Google
# Docs— se sustituye por Carlito, que es métricamente idéntica: el documento se
# ve igual en cualquier parte. La identidad Mi CompañIA la sostienen aquí la
# paleta, la jerarquía y la composición, no el tipo de letra.
FUENTE = "Calibri"

AZUL_PROFUNDO = "28467E"   # --color-azul-profundo · títulos y encabezados
AZUL_CLARO = "529ED7"      # --color-azul-claro · antetítulo
GRIS_TEXTO = "4B5563"      # --color-gris-texto · cuerpo
AMARILLO = "F7C031"        # --color-amarillo · filete del título
BORDE_TABLA = "C9D3E4"     # azul profundo desaturado: rejilla visible sin pesar
BANDA_TABLA = "F3F6FB"     # banda alterna, tenue para no competir con el texto

# Jerarquía tipográfica: (estilo, tamaño pt, espacio antes pt, espacio después pt).
JERARQUIA = (
    ("Title", 20, 0, 4),
    ("Heading 1", 14, 18, 6),
    ("Heading 2", 11.5, 14, 4),
    ("Heading 3", 10.5, 12, 3),
)

# El esquema OOXML fija el orden de los hijos: w:pBdr, w:shd y w:tblCellMar no
# van al final de su padre. Estas tuplas son los hermanos que deben quedar
# después, para insert_element_before.
TRAS_PBDR = (
    "w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
    "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
    "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
    "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
    "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl",
    "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange",
)
TRAS_SHD_CELDA = (
    "w:noWrap", "w:tcMar", "w:textDirection", "w:tcFitText", "w:vAlign",
    "w:hideMark", "w:headers", "w:tcPrChange",
)
TRAS_BORDES_TABLA = ("w:shd", "w:tblLayout", "w:tblCellMar", "w:tblLook",
                     "w:tblCaption", "w:tblDescription", "w:tblPrChange")
TRAS_MARGEN_TABLA = ("w:tblLook", "w:tblCaption", "w:tblDescription",
                     "w:tblPrChange")


def _fijar_fuente(style, nombre):
    """style.font.name solo escribe w:ascii; hay que cubrir las demás variantes."""
    style.font.name = nombre
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), nombre)


def _filete(parrafo, lado, color, grosor=6, espacio=6):
    """Línea sobre o bajo un párrafo. En OOXML el borde vive en w:pBdr."""
    pPr = parrafo._p.get_or_add_pPr()
    bordes = pPr.find(qn("w:pBdr"))
    if bordes is None:
        bordes = OxmlElement("w:pBdr")
        pPr.insert_element_before(bordes, *TRAS_PBDR)
    linea = OxmlElement("w:%s" % lado)
    linea.set(qn("w:val"), "single")
    linea.set(qn("w:sz"), str(grosor))
    linea.set(qn("w:space"), str(espacio))
    linea.set(qn("w:color"), color)
    bordes.append(linea)


def aplicar_marca(document):
    """Tipografía, paleta y ritmo vertical del sistema de diseño."""
    normal = document.styles["Normal"]
    _fijar_fuente(normal, FUENTE)
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor.from_string(GRIS_TEXTO)
    formato = normal.paragraph_format
    formato.line_spacing = 1.15
    formato.space_after = Pt(8)
    formato.widow_control = True

    for nombre, tam, antes, despues in JERARQUIA:
        try:
            estilo = document.styles[nombre]
        except KeyError:
            continue
        _fijar_fuente(estilo, FUENTE)
        estilo.font.size = Pt(tam)
        estilo.font.bold = True
        estilo.font.color.rgb = RGBColor.from_string(AZUL_PROFUNDO)
        formato = estilo.paragraph_format
        formato.space_before = Pt(antes)
        formato.space_after = Pt(despues)
        formato.line_spacing = 1.1
        # Un título solo al pie de la página deja al lector sin su contenido.
        formato.keep_with_next = True

    for nombre in ("List Bullet", "List Number"):
        try:
            estilo = document.styles[nombre]
        except KeyError:
            continue
        _fijar_fuente(estilo, FUENTE)
        estilo.font.size = Pt(10.5)
        estilo.font.color.rgb = RGBColor.from_string(GRIS_TEXTO)
        estilo.paragraph_format.space_after = Pt(3)
        estilo.paragraph_format.line_spacing = 1.15


def aplicar_marca_excel(workbook):
    """openpyxl arranca en Calibri 11; el estilo Normal es lo que hereda todo."""
    try:
        workbook._named_styles["Normal"].font = Font(
            name=FUENTE, size=10.5, color=GRIS_TEXTO)
    except (AttributeError, KeyError):
        pass


def preparar_pagina(document):
    """Márgenes y pie: medida cómoda de lectura para un cuerpo de 10.5 pt."""
    seccion = document.sections[0]
    seccion.top_margin = Inches(0.8)
    seccion.bottom_margin = Inches(0.75)
    seccion.left_margin = Inches(0.8)
    seccion.right_margin = Inches(0.8)
    seccion.footer_distance = Inches(0.4)
    return seccion


def _campo_pagina(run):
    """Campo PAGE: tres nodos —inicio, instrucción y fin— dentro del run."""
    inicio = OxmlElement("w:fldChar")
    inicio.set(qn("w:fldCharType"), "begin")
    instruccion = OxmlElement("w:instrText")
    instruccion.set(qn("xml:space"), "preserve")
    instruccion.text = " PAGE "
    fin = OxmlElement("w:fldChar")
    fin.set(qn("w:fldCharType"), "end")
    for nodo in (inicio, instruccion, fin):
        run._r.append(nodo)


def pie_de_pagina(document):
    """Pie de marca con numeración: ubica la hoja cuando se imprime suelta."""
    seccion = document.sections[0]
    parrafo = seccion.footer.paragraphs[0]
    parrafo.text = ""
    ancho = seccion.page_width - seccion.left_margin - seccion.right_margin
    parrafo.paragraph_format.tab_stops.add_tab_stop(ancho, WD_TAB_ALIGNMENT.RIGHT)
    parrafo.paragraph_format.space_before = Pt(6)
    parrafo.paragraph_format.space_after = Pt(0)
    parrafo.add_run("Mi CompañIA · FUNDES México + Google.org	")
    parrafo.add_run("Página ")
    _campo_pagina(parrafo.add_run())
    for run in parrafo.runs:
        run.font.name = FUENTE
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor.from_string(GRIS_TEXTO)
    _filete(parrafo, "top", BORDE_TABLA, grosor=4, espacio=4)


def portada(document, titulo, antetitulo=None):
    """Antetítulo breve + título con filete amarillo, como el hero del sitio."""
    if antetitulo:
        linea = document.add_paragraph()
        linea.paragraph_format.space_after = Pt(2)
        run = linea.add_run(antetitulo.upper())
        run.bold = True
        run.font.name = FUENTE
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor.from_string(AZUL_CLARO)
    parrafo = document.add_heading(titulo, 0)
    parrafo.alignment = WD_ALIGN_PARAGRAPH.LEFT
    _filete(parrafo, "bottom", AMARILLO, grosor=12, espacio=6)
    parrafo.paragraph_format.space_after = Pt(14)
    return parrafo


def sombrear_celda(celda, relleno):
    tcPr = celda._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), relleno)
    tcPr.insert_element_before(shd, *TRAS_SHD_CELDA)


def encabezar_fila(celdas):
    """Fila de encabezado: fondo azul profundo y texto blanco, como en el sitio."""
    for celda in celdas:
        sombrear_celda(celda, AZUL_PROFUNDO)
        for parrafo in celda.paragraphs:
            for run in parrafo.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)


def _repetir_encabezado(fila):
    """Que el encabezado reaparezca al cortarse la tabla entre páginas."""
    trPr = fila._tr.get_or_add_trPr()
    for etiqueta in ("w:cantSplit", "w:tblHeader"):
        el = OxmlElement(etiqueta)
        el.set(qn("w:val"), "true")
        trPr.append(el)


def _rejilla(table, color):
    bordes = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        linea = OxmlElement("w:%s" % lado)
        linea.set(qn("w:val"), "single")
        linea.set(qn("w:sz"), "4")
        linea.set(qn("w:space"), "0")
        linea.set(qn("w:color"), color)
        bordes.append(linea)
    table._tbl.tblPr.insert_element_before(bordes, *TRAS_BORDES_TABLA)


def _aire_en_celdas(table, horizontal=108, vertical=60):
    """Sin esto el texto toca el filete. La unidad dxa es 1/20 de punto."""
    margenes = OxmlElement("w:tblCellMar")
    for lado, valor in (("top", vertical), ("left", horizontal),
                        ("bottom", vertical), ("right", horizontal)):
        el = OxmlElement("w:%s" % lado)
        el.set(qn("w:w"), str(valor))
        el.set(qn("w:type"), "dxa")
        margenes.append(el)
    table._tbl.tblPr.insert_element_before(margenes, *TRAS_MARGEN_TABLA)


def estilizar_tabla(table, filas_encabezado=(0,)):
    """Rejilla tenue, aire, bandas alternas y encabezado que se repite."""
    table.style = "Table Grid"
    _rejilla(table, BORDE_TABLA)
    _aire_en_celdas(table)
    encabezados = set(filas_encabezado)
    for indice, fila in enumerate(table.rows):
        if indice not in encabezados and indice % 2 == 0:
            for celda in fila.cells:
                sombrear_celda(celda, BANDA_TABLA)
        for celda in fila.cells:
            celda.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            for parrafo in celda.paragraphs:
                formato = parrafo.paragraph_format
                formato.space_before = Pt(0)
                formato.space_after = Pt(2)
                formato.line_spacing = 1.0
                for run in parrafo.runs:
                    run.font.size = Pt(9.5)
    if 0 in encabezados and len(table.rows):
        _repetir_encabezado(table.rows[0])


def antetitulo(ruta):
    """'Plantilla de trabajo · Estándar A', deducido de la carpeta contenedora."""
    carpeta = ruta.parent.parent.name
    if carpeta.startswith("estandar-") and len(carpeta) == len("estandar-x"):
        return "Plantilla de trabajo · Estándar %s" % carpeta[-1].upper()
    return "Plantilla de trabajo"


def fijar_anchos(table, anchos):
    """Word ignora el ancho de columna si no está repetido en cada celda."""
    table.autofit = False
    for fila in table.rows:
        for celda, ancho in zip(fila.cells, anchos):
            celda.width = ancho


def clean_text(node):
    return " ".join(node.get_text(" ", strip=True).split())


def provisional_language(markup):
    """Evita presentar los insumos de trabajo como estándares ya publicados."""
    replacements = {
        "Qué evalúa el F21 oficial": "Referencia de trabajo del F21",
        "F21 oficial": "versión de trabajo del F21",
        "documento oficial del estándar": "documento de trabajo de la propuesta",
        "documento oficial": "documento de trabajo",
        "glosario oficial": "glosario de trabajo",
        "estándar publicado por CONOCER": "propuesta de estándar aún no publicada",
    }
    for original, replacement in replacements.items():
        markup = markup.replace(original, replacement)
    return markup


def convert_doc(source):
    soup = BeautifulSoup(provisional_language(source.read_text(encoding="utf-8")), "html.parser")
    document = Document()
    preparar_pagina(document)
    aplicar_marca(document)
    pie_de_pagina(document)
    title = soup.find("h1")
    if title:
        portada(document, clean_text(title), antetitulo(source))

    body = soup.body or soup
    handled = {id(title)} if title else set()
    for node in body.find_all(["h1", "h2", "h3", "h4", "p", "li", "table"], recursive=True):
        if id(node) in handled or node.find_parent("table"):
            continue
        text = clean_text(node)
        if not text and node.name != "table":
            continue
        if node.name.startswith("h"):
            level = min(max(int(node.name[1]) - 1, 1), 3)
            document.add_heading(text, level=level)
        elif node.name == "li":
            document.add_paragraph(text, style="List Bullet")
        elif node.name == "p":
            document.add_paragraph(text)
        elif node.name == "table":
            rows = node.find_all("tr")
            width = max((len(row.find_all(["th", "td"], recursive=False)) for row in rows), default=1)
            table = document.add_table(rows=0, cols=width)
            encabezados = []
            for row_index, row in enumerate(rows):
                cells = row.find_all(["th", "td"], recursive=False)
                target = table.add_row().cells
                encabezado = False
                for index, cell in enumerate(cells):
                    target[index].text = clean_text(cell)
                    if row_index == 0 or cell.name == "th":
                        encabezado = True
                if encabezado:
                    encabezar_fila(target[: len(cells)])
                    encabezados.append(row_index)
            estilizar_tabla(table, encabezados)

    target = source.with_suffix(".docx")
    document.save(target)
    return target


def safe_sheet_name(name, used):
    base = re.sub(r"[\\/*?:\[\]]", " ", name).strip()[:31] or "Tabla"
    candidate = base
    number = 2
    while candidate in used:
        suffix = f" {number}"
        candidate = base[: 31 - len(suffix)] + suffix
        number += 1
    used.add(candidate)
    return candidate


def convert_xls(source):
    soup = BeautifulSoup(provisional_language(source.read_text(encoding="utf-8")), "html.parser")
    workbook = Workbook()
    aplicar_marca_excel(workbook)
    workbook.remove(workbook.active)
    used = set()
    tables = soup.find_all("table")
    for index, table in enumerate(tables, 1):
        heading = table.find_previous(["h1", "h2", "h3", "h4"])
        name = clean_text(heading) if heading else f"Tabla {index}"
        sheet = workbook.create_sheet(safe_sheet_name(name, used))
        filete = Side(style="thin", color=BORDE_TABLA)
        rejilla = Border(left=filete, right=filete, top=filete, bottom=filete)
        banda = PatternFill("solid", fgColor=BANDA_TABLA)
        for row_index, row in enumerate(table.find_all("tr"), 1):
            cells = row.find_all(["th", "td"], recursive=False)
            for col_index, cell in enumerate(cells, 1):
                target = sheet.cell(row=row_index, column=col_index, value=clean_text(cell))
                target.alignment = Alignment(vertical="top", wrap_text=True)
                target.border = rejilla
                if row_index == 1 or cell.name == "th":
                    target.font = Font(name=FUENTE, size=10.5, bold=True, color="FFFFFF")
                    target.fill = PatternFill("solid", fgColor=AZUL_PROFUNDO)
                    target.alignment = Alignment(vertical="center", wrap_text=True)
                elif row_index % 2:
                    target.fill = banda
        sheet.freeze_panes = "A2"
        sheet.row_dimensions[1].height = 30
        # Al imprimir varias páginas, el encabezado se repite arriba de cada una.
        sheet.print_title_rows = "1:1"
        for column in range(1, sheet.max_column + 1):
            values = [str(sheet.cell(row=row, column=column).value or "") for row in range(1, sheet.max_row + 1)]
            sheet.column_dimensions[get_column_letter(column)].width = min(max(max(map(len, values), default=10) + 2, 12), 42)
    if not tables:
        sheet = workbook.create_sheet("Plantilla")
        sheet["A1"] = clean_text(soup)
        sheet["A1"].alignment = Alignment(wrap_text=True, vertical="top")
        sheet.column_dimensions["A"].width = 80
    target = source.with_suffix(".xlsx")
    workbook.save(target)
    return target


def update_links(mapping):
    replacements = {old.name: new.name for old, new in mapping.items()}
    for html in ROOT.rglob("*.html"):
        if "extras" in html.parts:
            continue
        original = html.read_text(encoding="utf-8")
        updated = original
        for old_name, new_name in replacements.items():
            updated = re.sub(re.escape(old_name) + r"(?!x)", new_name, updated)
        # Repara ejecuciones antiguas no idempotentes (.docxx/.xlsxx, etc.).
        updated = re.sub(r"\.docx+\b", ".docx", updated, flags=re.I)
        updated = re.sub(r"\.xlsx+\b", ".xlsx", updated, flags=re.I)
        if updated != original:
            html.write_text(updated, encoding="utf-8")


def build_checklist(path, title, entries, eyebrow="Plantilla de trabajo"):
    document = Document()
    preparar_pagina(document)
    aplicar_marca(document)
    pie_de_pagina(document)
    portada(document, title, eyebrow)
    document.add_paragraph(
        "Material de autoevaluación basado en documentos de trabajo. "
        "Revisa la versión oficial cuando el estándar sea aprobado y publicado."
    )
    table = document.add_table(rows=1, cols=4)
    headings = ["Criterio o evidencia", "Preparado", "Por reforzar", "Notas / ubicación de evidencia"]
    for index, heading in enumerate(headings):
        table.rows[0].cells[index].text = heading
    encabezar_fila(table.rows[0].cells)
    for entry in entries:
        cells = table.add_row().cells
        cells[0].text = entry
        cells[1].text = "☐"
        cells[2].text = "☐"
        cells[3].text = ""
    estilizar_tabla(table)
    # El criterio es texto largo y las dos casillas no necesitan más que su
    # ancho: sin anchos fijos Word reparte las cuatro columnas por igual.
    fijar_anchos(table, [Inches(3.6), Inches(0.85), Inches(0.95), Inches(1.5)])
    for fila in table.rows:
        for celda in fila.cells[1:3]:
            celda.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.save(path)


def generate_c_checklists():
    directory = ROOT / "estandar-c" / "templates"
    route = BeautifulSoup((ROOT / "estandar-c" / "ruta-preparacion.html").read_text(encoding="utf-8"), "html.parser")
    product_entries = []
    for label in route.select('.printable-checklist label'):
        value = clean_text(label)
        if value.startswith("Producto "):
            product_entries.append(value)
    performance_entries = [
        "Desempeño 1.1 · Validar la estrategia de contenido con la persona responsable de la MiPyME",
        "Desempeño 2.1 · Generar contenido de texto con IA",
        "Desempeño 2.2 · Generar contenido de imagen con IA",
        "Desempeño 2.3 · Generar contenido de audio con IA",
        "Desempeño 2.4 · Generar contenido de video con IA",
        "Desempeño 3.1 · Publicar contenido en plataformas y documentar la implementación",
        "Desempeño 3.2 · Habilitar al personal responsable para operar el proceso",
        "Desempeño 4.1 · Presentar resultados, recomendaciones y obtener validación",
    ]
    eyebrow = "Plantilla de trabajo · Estándar C"
    build_checklist(directory / "checklist-productos.docx",
                    "Checklist de productos · Ruta C", product_entries, eyebrow)
    build_checklist(directory / "checklist-desempenos.docx",
                    "Checklist de desempeños · Ruta C", performance_entries, eyebrow)


def main():
    mapping = {}
    for directory in TEMPLATE_DIRS:
        for source in sorted(directory.glob("*.doc")):
            mapping[source] = convert_doc(source)
        for source in sorted(directory.glob("*.xls")):
            mapping[source] = convert_xls(source)
    update_links(mapping)
    generate_c_checklists()
    for source, target in mapping.items():
        if target.exists() and target.stat().st_size > 0:
            source.unlink()
            print(f"[ok] {source.relative_to(ROOT)} -> {target.name}")
    print(f"Convertidas {len(mapping)} plantillas a OOXML real.")


if __name__ == "__main__":
    main()
