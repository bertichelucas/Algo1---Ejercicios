def es_primo(n):
    'Calcula si un numero entero es primo o no '
    for i in range (2, int((n+ 1) ** 0.5)):
        if n % i == 0:
            return False
    return True

def filtrar_primos(numeros):
    '''
    Recibe una lista de numeros y devuelve una nueva lista con
    los numeros primos.
    '''
    listafinal= []
    for i in numeros:
        if es_primo(i):
            listafinal += [i]
    return listafinal

def promedio(numeros):
    ' Recibe una lista de numeros y devuelve el promedio'
    suma = 0
    cont = 0 
    for num in numeros:
        suma += 1 
        cont += 1
    return suma / cont


def factorial_de_numeros(numeros):
    '''
    Recibe una lista de numeros y devuelve una lista  con
    el factorial de cada numero
    '''
    res = []
    for i in numeros:
        res.append(factorial(i))
    return res

def factorial(n):
    'Funcion aux para calcular el factorial.'
    fact = 1
    for i in range(1, n):
        fact = fact * i
    return fact

