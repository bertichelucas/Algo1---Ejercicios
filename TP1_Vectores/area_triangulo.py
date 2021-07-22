import vectores
def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Recibe las coordenadas de 3 puntos en R3 ydevuelve el area del triangulo que conforman"""
    ax, ay, az = vectores.diferencia(x1, y1, z1, x2, y2, z2) # Calculo coordenadas del primer vector a partir de dos puntos
    bx, by, bz = vectores.diferencia(x1, y1, z1, x3, y3, z3) # Calculo coordenadas del segundo vector a partir de dos puntos
    px, py ,pz = vectores.producto_vectorial(ax, ay, az, bx, by, bz) # calculo coordenadas del vector dado por el producto vectorial entre coordenadas del primer y segundo vector
    norma = vectores.norma(px, py, pz) #calculo la norma del vector encontrado en la linea 6 con el producto vectorial
    area = norma / 2 #calculo del area del triangulo por definicion
    return area

print(area_triangulo(1, 2, 3, 3, 2, 1, 2, 3, 2))
print(area_triangulo(1, 7, 3, 5, 4, -1, 3, 2, 3))
print(area_triangulo(9, 8, 7, 6, 5, 4, 3, 2, 1))