def producto_escalar(primero, segundo):
    #Recibe dos vectores y devuelve su producto escalar.
    resultado = 0
    for contador in range(len(primero)):
        a = primero[contador]
        b = segundo[contador]
        resultado += a * b
    return resultado



    