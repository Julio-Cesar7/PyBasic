"""Control de excepciones"""
"""
TypeError
ZeroDivisionError
IndexError
KeyError
ImportError
FileNotFoundError
"""

"""Estructura y uso"""
"""
    try:
        bloque de código 1
    except 'excepción_1':
        bloque de código 2
    else:
        bloque de código 3
"""


def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("No es posible realizar esta división")
    else:
        print(resultado)


division(40, 0)
division(1000, 70)
