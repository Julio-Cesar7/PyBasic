"""Usando las propiedades de cadenas"""

"""Método string"""

cadena = "Conexión a base de datos con Python"

cadena_2 = cadena.replace(cadena[0:6], "ppppp")
print(cadena_2)

"""Eliminando espacios en blanco de mi cadena (después)"""

cadena_3 = "Conexion a base de datos con Python             "
cadena_4 = cadena_3.rstrip()

print(cadena_4)

"""Eliminando espacios en blanco de mi cadena (antes)"""

cadena_5 = "                Conexion a base de datos con Python"
cadena_6 = cadena_5.lstrip()
print(cadena_6)
