'''
Sabiendo que la clase Libro tiene los métodos obtener_autor y obtener_titulo que devuelven cadenas de caracteres, escribir la clase Biblioteca con los métodos:

agregar_libro que recibe un Libro y lo agrega a la colección.
sacar_libro que recibe el nombre de un título y el de un autor y lo saca de la biblioteca, devolviéndolo o levantando una excepción en caso de que los datos no correspondan con los de algún libro agregado.
contiene_libro que recibe el nombre de un título y el de un autor y devuelve True o False de acuerdo a si está en la colección o no.
'''

class Biblioteca:
    def __init__(self):
        self.coleccion = {}
    
    def agregar_libro(self, libro):
        if libro.obtener_autor not in self.coleccion:
            self.coleccion[libro.obtener_autor] = [libro]
        else:
            self.coleccion[libro.obtener_autor].append(libro)
    
    def sacar_libro(self, titulo, autor):
        if autor in self.coleccion:
            for libro in self.coleccion[autor]:
                if titulo == libro.obtener_autor:
                    self.coleccion[autor].remove(libro)
                    return libro
                else:
                    raise Exception('el libro no esta en la coleccion o los datos son erroneos')
    
    def contiene_libro(self, titulo, autor):
        if autor in self.coleccion:
            for libro in self.coleccion[autor]:
                if titulo == libro.obtener_autor:
                    return True
            return False

