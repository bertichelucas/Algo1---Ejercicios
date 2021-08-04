#Dado un diccionario cuyas claves son strings y sus valores son listas de enteros, escribir una función que invierta dicho diccionario de la siguiente forma: 
# cada valor de cada lista pasará a ser una clave del diccionario resultante, que tendrá como valor una lista de todas las claves en las que era un valor. 
# Por ejemplo, d = {"clave_1": [1,2,3], "clave_2": [4,6], "clave_3": [1,4]} dara como resultado {1: ["clave_1", "clave_3"], 2: ["clave_1"], 3: ["clave_1"], 4: ["clave_2", "clave_3"], 6: ["clave_2"]}.

def diccionario_invertido(d):
    nuevo_d = {}
    for clave in d:
        for elemento in d[clave]:
            if elemento not in nuevo_d:
                nuevo_d[elemento] = [clave]
            else:
                nuevo_d[elemento].append(clave)
    return nuevo_d

d = {
    "clave_1": [1,2,3], 
    "clave_2": [4,6], 
    "clave_3": [1,4]
    }

print(diccionario_invertido(d))