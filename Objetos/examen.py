#Se tiene una clase Ejercicio con los métodos calificar(n) y obtener_nota(), que reciben y devuelven, respectivamente, 
# un número entero entre 0 y 10 (si no está calificado, obtener_nota debe levantar una excepción). 
# Escribir una clase Examen que tenga los siguientes métodos:
#un constructor que cree un Examen nuevo en base a una lista de Ejercicios
#calificar(i,n), con i el número de ejercicio y n la calificación del mismo esta_aprobado(), que devuelve si un Examen está aprobado o no. 
# Unxamen está aprobado si tiene el 60% de los ejercicios con nota mayor o igual a 6.
#obtener_nota(), que devuelve la nota del Examen. Si esta aprobado, la misma es un promedio de la nota de todos los ejercicios. 
# Sino, es un 2 independientemente del promedio.

class Examen:
    def __init__(self, ejercicios):
        self.ejercicios = ejercicios
    
    def calificar(self, nro_ej, nota):
        self.ejercicios[nro_ej].calificar(nota)

    def esta_aprobado(self):
        return len(self.aprobados()) / len(self.ejercicios) > 0.6
    
    def obtener_nota(self):
        if not self.esta_aprobado():
            return 2
        notas_aprobados = [ej.obtener_nota() for ejercicio in self.ejercicios]
        return sum(notas_aprobados) / len(self.ejercicios)

    def aprobados(self):
        aprobados = [ejercicio for ejercicio in self.ejercicios if ejercicio.obtener_nota() >= 6]

