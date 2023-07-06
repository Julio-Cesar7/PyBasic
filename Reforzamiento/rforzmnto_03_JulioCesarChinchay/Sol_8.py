class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print(f"DNI: {contacto['dni']}")
                print("-----------------------")

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni:
                print("Contacto encontrado:")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print(f"DNI: {contacto['dni']}")
                return
        print("No se encontró ningún contacto con el DNI proporcionado.")

agenda = Agenda()

agenda.agregar_contacto("Juan Perez", "123456789", "juan@example.com", "70048491")
agenda.agregar_contacto("Maria Lopez", "987654321", "maria@example.com", "70048492")

agenda.mostrar_contactos()

agenda.buscar_contacto_por_dni("70048491")
agenda.buscar_contacto_por_dni("70048492")
agenda.buscar_contacto_por_dni("70048493")
