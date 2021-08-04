def cadena_censurar(texto, palabra):
    #Dada una cadena y una palabra, se censura la palabra cada vez que aparezca en la cadena.
    lista = texto.split(' ')
    resultado = ''
    for item in lista:
        if str(item.upper()) == palabra or str(item.lower()) == palabra:
            censura = ''
            for c in item:
                censura +=  '*'
            item = censura
        resultado += item
        resultado += ' '
    return resultado

