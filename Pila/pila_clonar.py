from pila import Pila

def clonar_pila(pila):
    #Clona la pila manteniendo la original.
    if pila.esta_vacia():
        res = pila
        return res
    pila_aux = Pila()
    res = Pila()
    while not pila.esta_vacia():
        pila_aux.apilar(pila.desapilar())

    while not pila_aux.esta_vacia():
        dato = pila_aux.desapilar()
        pila.apilar(dato)
        res.apilar(dato)
    return res

