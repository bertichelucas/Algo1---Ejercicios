def imprimir_caracteres(cadena):
    print(cadena[0:2])

def imprimir_ultcaracteres(cadena):
    print(cadena[-3:])

def imprimir_cada_dos_caracteres(cadena):
    print(cadena[::2])

def imprimir_sentido_inverso(cadena):
    print(cadena[::-1])

def imprimir_reflejo(cadena):
    print(cadena[::], end='')
    print(cadena[::-1])

imprimir_reflejo('eleven')