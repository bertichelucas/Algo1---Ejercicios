from cola import Cola

def mostrar_cola(cola):
    auxiliar = Cola()
    lista = []
    while not cola.esta_vacia():
        dato = cola.desencolar()
        lista.append(dato)
        auxiliar.encolar(dato)
    
    while not auxiliar.esta_vacia():
        cola.encolar(auxiliar.desencolar())
    return lista