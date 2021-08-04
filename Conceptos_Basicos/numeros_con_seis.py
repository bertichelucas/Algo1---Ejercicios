def numeros_con_seis(numero):
    #Dado un numero, devuelve en cuantos numeros del 0 al numero
    #tienen un 6 entre sus digitos.
    resultado = 0
    for i in range(numero +1):
        num = i
        if '6' in str(num):
            resultado += 1
    return resultado


