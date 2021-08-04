def numeros_segun_k(enteros, k):
    '''
    Dada una lista de enteros y un numero k
    devuelve tres listas con menores iguales y mayores
    a ese k.
    '''
    menores = []
    mayores = []
    iguales = []
    for elemento in enteros:
        if elemento < k:
            menores.append(elemento)
        elif elemento > k:
            mayores.append(elemento)
        else:
            iguales.append(elemento)
    return menores, mayores, iguales




