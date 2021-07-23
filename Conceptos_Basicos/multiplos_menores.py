def multiplos_menores(a, b):
    'Recibe dos numeros como parametros y devuelve cuantos numeros multiplos del primero hay que sean menores que el segundo.'
    suma = 0
    for i in range(a, b):
        if i % a == 0:
            suma += 1 
    return suma

