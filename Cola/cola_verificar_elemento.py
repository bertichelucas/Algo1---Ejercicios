from cola import Cola


def verificar_elemento(cola, elemento):
    #Dada una cola y un elemento, verifica si el elemento esta en la cola.
    lista_datos = []
    resultado = False
    while not cola.esta_vacia():
        lista_datos.append(cola.desencolar())

    for dato in lista_datos:
        if dato == elemento:
            resultado = True
        cola.encolar(dato)
    return resultado

