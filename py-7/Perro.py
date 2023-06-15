from Mascota import Mascota, Duenio

class Perro(Mascota):
    especie = 'Perro'

    def __init__(self, nom, edad):
        # Invoco el método constructor de la clase base
        super().__init__(nom, edad)
        # self.__especie = ''

    # Sobreescribir el método str
    def __str__(self):
        cadena = super().__str__()
        return cadena + ', Especie:' + self.especie

    # Estoy obligado a implementar el método
    def emitir_sonido(self):
        super().emitir_sonido()
        print('Guau')

p1 = Perro('Paka', 15)
print(p1)
# p1.emitir_sonido()
