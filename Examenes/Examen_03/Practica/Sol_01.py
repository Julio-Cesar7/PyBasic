import datetime
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.saldo = 0
        self.nacionalidad = "Peruana"

    def validar_edad(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            return edad
        except ValueError:
            print("Error: La edad debe ser un número entero no negativo")
            exit()

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validar_edad(input("Ingrese su edad: "))

    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_hora_actual = datetime.datetime.now()
        fecha_registro = fecha_hora_actual.strftime("%d-%m-%Y %H:%M")
        return fecha_registro

persona = Persona("", 0)
persona.solicitar_datos()
persona.cumpleaños()
persona.cumpleaños()

print("La edad actualizada es: {}".format(persona.edad))
fecha_registro = persona.obtener_fecha_registro()
print("La fecha de registro es: {}".format(fecha_registro))