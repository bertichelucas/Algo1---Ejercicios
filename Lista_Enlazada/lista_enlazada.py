class Nodo:
    def __init__(self, dato =None, prox = None):
        self.prox = prox
        self.dato = dato

    def __str__(self):
        return str(self.dato)


def ver_lista(nodo):
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox

'''
Todos los metodos que se hacen tienen mas o menos esta forma
La condicion varia segun que necesite el metodo 
actual = self.prim
while <condicion actual>:
    ...
    actual = actual.prox
'''

class ListaEnlazada:

    def __init__(self):
        self.prim = None
        self.len = 0
    
    def __str__(self):
        #print para la lista enlazada.
        actual = self.prim
        
        s = '{'
        while actual:
            s += f'[{actual.dato}] -> '
            actual = actual.prox
        
        return s.rstrip(' -> ') + '}'

    def __len__(self):    
        return self.len

    def append(self, dato):
        #Agrega el dato al final de la lista.
        n = Nodo(dato, None)
        if self.prim:
            nodo_actual = self.prim
            while nodo_actual.prox != None:
                nodo_actual = nodo_actual.prox
            nodo_actual.prox = n
        else:
            self.prim = n
        self.len += 1

    def insert(self, dato, posicion):
        #Inserta un dato en la posicion dada.
        if posicion < 0:
            raise IndexError
        if posicion == 0:
            self.prim = Nodo(dato= dato, prox = self.prim)
            self.len += 1 
            return
        nodo_actual = self.prim
        indice = 0 
        while indice < posicion -1:
            if not nodo_actual:
                raise IndexError
            nodo_actual = nodo_actual.prox
            indice += 1
        nuevo_nodo = Nodo(dato = dato, prox = nodo_actual.prox)
        nodo_actual.prox = nuevo_nodo
        self.len += 1

    def remover_todos(self, dato):
        #Vacia la lista enlazada.
        anterior = None
        nodo_actual = self.prim
        while nodo_actual:
            if nodo_actual.dato == dato:
                self.len -= 1
                if not anterior:
                    self.prim = nodo_actual
                else:
                    anterior.prox = nodo_actual.prox
            else:
                anterior = nodo_actual
                nodo_actual = nodo_actual.prox
    
    def pop(self, posicion = None):
        #Remueve el elemento de la posicion dada. Si no se especifica la posicion, se remueve el ultimo.
        if posicion == None:
            posicion = self.len - 1
        
        if posicion < 0 or posicion >= self.len:
            raise IndexError('Fuera de Rango')

        if posicion == 0:
            dato = self.prim.dato
            self.prim= self.prim.prox
        else:
            nodo_actual = self.prim
            indice = 0
            while indice < posicion - 1:
                nodo_actual = nodo_actual.prox
                indice += 1 
            dato = nodo_actual.prox.dato
            print(dato)
            nodo_actual.prox = nodo_actual.prox.prox
        self.len -= 1
        return dato
    
    def remove(self, dato):
        #Remueve la primera aparicion del dato en la lista.
        if self.prim == None:
            raise ValueError('La Lista se encuentra Vacia')
        
        if self.prim.dato == dato:
            self.prim = self.prim.prox
        else:
            nodo_anterior = self.prim
            nodo_actual = nodo_anterior.prox
            while  nodo_actual is not None and nodo_actual.dato != dato:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.prox
            
            if nodo_actual == None:
                raise ValueError('El valor no se encuentra en la lista')
            nodo_anterior.prox = nodo_actual.prox
        self.len -= 1

    def duplicar(self, elemento):
        #Duplica el elemento para cada aparicion del mismo dentro de la lista.
        if self.prim == None:
            return
        nodo_actual = self.prim
        duplicado = False
        while nodo_actual != None:
            if nodo_actual.dato == elemento and duplicado == False:
                self.len += 1
                proximo = nodo_actual.prox
                nodo_actual.prox = Nodo(dato = elemento, prox= proximo)
                duplicado = True
            else:
                duplicado = False
            nodo_actual = nodo_actual.prox

    def filter(self, f):
        #Remueve todos los elementos de la lista para los cuales la funcion f da false.
        res = ListaEnlazada()
        if self.prim == None:
            return res
        nodo_actual = self.prim
        ultimo = None
        while nodo_actual:
            dato = nodo_actual.dato
            if f(dato):
                res.len += 1
                nuevo = Nodo(dato = dato)
                if ultimo:
                    ultimo.prox = nuevo
                else:
                    res.prim = nuevo
                ultimo = nuevo
            nodo_actual = nodo_actual.prox
        return res

    def map(self, f):
        #Aplica la funcion f a todos los elementos de la lista.
        nodo_actual = self.prim
        res = ListaEnlazada()
        ultimo = None
        while nodo_actual:
            dato = nodo_actual.dato
            nuevo = Nodo(dato = f(dato))
            if ultimo:
                ultimo.prox = nuevo
            else:
                res.prim = nuevo
            ultimo = nuevo
            nodo_actual = nodo_actual.prox
        return res

    def merge(self, lista):
        #Recibe una lista que debe estar ordenada. Hace el merge
        #entre ambas listas en la actual. La lista actual tambien debe estar
        #ordenada.
        res = ListaEnlazada()
        if lista.prim == None:
            return
        if self.prim == None:
            return lista
        nodo_actual_a = self.prim
        nodo_actual_b = lista.prim
        while nodo_actual_a and nodo_actual_b:
                if nodo_actual_a.dato < nodo_actual_b.dato:
                    res.append(nodo_actual_a.dato)
                    nodo_actual_a = nodo_actual_a.prox
                else:
                    res.append(nodo_actual_b.dato)
                    nodo_actual_b = nodo_actual_b.prox
                if nodo_actual_b == None:
                    res.append(nodo_actual_a.dato)
                elif nodo_actual_a == None:
                    res.append(nodo_actual_b.dato)
        return res


    def invertir(self):
        #Inverte la lista enlazada.
        if self.prim == None:
            return
        primero = None
        for _ in range(self.len):
            nodo_actual = self.prim
            ultimo = None
            while nodo_actual.prox != None:
                ultimo = nodo_actual
                nodo_actual = nodo_actual.prox
            if primero == None:
                primero = nodo_actual
            if ultimo != None:
                ultimo.prox = None
            nodo_actual.prox = ultimo
        self.prim = primero
        

    def rotar(self, N):
        #Permite rotar n posiciones en la lista enlazada.
        if self.prim == None:
            return
        nodo_actual = self.prim
        indice = 0
        while N > self.len:
            N -= self.len
        referencia_primero = self.prim
        while nodo_actual.prox != None:
            indice += 1
            nodo_actual = nodo_actual.prox
            if indice == N:
                self.prim = nodo_actual
            if nodo_actual.prox == None:
                nodo_actual.prox = referencia_primero
            if nodo_actual.prox == self.prim:
                nodo_actual.prox = None
    
    def eliminar_posiciones(self, lista):
        #Recibe una lista con las posiciones a eliminar en la lista enlazada.
        if self.prim == None:
            return
        if not lista:
            return 
        nodo_actual = self.prim
        indice = 0
        while nodo_actual != None:
            for item in lista: 
                if item < 0 or item >= self.len:
                    raise IndexError('Fuera de rango')
                if item == 0 and indice == 0:
                    self.prim = nodo_actual.prox
                elif item == indice + 1:
                    nodo_actual.prox = nodo_actual.prox.prox
                    indice += 1
            nodo_actual = nodo_actual.prox
            indice += 1
        self.len = indice

    def suma_acumulativa(self):
        #Devuelve una nueva lista (del mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos de la lista original hasta el nodo i.
        res = ListaEnlazada()
        if self.prim == None:
            return res
             
        nodo_actual = self.prim.prox
        valor = self.prim.dato
        anterior = Nodo(nodo_actual.dato)
        res.prim = anterior

        while nodo_actual:
            valor += nodo_actual.dato

            nuevo_nodo = Nodo(valor)
            anterior.prox = nuevo_nodo
            anterior = nuevo_nodo

            nodo_actual = nodo_actual.prox    
        return res

    def distribuir_en_colas(self, k):
        #Distribuye los elementos de la lista en k colas.
        from cola import Cola
        colas = [Cola() for _ in range(k)]
        nodo_actual = self.prim 
        indice = 0
        while nodo_actual:
            colas[indice % len(colas)].encolar(nodo_actual.dato)
            nodo_actual = nodo_actual.prox
            indice += 1
        return colas
        
    def unir_medio(self, le):
        #Inserta la lista enlazada pasada por parametro en medio de la original.
        if self.prim == None:
            raise ValueError('La lista esta vacia')
        if le.prim == None:
            raise ValueError('La lista esta vacia')
        if self.prim.prox == None:
            self.prim.prox = le.prim
            le.prim = None
        else:
            nodo_actual = self.prim
            ultimo = nodo_actual
            contador = 0
            while nodo_actual.prox != None:
                contador += 1
                if contador % 2 != 0 and contador != 1:
                    ultimo = ultimo.prox
                nodo_actual = nodo_actual.prox
        
        final = ultimo.prox
        ultimo.prox = le.prim
        nodo_le = le.prim
        while nodo_le.prox != None:
            nodo_le = nodo_le.prox
        nodo_le.prox = final
        le.prim = None

    def swap(self, x, y):
        #Swapea dos posiciones de una lista enlazada.
        if self.prim == None:
            raise IndexError('La lista esta vacia')
        nodo_actual = self.prim
        contador = -1
        ultimo = nodo_actual
        ult_x = None
        ult_y = None
        while nodo_actual:
            contador += 1
            if contador == x:
                nodo_x = nodo_actual
                if contador != 0:
                    ult_x = ultimo
            if contador == y:
                nodo_y = nodo_actual
                if contador != 0:
                    ult_y = ultimo
            ultimo = nodo_actual
            nodo_actual = nodo_actual.prox

        if x > contador or y > contador or x < 0 or y < 0:
            raise IndexError('out of range')

        if nodo_x and nodo_y:
            if ult_x:
                ult_x.prox = nodo_y
            else:
                self.prim = nodo_y
            prox_y = nodo_y.prox
            nodo_y.prox = nodo_x.prox
            if ult_y:
                ult_y.prox = nodo_x
            else:
                self.prim = nodo_x
            nodo_x.prox = prox_y

    def menor_elemento_al_inicio(self):
        # Busca el menor elemento y lo guarda al princpio de la lista.
        if self.prim == None:
            return
        nodo_actual = self.prim
        dato = nodo_actual.dato
        ultimo = None
        nodo_modificable = None
        while nodo_actual.prox:
            ultimo = nodo_actual
            nodo_actual = nodo_actual.prox
            if nodo_actual.dato < dato:
                dato = nodo_actual.dato
                nodo_modificable = nodo_actual
                anterior = ultimo
        if nodo_modificable:
            anterior.prox = nodo_modificable.prox
            nodo_modificable.prox = self.prim
            self.prim = nodo_modificable

    def downsample(self, k):
        #Elimina todo elemento cuya posicion no sea multiplo del numero k.
        contador = 1
        actual = self.prim.prox
        anterior = self.prim
        while actual:
            if contador % k != 0:
                anterior.prox = actual.prox
            else:
                anterior = actual
            contador += 1
            actual = actual.prox
    '''
    def borrar_ultimo(self):
        #Elimina el ultimo elemento de la lista enlazada.
        actual = self.prim
        anterior = None
        while actual:
            anterior = actual
            actual = actual.prox
        anterior.prox = None
    '''
    def eliminar_consecutivos(self):
        #Elimina los elementos repetidos consecutivos de la lista enlazada.
        actual = self.prim
        anterior = actual
        while actual:
            if actual.dato == anterior.dato:
                anterior.prox = actual.prox 
            else:
                anterior = actual
            actual = actual.prox

