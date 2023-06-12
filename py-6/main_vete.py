'''
Les presento la tarea: crear un sistema para una veterinaria. Acá están los pasos a seguir:

    Primero, necesitan crear una mascota. Pidan al usuario que ingrese los datos necesarios, como el nombre, la raza, etc. ¡Asegúrate de capturar toda la información importante!
    Una vez que hayan creado la mascota, deberán agregarla a nuestra lista de mascotas en el sistema. Esto nos permitirá realizar un seguimiento de todas las mascotas que atendemos en la veterinaria.
    Por último, es momento de mostrar todas las mascotas que tenemos en nuestro sistema. De esta forma, podremos verificar que todas las mascotas han sido correctamente agregadas y visualizar la información de cada una.

Tienes dos opciones para realizar esta tarea:

a) Puedes escribir los métodos necesarios directamente en el programa principal. Es una forma sencilla de organizar tu código y realizar las acciones requeridas.

b) También puedes crear una clase llamada "Sistema" que contenga los métodos necesarios para crear, agregar y mostrar mascotas. Esta opción te permitirá estructurar mejor tu código y aprovechar los beneficios de la programación orientada a objetos.

¡Ahora es tu turno! Elige la opción que te resulte más cómoda y manos a la obra. Si tienen alguna duda, no dudes en consultar. ¡Éxitos!

'''
from Mascota import Mascota
from class_veterinaria import Veterinaria

# Prog ppal
v1 = Veterinaria("Vete Codo")
nombre = input("Ingrese el nombre de la mascota (ENTER para salir): ")
while nombre != '':
    edad = int(input("Ingrese la edad de su mascota: "))
    m = Mascota(nombre, edad)
    v1.agregar_mascota(m)
    nombre = input("Ingrese el nombre de la mascota (ENTER para salir): ")

print(v1)
