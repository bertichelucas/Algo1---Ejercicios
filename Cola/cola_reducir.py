#Escribir una funcion reducir que reciba por parametro una cola y una funcion f de dos parametros
# y aplique sucesivamente la funcion f a los dos primeros elementos de la cola luego de de desencolarlos
# y encole el resultado hasta que solo quede un elemento. La funcion reducir debe devolver el unico elemento restante en la cola

from cola import Cola

def  cola_reducir(cola, funcion):
    while not cola.esta_vacia():
        x = cola.desencolar()
        if not cola.esta_vacia():
            y = cola.desencolar()
        else:
            return x
        cola.encolar(funcion(x, y))

