# Gestión de un instituto


Es una aplicación que gestiona los datos de los profesores y alumnos desde un archivo csv, parsea las notas de los alumnos y calcula sus medias, valida sus email y exporta un resumen.

# Tecnologías usadas
- Python 3.9 - Lógica del programa 
- CSV - Almacenamiento de datos 
- Regex - Validación de emails 

# Software Necesario
Antes de ejecutar el proyecto debes tener instalado:
- Python 3.9 o superior

# Esctructura del proyecto
- main.py #Programa principal
- modelos.py #Clases necesarias para la gestión de los datos de las personas
- utilidades.py #Funciones de lógica como validación del email
- persistencia.py #Manipulación de los archivos csv
- README.md
- documentacion.md

# Formato del csv
El archivo csv debe que tener 6 columnas, separadas por comas. 
1. Tipo: (A(Alumno) o P(Profesor)) (ej. A)
2. Nombre de la persona (ej. Naiara Carvajal)
3. Email (ej. naiaracarvajal@gmail.com)
4. Telefono (ej. 656847598)
5. Grupo (ej. DAW)
6. Notas (ej. [8|10|5])

Ejemplo de línea válida:
A,Naiara Carvajal,naiara@gmail.com,656847598,DAW,8|10|5


# Instalación y Uso
1. Descargar los 4 archivos
   - main.py
   - modelos.py
   - utilidades.py
   - persistencia.py
2. Configurar o instalar la versión necesaria de Python
    ```bash
   python --version
3. Crear o mover el csv dentro de la misma carpeta del proyecto
4. Ejecución del programa desde el bash
    python main.py
        -Nombre del archivo del csv
        -Nombre de la persona que quieras buscar
    
    
