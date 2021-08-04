#Se cuenta con un archivo llamado ratings.csv que contiene en cada línea los puntajes que los usuarios de un conocido sitio de música dan a los artistas que escuchan. 
# El formato del archivo es usuario,genero,artista,puntaje. 
# Se pide realizar una función que reciba por parámetro un nombre de género musical y cree un nuevo archivo .csv que contenga todos los puntajes correspondientes a los artistas del género. 
# El formato debe ser usuario,artista,puntaje, y el nombre del archivo creado debe ser el nombre del género. (ejemplo, si el género recibido es "rock", el archivo se debe llamar rock.csv).

#Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.

import csv

def artista_del_genero(ruta, genero):
    ruta_des = 'D:/notepad/codespython/pruebas/'+ genero + '.csv'
    with open(ruta) as origen, open(ruta_des, 'x') as destino:
        csv_reader = csv.reader(origen)
        for linea in csv_reader:
            if genero in linea:
                linea.remove(genero)
                destino.write(",".join(linea) + '\n')

