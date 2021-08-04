def palabra_mas_larga_por_caracter(texto):
    #Recibe un texto y para cada caracter
    #Guarda la palabra mas larga que contenga a ese caracter.
    resultado = {}
    for palabra in texto.split(' '):
        for caracter in palabra:
            if caracter not in resultado:
                resultado[caracter] = palabra
            elif len(palabra) > len(resultado[caracter]):
                resultado[caracter] = palabra
    return resultado

