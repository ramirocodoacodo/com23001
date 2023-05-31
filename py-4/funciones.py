# def sumar(num1, num2):
def sumar(num1, num2, num3=0):
    # docstring
    '''
    pre: recibe 3 números (num3 valor por defecto).
    pos: devuelve la suma de ambos números.

    '''
    # resultado = num1 + num2 + num  # Mal práctica (var. global)
    resultado = num1 + num2 + num3
    return resultado  # Valor de retorno*

# Prog ppal
num = int(input("Ingrese un número: "))
print(sumar(1,3))  # Invocando a la fx
# No se recomienda el uso de var. globales
# print(resultado)  # NameError: name 'resultado' is not defined

# Parámetros por defecto
print(sumar(1,3,num))
print(sumar(1,3,num3=num))
# print(sumar(num3=num,1,3))  # SyntaxError: positional argument follows keyword argument
print(sumar(num3=num,num1=1,num2=3))
