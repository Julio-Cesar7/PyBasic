nombre= input("Escribe tu nombre: ")
apellidos=input("Escribe tu apellido: ")
edad= input("Escribe tu edad: ")
dni= input("Escribe tu DNI: ")

diccionario={'Nombre':nombre, "Apellido": apellidos, "Edad":edad, "DNI":dni}

print("Los values del diccionario es: {}".format(diccionario.values()))

diccionario["Profesion"]="Física"
print("Mi diccionario actualizado es: {}".format(diccionario))
