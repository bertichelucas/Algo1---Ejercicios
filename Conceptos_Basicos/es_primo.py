def es_primo(n):
    'Calcula si un numero entero es primo o no '
    for i in range (2, int((n+ 1) ** 0.5)):
        if n % i == 0:
            return False
    return True

#desde el punto de vista de eficiencia puedo tratar de hacer menos rango en el for, usando la raiz cuadrada de n +1 en el segundo miembro

