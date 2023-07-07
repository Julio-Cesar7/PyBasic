class Persona:
    def __init__(self):
        self.nombre_apellido = {}

    def ingresar_nombre_apellido(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        self.nombre_apellido = {'Nombre': nombre, 'Apellido': apellido}

    def ingresar_edad(self):
        edad = input("Ingrese su edad: ")
        self.nombre_apellido['Edad'] = edad

    def imprimir_datos(self):
        print("Nombre: ", self.nombre_apellido['Nombre'])
        print("Apellido: ", self.nombre_apellido['Apellido'])
        print("Edad: ", self.nombre_apellido['Edad'])

persona = Persona()

persona.ingresar_nombre_apellido()

persona.ingresar_edad()

persona.imprimir_datos()
