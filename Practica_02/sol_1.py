nomb=input("Ingrese su nombre: ",)
edad=int(input("Ingrese su edad: "))
print("El tipo de datos para la variable nomb y edad es respectivamente: {},{}".format(type(nomb), type(edad)))

trabajador_1 = input("Ingresar el nombre del primer trabajador: ")
edad_1= input("Ingrese la edad del primer trabajador: ")
trabajador_2=input("Ingresar el nombre del segundo trabajador: ")
edad_2= input("Ingrese la edad del segundo trabajador: ")

lista=[]
lista.append((trabajador_1, edad_1, trabajador_2, edad_2))

sum= int(edad_1) + int(edad_2)
print("Mi lista y la suma de las edades respectivamente son: {}, {}".format(lista, sum))

