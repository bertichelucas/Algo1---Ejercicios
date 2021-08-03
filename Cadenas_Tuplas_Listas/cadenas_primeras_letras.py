def primeras_letras(cadena):
    #Devuelve la primera letra de cada palabra
    #dentro de una cadena
    if not cadena:
        return ''
    resultado = ''
    last = True
    for c in cadena:
        if last and c != ' ':
            resultado += c
            last = False
        if c == ' ':
            last = True
    return resultado

def primera_letra_mayus(cadena):
    #Devuelve la misma cadena con las primeras letras en mayusculas.
    if not cadena:
        return ''
    return cadena.title()

def comienzan_con_a(cadena):
    #Recibe una cadena y devuelve las palabras que comiencen con la letra a.
    if not cadena:
        return ''
    resultado = ''

    anterior = cadena[0]
    if anterior == 'a' or anterior == 'A':
        agregar = True
    else:
        agregar = False
    
    for c in cadena:
        if anterior == ' ':
            if c == 'a' or c == 'A':
                agregar = True
        if agregar:
            resultado += c
        anterior = c
        if c == ' ':
            anterior = ' '
            agregar = False

    return resultado
