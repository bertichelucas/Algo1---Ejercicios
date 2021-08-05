#Cola con prioridad, si hay items en la cola de prioridad, se desapilan primero.

from cola import Cola

class ColaConPrioridad:
    def __init__(self):
        self.normales = Cola()
        self.prioritarios = Cola()

    def encolar(self, dato):
        self.normales.encolar(dato)

    def encolar_prioritario(self, dato):
        self.prioritarios.encolar(dato)

    def desencolar(self):
        if self.prioritarios.esta_vacia():
            return self.normales.desencolar()
        return self.prioritarios.desencolar()

    def esta_vacia(self):
        return self.normales.esta_vacia() and self.prioritarios.esta_vacia()