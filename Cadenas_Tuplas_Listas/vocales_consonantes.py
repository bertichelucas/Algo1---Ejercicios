def consonantes_cadena(cadena):
    #Conserva solo las consonantes de la cadena.
    resultado  = ''
    vocales = 'aeiouAEIOU'
    for c in cadena:
        if c not in vocales:
            resultado += c
    return resultado


def vocales_cadena(cadena):
    #Conserva solo las vocales de la cadena.
    resultado  = ''
    vocales = 'aeiouAEIOU'
    for c in cadena:
        if c in vocales:
            resultado += c
    return resultado


def reemplazar_vocales(cadena):
    #reemplaza cada vocal de la cadena por su siguiente vocal en orden alfabetico.
    resultado = ''
    vocales = 'aeioua'
    for c in cadena:
        if c in vocales:
            indice = vocales.index(c)
            resultado += vocales [indice + 1]
        else:
            resultado += c
    return resultado



