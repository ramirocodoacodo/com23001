from Mascota import Mascota

class Pajaro(Mascota):
    especie = 'Pajaro'

    def __init__(self, nom, edad):
        # Invoco el método constructor de la clase base
        super().__init__(nom, edad)

    # Sobreescribir el método str
    def __str__(self):
        cadena = super().__str__()
        return cadena + ', Especie del pájaro:' + self.especie

    def emitir_sonido(self):
        super().emitir_sonido()
        print('Pio pio')
