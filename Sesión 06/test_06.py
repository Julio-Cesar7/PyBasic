"""POO en Python"""
"""Polimorfismo"""


class Perro():
    def sonido(self):
        print("Guauuu")

class Gato():
    def sonido(self):
        print("Miauuu")


class Vaca():
    def sonido(self):
        print("Muuuu")


gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animales = [gato, perro, vaca]

def bulla(animales):
    for animal in animales:
        animal.sonido()

bulla(lista_animales)
