def tiene_mas_letra_a(cadena):
    #Determina si la cadena tiene mas letras A o E.
    #Devuelve False si hay mas e que a y true en caso contrario.
    contador = funcion_recursiva(cadena, 0, 0)
    if contador >= 1:
        return True
    return False

def funcion_recursiva(cadena, indice, contador):
    if indice == len(cadena):
        return contador
    letra = cadena[indice]
    indice += 1 
    if letra == 'e':
        contador -= 1
    if letra == 'a':
        contador += 1
    return funcion_recursiva(cadena, indice, contador)

print(tiene_mas_letra_a('aeeeaaaa'))