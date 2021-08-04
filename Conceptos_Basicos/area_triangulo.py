import vectores
def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Recibe las coordenadas de 3 puntos en R3 y devuelve el area del triangulo que conforman"""
    ax, ay, az = vectores.diferenciavectorial(x1, y1, z1, x2, y2, z2)
    bx, by, bz = vectores.diferenciavectorial(x1, y1, z1, x3, y3, z3)
    px, py ,pz = vectores.producto_vectorial(ax, ay, az, bx, by, bz) 
    norma = vectores.norma(px, py, pz)
    return norma / 2

