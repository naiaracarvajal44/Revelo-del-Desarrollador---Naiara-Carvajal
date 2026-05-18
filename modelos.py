"""
Modelos de Datos - Sistema de Gestión de Instituto (SGI).

Este módulo define las entidades de Programación Orientada 
a Objetos (POO). Aplica conceptos de encapsulamiento, herencia y polimorfismo 
para modelar los roles del instituto de forma mantenible y tipada.
"""

class Persona:
    """Representa la abstracción base de una persona."""

    def __init__(self, nombre: str, email: str, telefono: str):
        """
        Inicializa los atributos de una persona.
        
        Args:
            nombre (str): Nombre completo.
            email (str): Dirección de correo electrónico.
            telefono (str): Número de teléfono de contacto.
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def resumen(self) -> str:
        """
        Genera una representación de los datos de la persona.
        
        Returns:
            str: Fila de datos básicos.
        """
        return f"{self.nombre} - {self.email} - {self.telefono}"


class Alumno(Persona):
    """Crea a un estudiante del instituto, heredando las propiedades de Persona."""
    
    def __init__(self, nombre: str, email: str, telefono: str, grupo: str, notas: list = None):
        """
        Inicializa un objeto Alumno extendiendo el constructor de Persona.
        """
        super().__init__(nombre, email, telefono)
        self.grupo = grupo
        self.notas = notas if notas is not None else []

    def media(self) -> float:
        """
        Calcula la media de las notas del alumno.

        Returns:
            float: Nota media calculada. Retorna 0.0 si la colección está vacía.
        """
        # POR QUÉ: El control previene una excepción crítica de división 
        # por cero (ZeroDivisionError) en caso de que el alumno acabe de ser matriculado.
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def add_nota(self, nota: float, comentario: str) -> None:
        """
        Inserta una nueva calificación en el expediente del alumno.
        
        Args:
            nota (float): Valor numérico de la calificación.
            comentario (str): Observación opcional sobre la prueba.
        """
        self.notas.append(int(nota))


class Profesor(Persona):
    """Crea a un profesor, heredando de Persona."""

    def __init__(self, nombre: str, email: str, telefono: str, departamento: str, salario: float):
        """
        Inicializa un objeto Profesor validando los datos de entrada.
        """
        super().__init__(nombre, email, telefono)
        self.departamento = departamento

        try:
            self.salario = float(salario)
        except ValueError as e:
            raise ValueError(f"El salario proporcionado ('{salario}') no es un número válido.") from e

    def aplicar_subida(self, porcentaje: float) -> None:
        """
        Aplica un incremento porcentual sobre el salario actual.
        
        Args:
            porcentaje (float): Tasa de incremento (ej: 5.5 representa un 5.5% de subida).
        """
        self.salario = self.salario + (self.salario * porcentaje / 100)

    def resumen(self) -> str:
        """
        Polimorfismo: Sobrescribe el método resumen() de la clase base Persona
        para anexar las propiedades laborales específicas del profesor.
        
        Returns:
            str: Fila detallada con datos personales, departamento y salario.
        """
        base = super().resumen()
        return base + f" - {self.departamento} - {self.salario:.2f}€"
