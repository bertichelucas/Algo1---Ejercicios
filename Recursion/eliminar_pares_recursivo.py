def eliminar_pares(lista):
    #Elimina los elementos pares de una lista.
    if lista == []:
        return lista
    items = len(lista)
    iterador = 0
    return funcion_recursiva(lista, iterador, items)

def funcion_recursiva(lista, iterador, items):
    if iterador == items:
        return lista
    if lista[iterador] % 2 == 0:
        lista.pop(iterador)
        items -= 1
        return funcion_recursiva(lista, iterador, items)
    else:
        iterador += 1
        return funcion_recursiva(lista, iterador, items)

