#Busqueda binaria de manera recursiva

def busqueda_binaria(datos, elem, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if elem == datos[medio]:
        return medio
    if elem > datos[medio]:
        return busqueda_binaria(datos, elem, medio + 1, fin)
    return busqueda_binaria(datos, elem, inicio, medio - 1)

#Ejercicio recursivo 