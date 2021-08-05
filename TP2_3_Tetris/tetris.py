ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
CUBO = 0
Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6

ruta_piezas = 'D:/tetris/piezas.txt'
datos_guardados = 'D:/tetris/datosguardados.txt'

def piezas(ruta_piezas):
    PIEZAS = {}
    with open(ruta_piezas) as archivo:
        for linea in archivo:
            contador = 0
            resultado = linea.rstrip().split(' # ')
            if resultado != ['']:  
                resultado.pop()
                resultado = resultado[0].split(' ')
                for item in resultado:
                    rotacion = item.split(';')
                    rotacion_final = []
                    for item in rotacion:
                        tupla = tuple(map(int, item.split(',')))
                        rotacion_final.append(tupla)
                    if contador == 0:
                        rotacion_0 = tuple(rotacion_final)
                        PIEZAS[rotacion_0] = [tuple(rotacion_final)]
                        contador += 1 
                    else:
                        PIEZAS[rotacion_0].append(tuple(rotacion_final))
    return PIEZAS

PIEZAS = piezas(ruta_piezas)

def generar_pieza(pieza = None):
    if pieza == None:
        from random import choice
        pieza_inicial = choice(list(PIEZAS.keys()))
    else:
        pieza_inicial = PIEZAS[pieza]
    return pieza_inicial

def trasladar_pieza(pieza, dx, dy):
    traslado = []
    for tupla in pieza:
        x, y = tupla
        x += dx 
        y += dy
        resultado = (x,y)
        traslado.append(resultado)
    return tuple(traslado)

def crear_juego(pieza_inicial):
    pieza_actual = trasladar_pieza(pieza_inicial, ANCHO_JUEGO // 2, 0)
    grilla = []
    for x in range(ANCHO_JUEGO):
        for y in range(ALTO_JUEGO):
            celda = (x, y)
            grilla.append(celda)
    superficie = []
    juego = (grilla, pieza_actual, superficie)
    return juego

def dimensiones(juego):
    dimension = (ANCHO_JUEGO, ALTO_JUEGO)
    return dimension

def pieza_actual(juego):
    pieza_actual = juego [1]
    return pieza_actual

def rotacion(juego):
    grilla, pieza_actual, _ = juego
    pieza_ordenada = sorted(pieza_actual)
    primer_posicion = pieza_ordenada[0]
    x, y = primer_posicion
    pieza_en_origen = trasladar_pieza(pieza_ordenada, -x, -y)
    siguiente_rotacion = buscar_rotacion(pieza_en_origen, PIEZAS)
    for item in trasladar_pieza(siguiente_rotacion, x, y):
        if item not in grilla:
            return pieza_actual
    return trasladar_pieza(siguiente_rotacion, x, y)


def buscar_rotacion(pieza_en_origen, PIEZAS):
    for pieza in PIEZAS:
        if pieza_en_origen in PIEZAS[pieza]:
            index = PIEZAS[pieza].index(pieza_en_origen)
            if index == len(PIEZAS[pieza]) - 1:
                index = -1
            siguiente_rotacion = PIEZAS[pieza][index + 1]
    return siguiente_rotacion

def hay_superficie(juego, x, y):
    celda = (x, y)
    for tupla in juego [2]:
        if celda == tupla:
            return True
    return False


def mover(juego, direccion):
    grilla, pieza_actual, superficie = juego
    mover_ficha = trasladar_pieza(pieza_actual, direccion, 0)
    for tupla in mover_ficha:
        if tupla not in grilla:
            mover_ficha = pieza_actual
    nuevo_juego = (grilla, mover_ficha, superficie)
    return nuevo_juego   


def avanzar(juego, x = generar_pieza(pieza=None)):
    pieza_actual = juego [1]
    if terminado(juego):
        siguiente_pieza = False
        return (juego, siguiente_pieza)
    avance = trasladar_pieza(pieza_actual, 0, 1)
    juego, siguiente_pieza = consolidar_superficie(juego, avance)
    if siguiente_pieza:
        juego [1] = trasladar_pieza(x,ANCHO_JUEGO // 2, 0)
    juego = eliminar_fila(juego)
    return (juego, siguiente_pieza)

def consolidar_superficie(juego, avance):
    grilla, pieza_actual, superficie = juego
    siguiente_pieza = False
    if any(item not in grilla for item in avance):
        for parte in pieza_actual:
                superficie.append(parte)
                if parte in grilla:
                    grilla.remove(parte)
        siguiente_pieza = True
        juego = [grilla, pieza_actual, superficie]
    else:
        juego = [grilla, avance, superficie]
    return (juego, siguiente_pieza)

def eliminar_fila(juego):
    grilla, _, superficie = juego
    fila = []
    for y in range(ALTO_JUEGO):
        altura = y
        for x in range(ANCHO_JUEGO):
            celda = (x, y)
            if celda in superficie:
                fila.append(celda)
        if len(fila) == ANCHO_JUEGO:
            for celda in fila:
                superficie.remove(celda)
                grilla.append(celda)
            juego = bajar_elementos(juego, altura)
        fila = []
    return juego


def bajar_elementos(juego, altura):
    grilla, _, superficie = juego
    removidos = []
    agregados = []
    for celda in superficie:
        x, y = celda
        if y < altura:
            removidos.append(celda)
            celdanueva = x, y  + 1
            agregados.append(celdanueva)
    for item in removidos:
        superficie.remove(item)
        grilla.append(item)
    for item in agregados:
        superficie.append(item)
        grilla.remove(item)
    return juego

def guardar_partida(juego, datos_guardados):
    with open(datos_guardados, 'w') as archivo:
        for item in juego:
            archivo.write(str(item) + '\n')

def cargar_partida(datos_guardados):
    with open(datos_guardados) as archivo:
        grilla = archivo.readline().rstrip()
        pieza_actual = archivo.readline().rstrip()
        superficie = archivo.readline().rstrip()
        grilla = pasar_lista(grilla)
        superficie = pasar_lista(superficie)
        pieza_actual = tuple(pasar_lista(pieza_actual))
        juego = (grilla, pieza_actual, superficie)
        return juego

def pasar_lista(grilla):
    lista = grilla.split('), (')
    grilla_original = []
    posicion = []
    contador = 0
    for item in lista:
        lista_numeros = item.split(',')
        for item in lista_numeros:
            contador += 1
            numero = ''
            for caracter in item:
                if caracter.isdigit():
                    numero += caracter
            posicion.append(int(numero))
            if contador == 2:
                grilla_original.append(tuple(posicion))
                posicion = []
                contador = 0
    return grilla_original

def terminado(juego):
    pieza_actual = juego [1]
    superficie = juego [2]
    for parte in pieza_actual:
        if parte in superficie:
            return True
    return False