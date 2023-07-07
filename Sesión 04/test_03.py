"""Uso del flujo condicional: if"""

"""
    - Un usuario ingresará su edad y el sistema le dirá si es una persona, menor, adulta, tercera edad o si 
    la edad ingresada es incorrecta
"""

edad = int(input("Hola, ¿cual es su edad?: "))

print(type(edad))

if 0 < edad < 18:
    print("1. Usted es menor de edad")
elif 18 <= edad <= 65:
    print("2. Usted es una persona adulta")
elif 100 >= edad > 65:
    print("3. Usted es una persona de tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta, vuelva a ingresar su edad")
