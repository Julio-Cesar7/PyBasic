"""Programación funcional en python"""

"""
    Requerimiento:
    - Crear una función media.
    - Será la media de 3 números.
    - El usuario ingresará los 3 números: inputs
    - Output: es la media de estos 3 números
"""

"""Obteniendo la media"""

valor_1 = int(input("Ingrese el primero número: "))
valor_2 = int(input("Ingrese su segundo número: "))
valor_3 = int(input("Ingrese su tercer número: "))


def media(x, y, z):
    resultado = (x + y + z)/3
    return resultado


print(media(valor_1, valor_2, valor_3))
