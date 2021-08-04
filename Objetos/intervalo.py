
class IntervaloNegativo(Exception):
    pass

class InterseccionNula(Exception):
    pass

class UnionNula(Exception):
    pass

#Representa un intevalo entre dos instantes de tiempo.
class Intervalo:

    def __init__(self, desde, hasta):
        if desde >= hasta:
            raise IntervaloNegativo('el intervalo no puede ser negativo (desde < hasta)')
        self.desde = desde
        self.hasta = hasta
    
    def __duracion__(self):
        #Devuelve la duracion del intervalo en segundos.
        duracion = self.hasta - self.desde
        return duracion
    
    def __interseccion__(self, otro):
        #Recibe otro intervalo y devuelve la interseccion.
        if self.desde >= otro.desde:
            inicio_inter = self.desde
        else:
            inicio_inter = otro.desde

        if self.hasta >= otro.hasta:
            fin_inter = otro.hasta
        else:
            fin_inter = self.hasta

        if fin_inter < inicio_inter:
            raise InterseccionNula('no hay interseccion')

        return Intervalo(inicio_inter, fin_inter)
        

    def __union__(self, otro):
        #Recibe otro intervalo y devuelve la union.
        if self.desde <= otro.desde:
            inicio_union = self.desde
        else:
            inicio_union = otro.desde

        if self.hasta <= otro.hasta:
            fin_union = otro.hasta
        else:
            fin_union = self.hasta

        if (not self.desde == otro.hasta or not self.hasta == otro.desde) and (self.hasta < otro.desde or otro.hasta < self.desde):
            raise UnionNula('no hay union')
        return Intervalo(inicio_union, fin_union)

