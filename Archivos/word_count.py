def wc(ruta):
    #Cuenta las palabras, lineas y caracteres de un archivo.
    resultado = []
    linea = 'x'
    with open(ruta) as archivo:
        while linea:
            linea = archivo.readline().rstrip()
            if linea == '':
                break
            resultado.append(linea)    
        print(resultado)

        palabras = 0
        for item in resultado:
            linea = item.split(' ')
            palabras += len(linea)
        
        caracteres = 0
        for item in resultado:
            caracteres += len(item)
        
        print('el archivo tiene: ', palabras, 'palabras')
        
        print('el archivo tiene:', caracteres, 'caracteres')

        print('el archivo tiene: ', len(resultado), 'lineas')

    return caracteres, palabras, len(resultado)