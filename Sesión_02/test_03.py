"""
Requisitos:

- Crear 3 variables: nombre, apellido, edad y sueldo (float)
- Imprimir el siguiente mensaje: "Hola 'nombre apellido', su sueldo actual es de: sueldo soles"
- Mostrar la suma (concatenanción) del sueldo y la edad en un mensaje.

"""
nom="Julio Cesar"
ape="Chinchay Quiñonez"
ed= 22
sue= 1200.34
sum= sue + ed
print("Hola {} {},su sueldo actual es de:{} soles".format(nom,ape,sue))
print("La suma de su sueldo ({}) y edad ({}) es: {}".format(sue, ed, sum))
