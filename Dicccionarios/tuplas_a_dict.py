def tuplas_a_dict(tuplas):
    '''
    Recibe una lista de tuplas y devuelve un diccionario
    donde las claves son los primeros valores de las tuplas
    y los valores una lista con los segundos.
    '''
    resultado = {}
    for tupla in tuplas:
        if tupla [0] in resultado:
            resultado[tupla[0]].append(tupla[1])
        else: 
            resultado[tupla[0]] = [tupla[1]]
    return resultado

