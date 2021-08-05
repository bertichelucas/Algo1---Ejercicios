def replicar_elementos(lista, n):
    #Replica n veces cada elemento de la lista.
    longitud = len(lista)
    return funcion_repetitiva(lista, longitud, 0, n)

def funcion_repetitiva(lista, longitud, iterador, n):
    if iterador >= longitud * n - 1:
        return lista
    numero = lista[iterador]
    for i in range(n-1):
        print(iterador)
        lista.insert(iterador + i, numero)
    iterador += n
    return funcion_repetitiva(lista, longitud, iterador, n)



