class CalculadoraCubos:
    def __init__(self):
        self.resultado = None

    def ingresar_valor(self):
        valor = input("Por favor, ingresar un valor numérico: ")
        try:
            valor = int(valor)
            self.resultado = valor ** 3
        except ValueError:
            print("El valor ingresado no es válido.")

    def obtener_cuadrado_resultado(self):
        if self.resultado is not None:
            cuadrado = self.resultado ** 2
            return cuadrado
        else:
            print("No se ha calculado el resultado todavía.")

calculadora = CalculadoraCubos()
calculadora.ingresar_valor()
cuadrado_resultado = calculadora.obtener_cuadrado_resultado()
if cuadrado_resultado is not None:
    print("El cuadrado del resultado es:", cuadrado_resultado)