# fuertemente tipado y dinámicamente tipado
variable = 12.8
print(type(variable))
variable = str(12)
print(type(variable))

# Calcular el promedio de notas hasta ingresar 0 (cero)
suma = 0
cont = 0
nota = int(input("Ingrese una nota (0 para salir): "))
# while not(nota >= 0 and nota <= 10):
while nota < 0 or nota > 10:
    print("Error en los datos ingresados.")
    nota = int(input("Error. Ingrese una nota: "))

while nota != 0:
    if 10 >= nota >= 7:
        print("PROMOCIONA")
    elif nota < 7 and nota >= 4:
        print("APRUEBA")
    else:
        print("DESAPRUEBA")
    suma = suma + nota
    cont += 1  # cont = cont + 1

    nota = int(input("Ingrese una nota (0 para salir): "))
    while not(nota >= 0 and nota <= 10):
        print("Error en los datos ingresados.")
        nota = int(input("Error. Ingrese una nota: "))

if cont != 0:
    promedio = suma / cont
    print('El "promedio" de notas es:', promedio)
else:
    print("No ha ingresado notas.")

# for, operador in
numeros = [1,2,4,6,-1,0,100]
for i in range(len(numeros)):  # 0 1 2 3 ... 6
    print(str(i) + ":", numeros[i])

for i in range(1,11):
    print(i)

for i in range(1,11,2):  # 1 3 5 ... 9
    print(i)

cadena = "Ramiro"
print("R" in cadena)

# break y continue
num = int(input("Ingrese un valor: "))
while True:
    if num == 5:
        break
    else:
        num = int(input("Ingrese un valor: "))
        continue
print("Fin del programa.")

# PY 3: Cadenas y Listas
