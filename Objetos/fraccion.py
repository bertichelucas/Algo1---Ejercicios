from math import gcd

class DenIsZero(Exception):
    pass

class Fraccion:
    def __init__(self, num, den):
        if den == 0:
            raise DenIsZero('el denominador no puede ser cero')
        divisor = gcd(num,den)
        self.numerador = num // divisor
        self.denominador = den // divisor
    
    def sumar(self, otra):
        num_res = self.numerador * otra.denominador + otra.numerador * self.denominador
        den_res = self.denominador * otra.denominador
        return Fraccion(num_res, den_res)

    def __mul__(self, otra):
        num_res = self.numerador * otra.numerador
        den_res = self.denominador * otra.denominador
        return Fraccion(num_res, den_res)
    
    def __eq__(self, otra):
        return self.numerador == otra.numerador and self.denominador == otra.denominador

    def __str__(self):
        return f"{self.numerador} / {self.denominador}"
    
    def __repr__(self):
        return self.__str__()
