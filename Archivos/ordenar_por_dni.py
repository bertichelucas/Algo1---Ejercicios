#Ejercicio 97 archivos
#Se tienen dos archivos cuyos campos son DNI,Apellido,Nombre, y están ordenados por DNI. 
# Escribir una función que reciba los nombres de dos archivos como los mencionados, y genere un nuevo archivo que incluya los datos de ambos archivos de entrada, también ordenados por DNI y sin duplicados.
#Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.


import csv

def orden_por_dni(ruta, ruta2):
    diccionario = {}
    with open(ruta) as origen, open(ruta2) as origen2, open('D:/notepad/codespython/pruebas/dnis.txt', 'x') as destino:
        reader, reader2 = csv.reader(origen), csv.reader(origen2)
        for dni in reader:
            dni, apellido, nombre = dni
            if dni not in diccionario:
                diccionario[dni] = [apellido, nombre]
        for dni, apellido, nombre in reader2:
             if dni not in diccionario:
                diccionario[dni] = [apellido, nombre]
        print(diccionario)
        for clave in sorted(diccionario):
            cadena = clave +',' + ','.join(diccionario[clave])
            destino.write(cadena + '\n')

        
