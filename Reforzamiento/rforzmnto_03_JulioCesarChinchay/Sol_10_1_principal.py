import Sol_10

nombre, apellido = Sol_10.ingresar_nombre_apellido()
print("Nombre:", nombre)
print("Apellido:", apellido)

tipo_seguro = Sol_10.pedir_tipo_seguro()
print("Tipo de seguro:", tipo_seguro)

es_mayor_edad = Sol_10.verificar_mayor_edad()
if es_mayor_edad:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")
