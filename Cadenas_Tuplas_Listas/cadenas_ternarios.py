def subcadenas(cadena, subcadena):
    #Indica si la subcadena forma parte de la cadena. 
    return True if subcadena in cadena else False

print(subcadenas('pelotudo', 'pelo'))

def ordenalfabetico(primero, segundo):
    #Devuelve el menor en orden alfabetico.
   return primero if primero < segundo else segundo

print(ordenalfabetico('ella', 'peron'))
