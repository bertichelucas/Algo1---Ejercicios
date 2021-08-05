from cola import Cola

def intercalar(colas):
    #Recibe una lista de colas y devuelve una cola con
    #los elementos intercalados.
    resultado = Cola()
    while colas != []:
        for cola in colas:
            if not cola.esta_vacia():
                dato = cola.desencolar()
                resultado.encolar(dato)
            else:
                colas.remove(cola)
    return resultado

