import tetris
import gamelib
import csv

ESPERA_DESCENDER = 15
ruta_teclas = 'D:/tetris/teclas.txt'
datos_puntajes ='D:/tetris/puntajes.txt'

def dibujar_grilla(matriz):
    #dibuja la grilla y añade asigna a cada posicion posible dentro de la matriz una posicion dada
    # en base a cuatro coordenadas
    x = 50
    y = 50
    yo = 500
    valores_x = []
    valores_y = []
    for _ in range(tetris.ANCHO_JUEGO + 1):
        gamelib.draw_line(x, y, x, yo)
        valores_x.append(x)
        x += 25

    for _ in range(tetris.ALTO_JUEGO + 1):
        gamelib.draw_line(50, y, x - 25, y)
        valores_y.append(y)
        y += 25

    if matriz == {}:
        for x in range(9):
            for y in range(18):
                tupla =(x, y)
                matriz[tupla] = (valores_x[x], valores_y[y], valores_x[x + 1], valores_y[y + 1])

def dibujar_puntaje(puntaje):
    # dibuja el puntaje
    cadena = 'Puntaje:  ' + str(puntaje)
    gamelib.draw_text(cadena, 300, 75, fill = 'red', anchor = 'w')

def dibujar_pieza(juego, matriz):
    #dibuja la pieza y la superficie del juego
    _, pieza_actual, superficie = juego
    for elemento in pieza_actual:
        if elemento in matriz:
            x, y, x1, y1 = matriz[elemento]
            gamelib.draw_rectangle(x, y, x1, y1, fill = 'purple')
    for elemento in superficie:
        if elemento in matriz:
            x, y, x1, y1 = matriz[elemento]
            gamelib.draw_rectangle(x, y, x1, y1, fill = 'magenta')

def dibujar_prox_pieza(matriz, proxima_pieza):
    # dibuja la proxima pieza a aparecer en el tablero
    gamelib.draw_text( 'Prox Pieza:', 300, 100, fill = 'red', anchor = 'w')
    for elemento in proxima_pieza:
        if elemento in matriz:
            x, y, x1, y1 = matriz[elemento]
            gamelib.draw_rectangle(x + 250, y + 75, x1 + 250, y1 + 75, fill = 'yellow')

def configuracion_teclas(ruta_teclas):
    # se encarga de leer el archivo de teclas
    with open(ruta_teclas) as archivo:
        teclas = {}
        csv_reader = csv.reader(archivo)
        for linea in csv_reader:
            if linea != []:
                tecla, orden = linea[0].split(' = ')
                teclas[tecla] = orden
    return teclas

def uso_de_tecla(tecla, juego, proxima_pieza, teclas):
    # realiza una funcion determinada para cada tecla segun la tecla
    # que presiona el jugador
    grilla, _, superficie = juego
    if tecla in teclas:
        if teclas[tecla] == 'IZQUIERDA':
            juego = tetris.mover(juego, -1)
            return juego
        if teclas[tecla] == 'DERECHA':
            juego = tetris.mover(juego, 1)
            return juego
        if teclas[tecla] == 'DESCENDER':
            siguiente_pieza = False
            while not siguiente_pieza:
                juego, siguiente_pieza = tetris.avanzar(juego, proxima_pieza)
            return juego
        if teclas[tecla] == 'ROTAR':
            juego = (grilla, tetris.rotacion(juego), superficie)
            return juego
        if teclas[tecla] == 'SALIR':
            return None
        if teclas[tecla] == 'GUARDAR':
            tetris.guardar_partida(juego, tetris.datos_guardados)
        if teclas[tecla] == 'CARGAR':
            juego = tetris.cargar_partida(tetris.datos_guardados)
            return juego
    return juego

