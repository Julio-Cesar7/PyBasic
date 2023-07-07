"""Uso de la librería JSON para tratar tipos de datos JSON"""

from json import dumps

"""Uso de librería JSON"""

pythonData = {"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}

"""Convirtiendo a un dato JSON: dumps()"""

pythonToJson = dumps(pythonData)

print("Nuestro dato tipo JSON a dato para Python es: {}".format(pythonToJson))
print("El tipo de dato de nuestra variable es: {}".format(type(pythonToJson)))
