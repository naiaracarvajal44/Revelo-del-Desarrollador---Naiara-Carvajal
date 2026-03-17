class Persona:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def resumen(self):
        return f"{self.nombre} - {self.email} - {self.telefono}"


class Alumno(Persona):
    def __init__(self, nombre, email, telefono, grupo, notas=[]):
        super().__init__(nombre, email, telefono)
        self.grupo = grupo
        self.notas = notas

    #Controla que haya notas
    def media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    #Faltaba :
    def add_nota(self, nota, comentario):
        self.notas.append(int(nota))


class Profesor(Persona):
    def __init__(self, nombre, email, telefono, departamento, salario):
        super().__init__(nombre, email, telefono)
        self.departamento = departamento
        try:
            self.salario = float(salario)
        except ValueError:
            print("Salario no valido")

    def aplicar_subida(self, porcentaje):
        self.salario = self.salario + self.salario * porcentaje / 100

    def resumen(self):
        base = super().resumen()
        return base + f" - {self.departamento} - {self.salario}"