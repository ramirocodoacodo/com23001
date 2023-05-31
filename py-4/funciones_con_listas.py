import random

def mostrar_lista(lista):
    '''
    Muestra los valores de una lista por consola.
    Param.:
    lista: valores a mostrar.

    '''
    for valor in lista:
        print(valor, end=' ')
    print()  # Salto de línea

# Prog ppal
# help(mostrar_lista)
numeros = [1,5,66,0,-100]
mostrar_lista(numeros)

print(mostrar_lista(numeros))  # None

def calcular_prom_sum(lista):
    suma = 0
    for valor in lista:
        suma += valor

    if len(lista) > 0:
        prom = suma / len(lista)

    return prom, suma  # UnboundLocalError: local variable 'prom' referenced before assignment
    # Manejo de excepciones

def calcular_prom_sum2(lista):
    '''
    pre: recibe una lista.
    pos: devuelve promedio y suma de la lista. 
         Si la lista está vacía, devuelve None.

    '''
    if len(lista) > 0:
        suma = 0
        for valor in lista:
            suma += valor
        prom = suma / len(lista)

        return prom, suma

# print(calcular_prom_sum(numeros))
# print(calcular_prom_sum([]))
print(calcular_prom_sum2(numeros))
print(calcular_prom_sum2([]))  # Tupla: (-5.6, -28)
prom, suma = calcular_prom_sum2(numeros)  # Desempaquetado

# Objeto mutable (lista, diccionario) o inmutable (tupla, cadena)
def duplicar(lista):
    # for valor in lista:
    #     valor *= 2  # valor = valor * 2 (no cumple con mi objetivo)
    for i in range(len(lista)):
        lista[i] *= 2  # lista[i] = lista[i] * 2

print(numeros)
duplicar(numeros)  # [2, 10, 132, 0, -200]
print(numeros)

cadena = "Hola Mundo!"
cadena2 = "Ramiro"
cadena = cadena + cadena2
cadena = cadena.upper()
print(cadena[2])
# cadena[2] = "L"  # TypeError: 'str' object does not support item assignment

# import
def crear_lista(n:int):
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 10))
    return lista

lista = crear_lista(10)
mostrar_lista(lista)

# funciones lambda
def fx_es_par(num):
    return num%2==0

es_par = lambda num:num%2==0
cuadrado = lambda num:num**2

print(es_par(4))

# lista_cuadrados = list(map(cuadrado, numeros))
lista_cuadrados = list(map(lambda num:num**2, numeros))
mostrar_lista(lista_cuadrados)
