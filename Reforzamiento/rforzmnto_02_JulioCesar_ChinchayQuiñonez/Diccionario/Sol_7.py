departamentos = { '1': 'Lima', '2': 'Apurimac', '3': 'Piura', '4': 'Loreto', '5': 'Cajamarca', '6': 'La Libertad'}
departamento_borrado = '4'

del departamentos[departamento_borrado]

if departamento_borrado in departamentos.values():
    print(f"El departamento {departamento_borrado} aún existe en el diccionario.")
else:
    print(f"El departamento {departamento_borrado} no existe en el diccionario.")

print("Diccionario de departamentos después de la eliminación: {}".format(departamentos))
