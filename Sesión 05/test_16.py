"""
16. Solicitar a un usuario ingresar su nombre y apellido, para lo cual se solicita mostrar en pantalla solamente
    sus dos apellidos
    split
"""

nombre = input("Ingrese sus nombres y apellidos: ")

# Uso de split

nombre_lista = nombre.split()
print(nombre_lista)
print("Sus apellidos son: {} {}".format(nombre_lista[-2], nombre_lista[-1]))
