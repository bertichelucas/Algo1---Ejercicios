class ListaCircular:

    def append(self, dato):
        if self.prim:
            n = _Nodo(dato, self.prim)
            nodo_actual = self.prim
            while nodo_actual.prox != self.prim:
                nodo_actual = nodo_actual.prox
            nodo_actual.prox = n
        else:
            n = _Nodo(dato, None)
            self.prim = n
            self.prim.prox = n
        self.cant += 1

    def pop(self, i=None):
        if i == None:
            i = self.cant - 1
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            nodo_actual = self.prim
            indice = 0
            while indice < i - 1:
                nodo_actual = nodo_actual.prox
                indice += 1
            dato = nodo_actual.dato
            nodo_actual.prox = nodo_actual.prox.prox
        self.cant -= 1
        return dato

    def __len__(self):
        return self.cant

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox