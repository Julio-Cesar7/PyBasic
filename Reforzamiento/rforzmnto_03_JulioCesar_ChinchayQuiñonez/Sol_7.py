class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def bonificacion(self):
        return self.sueldo * 0.2

persona1 = Persona("Juan", 25, 3000)
persona2 = Persona("María", 17, 2500)

print("Datos de persona1:")
persona1.mostrar_datos()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
print("Bonificación:", persona1.bonificacion())

print()

print("Datos de persona2:")
persona2.mostrar_datos()
if persona2.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
print("Bonificación:", persona2.bonificacion())
