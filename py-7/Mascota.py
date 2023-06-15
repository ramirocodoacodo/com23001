from abc import ABC, abstractmethod

class Mascota(ABC):
    # Atributo de clase
    # nombre = "Vete Codo"

    # constructor
    # def __init__(self, nom, e, edad):
    def __init__(self, nom, edad):
        # Atributos privados
        self.__nombre = nom
        self.__edad = edad
        # self.raza = "-"
        self.__raza = ""
        # self.__especie = e
        self.__duenio = None

    # Getters y Setters
    # nombre
    @property  # decorador
    def nombre(self):
        return self.__nombre

    # @property  # decorador
    # def especie(self):
    #     return self.__especie

    # edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad

    # raza
    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, r):
        self.__raza = r

    # SI tiene un método abs, obligo a que las clases derivadas impl. ese método
    @abstractmethod
    def emitir_sonido(self):
        pass

    def __str__(self):
        cadena = "Nombre:" + self.nombre + ", Edad:" + str(self.edad)
        return cadena

class Duenio:
    pass

# Prog ppal
'''
m1 = Mascota("Firulais", 1)
# m1.raza = "Mestizo"
print(m1.raza)

# print(m1.__nombre)  # AttributeError: 'Mascota' object has no attribute '__nombre'
# m1.__nombre = "F"
print(m1.nombre)
# m1.nombre = "."
print(m1.edad)
m1.edad = -1
print(m1.edad)

# m1.emitir_sonido()
'''