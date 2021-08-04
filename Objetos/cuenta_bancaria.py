'''
Escribir una clase Cuenta que tenga el siguiente comportamiento:

>>> c = Cuenta('Pérez')              >>> d = Cuenta('López')
>>> c.acreditar(100, 'Sueldo')       >>> c.transferir(30, d)
>>> c.extraer(60, 'Shopping')        >>> c.saldo()
>>> c.saldo()                        10
40                                   >>> d.saldo()
>>> print(c)                         30
Cuenta de Pérez

>>> c.movimientos()
[('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
>>> d.movimientos()
[('acreditación',30,'Cuenta de Pérez')]
>>> d.extraer(100, 'Deudas')
ERROR ValueError: Fondos Insuficientes  
'''

class Cuenta:
    
    def __init__(self, apellido):
        self.apellido = apellido
        self.fondos = 0
        self.operaciones = []
    
    def saldo(self):
        return self.fondos

    def __str__(self):
        return f'Cuenta de {self.apellido}'
    
    def movimientos(self):
        return self.operaciones

    def acreditar(self, cantidad, razon):
        self.fondos += cantidad
        self.operaciones.append(('acreditación',cantidad, razon))
    
    def extraer(self, cantidad, razon):
        if self.fondos - cantidad < 0:
            raise ValueError('Fondos Insuficientes')
        self.fondos -= cantidad
        self.operaciones.append(('extracción',cantidad, razon))

    def transferir(self, cantidad, cuenta):
        if self.fondos - cantidad < 0:
            raise ValueError('Fondos Insuficientes')
        self.fondos -= cantidad
        cuenta.fondos += cantidad
        self.operaciones.append(('extracción',cantidad, f'Cuenta de {cuenta.apellido}'))
        cuenta.operaciones.append(('acreditación',cantidad, f'Cuenta de {self.apellido}'))

