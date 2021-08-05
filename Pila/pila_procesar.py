from pila import Pila

def procesar(pila, cadena):
    #Recibe una pila y una cadena.Cada numero en la cadena
    #suma al total y cada letra en la cadena resta el ultimo numero de la cadena.
    sumatoria = 0
    for caracter in cadena:
        if caracter.isdigit():
            sumatoria += int(caracter)
            pila.apilar(int(caracter))
        else:
            if not pila.esta_vacia():
                dato = pila.desapilar()
                sumatoria -= dato
            else:
                raise ValueError('No se puede procesar el archivo')
    return sumatoria

