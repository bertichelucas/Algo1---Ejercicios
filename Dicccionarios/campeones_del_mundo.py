def campeones_mundo(lista):
    #Recibe una lista de tuplas con formato año, pais.
    #Devuelve un diccionario con clave pais y de dato la cantidad de mundiales ganados.
    dic = {}
    for tupla in lista:
        _, pais = tupla
        if pais not in dic:
            dic[pais] = 1
        else:
            dic[pais] += 1
    return dic

def mayores_campeones(dic):
    #Recibe un diccionario de  campeones y devuelve una lista con los que mas copas ganaron.
    lista =[]
    mayor = 0
    for clave in dic:
        numero = dic[clave]
        if numero > mayor:
            lista = []
            mayor = numero
            lista.append(clave)
        elif numero == mayor:
            lista.append(clave)
    return lista
