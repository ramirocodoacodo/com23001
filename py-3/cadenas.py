# Cadenas (es NO mutable)
cadena= "   Hola Mundo! 123"
print(type(cadena)) # <class 'str'>
print(cadena)
print(cadena[0]) # H
print(cadena[11]) # 1
print(len(cadena)) # 14
print(cadena[-1]) # 3

# Buscar
print(cadena.find("Hola")) # 0
print(cadena.find("Hola", 1)) # -1

# Cadena: Objeto NO mutable
# cadena[0]= 'h' # TypeError: 'str' object does not support item assignment

# Iteracíon
for valor in cadena: 
    print(valor)

# Iteracíon: sólo muestro los números, letras, etc.
for valor in cadena: 
    if not valor.isnumeric():
    # if valor.isalpha():
        print(valor)

# Reemplazar
cadena= cadena.replace('Hola', 'HOLA')
print(cadena)

print()

# Más métodos de cadenas
print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena)

# Más info: https://www.w3schools.com/python/python_ref_string.asp
