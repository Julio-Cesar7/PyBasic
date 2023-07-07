"""
   Programación orientada a objetos
   Clase y métodos
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


carro_1 = Carro("Azul", 90)
print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()

print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()

print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.frena()

print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.frena()
carro_1.frena()
carro_1.frena()

print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))
