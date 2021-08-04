def invertir_palabras(cadena):
    #Inverte las palabras dentro de una cadena
    resultado = ''
    lista = cadena.split(' ')
    for palabra in lista:
        for i in range(len(palabra) - 1, -1, -1):
            resultado += palabra[i]
        resultado += ' '
    return resultado

