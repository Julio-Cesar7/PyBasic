"""Uso de 'for'"""

ingenierias = ["Software", "Sistemas", "Civil", "Industrial", "Química"]

print("El tamaño de mi lista es: {}".format(len(ingenierias)))
i = 1

for ingenieria in ingenierias:
    print("Ing. {}".format(ingenieria))
    print("Esta es la vuelta número {}".format(i))
    i = i + 1




