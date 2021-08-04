#dada una matriz representada como una lista de listas de numeros(donde cada sublista representa una fila)
#devolver una lista con los maximos de cada columna
# Ejemplo
# maximos_columnas([1, 2, 8, 4],
#                  [6, 7, 3, 3]    -- [6, 7, 8, 9]
#                  [6, 5, 4, 9])

def maximos_columnas(matriz):
    resultado = []
    maximos = matriz[0]
    long_fila = len(maximos)
    for fila in matriz:
        for i in range(long_fila):
            if fila[i] > maximos[i]:
                maximos[i] = fila[i]
    return maximos
    
print(maximos_columnas([[1,2,8,4],[6,7,3,3],[6,5,4,9]]))