#Un grupo de amigos quieren juntarse a cenar pero tienen todos calendarios muy ajustados y les es difícil ver qué días pueden juntarse todos. 
# Se pide escribir una función que reciba un diccionario con los nombres de cada persona, 
# y que como valor asociado tenga los días del mes en los que esa persona no puede juntarse (una lista de números, que pueden ser del 1 al 31), 
# y que devuelva un diccionario con todos los días como claves (también del 1 al 31), y como valor qué amigos pueden asistir cada día.

def dias_en_comun(diccionario):
    resultado = {}
    
    for clave in diccionario:
        dias_ocupados = []
        for dia in diccionario[clave]:
            dias_ocupados.append(dia)
        for i in range(1, 32):
            if i not in dias_ocupados:
                if i not in resultado:
                    resultado[i] = [clave]
                else:
                    resultado [i].append(clave)                
    return resultado

dic = {
    'juan' : [1,4,5,7,9,15,16,17,18,23,26,28],
    'ricardo' : [1,3,7,11,14,23,24,25,26,27,28,29,31],
    'fernando': [2,5,7,8,10,12,14,16,17,20,22,24],
    'enrique' : [5,10,15,20,26,30]
    }

print(dias_en_comun(dic))