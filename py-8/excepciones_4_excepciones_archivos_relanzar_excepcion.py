try:
    f = open('archivo.txt')
    s = f.readline()
    i = int(s.rstrip('\n'))
    f.close()
# except IOError as err:
#    print("IO error: {}".format(err))
except ValueError:
    print("No puedo convertir a entero.")
except:
    print("Error inesperado")
    raise # Re-lanza la excepción: FileNotFoundError
finally:
    print("Listo")
