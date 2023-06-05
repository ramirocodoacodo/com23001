lista1 = ['uno', 2, True]  # declara una lista heterogénea
lista2 = [1, 2, 3, 4, 5]  # declara lista numérica (homogénea)
lista3 = ['nombre', ['ap1', 'ap2']]  # declara lista dentro de otra
lista4 = [54,45,44,22,0,2,99]  # declara una lista numérica
print(lista1)  # ['uno', 2, True], muestra toda la lista
print(lista1[0])  # uno, muestra el primer elemento de la lista
print(lista2[-1])  # 5, muestra el último elemento de la lista
print(lista3[1][0])  # calle, primer elemento de la lista anidada
print(lista2[0:3:1])  # [1,2,3], responde al patrón inicio:fin:paso
print(lista2[::-1])  # devuelve la lista ordenada al revés
lista1[2] = False  # cambia el valor de un elemento de la lista
lista2[-2] = lista2[-2] + 1  # 4+1 → 5 – cambia valor de elemento
lista2.pop(0)  # borra elemento indicado o último si no indica
lista1.remove('uno')  # borra el primer elemento que coincida
del lista2[1]  # borra el segundo elemento (por índice)  
lista2 = lista2 + [6]  # añade elemento al final de la lista
lista2.append(7)  # añade un elemento al final con append()
lista2.extend([8, 9])  # extiende lista con otra por el final
lista1.insert(1, 'dos')  # inserta nuevo elemento en posición
del lista2[0:3]  # borra los elementos desde:hasta
lista2[:] = []  # borra todos los elementos de la lista 
print(lista1.count(2))  # cuenta el nº de veces que aparece 2
print(lista1.index("dos"))  # busca posición que ocupa elemento
lista3.sort()  # ordena la lista
lista3.sort(reverse=True)  # ordena la lista en orden inverso
lista5 = sorted(lista4)  # ordena lista destino 
tupla1 = (1, 2, 3)  # declara tupla (se usan paréntesis)...
tupla2 = 1, 2, 3  # ...aunque pueden declararse sin paréntesis
tupla3 = (100,)  # con un elemento hay terminar con “,”
tupla4 = tupla1, 4, 5, 6  # anida tuplas
tupla5 = ()  # declara una tupla vacía
tupla6 = tuple([1, 2, 3, 4, 5])  # Convierte una lista en una tupla
tupla2[0:3]  # (1, 2, 3), accede a los valores desde:hasta
