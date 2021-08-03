def caracter_entre_letras(cadena, caracter):
    #Recibe una cadena y un caracter
    #Inserta el caracter entre cada letra de la cadena
    #Devuelve la nueva cadena.
    x = cadena[0]
    for c in cadena[1:]:
        x += caracter + c
    return x

def reemplazar_espacios_cadena(cadena, caracter, reemplazo):
    #Recibe una cadena, un caracter y un reemplazo.
    #Crea una nueva cadena donde por cada aparicion del caracter
    #Se escribe el reemplazo.
    if not cadena:
        return ''
    x = ''
    for c in cadena:
        if c != caracter:
            x += c
        else:
            x += reemplazo
    return x 

def reemplazar_digitos(cadena, caracter):
    #Reemplaza todos los numeros de una cadena por el caracter.
    #devuelve la nueva cadena.
    if not cadena:
        return ''
    numeros = '1234567890'
    resultado = ''
    for c in cadena:
        if c not in numeros:
            resultado += c
        else:
            resultado += caracter
    return resultado

def insertar_cada_tres_digitos(cadena, caracter):
    #Inserta el caracter cada 3 digitos de la cadena.
    if not cadena:
        return ''
    resultado = ''
    contador = 0 
    for c in cadena:
        contador+= 1
        resultado+= c
        if contador % 3 == 0:
            resultado += caracter
    return resultado
