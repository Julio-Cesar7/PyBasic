"""
   Programación orientada a objetos
   Atributos
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


carro_1 = Carro("Blanco", 30)

print("El color de mi primer carro es: {}".format(carro_1.color))

carro_2 = Carro("Rojo", 45)
carro_2.marchas = 30000

print("El número de marchas de mi segundo carro es: {}".format(carro_2.marchas))

"""IMPORTANTE"""
"""No es posible llamar un atributo de datos que se le ha asignado a otra instancia de la clase"""
#print("El número de marchas del carro 1 es: {}".format(carro_1.marchas))
