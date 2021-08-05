def duracion_lista_reproduccion(dic_canciones, dic_listas):
    #Recibe un diccionario de canciones y sus duraciones.
    #Recibe un diccionario de listas de reproduccion con sus canciones
    #Devuelve un diccionario con las listas de reproduccion como clave
    #y su duracion total como dato.
    resultado = {}
    for lista_repr in dic_listas:
        tiempo = 0
        for cancion in dic_listas[lista_repr]:
            print(cancion)
            tiempo +=  dic_canciones[cancion]
        resultado[lista_repr] = tiempo
    return resultado

