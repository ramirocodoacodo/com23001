# Diccionarios (mutable)
dicc= {"Ramiro":41, "Juan":17, "Pedro":18}
print(dicc)
print(dicc["Ramiro"])
print(list(dicc.keys())) # Le pido al dicc sus claves y lo convierto a lista
print(list(dicc.values()))

# Ejemplo: mostrar personas mayores de edad.
for clave in dicc:
    if dicc[clave]>=18:
        print(clave, "es mayor de edad.")

# Reemplazar
dicc["Ramiro"]= 42

dicc["Ezequiel"]= 10
print(dicc)

# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}
 
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
 # update the value of key 'B'
Dictionary1.update(Dictionary2)

# Output: 
# Original Dictionary:
{'A': 'Geeks', 'B': 'For'}
# Dictionary after updation:
{'A': 'Geeks', 'B': 'Geeks'}

print()

# Tuplas (no mutable)
fecha= (2022,6,6)
fecha= (2022,6,7)
print(fecha)
print(fecha[0])

# Desempaqueetado
anio, mes, dia= fecha
print(anio)

# Iterar sobre una tupla (for)
# Aplicar rebanadas
copia= fecha[:] # copia con rebanadas

# Conjuntos
conj= {-1,3,4,5}
numeros= [1,1,3,3,5,9,8,10,5]

# Ejemplo: eliminar repetidos de una lista
numeros_sin_repetir= set(numeros)
print(numeros_sin_repetir)
numeros= list(numeros_sin_repetir)
print(numeros)

print()

# Más métodos
conj= {-1,3,4,5}
print(conj)
conj.add(100) # Agregar
conj.remove(5)
# conj.remove(101) # Error
copia_conj= conj.copy()
elem_elim= conj.pop() # eliminar al azar y lo retorna

print(conj)
print(copia_conj)
