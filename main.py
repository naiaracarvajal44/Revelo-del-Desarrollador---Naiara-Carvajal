from persistencia import cargar_desde_csv, exportar_resumen, crear_persona_desde_campos
from utilidades import buscar_por_nombre, resumen_general, validar_email, parsear_notas

def main():
    ruta = input("Ruta CSV: ")
    personas = cargar_desde_csv(ruta)

    texto = input("Buscar nombre: ")
    encontrado = buscar_por_nombre(personas, texto, modo="parcial", ignore_case=True)


    if encontrado:
        if validar_email(encontrado.email):
            print(f"El email de {encontrado.nombre} es válido")
        else:
            print(f"El email de {encontrado.nombre} es inválido")

        print("Resumen:", encontrado.resumen())
    else:
        print("No encontrado")

    total, nalum, nprof, media_global = resumen_general(personas)
    print("Total:", total, "Alumnos:", nalum, "Profesores:", nprof, "Media global:", media_global)

    exportar_resumen(personas, "salida.csv")
    print("Exportado a salida.csv")

main()