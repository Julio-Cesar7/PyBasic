"""Manejo de errores"""

"""
05. Crear una función aplicando exepciones donde no se puede realizar una suma de diferentes tipo de datos
"""

def operacion(x, y):
    try:
        resultado = x + y
        resultado = x/y
        return resultado
    except TypeError:
        print("No se puede realizar la operación")
    except ZeroDivisionError:
        print("No es posible dividir estos dos valores")
    else:
        print(resultado)


operacion(4, "Hola pythonista")
print(operacion(50, 100))
