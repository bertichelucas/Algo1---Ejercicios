def inversion(C,X,N):
    'Recibe una cantidad de pesos, tasa de interes y numero de años y devuelve el monto final a obtener'
    return C * ((1 + (X / 100)) ** N)

