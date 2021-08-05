'''
    Implementar una función que calcule el promedio de los
    elementos de una pila de números que recibe por parámetro.

    La pila debe quedar en el mismo estado en el que fue
    recibida (con los mismos elementos y en el mismo orden).
    '''

from pila import Pila

def promediar_pila(pila):
    if pila.esta_vacia():
        raise ValueError('Pila Vacia')
    auxiliar = Pila()
    sumatoria = 0
    cantidad = 0
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        sumatoria += elemento
        cantidad += 1
        auxiliar.apilar(elemento)

    while not auxiliar.esta_vacia():
        pila.apilar(auxiliar.desapilar())
    
    return sumatoria / cantidad