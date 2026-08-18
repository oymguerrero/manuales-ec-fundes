"""Aplica mejoras semánticas repetibles sin reformatear las páginas completas."""

from html import escape
from pathlib import Path
import re

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
TABLE_RE = re.compile(r"(?P<indent>^[ \t]*)(?P<table><table\b[^>]*>.*?</table>)", re.I | re.M | re.S)


def plain_text(markup):
    return " ".join(BeautifulSoup(markup, "html.parser").get_text(" ", strip=True).split())


def preceding_heading(source, position):
    matches = list(re.finditer(r"<h[2-4]\b[^>]*>(.*?)</h[2-4]>", source[:position], re.I | re.S))
    return plain_text(matches[-1].group(1)) if matches else "Información de la unidad"


def enhance_table(table, label):
    if not re.search(r"<caption\b", table, re.I):
        table = re.sub(
            r"(<table\b[^>]*>)",
            r'\1\n<caption class="visually-hidden">' + escape(label) + "</caption>",
            table,
            count=1,
            flags=re.I,
        )
    row_number = -1

    def row_scope(row_match):
        nonlocal row_number
        row_number += 1
        cell_number = -1

        def cell_scope(cell_match):
            nonlocal cell_number
            cell_number += 1
            tag = cell_match.group(0)
            if re.search(r"\bscope=", tag, re.I):
                return tag
            scope = "col" if row_number == 0 else ("row" if cell_number == 0 else "col")
            return re.sub(r"<th\b", f'<th scope="{scope}"', tag, count=1, flags=re.I)

        return re.sub(r"<th\b[^>]*>", cell_scope, row_match.group(0), flags=re.I)

    return re.sub(r"<tr\b[^>]*>.*?</tr>", row_scope, table, flags=re.I | re.S)


def migrate(path):
    source = path.read_text(encoding="utf-8")
    updated = source
    updated = re.sub(r'\s*<h2 class="visually-hidden">Contenido de la unidad</h2>', '', updated)
    if path.as_posix().endswith("maestro/es-para-ti.html"):
        updated = updated.replace('<h4 class="process-step__title">', '<h3 class="process-step__title">')
        updated = updated.replace('</h4>', '</h3>')
    if "skip-link" not in updated and re.search(r"<main\b", updated, re.I):
        updated = re.sub(
            r"(<body\b[^>]*>)",
            r'\1\n<a class="skip-link" href="#contenido-principal">Saltar al contenido principal</a>',
            updated,
            count=1,
            flags=re.I,
        )
    main_match = re.search(r"<main\b([^>]*)>", updated, re.I)
    if main_match:
        attrs = main_match.group(1)
        if not re.search(r"\bid=", attrs, re.I):
            attrs += ' id="contenido-principal"'
        if not re.search(r"\btabindex=", attrs, re.I):
            attrs += ' tabindex="-1"'
        updated = updated[: main_match.start()] + "<main" + attrs + ">" + updated[main_match.end() :]

    def table_replace(match):
        table = match.group("table")
        if "table-scroll" in updated[max(0, match.start() - 180) : match.start()]:
            return match.group(0)
        label = "Tabla: " + preceding_heading(updated, match.start())
        enhanced = enhance_table(table, label)
        indent = match.group("indent")
        return (
            f'{indent}<div class="table-scroll" role="region" tabindex="0" aria-label="{escape(label, quote=True)}">\n'
            f"{enhanced}\n{indent}</div>"
        )

    updated = TABLE_RE.sub(table_replace, updated)
    if updated != source:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "extras" in path.parts:
            continue
        changed += migrate(path)
    print(f"Páginas migradas: {changed}")


if __name__ == "__main__":
    main()
