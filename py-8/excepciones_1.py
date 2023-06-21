try:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado = num1 / num2  # ZeroDivisionError: division by zero (Exception)
    print(resultado)
except ValueError:
    print("Debe ingresar un valor númerico.")
except ZeroDivisionError:
    print("El divisor no puede ser cero.")
except:
    print("Ha ocurrido un error!")
