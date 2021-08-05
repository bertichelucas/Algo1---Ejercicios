def es_potencia(n, b):
    #Recibe dos numeros enteros, devuelve true
    #si n es potencia de b.
    if n == 1 or n == b:
        return True
    n = n / b
    if n < b:
        return False
    elif n > b:
        return es_potencia(n, b)
    else:
        return True