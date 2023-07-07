"""Uso de la librería JSON para tratar tipos de datos JSON"""

from json import loads

"""Uso de librería JSON"""

jsonData = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convirtiendo a un dato manejable para Python: loads()"""

jsonToPython = loads(jsonData)

print("Nuestro dato tipo JSON a dato para Python es: {}".format(jsonToPython))
print("El tipo de datos de nuestra variable es: {}".format(type(jsonToPython)))
