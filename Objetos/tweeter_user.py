'''
Se pide implementar la clase TwitterUser con los siguientes métodos:

__init__(): recibe como parámetro el nombre del usuario.
tweet(): recibe como parámetro un mensaje (se debe validar que no sobrepase los 280 caracteres) 
y lo agrega —con la fecha actual— a la lista de tuits del usuario. (Para obtener la fecha actual, se puede importar el módulo datetime, e invocar datetime.datetime.now())
follow(): recibe como parámetro otro usuario (de tipo TwitterUser) y lo guarda como un usuario al que se está siguiendo.
get_timeline(): devuelve una lista con los mensajes que tuitearon los usuarios a los que se está siguiendo. 
Debe ser una lista de tuplas tal que: (fecha, nombre_usuario, mensaje). Este método no toma parámetros, y la lista devuelta debe estar ordenada por fecha.

'''

import datetime

class TwitterUser:

    def __init__(self, usuario):
        self.usuario = usuario
        self.tuits = []
        self.siguiendo = []

    def __tweet__(self, mensaje):
        if len(mensaje) < 280:
            self.tuits.append((datetime.datetime.now(), mensaje))
        
    
    def __follow__(self, otro):
        self.siguiendo.append(otro)

    def __get_timeline__(self):
        resultado = []
        for usuario in self.siguiendo:
            for elemento in usuario.tuits:
                fecha, mensaje = elemento
                resultado.append((fecha, usuario.usuario, mensaje))
        return resultado





