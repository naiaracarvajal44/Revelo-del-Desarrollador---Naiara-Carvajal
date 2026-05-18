"""
Módulo de Persistencia - Sistema de Gestión de Instituto (SGI).

Este modulo se encarga de implementar el parseo y la 
exportación de datos.
"""

from modelos import Alumno, Profesor
from utilidades import parsear_notas, validar_email

def crear_persona_desde_campos(campos: list) -> Alumno | Profesor | None:
    """
    Se encarga de crear una lista con los datos que se vayan generado.

    Args:
        campos (list): Segmentos de texto extraídos de una línea del archivo CSV.

    Returns:
        Alumno | Profesor | None: Instancia de objeto o None si los datos están corruptos.
    """
    if not campos:
        return None

    tipo = campos[0].strip()

    try:
        if tipo == "A":
            # POR QUÉ: Validamos la longitud mínima de las columnas antes de indexar.
            # Si el CSV tuviera filas incompletas, lanzaríamos un IndexError si no pusiéramos esto.
            if len(campos) < 6:
                raise ValueError("Estructura de Alumno incompleta: faltan campos obligatorios.")

            nombre = campos[1].strip()
            email = campos[2].strip()
            telefono = campos[3].strip()
            grupo = campos[4].strip()
            notas = parsear_notas(campos[5])

            if not validar_email(email):
                print(f"[AVISO]: Formato de email inválido para el Alumno: '{email}'")

            return Alumno(nombre, email, telefono, grupo, notas)

        elif tipo == "P":
            if len(campos) < 6:
                raise ValueError("Estructura de Profesor incompleta: faltan campos obligatorios.")

            nombre = campos[1].strip()
            email = campos[2].strip()
            telefono = campos[3].strip()
            departamento = campos[4].strip()
            salario = campos[5].strip()  # El constructor de Profesor ya se encarga de pasarlo a float de forma segura.

            if not validar_email(email):
                print(f"[AVISO]: Formato de email inválido para el Profesor: '{email}'")

            return Profesor(nombre, email, telefono, departamento, salario)

        else:
            raise ValueError(f"Identificador de registro desconocido: '{tipo}'")

    except ValueError as e:
        # POR QUÉ: Imprimimos el error para facilitar la depuración por consola al desarrollador
        # y propagamos la excepción hacia arriba para que la capa superior decida cómo gestionarla.
        print(f"[ERROR de Parseo]: Falló la conversión de la línea. Detalles: {e}")
        raise

def cargar_desde_csv(ruta: str, separador: str = ",", encoding: str = "utf-8-sig") -> list:
    """
    Lee un archivo CSV.

    Args:
        ruta (str): Ubicación física del archivo de datos.
        separador (str): Delimitador de columnas. Por defecto es ','.
        encoding (str): Codificación de caracteres. Usa 'utf-8-sig'.

    Returns:
        list: Colección de objetos de tipo Persona (Alumnos o Profesores) procesados con éxito.
    """
    personas = []
    
    # POR QUÉ: Abrimos el archivo con 'with open'.
    # Esto garantiza que el puntero del archivo sea liberado por el sistema operativo
    # de forma inmediata si el bucle falla o se interrumpe, evitando fugas de memoria.
    try:
        with open(ruta, "r", encoding=encoding) as f:
            lineas = f.readlines()
    except FileNotFoundError as e:
        print(f"Error de estructura: No se encontró el archivo de datos en '{ruta}'.")
        raise e
    except PermissionError as e:
        print(f"Error de Seguridad: Permisos del sistema denegados para leer '{ruta}'.")
        raise e

    for num_linea, linea in enumerate(lineas, start=1):
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue  # Salta líneas en blanco de forma segura sin romper el iterador.
            
        campos = linea_limpia.split(separador)
        
        try:
            p = crear_persona_desde_campos(campos)
            if p is not None:
                personas.append(p)
        except ValueError:
            print(f"[Alerta]: Saltando línea {num_linea} debido a errores en sus datos.")
            continue

    return personas

def exportar_resumen(personas: list, ruta_salida: str) -> None:
    """
    Serializa los datos y los exporta a un reporte estructurado.

    Args:
        personas (list): Colección de objetos que heredan de Persona.
        ruta_salida (str): Ruta donde se guardará el nuevo archivo CSV resultante.
    """
    # Definición de la cabecera del CSV de salida
    cabecera = "tipo;nombre;email;grupo_o_departamento;metrica_financiera_o_academica\n"
    
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(cabecera)
        for p in personas:
            if isinstance(p, Alumno):
                # POR QUÉ: Al exportar llamamos al método .media(). Al ser un cálculo síncrono
                # guardamos la foto fija del rendimiento del alumno en el reporte resultante.
                linea = f"A;{p.nombre};{p.email};{p.grupo};{p.media():.2f}\n"
            elif isinstance(p, Profesor):
                linea = f"P;{p.nombre};{p.email};{p.departamento};{p.salario:.2f}\n"
            else:
                linea = f"?;{p.nombre};{p.email};-;- \n"
            
            f.write(linea)
