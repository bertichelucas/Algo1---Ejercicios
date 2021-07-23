def matriz_identidad(n):
    'Recibe un numero n e imprime la matriz identidad de n * n'
    for filas in range(n):
        for columnas in range (n):
            if filas == columnas:
                print('1', end = ' ')
            else:
                print('0', end = ' ')
        print()
        
