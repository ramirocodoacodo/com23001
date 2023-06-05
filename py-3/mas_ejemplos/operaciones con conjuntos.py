conjunto = set()  # Define un conjunto vacío
lista = ['vino', 'cerveza', 'agua', 'vino']  # define lista
bebidas = set(lista)  # define conjunto a partir de una lista
print('vino' in bebidas)  # True, 'vino' está en el conjunto
print('anis' in bebidas)  # False, 'anis' no está en el conjunto
print(bebidas)  # imprime {'agua', 'cerveza', 'vino'}
bebidas2 = bebidas.copy()  # crea nuevo conjunto a partir de copia
print(bebidas2)  # imprime {'agua', 'cerveza', 'vino'}
bebidas2.add('anis')  # añade un nuevo elemento 
print(bebidas2.issuperset(bebidas)) # True, bebidas es subconjunto
bebidas.remove('agua')  # borra elemento
print(bebidas & bebidas2)  # imprime elementos comunes
tapas = ['croquetas', 'solomillo', 'croquetas']  # define lista
conjunto = set(tapas)  # crea conjunto (sólo una de croquetas)
if 'croquetas' in conjunto:  # evalúa si croquetas está
    pass
conjunto1 = set('Python')  # define conjunto: P,y,t,h,o,n 
conjunto2 = set('Pitonisa')  # define conjunto: P,i,t,o,n,s,a
print(conjunto2 - conjunto1)  # aplica diferencia: s, i, a
print(conjunto1 | conjunto2)  # aplica unión: P,y,t,h,o,n,i,s,a 
print(conjunto1 & conjunto2)  # intersección: P,t,o,n
print(conjunto1 ^ conjunto2)  # diferencia simétrica: y,h,i,s,a