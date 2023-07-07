class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def calcular_impuestos(self):
        impuesto = 0
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.1
        return impuesto

nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
sueldo = float(input("Ingrese el sueldo del empleado: "))

empleado = Empleado(nombre, edad, sueldo)

print("Sueldo del empleado:", empleado.sueldo)
print("Impuesto a pagar:", empleado.calcular_impuestos())
