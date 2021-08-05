def contar_digitos(n):
    #Cuenta la cantidad digitos de un numero n.
    if n < 10:
        return 1
    else:
        n = n / 10
        return 1 + contar_digitos(n)


         