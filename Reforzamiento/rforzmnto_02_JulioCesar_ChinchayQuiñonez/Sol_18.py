numeros_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
numeros_float = [3.3, 5.5, 7.7]
lista = numeros_impares[:2] + ['cadena'] + numeros_impares[2:] + numeros_float * 3
del lista[2]
print("Mi lista actualizada es: {}".format(lista))
