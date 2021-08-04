'''
Escribir una función que reciba una cadena (formada únicamente por letras y espacios), 
y devuelva un diccionario donde para cada palabra muestre la cantidad de veces que es precedida por otra palabra. 
Ejemplo: “a la a hola es a es la hora a hola” → {“a”: {“hora”: 1, “es”: 1, “la”: 1}, “hola”: {“a”: 2}, ... }
'''

def cant_precesores_por_palabra(cadena):
    resultado = {}
    lista_palabras = cadena.split(' ')
    anterior = None
    for palabra in lista_palabras:
        if palabra not in resultado:
            resultado[palabra] = {}
        if anterior != None:
            if anterior not in resultado[palabra]:
                resultado[palabra][anterior] = 1
            else:
                resultado[palabra][anterior] += 1
        anterior = palabra
    return resultado

