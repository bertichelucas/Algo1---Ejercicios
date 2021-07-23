
from es_primo import es_primo

def factores_primos(k):
    'Imprime la descompocicion en factores primos de un numero k'
    nroprimo = 2
    while k != 1:
        if k % nroprimo == 0:
            print(nroprimo)
            k = k // nroprimo
        else:
            nroprimo = siguiente_primo(nroprimo)

def siguiente_primo(nroprimo):
    actual = nroprimo + 1
    while True:
        if es_primo(actual):
            return actual
        actual += 1
        
factores_primos(36)