class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota Final: ", self.nota_final)

    def mostrar_resultado(self):
        if self.nota_final >= 11:
            print("El alumno", self.nombre, "ha aprobado.")
        else:
            print("El alumno", self.nombre, "no ha aprobado.")

alumno1 = Alumno("Juan", 18, 15)
alumno2 = Alumno("María", 17, 10)
alumno3 = Alumno("Pedro", 19, 8)

alumno1.imprimir_datos()
alumno1.mostrar_resultado()

alumno2.imprimir_datos()
alumno2.mostrar_resultado()

alumno3.imprimir_datos()
alumno3.mostrar_resultado()
