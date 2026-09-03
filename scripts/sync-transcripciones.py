# -*- coding: utf-8 -*-
"""
Sincroniza las transcripciones de las paginas con el guion de cada audio.

La etiqueta de la UI dice "Ver transcripcion", pero en 11 de 23 casos lo que
habia era un resumen corto: el audio del Elemento 2 del Estandar C dura 2:11 y
la pagina lo resumia en 60 palabras. Una transcripcion tiene que ser el texto
literal de lo que se escucha, o no sirve como alternativa textual.

Regla unica: el cuerpo de .audio-narration__transcript-body se reemplaza por el
texto de media/scripts/<nombre>.txt, sin las etiquetas SSML que algunos guiones
usan para marcar pausas (<speak>, <break/>, <emphasis>).

Uso:  python scripts/sync-transcripciones.py [--dry-run]
"""
import glob, io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = '<div class="audio-narration__transcript-body">'


def fallar(msg):
    raise SystemExit("ERROR: " + msg)


def texto_del_guion(ruta):
    """Guion -> lista de parrafos, sin SSML."""
    t = io.open(ruta, encoding="utf-8").read()
    t = re.sub(r"<break[^>]*/?>", " ", t)          # pausas: no se leen
    t = re.sub(r"</?(speak|emphasis|prosody|say-as|sub)[^>]*>", "", t)
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    parrafos = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", t)]
    return [p for p in parrafos if p]


def cuerpo(html, desde, archivo):
    """Devuelve (inicio, fin) del contenido interno del transcript-body."""
    i = html.find(MARCA, desde)
    if i < 0:
        return None
    ini = i + len(MARCA)
    fin_details = html.find("</details>", ini)
    region = html[ini:fin_details]
    if "<div" in region:
        fallar("%s: el transcript-body tiene divs anidados, revisalo a mano" % archivo)
    fin = html.rfind("</div>", ini, fin_details)
    if fin < 0:
        fallar("%s: no cierra el transcript-body" % archivo)
    return ini, fin


def main():
    seco = "--dry-run" in sys.argv
    cambios, iguales, sin_guion = 0, 0, []

    for pagina in sorted(glob.glob(os.path.join(RAIZ, "*", "*.html"))):
        if os.sep + "extras" + os.sep in pagina:
            continue
        html = io.open(pagina, encoding="utf-8").read()
        if MARCA not in html:
            continue
        nuevo = html
        desplazamiento = 0
        for m in re.finditer(r'<source src="\.\./media/([a-z0-9-]+)\.mp3"', html):
            nombre = m.group(1).replace("audio-", "", 1)
            guion = os.path.join(RAIZ, "media", "scripts", nombre + ".txt")
            if not os.path.exists(guion):
                sin_guion.append((os.path.basename(pagina), nombre))
                continue
            rango = cuerpo(nuevo, m.start() + desplazamiento, os.path.basename(pagina))
            if not rango:
                continue
            ini, fin = rango
            actual = nuevo[ini:fin]
            reemplazo = "\n" + "\n".join(
                "            <p>%s</p>" % p for p in texto_del_guion(guion)) + "\n          "
            if actual == reemplazo:
                iguales += 1
                continue
            nuevo = nuevo[:ini] + reemplazo + nuevo[fin:]
            desplazamiento += len(reemplazo) - len(actual)
            cambios += 1
            print("  %-30s %-30s %5d -> %5d car" % (
                os.path.relpath(pagina, RAIZ).replace(os.sep, "/"), nombre,
                len(re.sub(r"<[^>]+>", "", actual).strip()),
                len(re.sub(r"<[^>]+>", "", reemplazo).strip())))
        if nuevo != html and not seco:
            io.open(pagina, "w", encoding="utf-8", newline="\n").write(nuevo)

    print("\n%d transcripciones actualizadas, %d ya coincidian" % (cambios, iguales))
    if sin_guion:
        print("Sin guion (no se tocaron): %s" % sin_guion)
    if seco:
        print("(dry-run: no se escribio nada)")


if __name__ == "__main__":
    main()
