import math

def perimetro_rectangulo(a,b):
    'Perimetro del rectangulo dada su base y altura'

    return 2 * b + 2 * a

def area_rectangulo(a,b):
    'Area del rectangulo dada su base y altura'
    return b * a  

def area_rectangulo_coordenadas(xa, xb, ya ,yb):
    'Area del rectangulo con coordenadas xa xb ya yb'
    b = xb - xa
    a = yb - ya
    return b * a 

def perimetro_circulo(a):
    'Perimetro de un circulo dado su radio'
    return math.pi * a * 2

def area_circulo(a):
    'Area de un circulo dado su radio'
    return math.pi * a ** 2

def hipotenusa(ca,cb):
    'Hipotenusa de un triangulo rectangulo dados sus catetos'
    return (ca ** 2 + cb ** 2) ** 0.5