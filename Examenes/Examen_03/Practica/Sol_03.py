def ingresar_numero():
    while True:
        try:
            numero = float(input("Por favor, ingrese un número: "))
            return numero
        except ValueError:
            print("Error: El valor ingresado no es válido. Por favor, intente nuevamente.")
def division_entre_cero(a, b):
    try:
        resultado = a / b
        print("El resultado de la división es: {}".format(resultado))
    except ZeroDivisionError:
        print("Error: División entre cero.")
def evaluar_suma(a, b):
    if a == b:
        print("Los números que ingresaste son iguales.")
    else:
        print("La suma de los números es:".format( a + b))
def main():
    print("Programa de gestión de errores")
    print("")
    numero_1 = ingresar_numero()
    numero_2 = ingresar_numero()
    division_entre_cero(numero_1, numero_2)
    evaluar_suma(numero_1, numero_2)
if __name__ == "__main__":
    main()
