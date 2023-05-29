print("Hola Mundo!")

# num1 = int(input("Ingrese un número: ")); num2 = int(input("Ingrese un número: "))
# print(num1, num2)

# Condicionales
# Categorizar una calificación (1 a 10)
nota = int(input("Ingrese una nota: "))
# Iteraciones
# Validación
while not(nota >= 1 and nota <= 10):
    print("Error en los datos ingresados.")
    nota = int(input("Error. Ingrese una nota: "))  # Indentación

'''
if nota >= 7:
    print("PROMOCIONA")
else:
    if nota < 7 and nota >= 4:
        print("APRUEBA")
    else:
        print("DESAPRUEBA")
'''

if 10 >= nota >= 7:
    print("PROMOCIONA")
elif nota < 7 and nota >= 4:
    print("APRUEBA")
elif nota >= 1 and nota < 4:
    print("DESAPRUEBA")
else:
    print("Nota no válida.")
