artistas = {'Lorca':'Escritor', 'Goya':'Pintor'} # diccionario
paises = ['Chile','España','Francia','Portugal'] # declara lista
capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista
for c, v in artistas.items(): print(c,':',v)  # recorre diccionario
for i, c in enumerate(paises): print(i,':',c)  # recorre lista 
for p, c in zip(paises, capitales): print(c,' ',p) # recorre listas
for p in reversed(paises): print(p,)  # recorre en orden inverso
for c in sorted(paises): print(c,)  # recorre secuencia ordenada