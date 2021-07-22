
'Programa que imprime una palabra pedida al usuario y la imprime mil veces.'

def imprimir_mil_veces(palabra):
    for i in range(1000):
        print(palabra + ' ', end= '\0')

def main():
    palabra = input('Ingrese una palabra: ')
    imprimir_mil_veces(palabra)
    return 0

main()