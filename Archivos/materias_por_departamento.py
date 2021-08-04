'''
Ejercicio 92 archivos
Dado el nombre del archivo en el que están listadas las materias de la facultad con el formato:

dd.cc - nombre de materia
en dónde dd es el número del departamento y cc es el número de la materia, se pide escribir una función que devuelva un diccionario que 
asocie códigos de departamento con una lista de los nombres de las materias del departamento.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
'''

def materias_departamento(ruta):
    
    with open(ruta) as archivo:
        resultado = {}
        for linea in archivo:
            linea = linea.rstrip()
            codigo, materia = linea.split('.')
            materia.rstrip()
            _, nombre_materia  = materia.split(' - ')
            if codigo not in resultado:
                resultado[codigo] = [nombre_materia]
            else:
                resultado[codigo].append(nombre_materia)
    return resultado

