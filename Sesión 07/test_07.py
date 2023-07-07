"""Uso de librería de fecha y tiempo"""

from datetime import datetime

strFecha = "4/7/2023"

"""
    d: día
    m: mes 
    Y: año
"""

"""
    strptime: Convierte a un tipo de dato datetime
"""
conversion = datetime.strptime(strFecha, "%d/%m/%Y")

print("La fecha formateada es: {}".format(conversion))
print(type(conversion))

conversionMes = datetime.strftime(conversion, "%d %b del %Y")
print("Muestra fecha con cambio en el mes es el siguiente: {}".format(conversionMes))

"""
    b: reemplaza a 'm' para mostrar el mes literalmente
"""
