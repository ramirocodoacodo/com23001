# Declaro un lista (objeto MUTABLE, estructura dinámica)
numeros= [1,2,9,10,-20,0]
palabras= ["ANANA", "KIWI", "MANZANA"]
lista_vacia= []

print(type(numeros)) # <class 'list'>

# Iteración
for valor in palabras:
    print(valor)
    if valor == "KIWI":
        valor= valor.lower() # Esto no tiene efecto sobre la lista

# len tmb aplica

# Acceder a cada posición y modificarla
palabras[1]= palabras[1].lower()
print(palabras[1])
print(palabras)

# Ejemplo: duplicar los valores de una lista numérica
for i in range(len(numeros)):
    numeros[i]= numeros[i]*2
print(numeros)

# Ejemplo: mostrar un caracter de un elemento determinado de mi lista palabras
print(palabras[1]) # kiwi
print(palabras[1][2]) # w

# Más métodos asociados a listas
# Agregar
palabras.append('PERA')

# Insertar
palabras.insert(0, 'BANANA')
print(palabras)

print()

# Eliminar
palabras.pop() # Elimina el ÚLTIMO elem.
print(palabras)
palabras.pop(0) # Elim. en la pos. N (0 en el ejemplo)
print(palabras)

# Eliminar por elemento
# palabras.remove('ANAN') # ValueError: list.remove(x): x not in list
palabras.remove('ANANA') 
print(palabras)

# Ordenar
numeros.sort() # [-40, 0, 2, 4, 18, 20]
numeros.sort(reverse=True) # [20, 18, 4, 2, 0, -40]
print(numeros)

# Sumar y Contar
print(sum(numeros)) # 4
print(numeros.count(0)) # 1

# Listas de listas (Matrices)
matriz= [
         [1,2],
         [3,4]
        ]
print(matriz[1]) # fila 1: [3,4]
print(matriz[1][0]) # elemento de la fila 1 y columna 0: 3
