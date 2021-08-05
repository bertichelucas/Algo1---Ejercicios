def ordenar_seleccion(L):
    for i in range (len(L) - 1):
        p = buscar_pos_minimo(L, i)
        L[p], L[i] = L[i], L[p]

def buscar_pos_minimo(L, i):
    #devuelve la pos del elemento min en l[i:]
    pos_min = i
    while i < len(L):
        if L[i] < L[pos_min]:
            pos_min = i
        i += 1
    return pos_min