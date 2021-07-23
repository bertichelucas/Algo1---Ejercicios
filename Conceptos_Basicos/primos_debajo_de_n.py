from es_primo import es_primo

def numeros_primos_debajode_n(n):
    'Imprime los n numeros primos por debajo de n'
    for i in range(n):
        if es_primo(i) == True:
            print (i)

numeros_primos_debajode_n(9) 