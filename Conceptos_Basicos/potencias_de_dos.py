def es_potencia_de_dos(n):
    'Calcula si un numero es o no potencia de dos.'
    while n > 2:
        if  n ** 0.5 != float:
            n = n / 2
        else:
            n = n ** 0.5
    
    if n == 2:
        return True 
    return False

def multiples_potencias_de_dos(m, n):
    'Calcula dentro de un rango entre dos numeros m y n la suma de todos aquellos numeros que son potencia de dos'
    suma = 0
    for i in range(m, n):
        if es_potencia_de_dos(i) == True:
            suma += i
    return suma


