from pila import Pila

def sumar_pilas(pila1, pila2):
    #Crea dos numeros con todos los digitos de la pila
    #Suma esos numeros y apila en una nueva pila los digitos del numero.
    if pila1.esta_vacia():
        return pila2
    if pila2.esta_vacia():
        return pila1
    resultado = Pila()
    numero1 = ''
    numero2 = ''
    while not pila1.esta_vacia():
        dato = pila1.desapilar()
        numero1 += str(dato)
    
    while not pila2.esta_vacia():
        dato = pila2.desapilar()
        numero2 += str(dato)

    numero = str(int(numero1) + int(numero2))
    for i in range(len(str(numero)) -1,-1, -1):
        resultado.apilar(int(str(numero)[i]))
    return resultado

