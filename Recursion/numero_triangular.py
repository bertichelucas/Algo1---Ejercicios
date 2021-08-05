def numero_triangular(n):
    #Calcula el n-esimo numero triangular.
    if n == 1:
        return 1
    return n + numero_triangular(n - 1)

