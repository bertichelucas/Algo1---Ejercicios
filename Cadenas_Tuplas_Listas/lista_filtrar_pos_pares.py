def filtrar_posicion_par(lista):
    #Filtra las posiciones pares de una lista in place.
    i = 0
    aux = 0
    for e in lista:
        if i % 2 == 0:
            lista.pop(aux)
            aux -= 1
        i += 1
        aux += 1
    return lista

