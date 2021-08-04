def rotaciones(palabra):
    #Recibe una palabra e imprime las rotaciones para la misma
    #Hola = olaH, laHo, aHol
    resultado = []
    for _ in range (len(palabra)):
        resultado.append(palabra)
        nueva = ''
        for i in range(len(palabra)):
            if i == len(palabra) - 1:
                nueva += palabra[0]
            else:
                nueva += palabra[i + 1]
        palabra = nueva
    return resultado

