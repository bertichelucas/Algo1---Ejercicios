'''
Implementar la clase CajaFuerte que reproduzca el siguiente comportamiento:

>>> caja = CajaFuerte(9158)
>>> caja.esta_abierta()
False
>>> caja.guardar("pulsera")
Exception: La caja fuerte está cerrada
>>> caja.abrir(1234)
Exception: La clave es inválida
>>> caja.abrir(9158)
>>> caja.esta_abierta()
True
>>> caja.guardar("pulsera")
>>> caja.guardar("reloj de oro")
Exception: No se puede guardar más de una cosa
>>> caja.cerrar()
>>> caja.sacar()
Exception: La caja fuerte está cerrada
>>> caja.abrir(9158)
>>> caja.sacar()
'pulsera'
>>> caja.sacar()
Exception: No hay nada para sacar
'''

class CajaFuerte:

    def __init__(self, clave):
        self.clave = clave
        self.estado = False
        self.interior = ''
    
    def esta_abierta(self):
        return self.estado
    
    def abrir(self, ingreso):
        if ingreso != self.clave:
            raise Exception('La clave es inválida')
        self.estado = True
    
    def cerrar(self):
        self.estado = False

    def guardar(self, objeto):
        if self.estado == False:
            raise Exception ('La caja fuerte está cerrada')
        if self.interior != '':
            raise Exception('No se puede guardar más de una cosa')
        self.interior = objeto
    
    def sacar(self):
        if self.estado == False:
            raise Exception ('La caja fuerte está cerrada')
        if self.interior == '':
            raise Exception('No hay nada para sacar')
        removido = self.interior
        self.interior = ''
        return removido

