#Se pide escribir una función que calcule el ganador de una liga de fútbol a partir de los resultados de los partidos realizados. 
# La función recibe una lista de tuplas de 4 elementos con el siguiente formato:
#(nombre_equipo1, goles_equipo1, nombre_equipo2, goles_equipo2)
#Ejemplo: ("Barcelona", 1, "Real Madrid", 2).

#La función devuelve el nombre del equipo ganador. En caso de haber más de un equipo con puntuación máxima, devolver uno cualquiera de entre ellos.
#Reglas de puntaje de la liga: el equipo ganador de un partido recibe 2 puntos, y el perdedor 0 puntos. En caso de empate, cada uno de los dos equipos recibe 1 punto.

import random

def ganador_liga(resultados):
    nuevo_diccionario = {}
    for partido in resultados:
        eq_uno, goles_uno, eq_dos, goles_dos = partido
        if eq_uno not in nuevo_diccionario:
            nuevo_diccionario [eq_uno] = 0
        if eq_dos not in nuevo_diccionario:
            nuevo_diccionario [eq_dos] = 0
        
        if goles_uno > goles_dos:
            nuevo_diccionario [eq_uno] += 2
        elif goles_dos > goles_uno:
            nuevo_diccionario [eq_dos] += 2
        else:
            nuevo_diccionario [eq_uno] += 1
            nuevo_diccionario [eq_dos] += 1
        
    puntajes = nuevo_diccionario.values()
    max_puntaje = max(puntajes)
    ganadores = []
    for equipo in nuevo_diccionario:
        if nuevo_diccionario [equipo] == max_puntaje:
            ganadores.append(equipo)
    return random.choice(ganadores)


liga = [
    ('Chelsea', 2, 'Liverpool', 3),
    ('City', 5, 'United', 5),
    ('Tottenham', 3, 'WestHam', 2),
    ('Liverpool', 5, 'City', 4),
    ('United', 0, 'WestHam', 0),
    ('Tottenham', 2, 'Chelsea', 0),
    ('Chelsea',2, 'City', 3),
    ('Tottenham',2, 'United', 1),
    ('WestHam', 0, 'Liverpool', 1)

    ]

print(ganador_liga(liga))