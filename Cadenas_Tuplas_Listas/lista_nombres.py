def nombre(lista):
    '''
    Dada una lista de tuplas con nombre, apellido y inicial 
    del segundo nombre, devuelve una lista de cadenas 
    con el nombre completo.
    '''
    resultado = []
    for tupla in lista:
        cadena = (tupla[1] + ' ' + tupla [2] + '. ' + tupla [0])
        resultado.append(cadena)
    return resultado

lista = [('Fernandez', 'Alberto', 'G'), ('Memem', 'Carlos', 'Z'), ('Peron', 'Juan', 'D')]
print(nombre(lista))


