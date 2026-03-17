import re
from modelos import Alumno, Profesor

def parsear_notas(texto_notas):
    if texto_notas == "":
        return []
    try:
        trozos = texto_notas.split("|")
        return [int(x) for x in trozos]
    except ValueError:
        raise ValueError("Notas no numéricas")


def validar_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return True
    else:
        return None


def buscar_por_nombre(personas, texto, modo="exacto", ignore_case=True):
    for p in personas:
        nombre = p.nombre
        if ignore_case:
            nombre = nombre.lower()
            texto = texto.lower()

        if modo == "exacto":
            if nombre == texto:
                return p
        elif modo == "parcial":
            if texto in nombre:
                return p
    return None

def resumen_general(personas):
    total = len(personas)
    alumnos = [p for p in personas if isinstance(p, Alumno)]
    profesores = [p for p in personas if isinstance(p, Profesor)]

    medias = []
    for a in alumnos:
        medias.append(a.media())
    try:
        media_global = sum(medias) / len(medias)
    except ZeroDivisionError:
        media_global = 0

    return total, len(alumnos), len(profesores), media_global