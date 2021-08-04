def pares_primero(lista):
    #Recibe una lista de numeros y crea una nueva lista con los pares al principio.
    resultado = []
    for numero in lista:
        if numero % 2 == 0:
            resultado.insert(0, numero)
        else:
            resultado.append(numero)
    return resultado


