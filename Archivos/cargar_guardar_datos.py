def cargar_datos(ruta):
    #Recibe un archivo de datos con formato calve valor
    #Devuelve un diccionario de claves y valores.
    resultado = {}
    linea = 'x'
    with open(ruta) as archivo:
        while linea: 
            linea = archivo.readline().rstrip()
            if linea == '':
                break
            clave, valor = linea.split(',')
            resultado [clave] = valor
        return resultado
    
def guardar_datos(diccionario, ruta2):
    #Guarda los datos de un diccionario en un archivo de destino.
    with open(ruta2, 'w') as f:
        for clave in diccionario:
            escrito = clave + ',' + diccionario[clave] + '\n'
            f.write(escrito)



