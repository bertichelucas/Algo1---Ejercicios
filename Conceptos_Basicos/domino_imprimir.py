'Imprime por pantalla todas las fichas de un Domino de n numeros '

def imprimir_domino(a, cant):
    for i in range (cant + 1):
        print (a, i)

def domino():
    cant = int(input('ingrese la cantidad de numeros para fichas del domino'))
    for i in range (cant + 1):
       imprimir_domino(i,cant)


