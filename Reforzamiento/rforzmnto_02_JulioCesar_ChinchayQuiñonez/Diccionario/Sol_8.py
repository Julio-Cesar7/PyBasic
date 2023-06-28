departamentos = { '1': 'Lima', '2': 'Apurimac', '3': 'Piura', '4': 'Loreto', '5': 'Cajamarca', '6': 'La Libertad'}

nombre_carrera = input("Ingrese el nombre de una carrera: ")

nueva_pos = str(len(departamentos) + 1)
departamentos[nueva_pos] = nombre_carrera

for i, j in departamentos.items():
    print(i, "-", j)

