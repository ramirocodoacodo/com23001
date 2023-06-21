import sys

# Ejemplo: quiero LANZAR (no capturar) una excepción si el número ingresado es NEGATIVO. 
# Posible uso del raise: def ingresar_entero_positivo
class NumeroNegativoError(Exception):
    pass # Ejemplo para crear una Excepción propia

def ingresar_natural():
    num_real= float(input("Ingrese un número: "))  # 12.0
    num= int(num_real)
    '''
    if num<=0:
        # raise Exception("El número no puede ser negativo.") # Invoco el método especial: __init__ (constructor)
        # raise NumeroNegativoError("El número no puede ser negativo.") # Invoco el método especial: __init__ (constructor)
        raise ValueError("El número no puede ser negativo.") # Invoco el método especial: __init__ (constructor)
    '''
    # Hago lo mismo que antes: Lanzar una excepción de tipo assert
    assert (num>0), "El número no puede ser negativo o cero."
    if not (num==num_real):  # 12.0 == 12
        raise TypeError("El valor ingresado debe ser entero.")

    return num

# Bloque ppal
def __main__():
    while True:
        try:
            valor= ingresar_natural()
            # break # opción 1 para cortar
        except AssertionError as error:
            # continue # Continua en el siguiente ciclo 
            # print("El número debe ser positivo.")
            print(error)
        except ValueError:
            print("El dato ingresado no es correcto.")
            # valor= ingresar_natural()
        except TypeError as error:
            print(error)
        except:
            print(sys.exc_info()[0]) # <class 'AssertionError'> # Me informa el tipo de excepción ocurrida (class)
        else:
            break        
    
    print(valor)

if __name__=='__main__':
    __main__()
