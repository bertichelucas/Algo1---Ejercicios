def contar_letras_o(cadena):
    #Cuenta las apariciones de la letra o en una cadena.
    variantes = ('o', 'O', 'ó', 'Ó')
    contador = 0
    for c in cadena:
        if c in variantes:
            contador += 1
    return contador

