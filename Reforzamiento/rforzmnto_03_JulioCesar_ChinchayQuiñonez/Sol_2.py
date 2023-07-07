class Revers:
    def reversa(self, input):
        palabras = input.split()
        invertir_palabra = palabras[::-1]
        cadena_inver = ' '.join(invertir_palabra)
        return cadena_inver

reverser = Revers()

input1 = "Hola Pythonista, seguimos adelante"
output1 = reverser.reversa(input1)
print(output1)

output2 = reverser.reversa(output1)
print(output2)
