"""Diccionarios en Python"""

empleado= {"nombre": "Alfredo", "edad": 31, "ciudad": "Lima"}

"""Para eliminar valores de nuestros diccionarios usamos: del"""

del empleado["edad"]

print("Los datos actualizados de mi diccionario son: {}".format(empleado))

del empleado["nombre"]

print("Los datos actualizados de mi diccionario son: {}".format(empleado))


