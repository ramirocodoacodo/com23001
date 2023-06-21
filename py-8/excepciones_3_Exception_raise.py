class NumeroNegativoError(Exception):
    pass

num = int(input("Ingrese un número: "))
if num < 0:
    raise NumeroNegativoError("El número no puede ser neg.")
print(num)
