class Vector:

    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        print(self.lista)
    
    def __add__(self, otro):
        #Recibe otro vector y devuelve un vector con la suma de ambos.
        if len(self.lista) == len(otro.lista):
            resultado = []
            contador = 0
            for item in self.lista:
                resultado.append(item + otro.lista[contador])
                contador += 1
        return Vector(resultado)

    def __mul__(self, numero):
        #Recibe un numero y devuelve un nuevo vector multiplicado por ese numero.
        resultado = []
        for item in self.lista:
            resultado.append(item * numero)
        return Vector(resultado)

