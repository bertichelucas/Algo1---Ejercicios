def maximo_comun_divisor(m, n):
    'Devuelve el maximo comun divisor entre dos numeros.'
    while True:
        resto = m % n
        if resto == 0:
            return n
        else:
            m = n
            n = resto
    
