def palabras_por_linea(archivo):
    #Devuelve la cantidad de palabras para cada linea en formato de diccionario.
    resultado = {}
    with open(archivo) as lector:
        numero = 0
        for linea in lector:
            numero += 1
            lista = linea.split(' ')
            resultado[numero] = len(lista) 
    return resultado


