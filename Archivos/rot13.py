import string

def rot13(ruta, ruta2):
    #Funcion para cifrar un archivo. 
    #https://es.wikipedia.org/wiki/ROT13
    letras = string.ascii_lowercase
    resultado = []
    nueva_linea = ''
    linea ='x'
    with open(ruta) as archivo:
        while linea:
            linea = archivo.readline().rstrip()
            if linea == '':
                break    
            for caracter in linea:
                if caracter in letras:
                    nueva_linea += letras[(letras.find(caracter) + 13) % 26]
                else:
                    nueva_linea += caracter
            resultado.append(nueva_linea)
            nueva_linea = ''
    

    with open(ruta2, 'w') as destino:
        for linea in resultado:
            destino.write(linea + '\n')

            
