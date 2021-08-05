from cola import Cola

def filtrar_cola(cola, funcion):
    #Recibe una cola y una  funcion de filtrado.
    #Para los elementos que la funcion da false, los elimina de la cola.
    if cola.esta_vacia():
        return cola
    resultado = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if funcion(dato):
            resultado.encolar(dato)
    return resultado

