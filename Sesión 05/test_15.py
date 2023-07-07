"""Programación funcional en python"""


def multiplicacion(a, b, c=100):
    resultado = a*b*c
    return resultado


"""Es correcto usar la función sin asignar un tercer valor"""
print("El resultado de mi función es: {}".format(multiplicacion(40, 3)))

"""Es correcto usar la función cambiando el valor del tercer parámetro"""
print("El resultado de mi función es: {}".format(multiplicacion(40, 3, 50)))
