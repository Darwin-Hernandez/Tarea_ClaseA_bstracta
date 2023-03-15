from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.profecion = "Profecion"
        self.edad = 23

    @abstractmethod
    def saludar(self):
        pass

    @abstractmethod
    def caracteristicas(self):
        print(f"el {self.profecion} tiene {self.edad} años de edad")

class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.profecion = "Alumno"
        self.edad = 23

    def caracteristicas(self):
        print(f"{self.nombre} es un {self.profecion}")
        super().caracteristicas()

    def saludar(self):
        print(f"hola buenos dias mi nombre es {self.nombre} y estoy estudiando como un buen {self.profecion} que soy")

class Docente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.profecion = "Docente"
        self.edad = 38

    def caracteristicas(self):
        print(f"{self.nombre} es un {self.profecion}")
        super().caracteristicas()

    def saludar(self):
        print(f"hola buenos dias mi nombre es {self.nombre} y estoy dando clases como el mejor {self.profecion}")

class Padre(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.profecion = "Padre de Familia"
        self.edad = 40

    def caracteristicas(self):
        print(f"{self.nombre} es un {self.profecion}")
        super().caracteristicas()

    def saludar(self):
        print(f"hola buenos dias mi nombre es {self.nombre} y siempre estoy pendiente de mis hijos como un buen {self.profecion} que soy")

persona1=Estudiante("Darwin")
persona1.caracteristicas()
persona1.saludar()

persona2=Docente("William")
persona2.caracteristicas()
persona2.saludar()

persona3=Padre("Emilio")
persona3.caracteristicas()
persona3.saludar()






