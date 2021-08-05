
"""Búsqueda binaria
Precondición: la lista está ordenada
Devuelve -1 si x no está en lista;
6 Devuelve p tal que lista[p] == x, si x está en lista
"""
def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1