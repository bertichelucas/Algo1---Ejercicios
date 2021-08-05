class Tatuaje:
    def __init__(self, nombre, area, dolor):
        self.nombre = nombre
        self.area = area
        self.dolor = dolor

class Tatuador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cant = 0

    def __tatuar__(self, brazo, tatuaje):
        if tatuaje.dolor > brazo.aguante:
            raise ValueError('No te lo vas a Bancar')
        elif tatuaje.area > brazo.area:
            raise ValueError('Ya no te queda mas lugar')
        else:
            brazo.area -= tatuaje.area
            self.cant += 1
    
    def __str__(self):
        return (f'{self.nombre}: {self.cant} tatuajes realizados')
    
class Brazo:
    def __init__(self, area, aguante):
        self.area = area
        self.aguante = aguante


