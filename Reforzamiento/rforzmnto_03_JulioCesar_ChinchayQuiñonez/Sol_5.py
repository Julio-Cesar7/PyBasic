class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio

def pedir_radio():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            return radio
        except ValueError:
            print("Error: El radio debe ser un valor numérico.")

for _ in range(2):
    radio = pedir_radio()
    circulo = Circulo(radio)
    print("Radio:", circulo.radio)
    print("Área:", circulo.area())
    print("Perímetro:", circulo.perimetro())
    print()
