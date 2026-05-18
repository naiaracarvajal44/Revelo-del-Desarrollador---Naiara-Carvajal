"""
Módulo de Utilidades - Sistema de Gestión de Instituto (SGI).

Este módulo concentra la lógica de la aplicación.
Proporciona motores de búsqueda, validaciones sintácticas mediante
expresiones regulares y cálculos.
"""

import re
from modelos import Alumno, Profesor

def parsear_notas(texto_notas: str) -> list[int]:
    """
    Descompone una cadena de texto en una lista de calificaciones enteras.

    Args:
        texto_notas (str): Cadena extraída del CSV (ej: "8|10|5").

    Returns:
        list[int]: Colección de notas numéricas.
        
    Raises:
        ValueError: Si la cadena contiene caracteres alfabéticos o no convertibles.
    """
    if not texto_notas.strip():
        return []
        
    try:
        trozos = texto_notas.split("|")
        # POR QUÉ: Utilizamos una list comprensión para realizar el cast a entero de forma
        # compacta y eficiente en tiempo de ejecución.
        return [int(x.strip()) for x in trozos]
    except ValueError as e:
        # POR QUÉ: Enmascaramos el ValueError original con un mensaje
        # para que el desarrollador final sepa exactamente qué módulo falló.
        raise ValueError(f"Error de formato en actas: Existen calificaciones no numéricas ('{texto_notas}').") from e


def validar_email(email: str) -> bool:
    """
    Verifica si una dirección de correo electrónico cumple con el estándar sintáctico básico.

    Args:
        email (str): Cadena de texto que representa el correo a evaluar.

    Returns:
        bool: True si el formato es válido, False en caso contrario.
    """
    # POR QUÉ: Modificamos el retorno (None) por un booleano estricto (False).
    # Esto asegura la consistencia de tipos y evita fallos si la función se integra
    # en operaciones lógicas o validaciones externas de tipo 'is True'.
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(patron, email):
        return True
    return False


def buscar_por_nombre(personas: list, texto: str, modo: str = "exacto", ignore_case: bool = True) -> Alumno | Profesor | None:
    """
    Ejecuta una búsqueda secuencial en la colección de personas aplicando filtros de coincidencia.

    Args:
        personas (list): Colección de objetos de tipo Persona (Alumnos o Profesores).
        texto (str): Cadena de texto de búsqueda.
        modo (str): Estrategia de comparación ("exacto" o "parcial").
        ignore_case (bool): Si es True, normaliza los textos eliminando la distinción de mayúsculas.

    Returns:
        Alumno | Profesor | None: La primera instancia que coincida con el criterio, o None.
    """
    for p in personas:
        nombre = p.nombre
        criterio = texto
        
        # POR QUÉ: Normalizamos las cadenas convirtiéndolas a minúsculas en cada iteración
        # si ignore_case está activo. Esto previene fallos de experiencia de usuario cuando
        # se introducen nombres con acentuaciones o capitalizaciones mixtas.
        if ignore_case:
            nombre = nombre.lower()
            criterio = criterio.lower()

        if modo == "exacto":
            if nombre == criterio:
                return p
        elif modo == "parcial":
            if criterio in nombre:
                return p
                
    return None


def resumen_general(personas: list) -> tuple[int, int, int, float]:
    """
    Calcula métricas analíticas descriptivas agregadas del estado actual del instituto.

    Args:
        personas (list): Lista total de registros cargados en memoria.

    Returns:
        tuple: Contiene (total_personas, total_alumnos, total_profesores, nota_media_global).
    """
    total = len(personas)
    
    # POR QUÉ: Utilizamos el operador isinstance para filtrar por tipo en tiempo de ejecución.
    # Esto aprovecha el diseño de herencia de modelos.py de forma limpia y polimórfica.
    alumnos = [p for p in personas if isinstance(p, Alumno)]
    profesores = [p for p in personas if isinstance(p, Profesor)]

    medias = [a.media() for a in alumnos]
    
    # POR QUÉ: Capturamos explícitamente ZeroDivisionError en el cálculo final. 
    # Si la base de datos CSV está vacía o solo contiene profesores, el sistema
    # no colapsará aritméticamente y devolverá una media por defecto de 0.0.
    try:
        media_global = sum(medias) / len(medias)
    except ZeroDivisionError:
        media_global = 0.0

    return total, len(alumnos), len(profesores), media_global
