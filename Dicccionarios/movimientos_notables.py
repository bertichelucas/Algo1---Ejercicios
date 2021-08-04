"""
Ejercicio 59 diccionarios

Dada una partida en forma de una lista de tuplas de la forma <personaje>,<movimiento> y un número k, 
imprimir por pantalla todos los movimientos notables de cada personaje y cuántas veces se usaron. 
Se dice que un movimiento es notable si el personaje lo utilizó más de k veces durante la partida. Ejemplo:

>>> movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"),
                   ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]
>>> imprimir_notables(movimientos, 1)
Charizard - Lanzallamas (2)

"""
movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"),
                   ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]

def imprimir_movimientos_notables(movimientos, k):
    movimientodic = {}

    for pokemon, movimiento in movimientos:
        movimientodic[f'{pokemon} - {movimiento}'] = movimientodic.get(f'{pokemon} - {movimiento}', 0) + 1
    for clave, valor in movimientodic.items():
        if valor > k:
            print(f'{clave} ({valor})')

