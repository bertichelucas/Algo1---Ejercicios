'''
Ejercicio 91 archivos
Se tiene un archivo CSV de cuatro columnas con formato equipo,jugador,fecha,goles. 
Se pide implementar una función que reciba el nombre del archivo como parámetro y devuelva un diccionario con los goles por jugador por equipo. 
Por ejemplo: { equipo1: { jugador1: 3, jugador2: 1 }, equipo2: { ... } ... }

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
'''
import csv

def goles_por_jugador_por_equipo(ruta):
    resultado = {}
    with open(ruta) as archivo:
        csv_reader = csv.reader(archivo)
        for linea in csv_reader:
            equipo, jugador, _, goles = linea
            print(goles)
            if equipo not in resultado:
                resultado[equipo] = {}
            if jugador not in resultado[equipo]:
                resultado[equipo][jugador] = int(goles)
            else:
                resultado[equipo][jugador] += int(goles)
        return resultado

