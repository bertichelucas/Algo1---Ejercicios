def campana_electoral(nombres, n, p):
    #Recibe una tupla de nombres, una cantidad n y
    #una posicion de origen.
    #Pide para n nombres desde origen un voto.
    contador = -1
    cantidad = 0
    for element in nombres:
        contador += 1
        if contador >= p:
            print('Estimado ', element, ' vote por mi')
            cantidad += 1
        if cantidad == n:
            break
