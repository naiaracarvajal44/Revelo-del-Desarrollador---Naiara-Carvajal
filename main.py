"""
Módulo Principal (Controlador CLI) - Sistema de Gestión de Instituto (SGI).

Este script actúa como controlador CLI del sistema. Se encarga
de capturar los parámetros de la línea de comandos, gestionar el flujo síncrono
entre la capa de datos y servicios, y realizar el control de excepciones de último nivel.
"""

import sys
from persistencia import cargar_desde_csv, exportar_resumen
from utilidades import buscar_por_nombre, resumen_general, validar_email

def main():
    """
    Punto de entrada único de la aplicación.
    Coordina la carga, búsqueda, validación y exportación de datos académicos.
    """
    # POR QUÉ: Validamos la longitud de argv para asegurar que el usuario ha introducido
    # los dos parámetros obligatorios. Si no lo hacemos, Python lanzaría un IndexError oculto.
    if len(sys.argv) < 3:
        print("\n Error: Faltan argumentos de ejecución.")
        print("Sintaxis correcta: python main.py <ruta_archivo_csv> \"<nombre_a_buscar>\"")
        print("Ejemplo: python main.py alumnos.csv \"Naiara Carvajal\"\n")
        sys.exit(1)

    # Asignación de argumentos desde la CLI
    ruta_csv = sys.argv[1]
    nombre_busqueda = sys.argv[2]

    print("=== Iniciando Sistema de Gestión de Instituto ===")
    
    # POR QUÉ: Implementamos un bloque try-except en el controlador para capturar
    # errores del sistema de archivos o de parseo, evitando que la aplicación colapse
    # mostrando trazas de código internas que confundan al operador final.
    try:
        print(f"[*] Cargando y parseando registros desde: '{ruta_csv}'...")
        personas = cargar_desde_csv(ruta_csv)
        print(f"Base de datos procesada correctamente. Registros en memoria: {len(personas)}")
        
    except FileNotFoundError:
        print(f"Error Crítico: El archivo '{ruta_csv}' no existe en la ruta especificada.")
        sys.exit(1)
    except PermissionError:
        print(f"Error Crítico: Permisos insuficientes para leer el archivo '{ruta_csv}'.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error de Estructura: El CSV contiene datos corruptos o inválidos. Detalles: {e}")
        sys.exit(1)

    print(f"\n[*] Ejecutando busqueda para: '{nombre_busqueda}'...")
    encontrado = buscar_por_nombre(personas, nombre_busqueda, modo="parcial", ignore_case=True)

    if encontrado:
        print(f"Nombre encontrado: {encontrado.nombre}")
        
        # Validación sintáctica del correo electrónico del usuario
        if validar_email(encontrado.email):
            print(f"Email ({encontrado.email}): VÁLIDO.")
        else:
            print(f"Email ({encontrado.email}): INVÁLIDO (No cumple el estándar RFC 5322).")

        # POR QUÉ: llama a la funcioón resumen().  Dependiendo de si la instancia
        # es Alumno o Profesor, se ejecutará una sobreescritura distinta automáticamente.
        print(f"{encontrado.resumen()}")
    else:
        print(f"Resultado: No se encontró a ninguna persona con '{nombre_busqueda}'.")

    # Generación y extracción de estadísticas del instituto
    print("\n[*] Computando métricas agregadas del centro...")
    total, nalum, nprof, media_global = resumen_general(personas)
    
    
    print(f"ESTADÍSTICAS DEL INSTITUTO:")
    print(f"  • Total de personas : {total} personas")
    print(f"  • Total de alumnos : {nalum}")
    print(f"  • Total de Profesores      : {nprof}")
    print(f"  • Media global : {media_global:.2f} / 10")

    # Volcado final del procesamiento de datos
    ruta_salida = "salida.csv"
    print(f"[*] Exportando base de datos consolidada a: '{ruta_salida}'...")
    exportar_resumen(personas, ruta_salida)
    print("Proceso finalizado con éxito.\n")

if __name__ == "__main__":
    # POR QUÉ: Asegura que el método main() solo se ejecute si el script es invocado
    # directamente desde la consola, permitiendo que sea importable de forma segura
    # en suites de pruebas unitarias automatizadas como PyTest sin disparar el CLI.
    main()
