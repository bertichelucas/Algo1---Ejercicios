
def es_palindromo(cadena):
    #Devuelve si una cadena es o no palindromo.
    if not cadena:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])