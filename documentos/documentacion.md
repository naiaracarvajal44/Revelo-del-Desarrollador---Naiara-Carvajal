# Documentacion de clases y funciones

# Clases
### Persona
- Atributos: 
    - nombre: str, Nombre de la persona.
    - email: str, Correo electrónico.
    - telefono: str, Numero de teléfono.
    
- Métodos: 
    - resumen() : Devuelve los datos básicos de la persona.

### Alumno(Persona)
- Atributos: 
    - nombre: str, Nombre de la persona.
    - email: str, Correo electrónico.
    - telefono: str, Numero de teléfono.
    - grupo: str, Grupo al que pertenece.
    - notas: list[int], Notas que ha obtenido.
- Métodos: 
    - media() Calcula la media de las notas que tiene el alumno. 
    - add_nota(nota, comentario) Añade la nota a la lista de las notas del alumno.

### Profesor(Persona)
- Atributos: 
    - nombre: str, Nombre de la persona.
    - email: str, Correo electrónico.
    - telefono: str, Numero de teléfono.
    - departamento: str, Departamento al que pertenece el profesor.
    - salario: float, Salario que recibe el profesor.
- Métodos: 
    - aplicar_subida(porcentaje) Incrementa el salario seguún el porcentaje introducido.
    - resumen() : Devuelve los datos básicos de la persona.


# Funciones
### parsear_notas(texto_notas)
Si text_notas está vacía devuelve una lista pero si no intenta separar el texto con el separador "|" y convierte cada trozo en un entero y despues devolver la lista de los enteros, si no se pudiera convertir algún trozo lanza una excepción.

### validar_email(email)
Valida el email con la biblioteca externa regex, compara el patrón con el email introducido devuelve True o False.

### buscar_por_nombre(personas, texto, modo="exacto", ignore_case=True)
- Recorre la lista personas buscando una persona cuyo nombre coincida con texto.
- Si ignore_case es True, convierte el nombre y el texto a minúsculas para que la búsqueda no distinga entre mayúsculas y minúsculas.
- Si modo es "exacto", devuelve la persona cuyo nombre sea exactamente igual al texto.
- Si modo es "parcial", devuelve la persona si el texto aparece dentro del nombre.

### resumen_general(personas)
- Hace un total de personas con la lista
- Obtiene el numero de alumnos que hay usando isinstance de Alumnos.
- Obtiene el numero de profesores que hay usando isinstance de Profesor.
- Crea una lista para guardar las medias de los alumnos.
- Usa un bucle para obtener todas las medias de los alumnos y guardarlas en la lista creada antes.
- Intenta calcular la media global y si no es posible lanza una excepción y devuelve media_global = 0 
- Devuelve la cantidad personas, la cantidad de alumnos, profesores, media_global.


### crear_persona_desde_campos(campos):
- Asigna tipo la columna 0 del archivo CSV.
- Si es tipo (A) comprueba la linea del archivo CSV tenga al menos 6 columnas; si no, lanza un ValueError.
- Asigna el nombre, email, telefono, grupo, notas (parseandolas) con su campo correspondiente.
- Comprueba que el email es correcto el patron y si no lo es lanza un AVISO.
- Devuelve un objeto Alumno con esos datos.
- Si fuera tipo (P) vuelve a comprobar que el archivo no tiene menos de 6 columnas.
- Asigna el nombre, email, telefono, departamento, salario lo convierte en float.
- Comprueba que el email es correcto el patron y si no lo es lanza un AVISO.
- Devuelve los datos del profesor.
- Si el tipo no es correcto, lanza un ValueError devolviendo tipo desconocido.
- Si hubiera un ValueError se lanzaría en cualquier momento.


### cargar_desde_csv(ruta, separador=",", encoding="utf-8")
- Crea una lista que le asigna el nombre de personas
- Intenta abrir el archivo csv en formato lectura y codificación UTF-8
- lee las lineas.
- Si no encuentra el archivo lanza una excepción.
- Si no tienes permisos para acceder al archivo lanza otra excepción.
- Un bucle que lee linea a linea el archivo
- Elimina espacios y separa la linea usando el separador para obtener los campos
- Con los campos y la funcion crear_persona_desde_campos() crea el objeto.
- Si devuelve una persona valida la añade a la lista.
- Cierra el archivo y devuelve la lista.
- Devuelve una lista de objetos Persona (Alumno o Profesor).

### exportar_resumen(personas, ruta_salida)
- Salida, creamos la cabecera del archivo CSV de salida.
- Bucle con la lista de personas.
- Si es alumno añade una lista con tipo A y sus datos nombre, email, grupo y media.
- Si es profesor añade una lista con tipo P y sus datos nombre, email, departamento y salario.
- Abre un archivo con formato escritura y escribe los datos correspondientes.
