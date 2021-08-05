class Partido:

    def __init__(self, equipo1, equipo2):
        self.local = equipo1
        self.visitante = equipo2
        self.goles1 = 0
        self.goles2 = 0
    
    def cargar_resultado(self, goles1, goles2):
        self.goles1 += goles1
        self.goles2 += goles2
    
    def obtener_ganador(self):
        if self.goles1 > self.goles2:
            return self.local
        elif self.goles2 > self.goles1:
            return self.visitante
        return None
    
    def obtener_perdedor(self):
        if self.goles1 > self.goles2:
            return self.visitante
        elif self.goles2 > self.goles1:
            return self.local
        return None
    

class Liga:
    def __init__(self):
        self.equipos = {}

    def cargar_partido(self, partido):
        if partido.obtener_ganador != None:
            if partido.obtener_ganador not in self.equipos:
                self.equipos[partido.obtener_ganador] = 3
            else:
                self.equipos[partido.obtener_ganador] += 3
        else:
            if partido.local not in self.equipos:
                self.equipos[partido.local] = 1
            else:
                self.equipos[partido.local] += 1
            
            if partido.visitante not in self.equipos:
                self.equipos[partido.visitante] = 1
            else:
                self.equipos[partido.visitante] += 1

    def obtener_campeon(self):
        puntos = 0
        ganador = ''
        for equipo in self.equipos:
            if self.equipos[equipo] > puntos:
                ganador = equipo
                puntos = self.equipos[equipo]
        return ganador