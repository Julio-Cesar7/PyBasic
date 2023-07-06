def ingresar_nombre_apellido():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    return nombre, apellido

def pedir_tipo_seguro():
    tipo_seguro = input("Ingresa el tipo de seguro que tienes: ")
    return tipo_seguro

def verificar_mayor_edad():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        return True
    else:
        return False
