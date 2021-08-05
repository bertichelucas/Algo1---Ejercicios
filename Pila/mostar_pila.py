from pila import Pila


def mostrar_pila(pila):
        auxiliar = Pila()
        lista_pila = []
        while not pila.esta_vacia():
            dato = pila.desapilar()
            auxiliar.apilar(dato)
        while not auxiliar.esta_vacia():
            dato =auxiliar.desapilar()
            lista_pila.append(dato)
            pila.apilar(dato)
        return lista_pila

