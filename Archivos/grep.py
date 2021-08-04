def grep(ruta, cadena):
    #Recibe una cadena y un archivo. Imprime
    #aquellas lineas del archivo que contienen a la cadena.
    resultado =[]
    linea ='x'
    with open(ruta) as archivo:
        while linea:
            linea = archivo.readline().rstrip()
            if linea == '':
                break
            resultado.append(linea)

        for item in resultado:
            if cadena in item:
                print(item)

