def cp(ruta, ruta2):
    #Copia todo el contenido de un archivo a otro.
    resultado = []
    linea ='vacio'
    with open(ruta) as archivo:
        while linea:
            linea = archivo.readline().rstrip()
            if linea == '':
                break
            resultado.append(linea)
            
    with open(ruta2, 'w') as f:
        for item in resultado:
            f.write(item + '\n')

