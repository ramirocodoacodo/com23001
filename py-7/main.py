from Mascota import Mascota
from Gato import Gato
from Pajaro import Pajaro
from Perro import Perro
from class_veterinaria import Veterinaria

# Prog ppal
v1 = Veterinaria("Vete Codo")
# nombre = input("Ingrese el nombre de la mascota (ENTER para salir): ")
# while nombre != '':
#     edad = int(input("Ingrese la edad de su mascota: "))
#     m = Mascota(nombre, edad)
#     v1.agregar_mascota(m)
#     nombre = input("Ingrese el nombre de la mascota (ENTER para salir): ")
p1 = Perro('Paka', 10)
g1 = Gato('Neko',15)
pa1 = Pajaro('Piolin',1)
v1.agregar_mascota(p1)
v1.agregar_mascota(g1)
v1.agregar_mascota(pa1)
print(v1)
v1.despertar_mascotas()


