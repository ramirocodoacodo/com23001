# Definiendo mi clase
class Perro:
    # Atributos de clase
    genero = 'Canis'
    id = 0  # contador gral de la clase

    # Comportamiento (Métodos)
    # Métodos especiales
    def __init__(self, n, edad):
        # Atributo de instancia
        self.nombre = n
        self.edad = edad
        Perro.id += 1  # Modifico el atributo de clase
        self.id = Perro.id

    # Método de instancia
    def cumplir_anios(self):
        self.edad += 1

    def ladrar(self):
        return f'{self.nombre} dice guau guau.'

    # Sobreescribimos el método __str__s
    def __str__(self):
        # f-strings
        return f'ID: {self.id} - {self.nombre} tiene {self.edad} años y su género es {self.genero}'

# Prog. ppal (main)
perro1 = Perro('Paka', 15)
perro2 = Perro('Paka', 15)
print(type(perro1))
print(perro1)  # Invocamos al método __str__
print(type(perro2))
print(perro2)
perro2.cumplir_anios()

print(perro2.edad)
perro2.edad += 1
print(perro2.edad)

# Método str
perro1.nombre = "Firulais"
print(str(perro1))
print(perro2)

print(perro1.ladrar())

# Tarea pendiente: Crear un sistema para una veterinaria. Voy a tener una lista de mascotas.
#                  Crear una mascota ingresando datos por teclado. Agregar una mascota a mi
#                  lista de mascotas. Método para mostrar todas las mascotas de mi sistema. 
#                  2 alternativas: crear métodos en el main, o bien crear una clase Sistema
#                  que tengan el comportamiento definido.
