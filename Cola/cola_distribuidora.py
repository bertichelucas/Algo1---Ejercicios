from cola import Cola

'''
Implementar la clase ColaDistribuidora con los siguientes métodos:
* ColaDistribuidora(ids, f): Crea una nueva instancia. ids es una lista de identificadores (cadenas), y f es una función que recibe cualquier cosa y devuelve siempre uno de los identificadores de la lista ids.
* encolar(elemento): Aplica la funcion f al elemento, y según el identificador obtenido encola el elemento en una cola específica para ese identificador.
* desencolar(identificador): Desencola y devuelve el elemento al frente de la cola para el identificador dado.
'''

class ColaDistribuidora:
    def __init__(self, ids, f):
        self.ids = ids
        self.colas = [Cola() for _ in range(len(self.ids))]
        self.funcion = f
    
    def encolar(self, elemento):
        posicion = self.ids.index(self.funcion(elemento))
        self.colas[posicion].encolar(elemento)
        
    def desencolar(self, identificador):
        posicion = self.ids.index(identificador)
        if self.colas[posicion].frente != None:
            elemento = self.colas[posicion].desencolar()
        else:
            raise IndexError('La lista esta vacia')
        return elemento
    
    def esta_vacia(self):
        for cola in self.colas[:]:
            if not cola.esta_vacia():
                return False
        return True

