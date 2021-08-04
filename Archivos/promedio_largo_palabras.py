#Ejercicio 89 archivos
#Escribir una función que reciba la ruta a un archivo de texto, y devuelva el promedio del largo de las palabras de dicho texto (considerando signos de puntuación y otros símbolos como parte de la palabra).
#Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.

def promedio_largo_palabras(ruta):
    with open(ruta) as archivo:
        contador_palabras = 0
        cantidad_caracteres = 0
        for linea in archivo:
            listapalabras = linea.rstrip().split(' ')
            for palabra in listapalabras:
                contador_palabras += 1
                cantidad_caracteres += len(palabra)
    return cantidad_caracteres / contador_palabras

