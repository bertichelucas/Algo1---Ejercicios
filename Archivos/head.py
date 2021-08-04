def head(ruta, n):
    #Recibe un archivo y un numero n
    #Imprime las primeras n lineas del archivo.
    with open(ruta) as f:
        for _ in range(n):
            linea = f.readline()
            if linea == '':
                return
            print(linea.rstrip('\n'))

