def posiciones_de_b_en_a(a, b):
    #Recibe dos cadenas y devuelve las posiciones 
    # en donde se encuentra b dentro de a.
    print(len(a))
    posiciones = []
    return funcion_recursiva(a, b, -1, posiciones)

def funcion_recursiva(a, b, indice, posiciones):
    if indice == len(a) - 1 or b == '':
        return posiciones
    indice += 1
    print(indice)
    if a[indice] == b[0]:
        if a[indice:indice + len(b)] == b:
            posiciones.append(indice)
            indice += len(b) - 1
    return funcion_recursiva(a, b, indice, posiciones)

                    

