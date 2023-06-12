class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def agregar_mascota(self, m):
        self.mascotas.append(m)

    def __str__(self):
        cadena = ""
        cadena += f'Veterina: {self.nombre}' + '\n'
        cadena += "Listado de mascotas de la Vete:\n"
        for m in self.mascotas:
            cadena += str(m) + '\n'
        cadena += '\n'
        return cadena
