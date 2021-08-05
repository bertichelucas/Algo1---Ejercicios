#escribir una funcion reemplazar que tome una pila, un valor nuevo 
# y un valor viejo y reemplace en la pila todas las ocurrencias del 
# valor viejo por el valor nuevo.
#Pila tiene apilar(dato), desapilar() y esta_vacia()

from pila import Pila

def reemplazar_valores(pila, valor_viejo, valor_nuevo):
    pila_aux = Pila()
    if pila.esta_vacia():
        return
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento == valor_viejo:
            pila_aux.apilar(valor_nuevo)
        else:
            pila_aux.apilar(elemento)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())