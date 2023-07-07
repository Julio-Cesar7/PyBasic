"""Programación funcional en python"""

var_1 = int(input("Ingrese un valor numérico: "))
var_2 = int(input("Ingrese un segundo valor numérico: "))

"""Input: dos variables que pasarán por parámetro a la función"""
"""x, y: parámetro de mi función 'resta'"""


def resta(x, y):
    rest = x - y
    return rest


print("El resultado de la resta es: {}".format(resta(var_1, var_2)))
