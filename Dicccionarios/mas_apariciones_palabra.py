def mas_apariciones(cadena):
    #Recibe una cadena. Devuelve una tupla con
    #la palabra de mas aparciones y la cantidad.
    diccionario = {}
    for palabra in cadena.split(' '):
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1

    maximo = 0
    tupla = ('', 0)
    for palabra in diccionario:
        if diccionario[palabra] > maximo:
            maximo = diccionario[palabra]
            tupla = (palabra, maximo)
    return tupla 

