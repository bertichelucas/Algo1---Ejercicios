def busqueda_numerica(listanum):
    'Recibe una lista de numeros. Devuelve el valor maximo y su posicion.'
    resultado = 0
    contador = -1
    for item in listanum:
        contador += 1 
        if item > resultado:
            resultado = item
    return resultado, contador

