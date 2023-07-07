"""Manejo de errores"""
"""Gestión de errores con try except"""

valor = True

while valor:
    try:
        x = int(input("Por favor ingresa un número: "))
        print("Su dato fue ingresado correctamente :)")
        break
    except:
        print("Upss!!... tipo de dato incorrecto, inténtelo de nuevo por favor.")
