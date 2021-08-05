from cola import Cola


def promedio_cola(cola):
    #Devuelve el promedio de los elementos de la cola.
    #La cola se mantiene igual.
    if cola.esta_vacia():
        raise ValueError('La cola esta vacia')
    auxiliar = Cola()
    sumatoria = 0 
    contador = 0
    while not cola.esta_vacia():
        dato = cola.desencolar()
        sumatoria += dato
        contador += 1
        auxiliar.encolar(dato)
    
    while not auxiliar.esta_vacia():
        cola.encolar(auxiliar.desencolar())
    return sumatoria / contador
