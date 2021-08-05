def es_palindromo(cola, n):
    from pila import Pila
    from cola import Cola
    '''
    Escribir una función que reciba una cola y la cantidad de
    elementos en la misma, y devuelva True si los elementos forman
    un palíndromo o False si no.

    Por ejemplo: es palindromo([n, e, u, q, u, e, n], 7) −> True
    '''
    auxiliar = Pila()
    for _ in range(n//2):
        auxiliar.apilar(cola.desencolar())
    
    if n % 2 != 0:
        cola.desencolar()
    
    while not auxiliar.esta_vacia and not cola.esta_vacia:
        if cola.desencolar() != auxiliar.desapilar():
            return False
    return True