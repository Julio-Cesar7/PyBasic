"""Uso de librería de fecha y tiempo"""
"""
    Conversión de fechas
"""

from datetime import datetime

fecha_1 = datetime(2023, 7, 13)
fecha_2 = datetime(2023, 7, 30)

if fecha_1 == fecha_2:
    print("Nacieron el mismo día")
elif fecha_1 < fecha_2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")
