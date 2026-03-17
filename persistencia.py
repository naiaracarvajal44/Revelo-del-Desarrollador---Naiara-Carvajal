from modelos import Alumno, Profesor
from utilidades import parsear_notas, validar_email

def crear_persona_desde_campos(campos):
    tipo = campos[0].strip()

    try:
        if tipo == "A":
            if len(campos) < 6:
                raise ValueError("Alumno incompleto: faltan grupo y/o notas")

            nombre= campos[1].strip()
            email = campos[2]
            telefono = campos[3]
            grupo = campos[4]
            notas = parsear_notas(campos[5])

            if not validar_email(email):
                print(f"[AVISO] Email invalido en linea: {email}")

            return Alumno(nombre, email, telefono, grupo, notas)

        elif tipo == "P":
            if len(campos) < 6:
                raise ValueError("Profesor incompleto")

            nombre = campos[1].strip()
            email = campos[2]
            telefono = campos[3]
            departamento = campos[4]
            salario = float(campos[5])

            if not validar_email(email):
                print(f"[AVISO] Email invalido: {email}")

            return Profesor(nombre, email, telefono, departamento, salario)

        else:
            raise ValueError("Tipo desconocido")

    except ValueError as e:
        print(f"[ERROR]: {e}")


def cargar_desde_csv(ruta, separador=",", encoding="utf-8"):
    personas = []
    try:
        f = open(ruta, "r", encoding="utf-8-sig")
        lineas = f.readlines()

    except FileNotFoundError:
        print("El archivo no existe")
        return []
    except PermissionError:
        print("No tienes permiso para cargar el archivo")
        return []

    for linea in lineas:
        if linea.strip() == "":
            continue
        campos = linea.strip().split(separador)
        p = crear_persona_desde_campos(campos)

        if p != None:
            personas.append(p)

    f.close()
    return personas

def exportar_resumen(personas, ruta_salida):
    salida = "tipo;nombre;email;extra\n"
    for p in personas:
        if isinstance(p, Alumno):
            salida += f"A;{p.nombre};{p.email};{p.grupo};{p.media()}\n"
        elif isinstance(p, Profesor):
            salida += f"P;{p.nombre};{p.email};{p.departamento};{p.salario}\n"
        else:
            salida += f"?;{p.nombre};{p.email};-\n"

    open(ruta_salida, "w").write(salida)