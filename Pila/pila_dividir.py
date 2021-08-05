from pila import Pila


def dividir_pila(pila, n):
    #Dada una pila, y un numero n, divide la pila original
    #en pilas con n elementos.
    if pila.esta_vacia():
        raise ValueError('la pila se encuentra vacia')
    if n < 0:
        raise ValueError('cantidad de elementos no valida')
    if n == 0:
        raise ValueError
    pilas = []
    indice = 0
    pila_auxiliar = Pila()
    pila_dividida = Pila()
    while not pila.esta_vacia():
        indice += 1
        dato  = pila.desapilar()
        pila_auxiliar.apilar(dato)
        pila_dividida.apilar(dato)
        if indice == n:
            indice = 0
            pilas.append(pila_dividida)
            pila_dividida = Pila()
    if not pila_dividida.esta_vacia():
        pilas.append(pila_dividida)

    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())
    return pilas

