"""Manejo de impresión de valores de cadena de caracteres"""
"""Tercera forma de imprimir valores"""

nombre = input("Por favor ingrese su nombre")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")

print("Bienvenido/a {nombre_usuario} {apellido_usuario} usted tiene {edad_usuario} años".format(nombre_usuario=nombre, apellido_usuario=apellido, edad_usuario=edad))