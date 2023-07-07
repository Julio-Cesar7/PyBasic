"""POO en Python"""
"""Encapsulamiento"""

class A:
    def __init__(self):
        """Encapsulamiento"""
        self.inicial = 30
        self._contador = 0    #Encapsulamiento débil

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B:
    def __init__(self):
        """Encapsulamiento"""
        self.inicial = True
        self.__contador = 0    #Encapsulamiento fuerte

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incrementa()
var_1.incrementa()

print(var_1.cuenta())

var_2 = B()
var_2.inicial = False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Valor de contador B es: {}".format(var_2.cuenta()))
print("Valor inicial en B: {}".format(var_2.inicial))

"""No es posible invocar a una variable porque el encapsulamiento es fuerte por los 2 guiones abajo previos"""
print("{}".format(var_2.__contador))
