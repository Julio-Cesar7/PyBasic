""" Solusión de Reforzamiento 1"""
#Pregunta 1:
mi_saludo = '¡Hi TuNombre!'
mi_nombre = 'Julio César'
print("Result_preg_1: {}; mi nombre es {} ".format(mi_saludo, mi_nombre))
#Pregunta 2:
val_1 = 30*10 - 10
print("Result_preg_2: El valor del resultado val_1 es: {}".format(val_1))
#Pregunta 3:
val_2= "40"
val_3= 10
sum= int(val_2) + val_3
print("Result_preg_3: La suma es: {}".format(sum))
#pregunta 4:
"""Libreria Numpy para el valor de Phi"""
import numpy as np
cte_1= (4/3)
phi= np.pi
rad_esf= 10
volumen_Esf= cte_1*phi*(rad_esf**3)
print("Result_preg_4: El volumen de la esfera es: {}".format(volumen_Esf))
#pregunta 5:
val_4= 1600
if(val_4%2 == 0):  #Si no hay resto al dividir entre 2,el valor es par, sino será impar al a ver un resto diferente de cero.
    a= "par"
    print("Result_preg.5: El sueldo que recibo es un número: {}".format(a))
else:
    b="impar"
    print("Result_preg.5: Result_preg.6: El sueldo que recibo es un número: {}".format(b))
#Pregunta 6:
val_5= 12.45
val_6= 12.45
val_7= 12.45
val_8= 12.45
val_9= 12.45

promedio= (val_5 + val_6 + val_7 + val_8 + val_9)/5
print("Result_preg_6: El valor de la media es: {}".format(promedio))
#pregunta 7:
val_10=63
val_11=53
val_12=143

suma = val_10%3 + val_11%5 +val_12%7
print("Result_preg_7: El valor de la suma es: {}".format(suma))
#pregunta 8:
"""Con lista Vacia"""
a_4=[]
if not a_4:
    print("Result_preg_8.1: ¿La lista no tiene elementos?: {}".format(not a_4))
else:
    print("Result_preg_8.1: La lista tiene elementos: {}".format(a_4))

"""Con lista con elementos"""
a_5=[1,2,3]
if not a_5:
    print("Result_preg_8.2: ¿La lista no tiene elementos?: {}".format(not a_5))
else:
    print("Result_preg_8.2: La lista tiene elementos: {}".format(a_5))
#pregunta 9:
a_1=2
res_0=pow(a_1,4) - a_1*2 #Funcion pow() devuelte un número(3) elevado a otro número(4)
print("Result_preg_9: El valor es: {}".format(res_0))
#pregunta 10:
nombre= "Julio César"
carrera= "Ciencias Físicas"
edad= 23
año_nacimiento=2000
inf = {'Nombre': 'Julio César',
       'Carrera': 'Ciencias Físicas',
       'Edad': 23,
       'Año_nacimiento': 2000}
print("Result_preg_10:El resultado de nuestro diccionario es: {}".format(inf))
#pregunta 11:
a_2= (2**5)/10
typ_dato= type(a_2)
print("Result_preg_11: El tipo de dato es:{}".format(typ_dato))