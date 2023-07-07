"""Listas en Python"""
"""Listas (pop()): Quita un elemento de una posición existente de la lista"""

paises=["Perú", "España", "Brazil", "Colombia"]
print("Mi lista inicial es la sig: {}".format(paises))

paises.pop()
print("Mi lista actual es:{}".format(paises))

"""Esta eliminando el valor del país de España"""

paises.pop(2)
print("Mi lista actualizada es:{}".format(paises))

paises.pop(1)
print("Eliminando valor que no existe: {}".format(paises))

