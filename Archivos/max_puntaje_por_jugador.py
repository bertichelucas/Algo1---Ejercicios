#Se tiene un archivo de texto donde cada línea es de la forma nombre_jugador,puntaje_1,puntaje_2,...,puntaje_n, 
# representando una serie de puntajes obtenidos por un jugador (puede haber cualquier cantidad de puntajes para cada jugador, pero todos tienen al menos uno). Los puntajes no tienen decimales. 
# Escribir un función que reciba el nombre de un archivo con la forma descripta 
# y el nombre de un archivo destino, y escriba en él líneas de la forma nombre_jugador,puntaje_mas_alto, siendo puntaje_mas_alto el más alto de entre los puntajes de ese jugador.

#Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.

import csv

def max_puntaje_por_jugador(ruta, ruta2):
    with open(ruta) as origen, open(ruta2, 'w') as destino:
        csv_reader = csv.reader(origen)
        for linea in csv_reader:
            for i in range(1, len(linea)):
                linea[i] = int(linea[i])
            destino.write(linea[0] + ', ' + str(max(linea[1:])) + '\n')
