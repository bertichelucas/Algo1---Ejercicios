def sumadedivisores(n):
    'Devuelve la suma de los divisores de un numero'
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def numeros_amigos(m):
    'Imprime las primeras m parejas de numeros amigos.'
    a = 0 
    b = 0
    numerom = 0
    while numerom != m:
        a += 1
        b = sumadedivisores(a)
        if sumadedivisores(b) == a and a != b:
            numerom += 1
            print(a, ' ', b)        

