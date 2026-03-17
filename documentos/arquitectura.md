### Arquitectura del proyecto
Es una arquitectura modular, separando cada responsabilidad en varios archivos para que sea más fácil su entendimeinto y su ampliación en un futuro si fuera necesario.

Gestión de un instituto
│
├── main.py
├── modelos.py
├── utilidades.py
├── persistencia.py
└── README.md
└── documentos
        |___ documentacion.md
        |___ arquitectura.md


### main.py
Es el programa principal.
- Coordina el flujo del programa.
- Recibe los parámetros del usuario.
- Llama a las funciones necesarias.

### modelos.py
Define las clases necesarias del programa.
- Representa las entidades del sistema (Persona, Alumno, Profesor)
- Aplica principios de Programación Orientada a Objetos (POO)

### utilidades.py
Define las funciones necesarias para la comprobación de los datos.
- Permite que los datos sean correctos
- Búsquedas de datos y cálculos.

### persistencia.py
Gestiona la lectura y escritura de datos.
- Lectura de los datos del CSV.
- Escritura de los datos.
- Exportación de los datos.