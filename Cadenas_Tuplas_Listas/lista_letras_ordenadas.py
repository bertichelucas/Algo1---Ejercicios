def letras_ordenadas():
    #Recibe letras por parametro. Imprime una cadena con las letras
    #ordenadas
    letra = ' '
    lista_deletras = []
    anterior = ''
    while letra:
        letra = input('Ingrese una letra: ')
        if letra == '':
            break
        elif len(letra) > 1 or not letra.isalpha():
            letra = ' '
        else:
            lista_deletras.append(letra)
    lista_deletras.sort()
    for letra in lista_deletras:
        if anterior != letra:
            print(letra, end = '')
        anterior = letra

letras_ordenadas()