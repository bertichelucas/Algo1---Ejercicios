from math import factorial

'Imprime los factoriales de los n numeros dados por el usuario.'

def main():
    cantidad = int(input('ingrese la cantidad de numeros que desea calcular'))
    for i in range(cantidad):
        numero = int(input('Ingrese el numero a calcular: '))
        fact = factorial(numero)
        print (numero, '-', fact)

main()        