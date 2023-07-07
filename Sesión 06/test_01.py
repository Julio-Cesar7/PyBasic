"""
   Programación orientada a objetos
"""


class Carro:
    """Atributos"""
    ruedas = 5

    """Constructor: Valores que van a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


"""Instanciamos nuetra clase"""

carro_1 = Carro("negro", 50)
print("CARRO 1")
print("Color: {}".format(carro_1.color))
print("Aceleración: {}".format(carro_1.aceleracion))
print("La cantidad de ruedas que tiene el carro 1 es: {}".format(carro_1.ruedas))

print("\nCARRO 2 ")
carro_2 = Carro("azul", 70)
print("Color: {}".format(carro_2.color))
print("Aceleración: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas que tiene el carro 2 es: {}".format(carro_2.ruedas))