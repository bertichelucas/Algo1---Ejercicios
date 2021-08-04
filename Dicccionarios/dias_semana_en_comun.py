#Escribir una función que dado un diccionario cuyas claves son los nombres de los integrantes de un grupo de amigos, 
# y los valores asociados una lista de los días de la semana que están disponibles, devuelva una lista de los días que pueden juntarse. 
# Por ejemplo, si recibe: {'Juan':['MIE', 'VIE', 'SAB'], 'Jose':['VIE', 'SAB', 'DOM'], 'Jorge':['JUE', 'VIE', 'SAB']} debe devolver ['VIE', 'SAB'].

def dias_libres_encomun(diccionario):
    resultado = []
    nuevo_diccionario = {}
    for clave in diccionario:
        for element in diccionario[clave]:
            if element not in nuevo_diccionario:
                nuevo_diccionario [element] = [clave]
            else:
                nuevo_diccionario[element].append(clave)

    for element in nuevo_diccionario:
        if len(nuevo_diccionario[element]) == len(diccionario):
            resultado.append(element)
    
    return resultado


diccionario = {
    'Juan':['MIE', 'VIE', 'SAB'], 
    'Jose':['VIE', 'SAB', 'DOM'], 
    'Jorge':['JUE', 'VIE', 'SAB']
    }

print(dias_libres_encomun(diccionario))