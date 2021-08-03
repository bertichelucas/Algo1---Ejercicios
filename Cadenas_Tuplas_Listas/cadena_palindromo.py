def palindromo(cadena):
    #Indica si la cadena es un palindromo. No toma en cuenta los espacios.
    #Devuelve true si la cadena es palindromo, false en caso contrario.
    if cadena == '':
        return True
    lista = cadena.split(' ')
    palindromo = ''
    for palabra in lista:
        palindromo += palabra

    mitad = len(palindromo) // 2

    if palindromo[mitad + 1] == palindromo [mitad]:
        return _palindromo(palindromo, mitad, mitad + 1, len(palindromo))
    elif palindromo[mitad - 1] == palindromo[mitad]:
        return _palindromo(palindromo, mitad -1, mitad, len(palindromo))

    return _palindromo(palindromo, mitad -1, mitad + 1, len(palindromo))
    

def _palindromo(palindromo, mitad, igual, n): 
    #Recursividad en palindromo.
    if mitad < 0 or igual >= n:
        return True
    
    if palindromo[mitad] != palindromo[igual]:
        return False
    
    return _palindromo(palindromo, mitad -1, igual + 1, n)
   

print(palindromo(''))