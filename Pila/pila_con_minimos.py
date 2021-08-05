from pila import Pila

class pila_min():
    #Pila con minimos
    def __init__(self):
        self.pila = Pila()
        self.minimos = Pila()

    def apilar(self, dato):
        #Al apilar, si es menor al tope de minimos, apila en minimos.
        self.pila.apilar(dato)
        if self.minimos.esta_vacia():
            self.minimos.apilar(dato)
        elif dato <= self.minimos.ver_tope():
            self.minimos.apilar(dato)

    def desapilar(self):
        #Al desapilar, si coincide el minimo con el desapilado, se desapila.
        dato = self.pila.desapilar()
        if dato == self.minimos.ver_tope():
            self.minimos.desapilar()
        return dato 
    
    def ver_min(self):
        return self.minimos.ver_tope()