def buscar_puntaje(puntaje, datos_puntajes, nombre = None):
    # se encarga de leer el archivo puntajes y si corresponde
    # lo reemplaza en la lista de puntajes.
    lista = []
    with open(datos_puntajes, 'r') as archivo:
        csv_reader = csv.reader(archivo)
        contador = 0
        for item in csv_reader:
            contador +=1
            puntuacion = (item[0], int(item[1]))
            lista.append(puntuacion)
    if nombre == None or puntaje == None:
        return lista
    if contador < 10:
        with open(datos_puntajes, 'a') as escritor:
            escritor.write(nombre + ',' + str(puntaje) + '\n')
            lista.append((nombre,puntaje))
    else:
        minimo = ('', 0)
        for item in lista:
            if minimo == ('', 0):
                minimo = item
            elif minimo[1] > item[1]:
                minimo = item                
        if puntaje > minimo[1]:
            lista.remove(minimo)
            lista.append((nombre,puntaje))
        with open(datos_puntajes, 'w') as reemplazo:
            for item in lista:
                reemplazo.write(item[0] + ',' + str(item[1]) + '\n')
    return lista


def dibujar_maximos_puntajes(lista_puntajes):
    # dibuja los puntajes maximos
    x= 300
    y = 250
    gamelib.draw_text('Maximos Puntajes', x, y, fill = 'red', anchor = 'w')
    lista_puntajes.sort(key=lambda x:x[1])
    for tupla in lista_puntajes[-1::-1]:
        y += 25
        gamelib.draw_text(tupla[0] + ': ' + str(tupla[1]), x, y, size = 9, anchor = 'w', fill = 'magenta')

def pedir_nombre(nombre):
    #pide un nombre al usuario y verifica que sea un nombre valido
    while nombre == '':
        cadena =','
        posible_nombre = gamelib.input('Ingrese su Nombre')
        if posible_nombre != None:
            for caracter in posible_nombre:
                if caracter == cadena:
                    nombre = ''
                    break
                else:
                    nombre = posible_nombre
    return nombre

def fin_del_juego(nombre, puntaje, juego):
    # a partir del nombre de un usuario y su puntaje al finalizar
    # verifica si debe o no incluirse en el top 10 y de ser asi lo hace
    # luego dibuja la tabla de puntajes actualizada y pregunta si se desea
    # comenzar un nuevo juego
    if nombre == '':
        nombre = pedir_nombre(nombre)
        lista = buscar_puntaje(puntaje, datos_puntajes, nombre)
        gamelib.draw_begin()
        dibujar_maximos_puntajes(lista)
        gamelib.draw_end()
        respuesta = ''
        while respuesta != 's' and respuesta != 'n':
            respuesta = gamelib.input('Quiere empezar otro juego? (s/n)')
            if respuesta == 's':
                juego = juego = tetris.crear_juego(tetris.generar_pieza(pieza= None))
                puntaje = 0
                return juego, puntaje, lista
            if respuesta == 'n':
                puntaje = 0
                juego = None
                return juego, puntaje, lista

def main():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza= None))
    proxima_pieza = tetris.generar_pieza(pieza= None)
    teclas = configuracion_teclas(ruta_teclas)
    lista_puntajes = buscar_puntaje(None, datos_puntajes, None)
    gamelib.resize(450, 600)
    matriz = {}
    timer_bajar = ESPERA_DESCENDER
    puntaje = 0
    nombre = ''
    while gamelib.loop(fps=30):
        gamelib.draw_begin()
        # Dibujar la pantalla
        dibujar_grilla(matriz)
        dibujar_puntaje(puntaje)
        dibujar_prox_pieza(matriz, proxima_pieza,)
        dibujar_maximos_puntajes(lista_puntajes)
        dibujar_pieza(juego, matriz)
        gamelib.draw_end()

        for event in gamelib.get_events():
          if not event:
              break
          if event.type == gamelib.EventType.KeyPress:
              tecla = event.key
              juego = uso_de_tecla(tecla, juego,proxima_pieza, teclas)
              if juego == None:
                  return
              if tecla == 's':
                  proxima_pieza = tetris.generar_pieza(pieza= None)
                  puntaje += 40
              # Actualizar el juego, según la tecla presionada

        timer_bajar -= 1
        if timer_bajar == 0:
            timer_bajar = ESPERA_DESCENDER
            juego, siguiente_pieza = tetris.avanzar(juego, proxima_pieza)
            if siguiente_pieza:
                proxima_pieza = tetris.generar_pieza(pieza= None)
                puntaje += 40
            # Descender la pieza automáticamente

        if tetris.terminado(juego):
            juego, puntaje, lista_puntajes =  fin_del_juego(nombre, puntaje, juego)
            if juego == None:
                return
                
        
gamelib.init(main)

