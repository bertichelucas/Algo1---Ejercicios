def tabla(n):
    'Tabla de multiplicar de N'
    for i in range (11):
        print (n * i)

def askn():
    n = int(input('seleccione un numero para obtener su tabla'))
    return (tabla (n))

print (askn(), end="end")
