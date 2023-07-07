"""Conversión de datos"""

"""De string: str a entero: int"""

var_1 = "800"     # string
var_2 = 3600      # int
var_3 = 40.90     # float

var_4 = "900"

#suma = var_1 + var_2
suma_string = var_1 + " + " + var_4
print("Suma de strings: {}".format(suma_string))

"""Conversión"""
conversion = int(var_1)
print("El valor de variable 'conversion' es: {}".format(conversion))
print("El tipo de dato de mi variable 'conversion' es: {}".format(type(conversion)))

suma = conversion + var_2
print("La suma de mis variables es: {}".format(suma))

"""Suma de dos variables: int + float = float"""

suma_2 = var_2 + var_3
print("La suma de 'var_2' y 'var_3' es: {}".format(suma_2))
print(type(suma_2))

"""Conversión: De flotante a int"""

conversion_2 = int(suma_2)
print("El valor de mi variable 'conversion_2' es: {}".format(conversion_2))
