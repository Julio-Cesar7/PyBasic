"""Listas en Python"""
"""Listas (count): cantidad de veces que aparece un elemento que se repite en una lista"""

lis_1= ["Python", "Java","Java", "PHP", "Ruby","Java", "JavaScrip", "Typescrip"]
lis_1.append("Python")
lis_1.append("Python")

print("Mi lista es: {}".format(lis_1))
print("Cantidad de veces que aparece 'Java' es: {}".format(lis_1.count("Java")))
print("Cantidad de veces que aparece Python es: {}".format(lis_1.count("Python")))

