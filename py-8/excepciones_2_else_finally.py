try:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado = num1 / num2  # ZeroDivisionError: division by zero (Exception)
except ValueError:
    print("Debe ingresar un valor númerico.")
except ZeroDivisionError:
    print("El divisor no puede ser cero.")
except:
    print("Ha ocurrido un error!")
else:
    try:
        print(resultado)
    except:
        print("Ha ocurrido un error!")
finally:
    print("Fin de mi bloque try-except!")

print("Fin!")
'''
f = open('archivo.txt')
# ...
f.close()

IOError

'''
lista = [1,2,3,4]
print(lista[10])  # IndexError: list index out of range
