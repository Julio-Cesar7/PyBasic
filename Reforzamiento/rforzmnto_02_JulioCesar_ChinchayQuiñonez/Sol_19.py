lista = []

for i in range(10):
    valor = int(input("Ingresa un número_{}: ".format(i)))
    lista.append(valor)

suma = sum(lista)
media = suma / len(lista)

print("La suma de los números es:", suma)
print("La media de los números es:", media)
