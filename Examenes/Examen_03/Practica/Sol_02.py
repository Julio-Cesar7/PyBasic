import datetime
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.__saldo = 0
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
        fecha_registro = fecha_hora_actual.strftime("%Y-%m-%d %H:%M")
        return fecha_registro
    def mostrar_saldo(self):
        return self.__saldo
    def transferencia(self, monto, persona_destino):
        if self.__saldo >= monto:
            self.__saldo -= monto
            persona_destino.__saldo += monto
            print("Transferencia realizada con éxito.")
        else:
            print("Saldo insuficiente. No se puede realizar la transferencia.")

persona_1 = Persona("", 0)
persona_2 = Persona("", 0)
persona_1.solicitar_datos()
persona_2.solicitar_datos()

monto_transferencia = int(input("Por favor, ingrese el monto a transferir de persona_1 a persona_2: "))
persona_1.transferencia(monto_transferencia, persona_2)

print("El saldo de la persona_1 es:{}".format(persona_1.mostrar_saldo()))
print("El saldo de la persona_2 es:{}".format(persona_2.mostrar_saldo()))