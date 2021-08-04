def contar_aparciones(cadena):
    #Recibe una cadena y devuelve un diccionario con.
    #clave: palabra.
    #valor: cant de apariciones de la palabra.
    dic = {}
    palabras = cadena.split()
    for palabra in palabras:
        # dic [palabra] = dic.get(palabra, 0) + 1  -- Esto reemplazaria todo, probar
        if palabra not in dic:
            dic [palabra] = 1
        else:
            dic [palabra] += 1
    return dic

def encontrar_maximo(dic):
    #Busca la palabra con mas apariciones.
    maximo = 0
    max_palabra = None
    for palabra in dic:
        if dic[palabra] > maximo:
            maximo = dic[palabra]
            max_palabra = palabra

    return max_palabra, maximo

