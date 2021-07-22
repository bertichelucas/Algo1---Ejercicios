'Recibe un numero n e imprime los primeros n numeros triangulares, junto con su indice'

def numeros_triangulares(n):
    for i in range (1, n + 1):
        a = int (i * (i + 1) / 2)
        print (i, ' - ', a)

def main():
    n = int(input('Escriba un numero: '))
    numeros_triangulares(n)
    return 0

main()