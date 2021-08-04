'''
Implementar la clase Vector que replica el comportamiento de un vector de N dimensiones, de manera que se adecúe al funcionamiento mostrado por las siguientes sentencias:

>>> vector1 = Vector([3,4])                     >>> print(vector_suma)
>>> print(vector1)                              "(8, 9)"
"(3, 4)"                                        >>> vector1 + Vector([1,2,3])
>>> vector2 = Vector([])                        ValueError: No se pueden sumar dos vectores de distintas 
ValueError: No se puede crear un vector vacío   dimensiones
>>> vector2 = Vector([5, 5])                    >>> vector1.norma()
>>> vector_suma = vector1 + vector2             5
Nota: no es necesario hacer más validaciones que las que se muestran en el ejemplo.
'''

class Vector:

    def __init__(self, coordenadas):
        if not coordenadas:
            raise ValueError('No se puede crear un vector vacío')
        self.coordenadas = coordenadas
        self.dimensiones = len(coordenadas)

    def __str__(self):
        return f'{tuple(self.coordenadas)}'

    def __add__(self, otro):
        if self.dimensiones != otro.dimensiones:
            raise ValueError('No se pueden sumar dos vectores de distintas dimensiones')
        contador = -1
        resultado = []
        for coordenada in self.coordenadas:
            contador += 1
            coordenada += otro.coordenadas[contador]
            resultado.append(coordenada)
        return Vector(resultado)
    
    def norma(self):
        norma = 0
        for coordenada in self.coordenadas:
            norma += coordenada ** 2
        norma = norma ** 0.5
        return norma
