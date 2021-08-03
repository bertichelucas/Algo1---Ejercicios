def separar_numero_miles(cadena):
    #Recibe una cadena que contiene un numero entero 
    #y la separa en miles.
    resultado = ''
    largo = len(cadena)
    
    puntos = largo// 3
    resto = largo % 3
    if resto == 0:
        puntos -= 1

    contador = 0

    for c in cadena:
        contador += 1
        resultado += c
        if contador % 3 == 0 and puntos != 0:
            resultado +=  '.'
            puntos -= 1

        if resto != 0:
            contador -= 1
            resto -= 1
            if resto == 0:
                resultado += '.'
                puntos -= 1    
    
    return resultado

print(separar_numero_miles('111121'))