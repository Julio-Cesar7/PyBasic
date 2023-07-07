"""Listas en Python"""
"""Listas (insert()): insertar elementos en una posición dada"""
lista=[10,50,80,22,100]
lista.insert(1,200)
print("El valor de mi lista es: {}".format(lista))
"""Insertar valor "Hola pytonista" al final de la lista"""
a="Hola pytonista"
lista.insert(len(lista),a)
print("Mi lista actual es: {}".format(lista))