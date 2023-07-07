"""
   Programación orientada a objetos
   Herencia en python
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

"""Aplicando herencia"""
"""Creamos nuestra clase hija"""

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estado_volando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro_1 = Carro("Rojo", 70)

carro_volador = CarroVolador("Blanco", 50)
print("El estado inicial de mi carro volador es: {}".format(carro_volador.estadoVolando))

carro_volador.vuela()
print("El estado actualizado de mi carro volador es: {}".format(carro_volador.estadoVolando))

carro_volador.acelerar()
carro_volador.acelerar()

print("La velocidad actual de mi carro volador es: {}".format(carro_volador.velocidad))

"""IMPORTANTE"""
"""La clase padre no puede usar los métodos ni los atributos de la clase hija al aplicar herencia
pero si la clase hija de la clase padre"""