# import calculadora
# from calculadora import resta, dividir
from mi_proyecto import calculadora

var_1 = int(input("Ingrese su primer valor: "))
var_2 = int(input("Ingrese su segundo valor: "))

res = calculadora.resta(var_1, var_2)
# res = resta(var_1, var_2)
print("El resultado de resta de los valores ingresados es: {}".format(res))

# div = dividir(var_1, var_2)
div = calculadora.dividir(var_1, var_2)
print("El resultado de la división de los valores ingresado es: {}".format(div))
