def obtener_mayor_elemento(lista):
    #Obtiene el mayor elemento de una lista.
    if lista == []:
        return None
    mayor = lista[0]
    return funcion_recursiva(lista, 0, None)

def funcion_recursiva(lista, contador, mayor):
    if contador == len(lista):
        return mayor
    if lista[contador] > mayor:
        mayor = lista[contador]
    contador += 1
    return funcion_recursiva(lista, contador, mayor)


