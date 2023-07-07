"""Uso del flujo condicional: if"""

"""
  Requisitos:
  - El usuario debe ingresar 2 valores (tiene que ser numéricos)
  - Usar la condicional if para que el sistema indique cual de las 2 variables es mayor
  o si son iguales
"""

var_1 = int(input("Ingrese su primer valor numérico: "))
var_2 = int(input("Ingrese su primer segundo numérico: "))

if var_1 > var_2:
    print("El valor de var_1 es mayor que segundo valor ingresado")
elif var_1 == var_2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de var_1 no es mayor que el valor de la segunda variable")
