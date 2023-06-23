import random
lista =[]
lis_cubo=[]
lis_cuadrados=[]
for i in range(10):
    lista.append(random.randint(1,100))

for i in lista:
    lis_cubo.append(i**3)

for i in lista:
    lis_cuadrados.append(i**2)
l_1=lista.reverse()
l_2=lis_cubo.reverse()
l_3=lis_cuadrados.reverse()
suma=[]
for i in range(len(lista)):
    suma.append(lista[i] + lis_cubo[i] + lis_cuadrados[i])
print(suma)
