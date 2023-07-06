def mostrar_cuadrados_entre_numeros(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    for num in range(num1 + 1, num2):
        cuadrado = num ** 2
        print(cuadrado)

numero1 = int(input("Por facor, ingrese el primer número: "))
numero2 = int(input("Por favor,ingrese el segundo número: "))
mostrar_cuadrados_entre_numeros(numero1, numero2)

