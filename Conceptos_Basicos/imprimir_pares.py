'Programa que imprime todos los numeros pares entre dos numeros dados.'

def imprimir_pares(a, b):
    for i in range (a,b):
        if i % 2 == 0:
            print (i)

def main():
    a = int(input('escriba el primer numero entero'))
    b = int(input('escriba el segundo numero entero'))
    imprimir_pares(a, b)
    return 0

main()