from cola import Cola
'''
Escribir una función tail, que recibe una ruta a un archivo de texto y un número n, y que imprima por pantalla las últimas n líneas del archivo. 
No está permitido almacenar todo el archivo en memoria ni recorrer el archivo más de una vez.
'''
def tail(ruta, n):
    cola = Cola()
    count = 0
    with open(ruta) as archivo:
        for linea in archivo:
            if count < n:
                cola.encolar(linea.rstrip())
                count += 1
            else:
                cola.desencolar()
                cola.encolar(linea.rstrip())
    while not cola.esta_vacia():
        print(cola.desencolar())        